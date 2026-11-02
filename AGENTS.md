# Consignes — Cas d'usage API DGEFP–RCO

## Objectif
Concevoir et documenter les parcours utilisateurs à partir de l'API spécifique DGEFP–RCO.

## Périmètre impératif
- Utiliser exclusivement les 21 endpoints GET documentés dans le contrat OpenAPI du dossier.
- Ne jamais ajouter de source externe, de table SQL, de champ ou d'endpoint non prévu.
- Référentiel métier : ROME V3 uniquement.
- Les données ROME 4.0 sont consolidées vers le parent ROME V3. Ne jamais restituer de codes métier ROME 4.0.
- Ne jamais inventer de données, de calculs, de scores ou de correspondances.

## Sources de référence
Lire les documents du contrat, les diagrammes UML, la matrice des relations et les preuves JSON du dossier.
Distinguer systématiquement :
- Documenté dans le contrat
- Observé dans un JSON
- Testé et validé
- À confirmer

## Méthode
Travailler sur un parcours à la fois.
Documenter chaque étape dans la table commune des parcours.
Pour chaque appel, préciser les paramètres, champs JSON, règles métier, affichage, gestion des valeurs manquantes et critères de validation.
Ne pas confondre source documentaire et source de données accessible par l'API.

## Contrôles
Ne pas modifier les sources de référence du contrat sans demande explicite.
Conserver les preuves des décisions et les résultats des tests.
Signaler tout besoin non couvert par l'API, sans proposer d'autre source de données.
