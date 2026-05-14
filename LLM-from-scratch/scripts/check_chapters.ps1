param(
  [string]$Root = "D:\Codes\Course"
)

$yamlPath = Join-Path $Root "chapters.yml"
if (-not (Test-Path $yamlPath)) {
  Write-Error "chapters.yml not found: $yamlPath"
  exit 1
}

$yaml = Get-Content -Encoding UTF8 -Path $yamlPath
$chapters = @()
$curr = @{}
foreach ($line in $yaml) {
  if ($line -match '^\s*-\s*$') {
    if ($curr.id) { $chapters += [pscustomobject]$curr; $curr = @{} }
    continue
  }
  if ($line -match '^\s*id:\s*(ch\d{2})') { $curr.id = $matches[1]; continue }
  if ($line -match '^\s*title:\s*(.*)$') {
    $val = $matches[1].Trim().Trim('"')
    $curr.title = $val
    continue
  }
  if ($line -match '^\s*folder:\s*(.*)$') {
    $val = $matches[1].Trim().Trim('"')
    $curr.folder = $val
    continue
  }
}
if ($curr.id) { $chapters += [pscustomobject]$curr }

function Sanitize-Name([string]$name) {
  $name = $name -replace '/', '／'
  $name = $name -replace ':', '：'
  $name = $name -replace '[\\*?"<>|]', ''
  $name = $name -replace '\s+', ' '
  return $name.Trim()
}

$rows = @()
$warnings = @()
foreach ($ch in $chapters) {
  $num = [int]$ch.id.Substring(2)
  $base = Sanitize-Name "第${num}章：$($ch.title)"
  $folderPath = Join-Path $Root $ch.folder
  $slides = Join-Path $folderPath "slides"
  $tutorial = Join-Path $folderPath "tutorial"
  $readme = Join-Path $folderPath "README.md"

  $pptx = if (Test-Path $slides) { Get-ChildItem -Path $slides -Filter *.pptx -File } else { @() }
  $pdf = if (Test-Path $slides) { Get-ChildItem -Path $slides -Filter *.pdf -File } else { @() }
  $ipynb = if (Test-Path $tutorial) { Get-ChildItem -Path $tutorial -Filter *.ipynb -File } else { @() }

  $expectedPptx = "$base.pptx"
  $expectedPdf = "$base.pdf"
  $pptxOk = $pptx.Name -contains $expectedPptx
  $pdfOk = $pdf.Name -contains $expectedPdf

  if (-not (Test-Path $readme)) { $warnings += "$($ch.id): missing README.md" }
  if (-not (Test-Path $slides)) { $warnings += "$($ch.id): missing slides/" }
  if (-not (Test-Path $tutorial)) { $warnings += "$($ch.id): missing tutorial/" }
  if (-not $pptxOk) { $warnings += "$($ch.id): PPTX name mismatch (expected: $expectedPptx)" }
  if (-not $pdfOk) { $warnings += "$($ch.id): PDF name mismatch (expected: $expectedPdf)" }
  if ($ipynb.Count -eq 0) { $warnings += "$($ch.id): no ipynb in tutorial/" }

  $rows += [pscustomobject]@{
    Chapter = $ch.id
    Folder = $ch.folder
    Readme = (Test-Path $readme)
    Slides = $pptx.Count + $pdf.Count
    PptxOk = $pptxOk
    PdfOk = $pdfOk
    Notebooks = $ipynb.Count
  }
}

$rows | Format-Table -AutoSize
if ($warnings.Count -gt 0) {
  Write-Host "\nWarnings:" -ForegroundColor Yellow
  $warnings | Sort-Object | ForEach-Object { Write-Host "- $_" }
}
