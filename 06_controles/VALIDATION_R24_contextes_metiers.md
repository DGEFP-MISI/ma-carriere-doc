# Validation R24 — Contextes de travail → Métiers

**Date de contrôle :** 1er novembre 2026

**Périmètre :** API DGEFP–RCO, endpoint `GET /metiers`, domaine `F16`, code OGR de contexte `300782` (« En grande hauteur »). Vérification sur deux réponses JSON réellement exportées depuis Swagger. Aucun appel API ni accès SQL effectué par le script d'analyse.

## Requêtes

1. `GET /metiers?domaine=F16&contexte=300782&page=1`
2. `GET /metiers?domaine=F16&sans_contexte=300782&page=1`

## Résultats

| Contrôle | Avec contexte | Sans contexte |
|---|---:|---:|
| `total` | 10 | 3 |
| Nombre d'éléments dans `items` | 10 | 3 |
| `last_page` | 1 | 1 |
| Code `300782` dans les contextes de chaque réponse | Oui (10/10) | Non (3/3) |

### Avec le contexte

| Code ROME | Libellé |
|---|---|
| `F1601` | Application et décoration en plâtre, stuc et staff |
| `F1602` | Électricité bâtiment |
| `F1603` | Installation d'équipements sanitaires et thermiques |
| `F1604` | Montage d'agencements |
| `F1605` | Montage de réseaux électriques et télécoms |
| `F1606` | Peinture en bâtiment |
| `F1607` | Pose de fermetures menuisées |
| `F1610` | Pose et restauration de couvertures |
| `F1611` | Réalisation et restauration de façades |
| `F1612` | Taille et décoration de pierres |

### Sans le contexte

| Code ROME | Libellé |
|---|---|
| `F1608` | Pose de revêtements rigides |
| `F1609` | Pose de revêtements souples |
| `F1613` | Travaux d'étanchéité et d'isolation |

## Contrôles croisés

- Tous les éléments retournés portent `domaine_code = F16`.
- Les 10 métiers du premier résultat portent le contexte `300782`.
- Les 3 métiers du second résultat ne portent pas le contexte `300782`.
- L'intersection des codes ROME des deux réponses est vide.
- L'union représente 13 codes ROME distincts sur ce périmètre.
- `F1610` apparaît uniquement dans la réponse avec `contexte`.
- Les réponses déclarent chacune une seule page : il n'existe pas de pagination supplémentaire pour les résultats de ces requêtes.

## Observations et limites

- **Statut : validé** pour les deux filtres sur le contexte `300782`, au sein du domaine `F16`.
- Ce test ne prouve pas l'exactitude de tous les autres contextes et ne valide pas la totalité des combinaisons de filtres.
- Les précédentes réponses 422 indiquaient `fields` / champ inconnu `contexte_travail_code` (singulier). Les requêtes sans `fields` ont réussi. L'origine précise de l'interprétation au singulier reste à investiguer si besoin.
- Vérification effectuée sur les réponses d'API observées, pas sur le modèle SQL physique.

Les erreurs HTTP 422 initiales liées à `fields` sont conservées séparément dans `resultats/R24/erreurs_422_initiales/` ; elles ne sont pas des échecs des deux filtres testés sans `fields`.

## Fichiers de preuve

- `R24 GET metiersdomaine=F16&contexte=300782&page=1.json`
- `R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json`

## Suite de la cartographie

- R17 : traitement du filtre ROME dans `/secteurs` à clarifier auprès du RCO.
- R18 / R19 : association aux certifications non vérifiable indépendamment ligne à ligne, car aucun identifiant de certification ou de session n'est renvoyé.
- Vérifier éventuellement `mode_competence` avec plusieurs codes de compétences (comportement d'intersection vs union).
