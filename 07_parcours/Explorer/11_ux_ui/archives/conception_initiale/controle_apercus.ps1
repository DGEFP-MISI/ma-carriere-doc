param([ValidatePattern('^[a-z0-9_-]+$')][string]$Screen = 'essentiel', [switch]$Board)
# Aperçu de contrôle géométrique SVG, avec Arial en repli local ; ce n'est pas un export Figma.
Add-Type -AssemblyName System.Drawing
$svgPath = Join-Path $PSScriptRoot "mobile/$Screen.svg"
if ($Board) { $svgPath = Join-Path $PSScriptRoot "$Screen.svg" }
[xml]$svg = Get-Content -LiteralPath $svgPath -Raw -Encoding UTF8
$bitmap = New-Object System.Drawing.Bitmap([int]$svg.svg.width, [int]$svg.svg.height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.Clear([System.Drawing.Color]::White)
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
foreach ($element in $svg.SelectNodes('//*')) {
  if ($element.LocalName -eq 'rect') {
    $color = $element.GetAttribute('fill')
    if ($color -and $color -ne 'none') {
      $brush = New-Object System.Drawing.SolidBrush([System.Drawing.ColorTranslator]::FromHtml($color))
      $graphics.FillRectangle($brush, [single]$element.x, [single]$element.y, [single]$element.width, [single]$element.height)
      $brush.Dispose()
    }
  }
  if ($element.LocalName -eq 'circle') {
    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.ColorTranslator]::FromHtml($element.fill))
    $graphics.FillEllipse($brush, ([single]$element.cx - [single]$element.r), ([single]$element.cy - [single]$element.r), (2 * [single]$element.r), (2 * [single]$element.r))
    $brush.Dispose()
    if ($element.GetAttribute('stroke') -and $element.GetAttribute('stroke') -ne 'none') {
      $pen = New-Object System.Drawing.Pen([System.Drawing.ColorTranslator]::FromHtml($element.GetAttribute('stroke')), 2)
      $graphics.DrawEllipse($pen, ([single]$element.cx - [single]$element.r), ([single]$element.cy - [single]$element.r), (2 * [single]$element.r), (2 * [single]$element.r))
      $pen.Dispose()
    }
  }
  if ($element.LocalName -eq 'text') {
    $style = [System.Drawing.FontStyle]::Regular
    if ($element.GetAttribute('font-weight') -eq '700') { $style = [System.Drawing.FontStyle]::Bold }
    $font = New-Object System.Drawing.Font('Arial', [single]$element.GetAttribute('font-size'), $style, [System.Drawing.GraphicsUnit]::Pixel)
    $textFill = $element.GetAttribute('fill')
    if (-not $textFill) { $textFill = '#161616' }
    $brush = New-Object System.Drawing.SolidBrush([System.Drawing.ColorTranslator]::FromHtml($textFill))
    $graphics.DrawString($element.InnerText, $font, $brush, [single]$element.x, ([single]$element.y - [single]$element.GetAttribute('font-size')))
    $font.Dispose(); $brush.Dispose()
  }
}
$outDirectory = Join-Path $PSScriptRoot 'apercus_controle'
[System.IO.Directory]::CreateDirectory($outDirectory) | Out-Null
$outPath = Join-Path $outDirectory "$Screen.png"
$bitmap.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose(); $bitmap.Dispose()
Write-Output $outPath
