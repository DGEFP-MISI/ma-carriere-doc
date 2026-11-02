param(
 [ValidateSet('avant','apres')][string]$Phase='apres',
 [string]$Scenario='',
 [string]$Browser='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
)
$ErrorActionPreference='Stop'
$htmlRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$explorerRoot=(Resolve-Path -LiteralPath (Join-Path $htmlRoot '..')).Path
$workspaceRoot=(Resolve-Path -LiteralPath (Join-Path $explorerRoot '../..')).Path
$node=Join-Path $workspaceRoot '07_parcours/commun_datavisualisation/outils/node-v24.22.2-win-x64/node.exe'
$page=Join-Path $htmlRoot 'index.html'
if($Phase -eq 'avant'){
 $archiveRoot=Join-Path $explorerRoot '99_archives/2026-11-02_ameliorations_ux'
 $page=Join-Path $archiveRoot 'AVANT.html'
 if(-not(Test-Path -LiteralPath $page)){
  $zip=[System.IO.Compression.ZipFile]::OpenRead((Join-Path $archiveRoot 'ETAT_AVANT.zip'))
  try{
   $entry=$zip.GetEntry('07_parcours/Explorer/12_maquette_html/index.html')
   if(-not $entry){throw 'HTML de référence absent de la sauvegarde.'}
   $inputStream=$entry.Open();$outputStream=[System.IO.File]::Create($page)
   try{$inputStream.CopyTo($outputStream)}finally{$inputStream.Dispose();$outputStream.Dispose()}
  }finally{$zip.Dispose()}
 }
}
$uxProfilePath=Join-Path $env:TEMP ('Explorer_UX_CDP_'+[guid]::NewGuid().ToString('N'))
$log=Join-Path $htmlRoot "controles/traces/edge-ux-$Phase.log"
$arguments=@('--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-background-networking','--disable-extensions','--disable-component-update','--remote-debugging-address=127.0.0.1','--remote-debugging-port=0',"--user-data-dir=`"$uxProfilePath`"",'about:blank')
$process=Start-Process -FilePath $Browser -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardError $log
try{
 $portFile=Join-Path $uxProfilePath 'DevToolsActivePort'
 for($attempt=0;$attempt -lt 100 -and -not(Test-Path -LiteralPath $portFile);$attempt++){Start-Sleep -Milliseconds 100}
 if(-not(Test-Path -LiteralPath $portFile)){throw 'Port de contrôle Edge introuvable.'}
 $port=(Get-Content -LiteralPath $portFile -TotalCount 1).Trim()
 & $node (Join-Path $PSScriptRoot 'tester_ux_cdp.mjs') $port $page $Phase $htmlRoot $Scenario
 $testExit=$LASTEXITCODE
}finally{
 if(-not $process.HasExited){Stop-Process -Id $process.Id -ErrorAction SilentlyContinue}
}
if($testExit -ne 0){throw "La recette UX comporte des échecs : phase $Phase. Consulter TESTS_UX_CDP_$($Phase.ToUpper()).json."}
