[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^v\d+\.\d+\.\d+([.-][0-9A-Za-z.-]+)?$')]
    [string]$Version,

    [switch]$Push
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $RepoRoot

$status = git status --porcelain
if ($LASTEXITCODE -ne 0) {
    throw "Unable to read Git status."
}

if ($status) {
    throw "The repository is not clean. Commit or discard changes before creating a release."
}

& (Join-Path $PSScriptRoot "build.ps1") -Clean
if ($LASTEXITCODE -ne 0) {
    throw "PDF build failed. No tag was created."
}

git tag -a $Version -m "Release $Version"
if ($LASTEXITCODE -ne 0) {
    throw "Unable to create tag $Version."
}

Write-Host "Created local tag: $Version" -ForegroundColor Green

if ($Push) {
    git push origin $Version
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to push tag to GitHub."
    }
    Write-Host "Tag pushed. The release workflow will start automatically." -ForegroundColor Green
}
else {
    Write-Host "To publish, run: git push origin $Version" -ForegroundColor Yellow
}
