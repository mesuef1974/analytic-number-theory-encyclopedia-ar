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

function Run-Tool {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )

    Write-Host ""
    Write-Host "$Name $($Arguments -join ' ')" -ForegroundColor DarkGray
    & $Name @Arguments

    if ($LASTEXITCODE -ne 0) {
        throw "$Name failed with exit code $LASTEXITCODE."
    }
}

Set-Location $RepoRoot

if ($Clean -and (Test-Path $BuildDir)) {
    Remove-Item $BuildDir -Recurse -Force
}

if ($Clean) {
    $RootAuxiliaryFiles = @(
        "main.aux",
        "main.bcf",
        "main.bbl",
        "main.blg",
        "main.log",
        "main.out",
        "main.run.xml",
        "main.toc"
    )

    foreach ($FileName in $RootAuxiliaryFiles) {
        $FilePath = Join-Path $RepoRoot $FileName
        if (Test-Path $FilePath) {
            Remove-Item $FilePath -Force
        }
    }
}

New-Item -ItemType Directory -Force $BuildDir | Out-Null
New-Item -ItemType Directory -Force $ReleaseDir | Out-Null

Require-Command "xelatex"
Require-Command "biber"

Write-Host "Building encyclopedia PDF without latexmk..." -ForegroundColor Cyan

$XeLaTeXArgs = @(
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-file-line-error",
    "-output-directory=$BuildDir",
    $MainTex
)

Run-Tool -Name "xelatex" -Arguments $XeLaTeXArgs
Run-Tool -Name "biber" -Arguments @("--input-directory=$BuildDir", "--output-directory=$BuildDir", "main")
Run-Tool -Name "xelatex" -Arguments $XeLaTeXArgs
Run-Tool -Name "xelatex" -Arguments $XeLaTeXArgs

if (-not (Test-Path $OutputPdf)) {
    throw "The build completed but build\main.pdf was not found."
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
