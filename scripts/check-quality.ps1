[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $RepoRoot

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    $Python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $Python) {
    throw "Python was not found in PATH."
}

if ($Python.Name -eq "py.exe") {
    & py -3 ".\scripts\quality_check.py"
}
else {
    & python ".\scripts\quality_check.py"
}

if ($LASTEXITCODE -ne 0) {
    throw "Quality checks failed."
}
