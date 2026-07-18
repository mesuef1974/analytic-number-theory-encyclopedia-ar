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
        throw "الأداة '$Name' غير موجودة في PATH. راجع docs\BUILD.md."
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
    throw "فشل بناء LaTeX. راجع ملفات السجل داخل build."
}

if (-not (Test-Path $OutputPdf)) {
    throw "اكتمل الأمر دون العثور على build\main.pdf."
}

Copy-Item $OutputPdf $PreviewPdf -Force

$Hash = (Get-FileHash $PreviewPdf -Algorithm SHA256).Hash
$HashFile = "$PreviewPdf.sha256"
"$Hash  preview.pdf" | Set-Content -Path $HashFile -Encoding ascii

Write-Host ""
Write-Host "تم إنشاء:" -ForegroundColor Green
Write-Host "  $OutputPdf"
Write-Host "  $PreviewPdf"
Write-Host "SHA256: $Hash"

if ($Open) {
    Start-Process $PreviewPdf
}
