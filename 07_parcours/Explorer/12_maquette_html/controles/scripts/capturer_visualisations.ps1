param([string]$Browser='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
$ErrorActionPreference='Stop'
$htmlRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
foreach($kind in @('desktop','mobile')){
 foreach($view in @('salaires','territoires')){
  $file=Join-Path $htmlRoot 'controles/controle-desktop-apercu.html';$window='--window-size=1440,1100'
  if($kind -eq 'mobile'){$file=Join-Path $htmlRoot 'controles/controle-mobile.html';$window='--window-size=500,1000'}
  $uri=[System.Uri]::new($file).AbsoluteUri+"?apercu=$view"
  $profile=Join-Path $env:TEMP ('Explorer_DSFR_Capture_'+[guid]::NewGuid().ToString('N'))
  $screenshot=Join-Path $htmlRoot "apercus/dsfr-$view-$kind.png"
  $errorLog=Join-Path $htmlRoot "controles/traces/capture-$view-$kind.log"
  $arguments=@('--headless','--disable-gpu','--no-first-run','--disable-background-networking','--disable-extensions','--disable-component-update',"--user-data-dir=`"$profile`"",$window,'--virtual-time-budget=4000',"--screenshot=`"$screenshot`"","`"$uri`"")
  $process=Start-Process -FilePath $Browser -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardError $errorLog
  if(-not $process.WaitForExit(45000)){throw "Délai dépassé : $view $kind"}
  if($process.ExitCode -ne 0){throw "Capture échouée : $view $kind"}
  Write-Output "$view $kind : $screenshot"
 }
}
