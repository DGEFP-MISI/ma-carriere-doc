# R24 — Contextes de travail → Métiers : erreur 422, nouveau test requis

Date : 1er novembre 2026

## Appels prévus

- `GET /metiers?domaine=F16&contexte=300782&fields=rome_code,rome_libelle,contexte_travail_codes&page=1`
- `GET /metiers?domaine=F16&sans_contexte=300782&fields=rome_code,rome_libelle,contexte_travail_codes&page=1`

## Observations factuelles

Les deux réponses JSON fournies retournent une erreur HTTP métier `422` (dans le corps : `code: 422`) :

- `message`: « Paramètres de requête invalides. »
- `violations[0].propertyPath`: `fields`
- `violations[0].message`: « Champ(s) inconnu(s) : contexte_travail_code ».

Le champ **autorisé** présenté dans la même erreur est `contexte_travail_codes` (avec **s**), en accord avec le contrat et le schéma des métiers.

**Limite :** les noms des fichiers parlent de `contexte_travail_codes`, mais les JSON ne montrent pas les URL effectivement envoyées. On ne peut donc pas déterminer si la valeur singulière provient de la saisie dans Swagger ou d'une autre transformation.

**Statut R24 : non testée sur le plan fonctionnel** — le contrôle du filtre `fields` échoue avant restitution de la liste des métiers. Ne pas classer `contexte` ou `sans_contexte` comme défaillants.

## Re-test minimal sans `fields`

1. `GET /metiers?domaine=F16&contexte=300782&page=1`
2. `GET /metiers?domaine=F16&sans_contexte=300782&page=1`

Vérifier le code HTTP, `total`, et la présence ou absence de `F1610` dans les résultats (le cas échéant au-delà de la première page). Selon le contrat, le filtre `sans_contexte` exclut un métier dès lors qu'au moins une fiche ROME 4.0 rattachée porte ce contexte.

Si nécessaire pour réduire les retours, essayer séparément `fields=rome_code,rome_libelle` ; ne réintroduire `contexte_travail_codes` qu'après confirmation que le filtrage fonctionne.

## Sources

- JSON R24 fournis, fichiers du 1er novembre 2026
- Contrat d'interface `/metiers`, paramètres `fields`, `contexte` et `sans_contexte`
