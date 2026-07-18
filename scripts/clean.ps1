[CmdletBinding()]
param(
    [switch]$IncludePreview
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$BuildDir = Join-Path $RepoRoot "build"
$PreviewPdf = Join-Path $RepoRoot "releases\preview.pdf"
$PreviewHash = "$PreviewPdf.sha256"

if (Test-Path $BuildDir) {
    Remove-Item $BuildDir -Recurse -Force
    Write-Host "Removed the build directory." -ForegroundColor Green
}

if ($IncludePreview) {
    foreach ($Path in @($PreviewPdf, $PreviewHash)) {
        if (Test-Path $Path) {
            Remove-Item $Path -Force
        }
    }
    Write-Host "Removed the local preview files." -ForegroundColor Green
}
