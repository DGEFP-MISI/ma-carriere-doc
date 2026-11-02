param(
    [string]$Python = (Join-Path $env:LOCALAPPDATA 'Programs/Python/Python313/python.exe'),
    [string]$Browser = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
)
$ErrorActionPreference = 'Stop'
$controlRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$htmlRoot = (Resolve-Path -LiteralPath (Join-Path $controlRoot '..')).Path
foreach ($binary in @($Python, $Browser)) {
    if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) { throw "Exécutable introuvable : $binary" }
}
& $Python -B (Join-Path $htmlRoot 'sources/construire.py')
if ($LASTEXITCODE -ne 0) { throw 'Échec de construction.' }
foreach ($kind in @('desktop','mobile')) {
    $uri = [System.Uri]::new((Join-Path $htmlRoot 'index.html')).AbsoluteUri + '?verification=1'
    $window = '--window-size=1440,1100'
    if ($kind -eq 'mobile') {
        $uri = [System.Uri]::new((Join-Path $controlRoot 'controle-mobile.html')).AbsoluteUri
        $window = '--window-size=500,1000'
    }
    $profile = Join-Path $env:TEMP ('Explorer_Citoyen_Controle_' + [guid]::NewGuid().ToString('N'))
    $dom = Join-Path $controlRoot "traces/controle-$kind.dom.html"
    $errorLog = Join-Path $controlRoot "traces/edge-$kind.log"
    $screenshot = Join-Path $htmlRoot "apercus/apercu-$kind.png"
    $arguments = @('--headless','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-background-networking','--disable-extensions','--disable-component-update',"--user-data-dir=`"$profile`"",$window,'--virtual-time-budget=9000',"--screenshot=`"$screenshot`"",'--dump-dom',"`"$uri`"")
    $process = Start-Process -FilePath $Browser -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput $dom -RedirectStandardError $errorLog
    if (-not $process.WaitForExit(45000)) { throw "Délai dépassé pour le contrôle : $kind" }
    if ($process.ExitCode -ne 0) { throw "Échec Edge : $kind, code $($process.ExitCode)" }
    & $Python -B (Join-Path $PSScriptRoot 'extraire_controle.py') $kind | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Échec du contrôle : $kind" }
    $report = Get-Content -LiteralPath (Join-Path $controlRoot "resultats/CONTROLE_$($kind.ToUpper()).json") -Raw | ConvertFrom-Json
    Write-Output "$kind : $($report.passed) réussis, $($report.failed) échoués ; largeur $($report.viewport.width)px."
}
