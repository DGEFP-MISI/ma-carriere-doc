# Chaînes d'appels entre ressources — API DGEFP–RCO

Ce document décrit **des correspondances techniques**, sans hypothèse d'usage.

## Identifiants et transferts prévus dans le contrat

| Source | Champ récupéré | Destination | Paramètre transmis | Nature / limite |
|---|---|---|---|---|
| `/metiers` | `rome_code` | `/metiers/{rome}` | `rome` (chemin) | Code ROME V3 |
| `/metiers/{rome}` | `rome_code` | `/metiers/{rome}/competences` | `rome` (chemin) | Code ROME V3 |
| `/metiers/{rome}` | `rome_code` | `/certifications` | `rome` | Relation par `rome_codes` (potentiellement plusieurs métiers par certification) |
| `/metiers/{rome}` | `rome_code` | `/formacodes` | `rome` | Correspondance via table Certif Info ROME × Formacode décrite dans le contrat |
| `/competences` | `competence_code` | `/metiers` | `competence` | Code OGR ; plusieurs codes possibles |
| `/competences` | `competence_code` | `/metiers` | `contexte` ou `sans_contexte` | Seulement si la catégorie correspond à un contexte de travail |
| `/metiers/{rome}` | `metiers_proches_codes[]` | `/metiers/{rome}` | `rome` (chemin) | Codes des métiers proches ; relation de proximité, pas une FK physique |
| `/certifications` | `certifinfo_code` | `/certifications/{certifinfo}` | `certifinfo` (chemin) | Code Certif Info |
| `/certifications` | `fiche_code` | `/certifications/blocs` | `fiche` | Code de fiche RNCP (pour RNCP) |
| `/certifications` | `certifinfo_code` | `/certifications/blocs` | `certifinfo` | Alternative documentée à `fiche` |
| `/certifications` | `formacode_codes[]` | `/formacodes` | `code` | Formacode V14 |
| `/formacodes` | `formacode_code` | `/certifications` | `formacode` | Filtre de certifications |
| `/territoires` | `zonage` + `territoire_code` | `/indicateurs` | `zonage` + `territoire` | Préserver les deux codes, respecter les règles de repli |
| `/metiers/{rome}` | `rome_code` | `/indicateurs` | `rome` | Mesures possibles à différents `grain` (ROME, FAP 225, FAP 228, FAP 87) |
| `/mesures` | `code` / `champs[]` | `/indicateurs` | `fields` | `fields` porte sur les champs de valeur, pas sur le code mesure |

**Note :** cette table donne les chemins documentés, pas une validation de chaque combinaison
ni des tables SQL consultées. `fields`, pagination et paramètres obligatoires supplémentaires
sont disponibles dans `03_catalogue/routes_openapi.csv`.

## Exemple d'enchaînement purement technique

```text
GET /metiers?q=...
  -> items[].rome_code
GET /metiers/{rome}
  -> rome_code, metiers_proches_codes[], formacode_codes[]
GET /certifications?rome={rome_code}
  -> items[].certifinfo_code, items[].fiche_code
GET /certifications/{certifinfo_code}
GET /certifications/blocs?fiche={fiche_code}
```

Cette illustration ne présume pas que tous ces appels sont nécessaires dans une application.

## Règles de lecture des réponses

- Les listes paginées peuvent comporter plusieurs pages (`page`, `last_page`).
- `fields` peut restreindre les champs ; **ne jamais comparer un exemple partiel au schéma entier sans le signaler**.
- `null`, `0`, `[]` et `"secret_stat"` sont distincts.
- `grain` décrit l'unité statistique : **ne pas assimiler une FAP à un ROME unique**.
- `maille_reelle` peut différer du territoire demandé en raison du repli.
- La présence d'un code commun ne démontre pas, à elle seule, une clé étrangère physique.
