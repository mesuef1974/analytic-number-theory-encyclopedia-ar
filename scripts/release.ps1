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
    throw "تعذر قراءة حالة Git."
}
if ($status) {
    throw "المستودع غير نظيف. احفظ التغييرات أو ألغها قبل إنشاء إصدار."
}

& (Join-Path $PSScriptRoot "build.ps1") -Clean
if ($LASTEXITCODE -ne 0) {
    throw "فشل بناء PDF؛ لم يُنشأ Tag."
}

git tag -a $Version -m "Release $Version"
if ($LASTEXITCODE -ne 0) {
    throw "تعذر إنشاء Tag $Version."
}

Write-Host "تم إنشاء Tag محلي: $Version" -ForegroundColor Green

if ($Push) {
    git push origin $Version
    if ($LASTEXITCODE -ne 0) {
        throw "تعذر دفع Tag إلى GitHub."
    }
    Write-Host "تم دفع Tag. سيبدأ Workflow الإصدار تلقائيًا." -ForegroundColor Green
} else {
    Write-Host "للنشر نفّذ: git push origin $Version" -ForegroundColor Yellow
}
