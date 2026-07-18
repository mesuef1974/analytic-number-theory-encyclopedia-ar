[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$VersionFile = Join-Path $RepoRoot "docs\VERSION.md"
$VersionText = Get-Content $VersionFile -Raw -Encoding UTF8

$Match = [regex]::Match($VersionText, '```text\s+(\d+\.\d+\.\d+-dev)\s+```')
if (-not $Match.Success) {
    throw "Unable to parse docs\VERSION.md."
}

$Version = $Match.Groups[1].Value
$MainVersion = $Version -replace '-dev$', ''

$ReadmePath = Join-Path $RepoRoot "README.md"
$Readme = Get-Content $ReadmePath -Raw -Encoding UTF8
$Readme = [regex]::Replace($Readme, 'v\d+\.\d+\.\d+-dev', "v$Version")
Set-Content $ReadmePath $Readme -Encoding UTF8

$ProgressPath = Join-Path $RepoRoot "docs\PROGRESS.md"
$Progress = Get-Content $ProgressPath -Raw -Encoding UTF8
$Progress = [regex]::Replace($Progress, '\d+\.\d+\.\d+-dev', $Version, 1)
Set-Content $ProgressPath $Progress -Encoding UTF8

$MainPath = Join-Path $RepoRoot "manuscript\main.tex"
$Main = Get-Content $MainPath -Raw -Encoding UTF8
$Main = [regex]::Replace(
    $Main,
    'الإصدار التطويري \d+\.\d+\.\d+',
    "الإصدار التطويري $MainVersion"
)
Set-Content $MainPath $Main -Encoding UTF8

Write-Host "Synchronized version $Version." -ForegroundColor Green
