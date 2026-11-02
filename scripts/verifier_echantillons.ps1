# Controle hors ligne non destructif des JSON observes contre le dernier OpenAPI.
# Compatible Windows PowerShell 5.1 et PowerShell 7.
$ErrorActionPreference = 'Stop'
$racine = Split-Path -Parent $PSScriptRoot
$cheminSwagger = Join-Path $racine '01_sources/openapi/docs_json_interface.json'
$dossierJson = Join-Path $racine '02_reponses_observees'
$inventaire = Join-Path $dossierJson 'inventaire_echantillons.csv'
$dossierSortie = Join-Path $racine '06_controles/resultats'
New-Item -ItemType Directory -Force -Path $dossierSortie | Out-Null

$swagger = Get-Content -LiteralPath $cheminSwagger -Raw -Encoding UTF8 | ConvertFrom-Json
$echantillons = @(Import-Csv -LiteralPath $inventaire -Delimiter ';' -Encoding UTF8)
$rapport = foreach ($entree in $echantillons) {
    $relatif = [string]$entree.fichier_relatif
    $endpoint = [string]$entree.endpoint_associe
    $cheminJson = Join-Path $dossierJson $relatif
    $etat = ''
    $racineNonDeclaree = ''
    $itemsNonDeclares = ''
    $limite = ''
    $objet = $null
    try {
        $objet = Get-Content -LiteralPath $cheminJson -Raw -Encoding UTF8 | ConvertFrom-Json
    } catch {
        $etat = 'json_invalide'
        $limite = $_.Exception.Message
    }
    if ($etat -eq '') {
        $route = $swagger.paths.PSObject.Properties[$endpoint]
        $operation = if ($null -ne $route) { $route.Value.get } else { $null }
        $schema = $null
        if ($null -ne $operation) {
            $reponse200 = $operation.responses.'200'
            if ($null -ne $reponse200 -and $null -ne $reponse200.content) {
                $json200 = $reponse200.content.'application/json'
                if ($null -ne $json200) { $schema = $json200.schema }
            }
        }
        if ($null -eq $schema) {
            $etat = 'schema_200_non_documente'
            $limite = "Ne permet pas de conclure a une absence de champ"
        } else {
            $etat = 'comparaison_champs_observes'
            $proprietes = $schema.properties
            $clesDeclarees = @()
            if ($null -ne $proprietes) { $clesDeclarees = @($proprietes.PSObject.Properties.Name) }
            $clesObservees = @()
            if ($objet -is [pscustomobject]) { $clesObservees = @($objet.PSObject.Properties.Name) }
            $racineNonDeclaree = (@($clesObservees | Where-Object { $clesDeclarees -notcontains $_ } | Sort-Object -Unique) -join ',')

            $clesItemsDeclarees = @()
            if ($null -ne $proprietes -and $null -ne $proprietes.items -and $null -ne $proprietes.items.items -and $null -ne $proprietes.items.items.properties) {
                $clesItemsDeclarees = @($proprietes.items.items.properties.PSObject.Properties.Name)
            }
            $clesItemsObservees = @()
            if ($objet -is [pscustomobject] -and $null -ne $objet.items) {
                foreach ($element in $objet.items) {
                    if ($element -is [pscustomobject]) { $clesItemsObservees += @($element.PSObject.Properties.Name) }
                }
            }
            if ($clesItemsDeclarees.Count -gt 0) {
                $itemsNonDeclares = (@($clesItemsObservees | Where-Object { $clesItemsDeclarees -notcontains $_ } | Sort-Object -Unique) -join ',')
            }
            $limite = 'Des cles absentes peuvent resulter de fields, pagination ou variantes des parametres'
        }
    }
    [pscustomobject]@{
        fichier = $relatif
        endpoint = $endpoint
        etat = $etat
        cles_racine_non_declarees = $racineNonDeclaree
        cles_items_non_declarees = $itemsNonDeclares
        limite = $limite
    }
}
$sortie = Join-Path $dossierSortie 'comparaison_echantillons.csv'
$rapport | Export-Csv -LiteralPath $sortie -Delimiter ';' -NoTypeInformation -Encoding UTF8
$nonDocumentes = @($rapport | Where-Object { $_.etat -eq 'schema_200_non_documente' }).Count
Write-Host "Echantillons analyses : $($rapport.Count)"
Write-Host "Sans schema HTTP 200 : $nonDocumentes"
Write-Host "Rapport genere : $sortie"
