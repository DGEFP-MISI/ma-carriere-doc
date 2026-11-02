param([string]$Browser='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
$ErrorActionPreference='Stop'
$daRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$explorerDaRoot=(Resolve-Path -LiteralPath (Join-Path $daRoot '..')).Path
$workspaceDaRoot=(Resolve-Path -LiteralPath (Join-Path $explorerDaRoot '../..')).Path
$nodeDaPath=Join-Path $workspaceDaRoot '07_parcours/commun_datavisualisation/outils/node-v24.22.2-win-x64/node.exe'
$pageDaPath=Join-Path $explorerDaRoot '12_maquette_html/index.html'
$profileDaPath=Join-Path $env:TEMP ('Explorer_DA_'+[guid]::NewGuid().ToString('N'))
$logDaPath=Join-Path $daRoot 'preuves/EDGE.log'
$argsDa=@('--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-background-networking','--disable-extensions','--disable-component-update','--remote-debugging-address=127.0.0.1','--remote-debugging-port=0',"--user-data-dir=`"$profileDaPath`"",'about:blank')
$processDa=Start-Process -FilePath $Browser -ArgumentList $argsDa -WindowStyle Hidden -PassThru -RedirectStandardError $logDaPath
try{
 $portDaFile=Join-Path $profileDaPath 'DevToolsActivePort'
 for($tryDa=0;$tryDa -lt 100 -and -not(Test-Path -LiteralPath $portDaFile);$tryDa++){Start-Sleep -Milliseconds 100}
 if(-not(Test-Path -LiteralPath $portDaFile)){throw 'Port Edge introuvable.'}
 $portDa=(Get-Content -LiteralPath $portDaFile -TotalCount 1).Trim()
 & $nodeDaPath (Join-Path $PSScriptRoot 'recette_direction.mjs') $portDa $pageDaPath (Join-Path $daRoot 'preuves')
 $exitDaCode=$LASTEXITCODE
}finally{if(-not $processDa.HasExited){Stop-Process -Id $processDa.Id -ErrorAction SilentlyContinue}}
if($exitDaCode -ne 0){throw 'Échec de la recette DA ; consulter RECETTE_DIRECTION.json.'}
