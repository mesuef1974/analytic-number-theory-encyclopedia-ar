[CmdletBinding()]
param(
    [switch]$Clean,
    [switch]$Open
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$BuildDir = Join-Path $RepoRoot "build"
$ReleaseDir = Join-Path $RepoRoot "releases"
$MainTex = Join-Path $RepoRoot "manuscript\main.tex"
$OutputPdf = Join-Path $BuildDir "main.pdf"
$PreviewPdf = Join-Path $ReleaseDir "preview.pdf"

function Require-Command {
    param([Parameter(Mandatory = $true)][string]$Name)

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH. See docs\BUILD.md."
    }
}

Set-Location $RepoRoot

if ($Clean -and (Test-Path $BuildDir)) {
    Remove-Item $BuildDir -Recurse -Force
}

New-Item -ItemType Directory -Force $BuildDir | Out-Null
New-Item -ItemType Directory -Force $ReleaseDir | Out-Null

Require-Command "latexmk"
Require-Command "xelatex"
Require-Command "biber"

Write-Host "Building encyclopedia PDF..." -ForegroundColor Cyan

& latexmk `
    -xelatex `
    -interaction=nonstopmode `
    -halt-on-error `
    -file-line-error `
    "-outdir=$BuildDir" `
    $MainTex

if ($LASTEXITCODE -ne 0) {
    throw "LaTeX build failed. Review the log files in the build directory."
}

if (-not (Test-Path $OutputPdf)) {
    throw "The build command completed but build\main.pdf was not found."
}

Copy-Item $OutputPdf $PreviewPdf -Force

$Hash = (Get-FileHash $PreviewPdf -Algorithm SHA256).Hash
$HashFile = "$PreviewPdf.sha256"
"$Hash  preview.pdf" | Set-Content -Path $HashFile -Encoding ascii

Write-Host ""
Write-Host "Created:" -ForegroundColor Green
Write-Host "  $OutputPdf"
Write-Host "  $PreviewPdf"
Write-Host "SHA256: $Hash"

if ($Open) {
    Start-Process $PreviewPdf
}
