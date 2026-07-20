[CmdletBinding()]
param(
    [string]$Branch = "agent/chapter-12-siegel-walfisz-v0.16.0",
    [switch]$Open,
    [switch]$CommitReceipt,
    [switch]$Push
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PreviewPdf = Join-Path $RepoRoot "releases\preview.pdf"
$ReceiptPath = Join-Path $RepoRoot "docs\LOCAL_BUILD_RECEIPT.md"

function Require-Command {
    param([Parameter(Mandatory = $true)][string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Run-Command {
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

function Get-PdfPageCount {
    param([Parameter(Mandatory = $true)][string]$PdfPath)

    $pdfinfo = Get-Command "pdfinfo" -ErrorAction SilentlyContinue
    if ($pdfinfo) {
        $metadata = & $pdfinfo.Source $PdfPath
        $line = $metadata | Where-Object { $_ -match '^Pages:\s+(\d+)' } | Select-Object -First 1
        if ($line -match '^Pages:\s+(\d+)') {
            return [int]$Matches[1]
        }
    }

    $mutool = Get-Command "mutool" -ErrorAction SilentlyContinue
    if ($mutool) {
        $metadata = & $mutool.Source info $PdfPath
        $line = $metadata | Where-Object { $_ -match '^Pages:\s+(\d+)' } | Select-Object -First 1
        if ($line -match '^Pages:\s+(\d+)') {
            return [int]$Matches[1]
        }
    }

    $python = Get-Command "python" -ErrorAction SilentlyContinue
    if ($python) {
        $code = @'
import sys
try:
    from pypdf import PdfReader
except Exception:
    raise SystemExit(2)
print(len(PdfReader(sys.argv[1]).pages))
'@
        $count = & $python.Source -c $code $PdfPath 2>$null
        if ($LASTEXITCODE -eq 0 -and $count -match '^\d+$') {
            return [int]$count
        }
    }

    return $null
}

Require-Command "git"
Set-Location $RepoRoot

$initialStatus = @(git status --porcelain)
if ($LASTEXITCODE -ne 0) {
    throw "Unable to inspect the Git working tree."
}
if ($initialStatus.Count -gt 0) {
    throw "Working tree is not clean. Commit, stash, or remove local changes before synchronization."
}

Run-Command -Name "git" -Arguments @("fetch", "--prune", "origin")

git show-ref --verify --quiet "refs/heads/$Branch"
$LocalBranchExists = ($LASTEXITCODE -eq 0)
if ($LocalBranchExists) {
    Run-Command -Name "git" -Arguments @("checkout", $Branch)
}
else {
    Run-Command -Name "git" -Arguments @("checkout", "--track", "-b", $Branch, "origin/$Branch")
}

Run-Command -Name "git" -Arguments @("pull", "--ff-only", "origin", $Branch)

$Head = (git rev-parse HEAD).Trim()
$RemoteHead = (git rev-parse "origin/$Branch").Trim()
if ($Head -ne $RemoteHead) {
    throw "Synchronization failed: local HEAD '$Head' differs from origin/$Branch '$RemoteHead'."
}

& (Join-Path $PSScriptRoot "build.ps1") -Clean
if (-not (Test-Path $PreviewPdf)) {
    throw "Expected PDF was not created: $PreviewPdf"
}

$Hash = (Get-FileHash $PreviewPdf -Algorithm SHA256).Hash
$Size = (Get-Item $PreviewPdf).Length
$Pages = Get-PdfPageCount -PdfPath $PreviewPdf
$PagesText = if ($null -eq $Pages) { "UNKNOWN - install pdfinfo, mutool, or Python pypdf" } else { [string]$Pages }
$XeLaTeXVersion = (& xelatex --version | Select-Object -First 1).Trim()
$BiberVersion = (& biber --version | Select-Object -First 1).Trim()
$Timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")

$ReceiptTemplate = @'
# إيصال البناء المحلي المتزامن

```text
TIMESTAMP        = __TIMESTAMP__
BRANCH           = __BRANCH__
LOCAL-HEAD       = __LOCAL_HEAD__
ORIGIN-HEAD      = __ORIGIN_HEAD__
SYNC             = PASS / FF-ONLY
SOURCE-BUILD     = PASS
PDF              = releases/preview.pdf
PDF-PAGES        = __PDF_PAGES__
PDF-SIZE-BYTES   = __PDF_SIZE__
PDF-SHA256       = __PDF_SHA256__
XELATEX          = __XELATEX__
BIBER            = __BIBER__
RELEASE-READY    = NO
```

أُنشئ هذا الإيصال آليًا بواسطة `scripts/sync-build.ps1`. نجاح البناء المحلي لا يرفع الفصل تلقائيًا إلى `REVIEWED` أو `RELEASE-READY`، ولا يغني عن المراجعة المستقلة.
'@

$Receipt = $ReceiptTemplate
$Receipt = $Receipt.Replace("__TIMESTAMP__", $Timestamp)
$Receipt = $Receipt.Replace("__BRANCH__", $Branch)
$Receipt = $Receipt.Replace("__LOCAL_HEAD__", $Head)
$Receipt = $Receipt.Replace("__ORIGIN_HEAD__", $RemoteHead)
$Receipt = $Receipt.Replace("__PDF_PAGES__", $PagesText)
$Receipt = $Receipt.Replace("__PDF_SIZE__", [string]$Size)
$Receipt = $Receipt.Replace("__PDF_SHA256__", $Hash)
$Receipt = $Receipt.Replace("__XELATEX__", $XeLaTeXVersion)
$Receipt = $Receipt.Replace("__BIBER__", $BiberVersion)

$Receipt | Set-Content -Path $ReceiptPath -Encoding utf8
Write-Host ""
Write-Host "Synchronized local build completed." -ForegroundColor Green
Write-Host "HEAD:    $Head"
Write-Host "PDF:     $PreviewPdf"
Write-Host "Pages:   $PagesText"
Write-Host "SHA256:  $Hash"
Write-Host "Receipt: $ReceiptPath"

if ($CommitReceipt) {
    Run-Command -Name "git" -Arguments @("add", "docs/LOCAL_BUILD_RECEIPT.md")
    $changes = @(git diff --cached --name-only)
    if ($changes.Count -gt 0) {
        Run-Command -Name "git" -Arguments @("commit", "-m", "docs(build): record synchronized local PDF build")
    }
    else {
        Write-Host "Receipt is unchanged; no commit created." -ForegroundColor Yellow
    }
}

if ($Push) {
    if (-not $CommitReceipt) {
        throw "-Push requires -CommitReceipt so the generated receipt is committed first."
    }
    Run-Command -Name "git" -Arguments @("push", "origin", $Branch)
}

if ($Open) {
    Start-Process $PreviewPdf
}
