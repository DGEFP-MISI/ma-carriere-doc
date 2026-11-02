# Audit hors ligne du contrat OpenAPI. Compatible Windows PowerShell 5.1 et PowerShell 7.
$ErrorActionPreference = 'Stop'
$racine = Split-Path -Parent $PSScriptRoot
$sourceCourante = Join-Path $racine '01_sources/openapi/docs_json_interface.json'
$sourcePrecedente = Join-Path $racine '01_sources/openapi/swagger_precedent.json'
$dossierSortie = Join-Path $racine '06_controles/resultats'
New-Item -ItemType Directory -Force -Path $dossierSortie | Out-Null

function Lire-Json([string]$chemin) {
    if (-not (Test-Path -LiteralPath $chemin)) { throw "Fichier introuvable : $chemin" }
    return (Get-Content -LiteralPath $chemin -Raw -Encoding UTF8 | ConvertFrom-Json)
}
function Lister-Operations($document) {
    $operations = @{}
    foreach ($chemin in $document.paths.PSObject.Properties) {
        foreach ($methode in @('get', 'post', 'put', 'patch', 'delete')) {
            $propriete = $chemin.Value.PSObject.Properties[$methode]
            if ($null -ne $propriete) {
                $operations[($methode + '|' + $chemin.Name)] = $propriete.Value
            }
        }
    }
    return $operations
}
function Parametres($operation) {
    $noms = @()
    if ($null -ne $operation -and $null -ne $operation.parameters) {
        foreach ($parametre in $operation.parameters) { $noms += [string]$parametre.name }
    }
    return @($noms | Sort-Object -Unique)
}

$actuel = Lister-Operations (Lire-Json $sourceCourante)
$precedent = Lister-Operations (Lire-Json $sourcePrecedente)
$clefs = @(@($actuel.Keys) + @($precedent.Keys) | Sort-Object -Unique)
$rapport = foreach ($clef in $clefs) {
    $parties = $clef.Split('|', 2)
    $methode = $parties[0]
    $endpoint = $parties[1]
    $nouveau = if ($actuel.ContainsKey($clef)) { $actuel[$clef] } else { $null }
    $ancien = if ($precedent.ContainsKey($clef)) { $precedent[$clef] } else { $null }
    $pNouveau = @(Parametres $nouveau)
    $pAncien = @(Parametres $ancien)
    $ajoutes = @($pNouveau | Where-Object { $pAncien -notcontains $_ })
    $retires = @($pAncien | Where-Object { $pNouveau -notcontains $_ })
    $schema200 = $null
    if ($null -ne $nouveau) {
        $reponse200 = $nouveau.responses.'200'
        if ($null -ne $reponse200 -and $null -ne $reponse200.content) {
            $applicationJson = $reponse200.content.'application/json'
            if ($null -ne $applicationJson) { $schema200 = $applicationJson.schema }
        }
    }
    [pscustomobject]@{
        methode = $methode.ToUpperInvariant()
        endpoint = $endpoint
        dans_docs_interface = if ($null -ne $nouveau) { 'oui' } else { 'non' }
        dans_swagger_precedent = if ($null -ne $ancien) { 'oui' } else { 'non' }
        parametres_ajoutes = ($ajoutes -join ',')
        parametres_retires = ($retires -join ',')
        schema_200_present = if ($null -ne $schema200) { 'oui' } else { 'non' }
    }
}
$sortie = Join-Path $dossierSortie 'comparaison_openapi.csv'
$rapport | Export-Csv -LiteralPath $sortie -Delimiter ';' -NoTypeInformation -Encoding UTF8
Write-Host "Endpoints dans docs interface : $($actuel.Count)"
Write-Host "Endpoints dans Swagger precedent : $($precedent.Count)"
Write-Host "Rapport genere : $sortie"
