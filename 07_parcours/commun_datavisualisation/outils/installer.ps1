$ErrorActionPreference='Stop'
$moduleRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$proxy='http://proxyweb.intranet.social.gouv.fr:8080/'
$vendor=Join-Path $moduleRoot 'vendor'
[System.IO.Directory]::CreateDirectory($vendor) | Out-Null
$versions=@{'@gouvfr/dsfr-chart'='2.1.1';'@gouvfr/dsfr'='1.15.4'}
$provenance=@()
foreach($name in $versions.Keys){
    $meta=Invoke-RestMethod -Uri ('https://registry.npmjs.org/'+$name.Replace('/','%2f')+'/'+$versions[$name]) -Proxy $proxy -ProxyUseDefaultCredentials
    $filename=($name.Split('/')[1]+'-'+$meta.version+'.tgz')
    $path=Join-Path $vendor $filename
    Invoke-WebRequest -Uri $meta.dist.tarball -Proxy $proxy -ProxyUseDefaultCredentials -OutFile $path
    $bytes=[System.IO.File]::ReadAllBytes($path)
    $actual='sha512-'+[Convert]::ToBase64String([System.Security.Cryptography.SHA512]::HashData($bytes))
    if($actual -ne $meta.dist.integrity){throw "Empreinte incorrecte : $name"}
    $provenance+=@{name=$name;version=$meta.version;url=$meta.dist.tarball;integrity=$actual;sha256=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash;license=$meta.license}
}
$runtimeVersion='v24.22.2'
$runtimeName="node-$runtimeVersion-win-x64"
$zipPath=Join-Path $PSScriptRoot "$runtimeName.zip"
$sums=Invoke-RestMethod -Uri "https://nodejs.org/dist/$runtimeVersion/SHASUMS256.txt" -Proxy $proxy -ProxyUseDefaultCredentials
Invoke-WebRequest -Uri "https://nodejs.org/dist/$runtimeVersion/$runtimeName.zip" -Proxy $proxy -ProxyUseDefaultCredentials -OutFile $zipPath
$expected=($sums -split "`n" | Where-Object { $_.Trim().EndsWith("$runtimeName.zip") }) -replace '\s+.*$',''
if((Get-FileHash -LiteralPath $zipPath -Algorithm SHA256).Hash.ToLower() -ne $expected.Trim().ToLower()){throw 'Empreinte Node incorrecte.'}
Expand-Archive -LiteralPath $zipPath -DestinationPath $PSScriptRoot
$provenance+=@{name='Node.js';version=$runtimeVersion;url="https://nodejs.org/dist/$runtimeVersion/$runtimeName.zip";sha256=$expected.Trim()}
$provenance | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $vendor 'PROVENANCE.json') -Encoding utf8
Write-Output "Archives officielles vérifiées ; Node local : $runtimeName"
