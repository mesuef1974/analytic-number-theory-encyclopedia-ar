param(
    [string] $BuildDir = "build",
    [string] $MainFile = "manuscript\main.tex"
)

$ErrorActionPreference = "Stop"

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Convert-ArabicDigitsToAscii {
    param(
        [Parameter(Mandatory)]
        [string] $Path
    )

    $text = [System.IO.File]::ReadAllText($Path)

    $digitMap = @{
        '٠' = '0'
        '١' = '1'
        '٢' = '2'
        '٣' = '3'
        '٤' = '4'
        '٥' = '5'
        '٦' = '6'
        '٧' = '7'
        '٨' = '8'
        '٩' = '9'
    }

    foreach ($digit in $digitMap.Keys) {
        $text = $text.Replace($digit, $digitMap[$digit])
    }

    $lines = $text -split '\r?\n'

    $normalizedLines = foreach ($line in $lines) {
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }

        if ($line -notmatch '^\\indexentry') {
            $line
            continue
        }

        if ($line -notmatch '^(?<entry>\\indexentry\{.*\})\{.*?(?<page>[0-9]+).*?\}\s*$') {
            throw "Cannot normalize index line in ${Path}: $line"
        }

        "$($Matches.entry){$($Matches.page)}"
    }

    $normalizedText = ($normalizedLines -join "`n") + "`n"

    $badLines = @(
        $normalizedLines |
            Where-Object {
                $_ -match '^\\indexentry' -and
                $_ -notmatch '\{[0-9]+\}$'
            }
    )

    if ($badLines.Count -gt 0) {
        throw "Unnormalized lines remain in ${Path}: $($badLines -join ' | ')"
    }

    [System.IO.File]::WriteAllText(
        $Path,
        $normalizedText,
        $utf8NoBom
    )
}
function Convert-AsciiDigitsToArabic {
    param(
        [Parameter(Mandatory)]
        [string] $Path
    )

    $text = [System.IO.File]::ReadAllText($Path)

    $map = @{
        '0' = '٠'
        '1' = '١'
        '2' = '٢'
        '3' = '٣'
        '4' = '٤'
        '5' = '٥'
        '6' = '٦'
        '7' = '٧'
        '8' = '٨'
        '9' = '٩'
    }

    foreach ($digit in $map.Keys) {
        $text = $text.Replace($digit, $map[$digit])
    }

    [System.IO.File]::WriteAllText(
        $Path,
        $text.TrimEnd("`r", "`n") + "`n",
        $utf8NoBom
    )
}

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory)]
        [string] $Command,

        [Parameter(Mandatory)]
        [string[]] $Arguments
    )

    & $Command @Arguments

    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed with exit code $LASTEXITCODE"
    }
}

if (-not (Test-Path $BuildDir)) {
    New-Item -ItemType Directory -Path $BuildDir | Out-Null
}

$indexNames = @(
    "people",
    "theorems",
    "symbols"
)

Write-Host "Pass 1: XeLaTeX"
Invoke-CheckedCommand "xelatex" @(
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-output-directory=$BuildDir",
    $MainFile
)

Write-Host "Bibliography: Biber"
Invoke-CheckedCommand "biber" @(
    (Join-Path $BuildDir "main")
)

foreach ($name in $indexNames) {
    $idx = Join-Path $BuildDir "$name.idx"
    $ind = Join-Path $BuildDir "$name.ind"
    $ilg = Join-Path $BuildDir "$name.ilg"

    if (-not (Test-Path $idx)) {
        throw "Missing index source: $idx"
    }

    Write-Host "Normalizing $idx"
    Convert-ArabicDigitsToAscii $idx

    Write-Host "Normalized contents of ${idx}:"
    Get-Content $idx -Encoding UTF8

    Write-Host "Building $name index"
    Invoke-CheckedCommand "makeindex" @(
        "-o", $ind,
        "-t", $ilg,
        $idx
    )

    if (-not (Test-Path $ind)) {
        throw "Missing generated index: $ind"
    }

    Write-Host "Localizing page numbers in $ind"
    Convert-AsciiDigitsToArabic $ind

    $logText = [System.IO.File]::ReadAllText(
        $ilg,
        [System.Text.Encoding]::UTF8
    )

    if ($logText -match 'Input index error|Nothing written') {
        throw "Index build problem detected in $ilg"
    }

    if ($logText -match '\(([1-9][0-9]*) rejected\)') {
        throw "Rejected index entries detected in $ilg"
    }

    if ($logText -notmatch '\([0-9]+ entries accepted, 0 rejected\)') {
        throw "Expected successful makeindex summary not found in $ilg"
    }
}

Write-Host "Pass 2: XeLaTeX"
Invoke-CheckedCommand "xelatex" @(
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-output-directory=$BuildDir",
    $MainFile
)

Write-Host "Pass 3: XeLaTeX"
Invoke-CheckedCommand "xelatex" @(
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-output-directory=$BuildDir",
    $MainFile
)

$mainLog = Join-Path $BuildDir "main.log"

if (-not (Test-Path $mainLog)) {
    throw "Missing build log: $mainLog"
}

$fatalPatterns = @(
    'LaTeX Error',
    'Undefined control sequence',
    'Emergency stop',
    'Fatal error occurred'
)

$mainLogText = [System.IO.File]::ReadAllText($mainLog)

foreach ($pattern in $fatalPatterns) {
    if ($mainLogText -match $pattern) {
        throw "Fatal LaTeX pattern found: $pattern"
    }
}

Write-Host ""
Write-Host "INDEX BUILD PASSED"
Write-Host "PDF: $(Join-Path $BuildDir 'main.pdf')"
