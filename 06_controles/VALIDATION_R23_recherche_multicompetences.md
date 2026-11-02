# API DGEFP–RCO / Octopilot — Contrôle R23 complémentaire
## Recherche multicompétences : `toutes` versus `au_moins_une`

**Date du contrôle :** 1er novembre 2026  
**Périmètre :** endpoint `GET /metiers`, deux compétences `125416` et `103659`  
**Nature de la preuve :** deux réponses JSON issues d'appels via Swagger fournis par l'utilisatrice. Aucun accès direct à l'API ni contrôle SQL.

### 1. Requêtes exécutées

- `GET /metiers?competence=125416,103659&mode_competence=toutes&page=1`
- `GET /metiers?competence=125416,103659&mode_competence=au_moins_une&page=1`

### 2. Résultats observés

| Code ROME | Libellé ROME | Mode `toutes` | Mode `au_moins_une` | `competences_trouvees_codes` en mode `au_moins_une` |
|---|---|---|---|---|
| F1610 | Pose et restauration de couvertures | Présent | Présent | `125416`, `103659` |
| F1705 | Pose de canalisations | Absent | Présent | `125416` |
| I1604 | Mécanique automobile et entretien de véhicules | Absent | Présent | `103659` |

- Mode `toutes` : `total=1`, `page=1`, `page_size=100`, `last_page=1`.
- Mode `au_moins_une` : `total=3`, `page=1`, `page_size=100`, `last_page=1`.
- L'intersection des ensembles des métiers portant chacune des deux compétences est F1610.
- Leur union comprend F1610, F1705 et I1604.
- En mode `au_moins_une`, F1610 possède `nb_competences_trouvees=2` et `nb_macro_competences_trouvees=2` ; F1705 et I1604 ont chacun 1 et 1.

### 3. Variations du schéma de réponse

En mode `au_moins_une`, les objets métier comportent trois champs de correspondance supplémentaires :
- `nb_competences_trouvees` : entier observé (1 ou 2) ;
- `competences_trouvees_codes` : tableau de codes OGR ;
- `nb_macro_competences_trouvees` : entier observé (1 ou 2).

Dans la réponse observée du mode `toutes`, ces trois champs ne sont pas présents. Ne pas conclure qu'ils sont systématiquement absents dans toute configuration future sans autre test.

### 4. Conclusion et limites

**R23 complémentaire : VALIDÉ sur les deux codes testés.** Le comportement observé correspond respectivement à une intersection (`toutes`) et à une union (`au_moins_une`).

Cette validation ne prouve ni la qualité sémantique de tous les rattachements, ni la logique de classement pour d'autres ensembles, ni les relations SQL physiques.

**Vérification complémentaire effective :** `GET /competences?code=103659&page=1` renvoie `competence_libelle = "Poser des panneaux solaires"`, `rome_codes = ["F1610", "I1604"]` et `rome_coeur_metier_codes = []`. La correspondance entre `/competences` et `/metiers` est cohérente sur les échantillons ; sa pertinence métier n'est pas auditée et **aucune erreur de l'API n'est démontrée**.

### 5. Fichiers sources

- `R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json`
- `R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json`
- `GET_competences__code_103659__page_1.json` (libellé et rattachements de la compétence)

**Emplacement recommandé dans le dossier VS Code :** `06_controles/VALIDATION_R23_recherche_multicompetences.md`
