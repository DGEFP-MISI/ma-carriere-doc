# Contrat d'interface — API DGEFP (indicateurs emploi-formation)

| | |
|---|---|
| Version du contrat | 0.1.0 (POC) — 19/10/2026 |
| Consommateur | Application d'IA « MaCarrière » (outil grand public), pour la DGEFP |
| Fournisseur | RCO — entrepôt RCO-Octopilot |
| Documentation exécutable | `GET /docs` (interface) et `GET /docs.json` (OpenAPI 3.0, utilisable comme définition d'outils) |

Ce document fixe ce que l'API s'engage à restituer : paramètres, structure des réponses, noms, types et sens des champs,
erreurs. La documentation OpenAPI est générée à partir du même catalogue de champs (`src/Data/ExposedFields.php`) ;
en cas d'écart, le comportement de l'API et `/docs.json` font foi et ce document doit être corrigé.

## 1. Principes

- **Référentiel métier : ROME V3 uniquement.** Les données publiées en ROME 4.0 sont ramenées au ROME V3 parent
  (`rome_v4.code_rome_parent`) ; aucun code ROME 4.0 n'est restitué. C'est le cas des définitions, tags, métiers proches,
  appellations ROME 4.0 et des compétences et contextes de travail (codes OGR). Un ROME V3 regroupe souvent plusieurs
  fiches ROME 4.0 (404 métiers sur 532) : une valeur vaut pour le métier dès qu'**au moins une fiche** la porte ;
  pour les compétences, `tx_fiches_rome4` donne la part des fiches du métier qui la portent.
- **Lecture seule** : uniquement des requêtes `GET`.
- **Format** : JSON UTF-8 (`application/json`), clés triées par ordre alphabétique dans les objets de données.
- **Mise à jour** : les données sont rechargées depuis l'entrepôt par lot (export SQL puis indexation) ; le millésime
  de chaque mesure est donné par `/mesures` et dans chaque entrée de `/indicateurs`.

## 2. Authentification et limites

- Jeton d'API obligatoire sur tous les points d'accès (sauf `/docs`), transmis par
  `Authorization: Bearer <jeton>` ou `X-API-Token: <jeton>`.
- Jeton absent, inconnu, révoqué ou expiré : `401`.
- Limite de débit : **40 requêtes par seconde et par jeton** (fenêtre fixe d'une seconde) ; au-delà : `429`.
- Les identifiants et les données ne doivent pas être transmis à des tiers ; le logo RCO doit figurer sur les supports
  affichant des données de l'API.

## 3. Conventions communes

### Noms de champs

| Motif | Sens | Exemple |
|---|---|---|
| `*_code` | code d'un référentiel | `rome_code`, `fap228_principale_code` |
| `*_libelle` | libellé associé au code | `rome_libelle` |
| `*_codes` / `*_libelles` | listes de codes / libellés, dans le même ordre | `rome_codes`, `rome_libelles` |
| `nb_*` | nombre (entier) | `nb_rome` |
| `tx_*` | taux en pourcentage (décimal, 1 décimale) | `tx_ij_apprentissage_emploi_12m` |
| `indice_*` | indice décimal | `indice_tension_fap228_principale` |
| `date_*` | date `AAAA-MM-JJ` | `date_fin_enregistrement` |
| `tag_*` | booléen | `tag_transition_ecologique` |

Les points d'accès de compatibilité (§ 6) gardent les noms d'origine d'api_entrepot_r3 (`*_lib`, `gd_domaine_*`).

### Valeurs absentes et secret statistique

- Une valeur inconnue ou non disponible vaut **`null`**, jamais `0`. Une liste sans élément vaut `[]`.
  Tous les champs exposés sont présents dans chaque objet, même à `null`.
- **Secret statistique** (l'API alimente un outil grand public) : les champs de type *effectif* et *taux* peuvent valoir
  la chaîne **`"secret_stat"`**. Règles, appliquées par groupe effectif total / sous-effectif / taux :
  1. effectif total de 1 à 4 → `"secret_stat"` ;
  2. sous-effectif de 1 à 4, ou écart effectif total − sous-effectif de 1 à 4 (sinon déductible par différence) → `"secret_stat"` ;
  3. taux → `"secret_stat"` dès que l'une des règles précédentes s'applique au groupe ;
  4. `0` et `null` sont restitués tels quels.

  Groupes : InserJeunes voie scolaire, InserJeunes apprentissage, InserSup, sortants de formation demandeurs
  d'emploi (`nb_de_*`), demandeurs d'emploi (`nb_demandeurs_emploi`, effectif seul).
  Le consommateur doit traiter `"secret_stat"` comme « donnée existante mais non diffusable » et l'afficher comme telle.

### Sélection des champs (`fields`)

- `fields=a,b,c` (noms exposés, séparés par des virgules, `[a-z0-9_]`) restreint la réponse à ces champs, sur les listes
  comme sur les fiches. Sans `fields`, tous les champs exposés sont restitués.
- L'identifiant de la ressource (`rome_code`, `certifinfo_code`) est **toujours** restitué ; l'identifiant technique
  interne n'est jamais restitué.
- Un nom de champ inconnu est refusé (`422`), avec la liste des champs disponibles dans le message.
- Sur les points d'accès d'indicateurs (`/indicateurs`, `/recrutements`, `/salaires`, `/salaires/secteurs`, `/secteurs`,
  `/prospective/metiers`, `/prospective/regions`, `/mobilites`), `fields` porte sur les **champs de valeur** des mesures
  (cf. `/mesures`, attribut `champs`) : les champs de structure (`rang`, `territoire_code`, `maille`, `repli`, en-tête de
  la réponse) sont toujours restitués. Sur `/indicateurs`, seules les mesures qui portent au moins un des champs demandés
  sont restituées (ex : `fields=tension_globale,salaire_net_annuel_median` ne renvoie que les mesures `tension` et
  `salaires`). Sur `/mesures`, `fields` porte sur les attributs du catalogue (`code` toujours restitué).

### Grain des valeurs (`grain`, `nb_rome_famille`)

Chaque mesure porte un `grain` (dans `/mesures`, dans chaque entrée de `/indicateurs` et en tête des réponses de
`/recrutements`, `/salaires`, `/salaires/secteurs`, `/prospective/*`, `/mobilites` et `/secteurs`) : ce pour quoi la
valeur est calculée.

| `grain` | La valeur est calculée pour | Mesures |
|---|---|---|
| `rome` | le métier | demandeurs d'emploi, offres d'emploi (diffusées, collectées, caractéristiques, mensuelles), compétences des offres, statut d'emploi, formations et insertion du métier |
| `fap_228` | une famille professionnelle FAP 2021 (228 postes) | tension, projets de recrutement (BMO), tension de la FAP principale d'une certification |
| `fap_225` | une famille professionnelle FAP 225 | salaires, salaires par secteur, emploi par secteur, mobilités |
| `fap_87` | une famille professionnelle FAP 87 | métiers 2030 |
| `secteur_naf38` | un secteur d'activité | dynamique des secteurs (`/secteurs`) |
| `certification` | une certification | mesures de `/certifications` |

Une valeur par famille (`fap_*`) est **commune à tous les ROME de la famille** : deux métiers d'une même famille ont
la même valeur, qui ne doit pas être présentée comme deux observations. Chacune de ces valeurs porte donc, toujours
(même avec `fields`), `nb_rome_famille` : nombre de ROME V3 de la famille, compté sur la table de passage qui rattache
la valeur au métier. Exemple : la tension de F1610 dans l'Hérault a deux valeurs, « Tension extrême » pour B1X34
(couvreurs, `nb_rome_famille` = 1, propre au métier) et « Tension faible » pour B6X73 (`nb_rome_famille` = 26, commune
à 26 métiers du BTP). `statut_emploi` est au grain `rome`, mais agrège des professions (PCS) partagées avec les autres
métiers des mêmes familles.

### Pagination (listes)

```json
{ "items": [ … ], "total": 532, "page_size": 100, "page": 1, "last_page": 6 }
```
- `page` commence à 1 ; 100 éléments par page.

### Recherche plein texte (`q`)

- 2 à 100 caractères ; accents, majuscules, élisions (`l'`, `d'`) et pluriels sont ignorés ; autocomplétion sur les
  débuts de mots (`couvr` trouve « couvreur »). Tous les mots doivent être présents.
- Avec `q`, les résultats sont triés par pertinence ; sans `q`, par code.
- Seuls lettres, chiffres, espaces, apostrophes et tirets sont pris en compte.

### Erreurs

Format unique :
```json
{
  "message": "Paramètres de requête invalides.",
  "code": 422,
  "violations": [ { "propertyPath": "rome", "message": "Doit être un code ROME V3 : une lettre de A à N suivie de 4 chiffres (ex : \"F1610\")." } ]
}
```

| Code | Cas |
|---|---|
| 400 | paramètre obligatoire manquant (avec `violations`) |
| 401 | jeton absent ou invalide |
| 404 | ressource ou territoire introuvable, route inconnue |
| 422 | paramètre invalide, champ `fields` inconnu (avec `violations`) |
| 429 | limite de débit atteinte |
| 503 | moteur de recherche indisponible |

## 4. Métiers

### `GET /metiers`

Recherche et liste des métiers ROME V3 (532).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `q` | string | non | recherche plein texte sur libellé ROME, appellations (V3 et 4.0) et définitions |
| `grand_domaine` | string | non | code de grand domaine (une lettre `A`–`N`, insensible à la casse) |
| `domaine` | string | non | code de domaine professionnel (lettre + 2 chiffres, ex. `F16`) |
| `competence` | string | non | 1 à 10 codes OGR (6 chiffres, séparés par des virgules) de savoir-faire, savoirs ou savoir-être (`/competences`) : métiers dont au moins une fiche ROME 4.0 porte **chacun** de ces codes |
| `contexte` | string | non | 1 à 10 codes OGR de contextes de travail : métiers dont au moins une fiche ROME 4.0 porte **chacun** de ces contextes |
| `sans_contexte` | string | non | 1 à 10 codes OGR de contextes de travail à éviter : exclut les métiers dont **au moins une** fiche ROME 4.0 porte l'un d'eux (exclusion prudente : un métier dont une seule spécialité travaille de nuit est écarté) |
| `mode_competence` | string | non | `toutes` (défaut) ou `au_moins_une` : avec `au_moins_une`, `competence` garde les métiers qui portent **au moins un** des codes, classés par compétences trouvées (ci-dessous) |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 |

Réponse : liste paginée d'objets *métier* (ci-dessous). Les filtres se combinent entre eux et avec `q`.

**Mode `au_moins_une`** (« quels métiers pour ce que je sais faire ? ») : les métiers sont classés par nombre de
macro-compétences trouvées, puis par nombre de compétences trouvées, puis par code (ou pertinence avec `q`). Une
macro-compétence et ses compétences comptent une fois, pour ne pas compter deux fois un métier qui porte les deux ; un
savoir (sans arborescence) compte pour lui-même. Chaque métier porte en plus, toujours restitués :

| Champ | Type | Définition |
|---|---|---|
| `nb_macro_competences_trouvees` | integer | Nombre de macro-compétences distinctes parmi les codes cités que le métier porte (critère de classement). |
| `nb_competences_trouvees` | integer | Nombre de codes cités que le métier porte. |
| `competences_trouvees_codes` | list | Codes cités que le métier porte, dans l'ordre de la requête. |

Exemple : `GET /metiers?competence=103659,125416,300021&mode_competence=au_moins_une` : 131 métiers (1 seul en mode
`toutes`), F1610 en tête (3 sur 3), puis F1705 (2 sur 3).

Exemple : `GET /metiers?contexte=300783&sans_contexte=300803,023376` (en extérieur, sans travail de nuit ni le week-end) : 44 métiers.

### `GET /metiers/{rome}`

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` (chemin) | string | oui | code ROME V3 `[A-N]` + 4 chiffres, insensible à la casse ; sinon `404` |
| `fields` | string | non | voir § 3 |

Réponse : un objet *métier* ; `404` si le code n'existe pas en ROME V3.

### `GET /domaines`

Arborescence des 14 grands domaines et 110 domaines professionnels du ROME V3 (« quels domaines découvrir ? »).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `grand_domaine` | string | non | ne restituer que ce grand domaine (une lettre) |

Réponse : `{ "items": [ … ], "total": 14 }` (non paginée), chaque grand domaine portant `grand_domaine_code`,
`grand_domaine_libelle`, `nb_metiers` et `domaines` (liste de `{ domaine_code, domaine_libelle, nb_metiers }`, par code).
Les métiers d'un domaine s'obtiennent par `GET /metiers?domaine=`.

Exemple (`GET /domaines?grand_domaine=F`, extrait) :
```json
{
  "items": [
    { "grand_domaine_code": "F", "grand_domaine_libelle": "Construction, Bâtiment et Travaux publics", "nb_metiers": 38,
      "domaines": [ { "domaine_code": "F11", "domaine_libelle": "Conception et études", "nb_metiers": 8 }, "…" ] }
  ],
  "total": 1
}
```

### `GET /metiers/{rome}/competences`

Savoir-faire, savoirs, savoir-être et contextes de travail du référentiel ROME 4.0 (codes OGR) des fiches rattachées au
ROME V3, avec l'arborescence des compétences (domaine, enjeu, macro-compétence). Répond à « que recouvre mon métier ? »,
« quelles conditions de travail ? » et, avec `depuis`, « quelles compétences réutiliser ou acquérir ? ».

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` (chemin) | string | oui | code ROME V3 du métier (le métier visé avec `depuis`) ; `404` s'il n'existe pas |
| `categorie` | string | non | `savoir_faire`, `savoir`, `savoir_etre` ou `contexte_travail` ; toutes par défaut (avec `depuis` : toutes sauf les contextes) |
| `coeur_metier` | boolean | non | `true` : seulement les savoir-faire et savoirs « cœur de métier » |
| `depuis` | string | non | code ROME V3 du métier de départ ; `404` s'il n'existe pas |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 (100 par page) |

Réponse : `rome_code`, `rome_libelle`, puis la liste paginée (`items`, `total`, `page_size`, `page`, `last_page`),
triée par catégorie (savoir-faire, savoirs, savoir-être, contextes), part des fiches décroissante, puis code ;
`competence_code` toujours restitué. Avec `depuis`, chaque compétence porte `tag_acquise` (aussi portée par le métier
de départ : réutilisable ; sinon à acquérir) et `tag_meme_macro_competence` (à acquérir, mais de même macro-compétence
qu'une compétence du métier de départ : compétence voisine), et la réponse ajoute `comparaison` : `rome_code_depuis`,
`rome_libelle_depuis`, `nb_competences`, `nb_acquises`, `nb_a_acquerir`, `nb_a_acquerir_meme_macro_competence`,
`tx_acquises` (%), `nb_coeur_metier`, `nb_coeur_metier_acquises`, `nb_coeur_metier_meme_macro_competence`, puis le
compte par macro-compétence (une macro-compétence et ses compétences comptent une fois, un savoir pour lui-même) :
`nb_macro_competences`, `nb_macro_competences_communes` (le métier de départ porte l'une d'elles),
`tx_macro_competences_communes` (%). Sans `depuis`, `tag_acquise` et `tag_meme_macro_competence` valent `null`.

**Lecture de `tx_fiches_rome4`** : 100 = la compétence vaut pour tout le métier ; moins = elle est propre à certaines
de ses spécialités (fiches ROME 4.0). 85 % des liens métier × compétence sont dans ce cas. Une compétence « acquise »
signifie qu'au moins une fiche du métier de départ la porte, pas que la personne la maîtrise.

| Champ | Type | Définition |
|---|---|---|
| `competence_code` | string | Code OGR de la compétence ou du contexte de travail (référentiel ROME 4.0 ; identifiant, toujours restitué ; cf. /competences). |
| `competence_libelle` | string | Libellé de la compétence ou du contexte de travail. |
| `categorie_competence_code` | string | Catégorie : savoir_faire, savoir, savoir_etre, contexte_travail. |
| `categorie_competence_libelle` | string | Libellé de la catégorie. |
| `tag_coeur_metier` | boolean | Savoir-faire ou savoir « cœur de métier » (compétence principale) pour au moins une fiche ROME 4.0 rattachée ; null pour les savoir-être et les contextes de travail. |
| `macro_competence_code` | string | Savoir-faire et savoir-être : code OGR de la macro-compétence de l'arborescence ROME 4.0 (le code lui-même pour une macro-compétence). |
| `macro_competence_libelle` | string | Libellé de la macro-compétence. |
| `enjeu_competence_code` | string | Savoir-faire et savoir-être : code de l'enjeu de l'arborescence des compétences. |
| `enjeu_competence_libelle` | string | Libellé de l'enjeu. |
| `domaine_competence_code` | string | Savoir-faire et savoir-être : code du domaine de compétences (1 à 6). |
| `domaine_competence_libelle` | string | Libellé du domaine de compétences. |
| `nb_fiches_rome4` | integer | Nombre de fiches ROME 4.0 rattachées au métier qui portent la compétence ou le contexte. |
| `nb_fiches_rome4_metier` | integer | Nombre de fiches ROME 4.0 rattachées au métier ROME V3. |
| `tx_fiches_rome4` | number | Part des fiches ROME 4.0 du métier qui portent la compétence ou le contexte (%) : 100 = vrai pour tout le métier, moins = propre à certaines de ses spécialités. |
| `tag_acquise` | boolean | Avec `depuis` : compétence aussi portée par le métier de départ (réutilisable), sinon à acquérir. |
| `tag_meme_macro_competence` | boolean | Avec `depuis` : compétence à acquérir, mais de même macro-compétence qu'une compétence du métier de départ (correspondance indirecte, compétence voisine). |
| `source_libelle` | string | Source des données. |

Exemple (`GET /metiers/F1613/competences?depuis=F1610&categorie=savoir_faire`, extrait) :
```json
{
  "rome_code": "F1613",
  "rome_libelle": "Travaux d'étanchéité et d'isolation",
  "comparaison": { "rome_code_depuis": "F1610", "rome_libelle_depuis": "Pose et restauration de couvertures",
    "nb_competences": 74, "nb_acquises": 12, "nb_a_acquerir": 62, "nb_a_acquerir_meme_macro_competence": 27,
    "tx_acquises": 16.2, "nb_coeur_metier": 34, "nb_coeur_metier_acquises": 5,
    "nb_coeur_metier_meme_macro_competence": 15, "nb_macro_competences": 54, "nb_macro_competences_communes": 25,
    "tx_macro_competences_communes": 46.3 },
  "items": [
    { "categorie_competence_code": "savoir_faire", "categorie_competence_libelle": "Savoir-faire",
      "competence_code": "119936", "competence_libelle": "Implanter une zone de chantier",
      "domaine_competence_code": "3", "domaine_competence_libelle": "Production, Construction, Qualité, Logistique",
      "enjeu_competence_code": "3D", "enjeu_competence_libelle": "Construction",
      "macro_competence_code": "300236", "macro_competence_libelle": "Préparer l'exécution du chantier",
      "nb_fiches_rome4": 3, "nb_fiches_rome4_metier": 3, "tag_acquise": false, "tag_coeur_metier": true,
      "tag_meme_macro_competence": true,
      "tx_fiches_rome4": 100, "source_libelle": "…" }
  ],
  "total": 74, "page_size": 100, "page": 1, "last_page": 1
}
```

### `GET /competences`

Référentiel des 32 208 savoir-faire, savoirs, savoir-être et contextes de travail du ROME 4.0 (codes OGR) cités par au
moins une fiche, avec les métiers ROME V3 qui les portent. Sert à trouver un métier à partir de ce que l'on sait faire
(« je cherche un métier sans connaître son nom ») : le `competence_code` se passe à `/metiers` (`competence`,
`contexte`, `sans_contexte`).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `q` | string | non | recherche plein texte dans le libellé (autocomplétion dès 2 lettres ; ex. `soudure`, `travail de nuit`) |
| `categorie` | string | non | `savoir_faire`, `savoir`, `savoir_etre` ou `contexte_travail` |
| `rome` | string | non | compétences portées par au moins une fiche ROME 4.0 du ROME V3 |
| `domaine` | string | non | domaine de compétences (`1` à `6`) |
| `enjeu` | string | non | enjeu de l'arborescence (chiffre du domaine et lettre, ex. `3D`) |
| `macro_competence` | string | non | code OGR de la macro-compétence (6 chiffres) |
| `code` | string | non | 1 à 10 codes OGR (6 chiffres, séparés par des virgules) : avec `rome_codes`, index inverse (métiers de chaque code) en un appel |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 |

Réponse : liste paginée, triée par code sans `q` ; `competence_code` toujours restitué. L'arborescence (domaine, enjeu,
macro-compétence) n'existe que pour les savoir-faire et les savoir-être : `null` pour les savoirs et les contextes.

| Champ | Type | Définition |
|---|---|---|
| `competence_code` | string | Code OGR de la compétence ou du contexte de travail (référentiel ROME 4.0 ; identifiant, toujours restitué). |
| `competence_libelle` | string | Libellé de la compétence ou du contexte de travail. |
| `categorie_competence_code` | string | Catégorie : savoir_faire, savoir, savoir_etre, contexte_travail. |
| `categorie_competence_libelle` | string | Libellé de la catégorie. |
| `macro_competence_code` | string | Savoir-faire et savoir-être : code OGR de la macro-compétence de l'arborescence ROME 4.0. |
| `macro_competence_libelle` | string | Libellé de la macro-compétence. |
| `enjeu_competence_code` | string | Savoir-faire et savoir-être : code de l'enjeu de l'arborescence des compétences. |
| `enjeu_competence_libelle` | string | Libellé de l'enjeu. |
| `domaine_competence_code` | string | Savoir-faire et savoir-être : code du domaine de compétences (1 à 6). |
| `domaine_competence_libelle` | string | Libellé du domaine de compétences. |
| `nb_metiers` | integer | Nombre de métiers ROME V3 dont au moins une fiche ROME 4.0 porte la compétence. |
| `rome_codes` | list | Codes ROME V3 de ces métiers (cf. /metiers?competence=). |
| `rome_libelles` | list | Libellés des ROME V3, dans le même ordre. |
| `rome_coeur_metier_codes` | list | Savoir-faire et savoirs : codes ROME V3 pour lesquels la compétence est « cœur de métier » (au moins une fiche ROME 4.0). |
| `source_libelle` | string | Source des données. |

### Objet *métier*

| Champ | Type | Définition |
|---|---|---|
| `rome_code` | string | Code ROME V3 (identifiant, toujours restitué). |
| `rome_libelle` | string | Libellé ROME V3. |
| `domaine_code` | string | Code du domaine professionnel ROME (lettre + 2 chiffres). |
| `domaine_libelle` | string | Libellé du domaine professionnel. |
| `grand_domaine_code` | string | Code du grand domaine ROME (lettre). |
| `grand_domaine_libelle` | string | Libellé du grand domaine. |
| `appellations` | list | Appellations du métier : appellations ROME V3 et appellations des ROME 4.0 rattachés. |
| `definitions` | list | Définitions des ROME 4.0 rattachés, sous la forme « libellé ROME 4.0 : définition ». |
| `tag_transition_ecologique` | boolean | Emploi vert ou stratégique pour la transition écologique (au moins un ROME 4.0 rattaché). |
| `tag_transition_numerique` | boolean | Métier concerné par la transition numérique (au moins un ROME 4.0 rattaché). |
| `tag_transition_demographique` | boolean | Métier concerné par la transition démographique (au moins un ROME 4.0 rattaché). |
| `tag_emploi_reglemente` | boolean | Emploi réglementé (au moins un ROME 4.0 rattaché). |
| `tag_emploi_cadre` | boolean | Emploi de cadre (au moins un ROME 4.0 rattaché). |
| `metiers_proches_codes` | list | Codes ROME V3 des métiers proches (mobilités ROME 4.0 ramenées au ROME V3), du plus proche au moins proche : meilleur rang de proximité parmi les fiches ROME 4.0 du métier. |
| `metiers_proches_libelles` | list | Libellés des métiers proches, dans le même ordre que metiers_proches_codes. |
| `savoir_etre_libelles` | list | Savoir-être professionnels du référentiel ROME 4.0 (au moins une fiche ROME 4.0 rattachée), des plus fréquents aux moins fréquents parmi les fiches du métier (détail : /metiers/{rome}/competences). |
| `contexte_travail_codes` | list | Codes OGR des contextes de travail du référentiel ROME 4.0 (horaires, lieux, conditions, statut, clientèle...) portés par au moins une fiche ROME 4.0 rattachée, des plus fréquents aux moins fréquents (part des fiches : /metiers/{rome}/competences?categorie=contexte_travail). |
| `contexte_travail_libelles` | list | Libellés des contextes de travail, dans le même ordre que contexte_travail_codes. |
| `fap228_codes` | list | Codes FAP 2021 (228 postes) liés au ROME V3 (table de passage DARES). |
| `formacode_codes` | list | Formacodes V14 liés au ROME V3 (table Certif Info) : thèmes de formation pour se former au métier ou à une de ses compétences, y compris hors certification (cf. /formacodes). |
| `formacode_libelles` | list | Libellés des Formacodes liés, dans le même ordre. |
| `source_libelle` | string | Sources des données. |

Exemple (`GET /metiers/F1610`, listes tronquées) :
```json
{
  "appellations": ["Aide couvreur / Aide couvreuse", "Artisan couvreur / Artisane couvreuse", "…"],
  "contexte_travail_codes": ["038055", "300778", "300779", "…"],
  "contexte_travail_libelles": ["Port d'équipement de protection individuelle (EPI) : gants, chaussures, casque, protections auditives", "Au domicile d'un particulier", "Déplacements professionnels", "…"],
  "definitions": ["… : …"],
  "domaine_code": "F16",
  "domaine_libelle": "Second oeuvre",
  "fap228_codes": ["B1X34", "B6X73"],
  "grand_domaine_code": "F",
  "grand_domaine_libelle": "Construction, Bâtiment et Travaux publics",
  "metiers_proches_codes": ["F1605", "F1613", "F1106"],
  "metiers_proches_libelles": ["Montage de réseaux électriques et télécoms", "Travaux d'étanchéité et d'isolation", "Ingénierie et études du BTP"],
  "rome_code": "F1610",
  "rome_libelle": "Pose et restauration de couvertures",
  "savoir_etre_libelles": ["Avoir l'esprit d'équipe", "Faire preuve de rigueur et de précision", "…"],
  "source_libelle": "France Travail - ROME V3 et ROME 4.0 (dont compétences et contextes de travail) ; DARES - table FAP 2021 x ROME",
  "tag_emploi_cadre": false,
  "tag_emploi_reglemente": false,
  "tag_transition_demographique": false,
  "tag_transition_ecologique": true,
  "tag_transition_numerique": false
}
```

## 5. Certifications

Certifications **actives** au sens France compétences (RNCP et RS), une par code Certif Info (6 862).

### `GET /certifications`

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | non | code ROME V3 lié (`[A-N]` + 4 chiffres) |
| `repertoire` | string | non | `RNCP` ou `RS` |
| `formacode` | string | non | code Formacode V14 lié (3 à 5 chiffres, cf. `/formacodes`) |
| `acces` | string | non | voie d'accès : `formation_initiale`, `apprentissage`, `formation_continue`, `contrat_professionnalisation`, `candidature_individuelle`, `vae` |
| `validation_partielle` | booléen | non | `true` : certifications validables partiellement (blocs RNCP, validation partielle RS) |
| `q` | string | non | recherche plein texte sur intitulés de la fiche et de la certification |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 |

Réponse : liste paginée d'objets *certification*, triée par `fiche_code` sans `q`.

### `GET /certifications/{certifinfo}`

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `certifinfo` (chemin) | string | oui | code Certif Info (chiffres) |
| `fields` | string | non | voir § 3 |

Réponse : un objet *certification* ; `404` si le code ne correspond à aucune certification active.

### `GET /certifications/blocs`

Blocs de compétences des certifications RNCP actives (20 914 blocs, 4 156 fiches). Chaque bloc peut être évalué et validé
séparément : certification partielle, VAE par bloc, parcours de formation par bloc. Le RS n'a pas de blocs. 1 228 fiches
RNCP actives n'ont pas de bloc publié dans la source.

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `certifinfo` | string | non | code Certif Info de la certification |
| `fiche` | string | non | code de fiche RNCP (`RNCP38362`) |
| `rome` | string | non | code ROME V3 lié à la certification |
| `q` | string | non | recherche plein texte dans l'intitulé et les compétences du bloc (« quelle certification valide cette compétence ? ») |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 |

Réponse : liste paginée de blocs, triée par fiche puis `rang_bloc` sans `q` ; `bloc_code` toujours restitué.

| Champ | Type | Définition |
|---|---|---|
| `bloc_code` | string | Code du bloc de compétences (identifiant, toujours restitué), ex : RNCP37099BC01. |
| `rang_bloc` | integer | Rang du bloc dans la fiche (ordre des codes). |
| `bloc_libelle` | string | Intitulé du bloc. |
| `competences` | string | Compétences du bloc (texte de la fiche France compétences). |
| `modalites_evaluation` | string | Modalités d'évaluation du bloc. |
| `fiche_code` | string | Code de la fiche RNCP (ex : RNCP37099). |
| `fiche_libelle` | string | Intitulé de la fiche RNCP. |
| `niveau_certification_code` | string | Niveau du cadre national des certifications (NIV3 à NIV8). |
| `certifinfo_codes` | list | Codes Certif Info de la certification (cf. /certifications/{certifinfo}). |
| `rome_codes` | list | Codes ROME V3 liés à la certification. |
| `source_libelle` | string | Source des données. |

Exemple (`GET /certifications/blocs?certifinfo=117293&fields=bloc_code,rang_bloc,bloc_libelle`, extrait) :
```json
{
  "items": [
    { "bloc_code": "RNCP38362BC01", "bloc_libelle": "Développement de la relation client et vente conseil", "rang_bloc": 1 },
    { "bloc_code": "RNCP38362BC04", "bloc_libelle": "Management de l'équipe commerciale", "rang_bloc": 4 }
  ],
  "total": 4, "page_size": 100, "page": 1, "last_page": 1
}
```

### Objet *certification*

Les indicateurs d'insertion sont nationaux. Types *effectif* et *taux* : voir secret statistique (§ 3).

Inscrits, examens, diplômés, Affelnet et Parcoursup sont nationaux ; une source qui cite un ancien code Certif Info est
rattachée à son successeur (`code_successeur`, un niveau), par exemple l'ancien BTS MCO 104239 au BTS MCO 117293.
Parcoursup compte des **candidatures** (un candidat compte dans chaque formation où il postule), non des personnes.

| Champ | Type | Définition |
|---|---|---|
| `certifinfo_code` | string | Code Certif Info (identifiant, toujours restitué). |
| `certifinfo_libelle` | string | Intitulé Certif Info de la certification. |
| `etat_certifinfo_libelle` | string | État de la fiche Certif Info. |
| `type_certification_libelle` | string | Type de certification (diplôme, titre, CQP, certification RS...). |
| `certificateur_libelle` | string | Certificateur(s). |
| `repertoire_code` | string | Répertoire France compétences : RNCP ou RS. |
| `fiche_code` | string | Numéro de fiche France compétences (ex : RNCP36101, RS5823). |
| `fiche_libelle` | string | Intitulé de la fiche France compétences. |
| `type_enregistrement_libelle` | string | Type d'enregistrement (de droit, sur demande...). |
| `date_fin_enregistrement` | date | Date de fin d'enregistrement de la fiche. |
| `niveau_certification_code` | string | Niveau européen (NIV3 à NIV8) ; absent pour la plupart des fiches RS. |
| `nsf_code` | string | Code NSF (spécialité de formation). |
| `nsf_libelle` | string | Libellé NSF. |
| `formacode_principal_code` | string | Formacode principal. |
| `formacode_principal_libelle` | string | Libellé du Formacode principal. |
| `formacode_codes` | list | Formacodes V14 liés à la certification, Formacode principal en premier (à passer à /formacodes ou à la recherche de formations par Formacode). |
| `formacode_libelles` | list | Libellés des Formacodes liés, dans le même ordre. |
| `tag_acces_formation_initiale` | boolean | Accessible après un parcours de formation sous statut d'élève ou d'étudiant (France compétences). |
| `tag_acces_apprentissage` | boolean | Accessible en contrat d'apprentissage. |
| `tag_acces_formation_continue` | boolean | Accessible après un parcours de formation continue. |
| `tag_acces_contrat_professionnalisation` | boolean | Accessible en contrat de professionnalisation. |
| `tag_acces_candidature_individuelle` | boolean | Accessible par candidature individuelle (sans parcours de formation). |
| `tag_acces_vae` | boolean | Accessible par la validation des acquis de l'expérience (VAE), selon la fiche France compétences. |
| `nb_blocs_competences` | integer | RNCP : nombre de blocs de compétences (null : aucun bloc publié, et pour le RS). |
| `bloc_competences_codes` | list | RNCP : codes des blocs de compétences (détail : /certifications/blocs). |
| `bloc_competences_libelles` | list | RNCP : intitulés des blocs de compétences, dans le même ordre. |
| `tag_validation_partielle` | boolean | Certification validable partiellement : RNCP avec blocs de compétences (chaque bloc est évalué et validé séparément), ou fiche RS déclarant une validation partielle ; null : RNCP sans bloc publié. |
| `nb_rome` | integer | Nombre de ROME V3 liés. |
| `rome_code` | string | Code ROME V3 lorsque la certification n'en a qu'un, sinon null (voir rome_codes). |
| `rome_libelle` | string | Libellé du ROME V3 lorsqu'il est unique, sinon null. |
| `rome_codes` | list | Codes ROME V3 liés. |
| `rome_libelles` | list | Libellés des ROME V3 liés, dans le même ordre que rome_codes. |
| `fap228_principale_code` | string | FAP 228 principale : FAP atteinte par le plus de ROME V3 de la certification compatibles avec son niveau, puis plus fort emploi moyen. |
| `fap228_principale_libelle` | string | Libellé de la FAP 228 principale. |
| `fap228_methode_libelle` | string | Méthode de choix de la FAP principale : « FAP unique », « majoritaire via ROME V3 », « egalite ROME V3 : plus fort emploi », « aucun ROME V3 commun : plus fort emploi ». |
| `nb_fap228` | integer | Nombre de FAP 228 liées. |
| `fap228_codes` | list | Codes FAP 228 liés. |
| `indice_tension_fap228_principale` | number | Indicateur de tension national (DARES - France Travail 2024) de la FAP principale. |
| `tension_discret_fap228_principale` | string | Niveau de tension discret de la FAP principale, du plus faible au plus fort : 1, 2, 3, 4, 5.1, 5.2. |
| `tension_niveau_max` | string | Niveau de tension le plus élevé parmi les FAP liées, sans décimale (1 à 5). |
| `nb_fap228_tension_4_et_plus` | integer | Nombre de FAP liées de niveau de tension 4 ou plus. |
| `tension_discret_par_fap228` | string | Niveau de tension de chaque FAP liée, au format « code:niveau » séparés par des virgules (ex : « B1X34:5.2 »). |
| `nb_ij_scolaire_sortants` | effectif | InserJeunes, voie scolaire : sortants (cumul 2023-2024, national). |
| `nb_ij_scolaire_emploi_12m` | effectif | InserJeunes, voie scolaire : sortants en emploi salarié à 12 mois. |
| `tx_ij_scolaire_emploi_12m` | taux | InserJeunes, voie scolaire : taux d'emploi à 12 mois (%). |
| `nb_ij_apprentissage_sortants` | effectif | InserJeunes, apprentissage : sortants (cumul 2023-2024, national). |
| `nb_ij_apprentissage_emploi_12m` | effectif | InserJeunes, apprentissage : sortants en emploi salarié à 12 mois. |
| `tx_ij_apprentissage_emploi_12m` | taux | InserJeunes, apprentissage : taux d'emploi à 12 mois (%). |
| `nb_ij_scolaire_annee_terminale` | effectif | InserJeunes, voie scolaire : inscrits en année terminale (poursuivants + sortants, cumul 2023-2024, national). |
| `nb_ij_scolaire_poursuite_etudes` | effectif | InserJeunes, voie scolaire : inscrits en année terminale qui poursuivent leurs études l'année suivante. |
| `tx_ij_scolaire_poursuite_etudes` | taux | InserJeunes, voie scolaire : taux de poursuite d'études (%). |
| `nb_ij_apprentissage_annee_terminale` | effectif | InserJeunes, apprentissage : inscrits en année terminale (poursuivants + sortants, cumul 2023-2024, national). |
| `nb_ij_apprentissage_poursuite_etudes` | effectif | InserJeunes, apprentissage : inscrits en année terminale qui poursuivent leurs études l'année suivante. |
| `tx_ij_apprentissage_poursuite_etudes` | taux | InserJeunes, apprentissage : taux de poursuite d'études (%). |
| `promotion_insersup_libelle` | string | InserSup : promotion des taux d'emploi : « 2024 », ou « 2023/2024 » (cumul de deux promotions pour un diplôme de moins de 20 sortants). |
| `nb_insersup_diplomes` | effectif | InserSup : diplômés de la promotion sortis des études, hors poursuivants (diffusion 2025_S2, niveau national) : base du taux d'emploi. |
| `nb_insersup_emploi_salarie_12m` | effectif | InserSup : diplômés en emploi salarié à 12 mois. |
| `tx_insersup_emploi_salarie_12m` | taux | InserSup : taux d'emploi salarié à 12 mois (%). |
| `nb_insersup_diplomes_ensemble` | effectif | InserSup : diplômés de la promotion, sortants et poursuivants (diplômes dont les poursuivants sont publiés). |
| `nb_insersup_poursuivants` | effectif | InserSup : diplômés qui poursuivent des études l'année suivante. |
| `tx_insersup_poursuite_etudes` | taux | InserSup : taux de poursuite d'études des diplômés (%). |
| `nb_insersup_salaire_base_12m` | integer | InserSup : diplômés 2022 en emploi salarié à 12 mois, base des salaires à 12 mois. |
| `salaire_insersup_q1_12m` | integer | InserSup : 1er quartile du salaire mensuel net à 12 mois (euros, diplômés 2022). |
| `salaire_insersup_median_12m` | integer | InserSup : salaire mensuel net médian à 12 mois (euros, diplômés 2022). |
| `salaire_insersup_q3_12m` | integer | InserSup : 3e quartile du salaire mensuel net à 12 mois (euros, diplômés 2022). |
| `salaire_insersup_q1_18m` | integer | InserSup : 1er quartile du salaire mensuel net à 18 mois (euros, diplômés 2022). |
| `salaire_insersup_median_18m` | integer | InserSup : salaire mensuel net médian à 18 mois (euros, diplômés 2022). |
| `salaire_insersup_q3_18m` | integer | InserSup : 3e quartile du salaire mensuel net à 18 mois (euros, diplômés 2022). |
| `salaire_insersup_q1_30m` | integer | InserSup : 1er quartile du salaire mensuel net à 30 mois (euros, diplômés 2021). |
| `salaire_insersup_median_30m` | integer | InserSup : salaire mensuel net médian à 30 mois (euros, diplômés 2021). |
| `salaire_insersup_q3_30m` | integer | InserSup : 3e quartile du salaire mensuel net à 30 mois (euros, diplômés 2021). |
| `nb_de_sortants` | effectif | France Travail : demandeurs d'emploi sortis de formation en 2024. |
| `nb_de_acces_emploi_6m` | effectif | France Travail : demandeurs d'emploi formés ayant accédé à l'emploi dans les 6 mois. |
| `tx_de_acces_emploi_6m` | taux | France Travail : taux d'accès à l'emploi à 6 mois des demandeurs d'emploi formés (%). |
| `nb_de_abandons` | effectif | France Travail : demandeurs d'emploi sortis de formation en 2024 qui l'ont abandonnée avant son terme. |
| `tx_de_abandons` | taux | France Travail : taux d'abandon de formation des demandeurs d'emploi (%). |
| `nb_inscrits_voie_scolaire` | effectif | Inscrits en voie scolaire, toutes années de la formation (DEPP, rentrée 2023, national). |
| `nb_inscrits_apprentissage` | effectif | Apprentis inscrits (DEPP, rentrée 2023, national). |
| `nb_inscrits_enseignement_sup` | effectif | Inscrits dans l'enseignement supérieur (SIES, rentrée 2024, national). |
| `nb_inscrits_sanitaire_social` | effectif | Inscrits en formation sanitaire et sociale (DREES, rentrée 2024, national). |
| `nb_entrees_formation_de` | effectif | Demandeurs d'emploi entrés en formation (France Travail, 2025, national). |
| `nb_examen_presents` | effectif | Candidats présents à l'examen de l'Éducation nationale, toutes situations (scolaire, apprentissage, formation continue, individuel ; DEPP, session 2023). |
| `nb_examen_admis` | effectif | Candidats admis à l'examen de l'Éducation nationale (DEPP, session 2023). |
| `tx_examen_reussite` | taux | Taux de réussite à l'examen de l'Éducation nationale : admis / présents (%). |
| `nb_diplomes_enseignement_sup` | effectif | Diplômés de l'enseignement supérieur (SIES, session 2023, national). |
| `nb_sanitaire_social_presents` | effectif | Candidats présents au diplôme sanitaire et social (DREES, 2024). |
| `nb_diplomes_sanitaire_social` | effectif | Diplômés sanitaires et sociaux (DREES, 2024). |
| `tx_sanitaire_social_reussite` | taux | Taux de réussite au diplôme sanitaire et social : diplômés / présents (%). |
| `nb_affelnet_places` | integer | Affelnet (voie scolaire après la 3e, rentrée 2025) : places offertes (capacité de la carte scolaire). |
| `nb_affelnet_voeux_1` | effectif | Affelnet : demandes en vœu de rang 1. |
| `indice_affelnet_pression` | taux | Affelnet : vœux de rang 1 par place (> 1 : plus de demandes que de places). |
| `nb_parcoursup_places` | integer | Parcoursup (session 2025) : places offertes. |
| `nb_parcoursup_candidatures` | integer | Parcoursup : candidatures (un candidat compte dans chaque formation où il postule). |
| `nb_parcoursup_admis` | effectif | Parcoursup : candidats ayant accepté une proposition d'admission. |
| `indice_parcoursup_candidatures_par_place` | number | Parcoursup : candidatures par place. |
| `tag_renovation_energetique_batiment` | boolean | Certification liée à une thématique de rénovation énergétique des bâtiments. |
| `thematique_reb_libelle` | string | Thématiques de rénovation énergétique des bâtiments, séparées par « \| ». |
| `tag_transition_ecologique` | boolean | Formacode principal relevant de la transition écologique et énergétique. |
| `source_libelle` | string | Sources des données. |

Exemple (`GET /certifications/112561?fields=fiche_code,nb_ij_apprentissage_sortants,tx_ij_apprentissage_emploi_12m,tension_discret_fap228_principale`) :
```json
{
  "certifinfo_code": "112561",
  "fiche_code": "RNCP36101",
  "nb_ij_apprentissage_sortants": 314,
  "tension_discret_fap228_principale": "5.2",
  "tx_ij_apprentissage_emploi_12m": 68.5
}
```

### `GET /formacodes`

Formacodes V14 (thésaurus de la formation, Centre Inffo, 3 663 codes) : thèmes de formation, pour se former à une compétence
sans changer de métier ou retrouver des formations sans code certifiant. Le `formacode_code` se passe à `/certifications`
(`formacode`) ou à la recherche de formations par Formacode de l'offre de formation (API Offre Info, hors de cette API).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `q` | string | non | recherche plein texte dans le libellé (autocomplétion dès 2 lettres) |
| `rome` | string | non | Formacodes liés au ROME V3 (table Certif Info ROME V3 × Formacode, 530 ROME) |
| `domaine` | string | non | code du domaine Formacode (`107` industrie… ; `50000` à `90000` : certifications, pays, logiciels, publics, mots-outils) |
| `code` | string | non | code Formacode |
| `fields` | string | non | voir § 3 |
| `page` | entier | non | ≥ 1, défaut 1 |

Réponse : liste paginée, triée par code sans `q` ; `formacode_code` toujours restitué.

| Champ | Type | Définition |
|---|---|---|
| `formacode_code` | string | Code Formacode V14 (identifiant, toujours restitué). |
| `formacode_libelle` | string | Libellé du Formacode. |
| `sous_domaine_formacode_code` | string | Code du sous-domaine Formacode. |
| `sous_domaine_formacode_libelle` | string | Libellé du sous-domaine Formacode. |
| `domaine_formacode_code` | string | Code du domaine Formacode. |
| `domaine_formacode_libelle` | string | Libellé du domaine Formacode. |
| `tag_transition_ecologique` | boolean | Formacode relevant de la transition écologique et énergétique. |
| `tag_numerique` | boolean | Formacode relevant du numérique. |
| `tag_sanitaire_social` | boolean | Formacode relevant du sanitaire et social. |
| `rome_codes` | list | Codes ROME V3 liés au Formacode (table Certif Info ROME V3 x Formacode). |
| `rome_libelles` | list | Libellés des ROME V3 liés, dans le même ordre. |
| `nb_certifications` | integer | Certifications actives (RNCP / RS) rattachées au Formacode (cf. /certifications?formacode=). |
| `nb_certifications_formacode_principal` | integer | Dont certifications dont c'est le Formacode principal. |
| `source_libelle` | string | Sources des données. |

## 6. Indicateurs territoriaux

### `GET /territoires`

Recherche et autocomplétion des territoires, dont le `territoire_code` se passe ensuite à `/indicateurs`
(`zonage` = `zonage` du territoire, `territoire` = `territoire_code`). Liste paginée, `fields` possible.

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `q` | string | non | texte recherché dans le nom (autocomplétion dès les premières lettres, accents et casse ignorés) |
| `zonage` | string | non | `region`, `departement`, `clpe`, `commune` |
| `region`, `departement`, `clpe` | string | non | territoires de cette région, de ce département, communes de cette CLPE |
| `code` | string | non | code exact (région, département, CLPE, commune INSEE) |

Ordre : pertinence, puis, à pertinence égale, régions, départements, CLPE et communes ; les communes des plus urbaines aux
plus rurales (grille de densité INSEE, à défaut de population dans l'entrepôt). Sans `q` : même ordre, puis par code.

| Champ | Type | Définition |
|---|---|---|
| `zonage` | string | `region`, `departement`, `clpe`, `commune` |
| `territoire_code`, `territoire_libelle` | string | territoire (toujours restitué) ; commune : code INSEE à 5 caractères |
| `region_code`, `region_libelle`, `departement_code`, `departement_libelle` | string\|null | territoires parents (un département ou une CLPE porte aussi sa région) |
| `clpe_code`, `clpe_libelle` | string\|null | CLPE (comité local pour l'emploi, France Travail) de la commune, ou la CLPE elle-même |
| `zone_emploi_code`, `zone_emploi_libelle` | string\|null | commune : zone d'emploi INSEE 2020 |
| `epci_code`, `epci_libelle` | string\|null | commune : intercommunalité |
| `densite_libelle` | string\|null | commune : grille communale de densité INSEE |
| `commune_codes` | list | CLPE : codes INSEE de ses communes (liste vide pour les autres territoires) |
| `nb_communes` | integer\|null | CLPE : nombre de ses communes |

Référentiel : communes INSEE 2026, arrondissements municipaux de Paris, Lyon et Marseille compris ; les anciennes
communes fusionnées ne sont pas reprises. Pas de code postal. Une CLPE est rattachée au département qui porte le plus de
ses communes ; elle porte la liste de toutes ses communes (`commune_codes`, de 1 à 357 communes : pour une
autocomplétion, l'écarter avec `fields`). Les collectivités d'outre-mer n'ont qu'une région et un département ; les pays étrangers sont exclus.
Deux communes homonymes se distinguent par leur département.

```
GET /territoires?q=montp
{ "items": [
  { "zonage": "clpe", "territoire_code": "CLPE34003", "territoire_libelle": "Montpellier", "region_code": "76", "departement_code": "34", "clpe_code": "CLPE34003", ... },
  { "zonage": "commune", "territoire_code": "34172", "territoire_libelle": "Montpellier", "departement_code": "34", "clpe_code": "CLPE34003",
    "zone_emploi_libelle": "Montpellier", "epci_libelle": "Montpellier Méditerranée Métropole", "densite_libelle": "Grands centres urbains", ... }, ... ],
  "total": 25, ... }
```

### `GET /indicateurs`

Tension, demandeurs d'emploi, offres d'emploi, projets de recrutement, salaires et prospective 2030 d'un métier sur un territoire.

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | oui | code ROME V3 |
| `zonage` | string | oui | `france`, `region`, `departement`, `clpe`, `commune` |
| `territoire` | string | oui sauf `france` | région : 2 chiffres (`76`) ; département : `01`–`95`, `2A`, `2B`, `971`–`976` ; CLPE : `CLPE` + 5 chiffres ; commune : code INSEE (`34172`, `2A004`) |
| `fields` | string | non | champs de valeur à restituer ; seules les mesures qui en portent un sont restituées (voir § 3) |

**Repli territorial** : chaque mesure est cherchée à la maille demandée puis, si elle n'y est pas publiée ou n'a pas de
valeur, au territoire parent (commune → CLPE → département → région → France). Aucune mesure n'est publiée à la commune :
une commune est toujours servie par sa CLPE ou au-delà (`repli` = true). Une CLPE est rattachée au département qui porte le
plus de ses communes.

Réponse :

| Champ | Type | Définition |
|---|---|---|
| `rome_code` | string | code ROME V3 demandé |
| `zonage`, `territoire` | string | paramètres demandés |
| `territoires` | liste | chaîne de repli : `{ maille, code, libelle }` du territoire demandé jusqu'à la France (`maille` : `com`, `clpe`, `dep`, `reg`, `nat`) |
| `items` | liste | une entrée par mesure, dans l'ordre de `/mesures` |
| `items[].mesure` | string | code de la mesure (`tension`, `demandeurs_emploi`, `offres_emploi_diffusees`, `offres_emploi_collectees`, `salaires`, `projets_recrutement`, `metiers_2030`, `offres_emploi_caracteristiques`, `offres_emploi_mensuelles`, `competences_offres`, `emploi_secteurs`, `statut_emploi`, `formations_metier`, `insertion_formations_metier`) |
| `items[].libelle` | string | libellé de la mesure |
| `items[].grain` | string | grain des valeurs (§ 3) : `rome`, `fap_228`, `fap_225` ou `fap_87` |
| `items[].maille_demandee` | string | maille correspondant au zonage demandé |
| `items[].maille_reelle` | string\|null | maille d'où proviennent les valeurs ; `null` si aucune valeur trouvée |
| `items[].territoire_code`, `items[].territoire_libelle` | string\|null | territoire d'où proviennent les valeurs |
| `items[].repli` | booléen | `true` si `maille_reelle` ≠ `maille_demandee` |
| `items[].source_libelle`, `items[].millesime` | string | provenance |
| `items[].valeurs` | liste | valeurs de la mesure (vide si aucune) ; champs ci-dessous, plus `nb_rome_famille` pour une mesure par famille (§ 3) |

Champs de `valeurs` :

| Mesure | Champs | Mailles publiées |
|---|---|---|
| `tension` | `fap_228_code`, `fap_228_libelle`, `tension_globale` et ses 7 composantes (`tension_intensite_embauche`, `tension_lien_formation_emploi`, `tension_manque_main_oeuvre`, `tension_non_durabilite_emploi`, `tension_conditions_travail_contraignantes`, `tension_inadequation_geographique`, `tension_non_attractivite_salariale`) : libellés « Tension très faible » à « Tension extrême ». Une entrée par FAP 228 liée au ROME. | dep, reg, nat |
| `demandeurs_emploi` | `nb_demandeurs_emploi` (*effectif*, catégories A, B, C) | clpe, dep, reg |
| `offres_emploi_diffusees` | `nb_offres_emploi_diffusees` (postes, 3 derniers mois) | clpe, dep |
| `offres_emploi_collectees` | `nb_offres_emploi_collectees` (postes, 3 derniers mois) | clpe, dep |
| `projets_recrutement` | `fap_228_code`, `fap_228_libelle`, `nb_projets_recrutement`, `nb_projets_recrutement_difficiles`, `tx_projets_recrutement_difficiles`, `nb_projets_recrutement_saisonniers`, `tx_projets_recrutement_saisonniers` (taux en %). BMO 2026, France Travail ; estimations d'enquête arrondies à l'unité. Une entrée par FAP 228 liée au ROME. | clpe, dep, reg, nat |
| `metiers_2030` | `fap_87_code`, `fap_87_libelle`, `nb_emplois_2019`, `tx_part_emploi_region_2019` et `indice_specificite_region_2019` (région seulement), puis, pour 2019-2030 : `nb_` / `tx_creations_nettes_emplois_2030`, `nb_` / `tx_departs_fin_carriere_2030`, `nb_` / `tx_postes_a_pourvoir_2030`, `nb_` / `tx_jeunes_debutants_2030`, `nb_` / `tx_desequilibre_potentiel_2030`, `tension_niveau_2019` (`"1"` à `"5"`). Méthode : « Prospective 2030 : méthode » ci-dessous. | reg (métropole), nat |
| `offres_emploi_caracteristiques` | `periode_libelle` (ex : `10/2025-09/2026`), `nb_offres_emploi_base` ; en % des offres : `tx_offres_cdi` (y compris CDI intérimaire), `tx_offres_cdd` (y compris CDD d'insertion), `tx_offres_interim`, `tx_offres_saisonnier`, `tx_offres_non_salarie` (libéral, franchise, commerçant, reprise), `tx_offres_emploi_durable` (CDI ou contrat d'au moins 6 mois), `tx_offres_alternance`, `tx_offres_debutant_accepte`, qualification demandée (`tx_offres_ouvrier_non_qualifie`, `tx_offres_ouvrier_qualifie`, `tx_offres_employe_non_qualifie`, `tx_offres_employe_qualifie`, `tx_offres_technicien_agent_maitrise`, `tx_offres_cadre`) ; `nb_offres_niveau_formation_renseigne` et, en % de ces offres, `tx_niveau_formation_infra_bac`, `_bac`, `_bac2`, `_bac3_4`, `_bac5`. Offres collectées par France Travail créées sur les 12 derniers mois complets (offres des partenaires exclues) ; publié à partir de 20 offres. | dep, reg, nat |
| `offres_emploi_mensuelles` | une entrée par mois, dans l'ordre chronologique : `periode_code` (AAAA-MM), `nb_offres_emploi_mois`, `nb_postes_offres_emploi_mois`. Mêmes offres, 12 derniers mois complets ; un mois sans offre est absent. Données brutes (non corrigées des variations saisonnières). | dep, reg, nat |
| `competences_offres` | une entrée par compétence, de la plus citée à la moins citée (20 au plus) : `rang_competence`, `competence_code` (référentiel ROME 4.0), `competence_libelle`, `competence_type_libelles` (`Savoir-faire`, `Compétence détaillée`), `nb_offres_competence`, `nb_offres_avec_competences`, `tx_offres_competence` (en % des offres du métier citant au moins une compétence). Offres collectées par France Travail enregistrées en 2024 (OEFM) ; environ 17 % des offres citent une compétence. | nat |
| `emploi_secteurs` | une entrée par FAP 225 liée au ROME et par secteur, les 10 premiers secteurs de chaque FAP : `fap_225_code`, `fap_225_libelle`, `rang_secteur`, `secteur_naf38_code`, `secteur_naf38_libelle` (NAF 38 postes), `nb_actifs_emploi` (salariés et non-salariés), `tx_actifs_secteur` (part des actifs de la FAP, %). Recensement 2021 ; estimations publiées à partir de 20 actifs. | reg, nat |
| `statut_emploi` | `nb_actifs_emploi`, puis effectifs et parts (%) des `salaries`, `independants`, `employeurs`, `aides_familiaux` (`nb_actifs_*`, `tx_actifs_*`). Actifs occupés par lieu de résidence, toutes professions (PCS) des FAP 225 du ROME ; recensement 2021, fichier détail ; publié à partir de 200 actifs. Seuls les départements de plus de 700 000 habitants sont identifiés (les autres : repli région). Les FAP d'exploitants agricoles indépendants ne sont rattachées à aucun ROME. | dep, reg, nat |
| `formations_metier` | formations dont la certification est rattachée au ROME (Certif Info) : `nb_inscrits_voie_scolaire` et `nb_inscrits_apprentissage` (DEPP, rentrée 2023), `nb_inscrits_enseignement_sup` (SISE 2024), `nb_inscrits_sanitaire_social` (DREES 2024), au lieu de formation ; `nb_entrees_formation_de` (2025), `nb_de_sortants`, `nb_de_acces_emploi_6m`, `tx_de_acces_emploi_6m` (sortants 2024, %), au lieu de résidence ; `nb_affelnet_places`, `nb_affelnet_voeux_1`, `indice_affelnet_pression` (2025, département au plus fin, `null` à la CLPE) ; `nb_parcoursup_places`, `nb_parcoursup_candidatures` (2025, un candidat compte dans chaque formation demandée) ; `nb_sessions_a_venir` (Offre info) ; `nb_certifications`. Une certification rattachée à plusieurs ROME compte pour chacun ; codes Certif Info archivés rattachés à leur successeur. Secret statistique sur les inscrits et les sortants DE. Détail par certification : `/certifications?rome=` et `/sessions_a_venir`. | clpe, dep, reg, nat |
| `insertion_formations_metier` | InserJeunes, cumul 2023-2024, voie scolaire et apprentissage : `nb_ij_{scolaire,apprentissage}_sortants`, `nb_` / `tx_ij_*_emploi_12m` (emploi salarié 12 mois après la sortie, %), `nb_ij_*_annee_terminale`, `nb_` / `tx_ij_*_poursuite_etudes` (%). Voie professionnelle seulement (CAP, bac pro, BTS…) : pas de diplômes d'État sanitaires ni de formations universitaires. Secret statistique. | reg, nat |
| `salaires` | `fap_225_code`, `fap_225_libelle`, `salaire_net_annuel_q1`, `salaire_net_annuel_median`, `salaire_net_annuel_q3`, `salaire_net_mensuel_median` (euros, entiers), `tranche_salaire_median_libelle`, `nb_salaries_temps_complet` (estimation pondérée). Une entrée par FAP 225 liée au ROME. Méthode : « Salaires : méthode » ci-dessous. | dep, reg, nat |

Exemple (`GET /indicateurs?rome=F1610&zonage=departement&territoire=976`, extrait) :
```json
{
  "rome_code": "F1610", "zonage": "departement", "territoire": "976",
  "territoires": [
    { "maille": "dep", "code": "976", "libelle": "MAYOTTE" },
    { "maille": "reg", "code": "06", "libelle": "MAYOTTE" },
    { "maille": "nat", "code": null, "libelle": "France" }
  ],
  "items": [
    {
      "mesure": "tension", "libelle": "Tension sur le marché du travail", "grain": "fap_228",
      "maille_demandee": "dep", "maille_reelle": "nat", "repli": true,
      "territoire_code": null, "territoire_libelle": "France",
      "source_libelle": "DARES & France travail - Métiers en tension 2024", "millesime": "2024",
      "valeurs": [ { "fap_228_code": "B1X34", "fap_228_libelle": "Couvreurs", "tension_globale": "Tension extrême", "…": "…", "nb_rome_famille": 1 } ]
    },
    {
      "mesure": "offres_emploi_diffusees", "libelle": "Offres d'emploi diffusées", "grain": "rome",
      "maille_demandee": "dep", "maille_reelle": null, "repli": false,
      "territoire_code": null, "territoire_libelle": null,
      "source_libelle": "France Travail, API Offres d'emploi", "millesime": "3 derniers mois",
      "valeurs": []
    }
  ]
}
```

### `GET /recrutements`

Territoires classés selon les projets de recrutement d'un métier (enquête BMO) : « le bassin voisin recrute-t-il
plus ? », « où recrute-t-on le plus de saisonniers ? ». Pour un seul territoire, utiliser `/indicateurs` (mesure
`projets_recrutement`).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | oui | code ROME V3 |
| `zonage` | string | non (`region`) | `region`, `departement`, `clpe` |
| `region` | string | non | avec `zonage=departement` ou `clpe` : territoires de cette région (2 chiffres) |
| `departement` | string | non | avec `zonage=clpe` : CLPE de ce département |
| `tri` | string | non (`projets`) | `projets`, `projets_difficiles`, `tx_difficiles`, `projets_saisonniers`, `tx_saisonniers` |

Un paramètre de périmètre qui ne s'applique pas au zonage renvoie 422 ; un territoire inconnu, 404.

Réponse : `rome_code`, `zonage`, `perimetre` (`{ maille, code, libelle }` ou `null`), `tri`, `source_libelle`,
`millesime`, `france` (valeurs nationales par FAP 228), `total` et `items` portant `rang` (par FAP 228, égalités
départagées par le nombre de projets), `territoire_code`, `territoire_libelle` et les champs de la mesure
`projets_recrutement`. Une CLPE à cheval sur deux départements est rattachée à celui qui porte le plus de ses projets.

Exemple (`GET /recrutements?rome=G1602&zonage=clpe&departement=34`, extrait) :
```json
{
  "rome_code": "G1602", "zonage": "clpe", "perimetre": { "maille": "dep", "code": "34", "libelle": "HERAULT" },
  "tri": "projets", "millesime": "2026",
  "france": [ { "fap_228_code": "S1X40", "fap_228_libelle": "Cuisiniers", "nb_projets_recrutement": 51272, "…": "…" } ],
  "items": [
    { "rang": 1, "territoire_code": "CLPE34003", "territoire_libelle": "Montpellier", "fap_228_code": "S1X40",
      "fap_228_libelle": "Cuisiniers", "nb_projets_recrutement": 722, "nb_projets_recrutement_difficiles": 338,
      "tx_projets_recrutement_difficiles": 46.8, "nb_projets_recrutement_saisonniers": 456,
      "tx_projets_recrutement_saisonniers": 63.2 }
  ],
  "total": 11
}
```

### Salaires : méthode

- Source : INSEE, Base Tous salariés 2023, fichier « salariés » open data (échantillon au 1/12, pondéré).
- Population : poste principal, emploi ordinaire (hors apprentis, contrats aidés, stagiaires), temps complet, présent
  toute l'année (360 jours) ; lieu de travail (établissement), hors Mayotte (absente de la BTS).
- Métier : la BTS est codée en PCS-ESE 2017, rattachée à la FAP 225 puis au ROME V3. Le salaire est celui de la **famille
  professionnelle**, pas du métier exact (ex. J1410 → V3Z71 « Spécialistes de l'appareillage médical »).
- La BTS open data ne donne qu'une tranche de rémunération nette : quartiles et médiane sont interpolés dans la tranche,
  arrondis à la centaine (médiane mensuelle = annuelle / 12, arrondie à la dizaine). Au-delà de 50 000 € (tranche
  ouverte) la valeur est `null` et `tranche_salaire_median_libelle` vaut « 50 000 euros et plus ».
- Publication à partir de 30 salariés dans l'échantillon ; en dessous, la valeur n'existe pas à cette maille
  (`/indicateurs` se replie sur le territoire parent, `/salaires` ne classe pas le territoire).

### `GET /salaires`

Classement des territoires selon le salaire d'un métier (« dans quelle région gagne-t-on le plus ? »). Pour un seul
territoire (« combien gagne-t-on en Occitanie ? »), utiliser `/indicateurs` (mesure `salaires`).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | oui | code ROME V3 |
| `zonage` | string | non (`region`) | `region` ou `departement` |
| `region` | string | non | avec `zonage=departement` : ne classer que les départements de cette région (2 chiffres) |

Réponse :

| Champ | Type | Définition |
|---|---|---|
| `rome_code`, `zonage`, `region`, `region_libelle` | string\|null | paramètres demandés (`region` inconnue : 404) |
| `source_libelle`, `millesime` | string | provenance |
| `france` | liste | valeurs France entière, une entrée par FAP 225 (champs de la mesure `salaires`) |
| `items` | liste | territoires classés, du salaire médian le plus élevé au plus faible, FAP par FAP |
| `items[].rang` | entier | rang du territoire dans sa FAP (une médiane `null`, au-delà de 50 000 €, passe en tête ; égalités départagées par le premier quartile) |
| `items[].territoire_code`, `items[].territoire_libelle` | string | région ou département |
| `items[].…` | | champs de la mesure `salaires` |
| `total` | entier | nombre d'éléments de `items` |

Exemple (`GET /salaires?rome=J1410`, extrait) :
```json
{
  "rome_code": "J1410", "zonage": "region", "region": null,
  "source_libelle": "INSEE - Base Tous salariés 2023, fichier salariés open data ; calculs RCO", "millesime": "2023",
  "france": [ { "fap_225_code": "V3Z71", "salaire_net_annuel_median": 27800, "salaire_net_mensuel_median": 2310, "…": "…" } ],
  "items": [
    { "rang": 1, "territoire_code": "11", "territoire_libelle": "ILE-DE-FRANCE", "fap_225_code": "V3Z71",
      "fap_225_libelle": "Spécialistes de l'appareillage médical", "salaire_net_annuel_q1": 27300,
      "salaire_net_annuel_median": 32400, "salaire_net_annuel_q3": 39400, "salaire_net_mensuel_median": 2700,
      "tranche_salaire_median_libelle": "30 000 à 34 999 euros", "nb_salaries_temps_complet": 2544 }
  ],
  "total": 12
}
```

### `GET /salaires/secteurs`

Salaires d'un métier selon le secteur d'activité de l'employeur (« dans quel secteur gagne-t-on le plus ? »), en France
ou dans une région. Même population et même méthode que la mesure `salaires` ; secteur en NAF rév. 2, 38 postes.

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | oui | code ROME V3 |
| `region` | string | non | code de région à 2 chiffres ; à défaut, France entière. Région inconnue : 404 |

Une FAP sans aucun secteur publié dans la région (moins de 30 salariés dans l'échantillon pour chaque secteur) est
restituée au niveau France (`maille` = `nat`, `repli` = `true`). Seuls les secteurs au seuil figurent : la somme des
`tx_salaries_secteur` d'une FAP est donc souvent inférieure à 100.

Réponse :

| Champ | Type | Définition |
|---|---|---|
| `rome_code`, `region`, `region_libelle` | string\|null | paramètres demandés |
| `source_libelle`, `millesime` | string | provenance |
| `ensemble` | liste | valeurs tous secteurs par FAP 225 (champs de la mesure `salaires`), avec `maille` (`reg` ou `nat`) |
| `items` | liste | secteurs classés, du salaire médian le plus élevé au plus faible, FAP par FAP |
| `items[].rang` | entier | rang du secteur dans sa FAP (même règle que `/salaires`) |
| `items[].maille`, `items[].repli` | string, booléen | maille des valeurs (`reg`, `nat`) ; `true` si la région demandée n'a pas de donnée pour la FAP |
| `items[].secteur_naf38_code`, `items[].secteur_naf38_libelle` | string | secteur d'activité (NAF 38) |
| `items[].tx_salaries_secteur` | nombre | part (%) des salariés de la FAP du territoire qui travaillent dans le secteur |
| `items[].…` | | `fap_225_code`, `fap_225_libelle` et champs de salaire de la mesure `salaires` |
| `total` | entier | nombre d'éléments de `items` |

Exemple (`GET /salaires/secteurs?rome=J1410&region=76`, extrait) :
```json
{
  "rome_code": "J1410", "region": "76", "region_libelle": "OCCITANIE", "millesime": "2023",
  "ensemble": [ { "maille": "reg", "fap_225_code": "V3Z71", "salaire_net_annuel_median": 27700, "…": "…" } ],
  "items": [
    { "rang": 1, "maille": "reg", "repli": false, "fap_225_code": "V3Z71", "secteur_naf38_code": "CM",
      "secteur_naf38_libelle": "Autres industries manufacturières, réparation et installation de machines et d'équipements",
      "tx_salaries_secteur": 32.3, "salaire_net_annuel_median": 28300, "…": "…" },
    { "rang": 2, "maille": "reg", "repli": false, "fap_225_code": "V3Z71", "secteur_naf38_code": "GZ",
      "secteur_naf38_libelle": "Commerce, réparation d'automobiles et de motocycles",
      "tx_salaries_secteur": 59, "salaire_net_annuel_median": 27500, "…": "…" }
  ],
  "total": 2
}
```

### Prospective 2030 : méthode

- Source : DARES - France Stratégie, « Les métiers en 2030 », exercice Prospective des métiers et qualifications (PMQ,
  2022), scénario de référence ; flux cumulés de 2019 à 2030.
- Grain : famille professionnelle FAP 2009 en 87 postes, rattachée au ROME V3 (`public.lien_fap_rome`). L'exercice
  regroupe 7 familles en 4 agrégats (`D0A` = D0Z + D3Z, `F0A` = F0Z + F1Z, `F2A` = F2Z + F3Z, `XK_` = K0Z + clergé et
  politique). En Corse, d'autres familles sont regroupées (code composé, ex. `A0Z;A1Z;A2Z;A3Z`).
- Postes à pourvoir = départs en fin de carrière + créations nettes d'emploi (négatives si l'emploi recule).
- Déséquilibre potentiel = postes à pourvoir − jeunes débutants (en région : − solde des mobilités entre régions).
  Positif : les jeunes débutants ne suffiraient pas à pourvoir les postes (risque de difficultés de recrutement) ;
  négatif : plus de jeunes débutants que de postes.
- Taux (`tx_*`) en % de l'emploi 2019. Indice de spécificité : part du métier dans l'emploi régional rapportée à sa
  part dans l'emploi national (> 1 : métier plus présent dans la région qu'en France).
- Couverture : France et 13 régions de métropole ; pas de donnée pour les DOM (`/indicateurs` se replie sur la France),
  ni par département.

### `GET /prospective/metiers`

Familles professionnelles classées selon leurs perspectives à 2030 (« quels métiers recruteront le plus ? »).

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `region` | string | non | région de métropole (2 chiffres) ; à défaut, France entière. Autre région : 404 |
| `tri` | string | non (`postes_a_pourvoir`) | `postes_a_pourvoir`, `desequilibre_potentiel`, `creations_nettes_emplois`, `departs_fin_carriere` (effectifs), leurs versions `tx_*` (en % de l'emploi 2019), `emplois_2019` |

Réponse : `region`, `region_libelle`, `tri`, `source_libelle`, `millesime`, `total` et `items` (toutes les familles,
du plus élevé au plus faible ; valeur nulle en dernier) portant `rang`, `rome_codes` et les champs de la mesure
`metiers_2030`.

Exemple (`GET /prospective/metiers`, extrait) :
```json
{
  "region": null, "region_libelle": null, "tri": "postes_a_pourvoir", "millesime": "2019-2030", "total": 83,
  "items": [
    { "rang": 1, "fap_87_code": "T4Z", "fap_87_libelle": "Agents d'entretien", "rome_codes": ["I1201", "…"],
      "nb_emplois_2019": 1226003, "nb_postes_a_pourvoir_2030": 488667, "tx_postes_a_pourvoir_2030": 39.9, "…": "…" }
  ]
}
```

### `GET /prospective/regions`

Régions de métropole classées pour la famille professionnelle d'un métier (« le métier est-il concentré dans une
région ? », « dans quelle région recrutera-t-on le plus ? »), avec la France en référence.

| Paramètre | Type | Obligatoire | Règle |
|---|---|---|---|
| `rome` | string | oui | code ROME V3 |
| `tri` | string | non (`specificite`) | `specificite` (indice de spécificité), `part_emploi` (part dans l'emploi régional), ou un tri de `/prospective/metiers` |

Réponse : `rome_code`, `tri`, `source_libelle`, `millesime`, `france` (valeurs nationales par FAP 87), `total` et
`items` portant `rang` (par FAP 87), `territoire_code`, `territoire_libelle` et les champs de la mesure
`metiers_2030`. Les familles regroupées propres à la Corse ne sont pas classées.

### `GET /mobilites`

D'où viennent (`sens=origines`) et où vont (`sens=destinations`) les personnes qui exercent un métier ROME V3, sur un an
(janvier 2022 → janvier 2023, DARES, dispositif ForCE et DSN-Sismmo), par famille professionnelle (FAP 225).

| Paramètre | Obligatoire | Valeurs |
|---|---|---|
| `rome` | oui | code ROME V3 |
| `sens` | non | `origines` (défaut : situation un an plus tôt des personnes en emploi dans le métier), `destinations` (situation un an plus tard de celles qui l'exerçaient) |
| `region` | non | code de région (2 chiffres) ; à défaut, France entière. Région inconnue : 404 |
| `age` | non | `ensemble` (défaut), `15-29`, `30-39`, `40-49`, `50-59`, `60+` (âge en fin de période pour les origines, en début de période pour les destinations) |

Réponse : `rome_code`, `sens`, `region`, `region_libelle`, `tranche_age_libelle`, `source_libelle`, `millesime`, `total`,
et `items` : les 15 situations les plus fréquentes par FAP, triées par FAP puis `rang`, chacune portant `rang`, `maille`
(`reg` ou `nat`), `repli` (true : FAP sans donnée dans la région, valeur France), `fap_225_code`, `fap_225_libelle`,
`tranche_age_libelle`, `origine_code` / `origine_libelle` (ou `destination_code` / `destination_libelle`) : une FAP 225, ou
une situation hors emploi (`UUUUU` demandeurs d'emploi, `WW000` apprentis, `WWWWW` jeunes sortants d'études initiales,
`VVVVV` retraités, `XXXXX` autres situations, `ZZZZZ` non renseigné), `tag_meme_metier` (resté dans la FAP), `tag_en_emploi`
(la situation est un métier), `tx_personnes` (part des personnes, %).

Parts seulement (la source ne publie pas d'effectifs) ; les parts sous secret statistique de la source ne sont pas
reprises : la somme des parts restituées peut être inférieure à 100, et une région peut compter moins de 15 situations.

Exemple (`GET /mobilites?rome=J1506&sens=destinations`, extrait) :
```json
{
  "rome_code": "J1506",
  "sens": "destinations",
  "items": [
    { "rang": 1, "maille": "nat", "repli": false, "fap_225_code": "V1Z80", "destination_code": "V1Z80", "destination_libelle": "Infirmiers", "tag_meme_metier": true, "tag_en_emploi": true, "tx_personnes": 90.7 },
    { "rang": 4, "maille": "nat", "repli": false, "fap_225_code": "V1Z80", "destination_code": "VVVVV", "destination_libelle": "Retraités", "tag_meme_metier": false, "tag_en_emploi": false, "tx_personnes": 1.4 }
  ]
}
```

### `GET /secteurs`

Dynamique des secteurs d'activité (NAF 38 postes) d'un territoire et, avec `rome`, secteurs qui emploient un métier ROME V3
et nombre d'établissements employeurs du territoire (comptages seulement, aucune liste nominative d'employeurs).

| Paramètre | Obligatoire | Valeurs |
|---|---|---|
| `zonage`, `territoire` | oui (`territoire` sauf `france`) | comme `/indicateurs` ; une commune est servie par sa CLPE |
| `naf` | non | code NAF 38 postes à 2 lettres (`FZ`, `IZ`…) ; à défaut, tous les secteurs |
| `rome` | non | code ROME V3 : seuls les secteurs qui emploient le métier figurent |

Réponse : `zonage`, `territoire`, `territoires` (chaîne de repli), `maille_demandee`, `maille_reelle`, `territoire_code`,
`territoire_libelle`, `repli`, `rome_code`, `metier_maille` (`reg` ou `nat` : maille des parts du métier),
`source_libelle`, `millesime`, `ensemble` (mêmes champs, tous secteurs : `secteur_naf38_code` = `ENS`), `total` et `items`.
Chaque élément porte `rang`, `secteur_naf38_code`, `secteur_naf38_libelle` et :

| Champ | Source | Contenu |
|---|---|---|
| `nb_etablissements`, `nb_etablissements_n5`, `tx_evolution_etablissements_5ans` | INSEE, SIDE | établissements actifs fin 2024, fin 2019, évolution (%) ; département au plus fin (null à la CLPE) |
| `nb_unites_legales` | INSEE, SIDE | unités légales (entreprises) actives fin 2024 ; département au plus fin |
| `nb_creations_etablissements`, `nb_creations_etablissements_n1`, `tx_evolution_creations_1an` | INSEE, SIDE | créations d'établissements 2025, 2024, évolution (%) |
| `nb_etablissements_employeurs`, `nb_salaries_prives`, `nb_salaries_prives_n5`, `tx_evolution_salaries_5ans` | URSSAF | établissements employeurs et salariés du secteur privé 2025 (l'administration publique y est donc peu représentée), salariés 2020, évolution (%) |
| `nb_defaillances`, `tx_defaillances_1000_unites_legales` | BODACC | entreprises ayant fait l'objet d'un jugement d'ouverture (liquidation, redressement, sauvegarde) entre `date_debut_defaillances` et `date_fin_defaillances` (12 mois au plus, depuis janvier 2026), et pour 1 000 unités légales |
| `nb_actifs_metier`, `tx_actifs_metier` | INSEE, recensement 2021 | avec `rome` : actifs du métier (FAP 225 du ROME) dans le secteur et leur part (%) ; région du territoire, à défaut France |

Sans `rome`, les secteurs sont classés du plus grand au plus petit nombre de salariés du privé ; avec `rome`, selon la
part des actifs du métier. Pas de fermetures d'établissements (SIDE ne les publie pas). Territoire inconnu : 404.

Exemple (`GET /secteurs?rome=F1610&zonage=commune&territoire=34172`, extrait) :
```json
{
  "maille_reelle": "clpe",
  "territoire_code": "CLPE34003",
  "territoire_libelle": "Montpellier",
  "repli": true,
  "rome_code": "F1610",
  "metier_maille": "reg",
  "items": [
    { "rang": 1, "secteur_naf38_code": "FZ", "secteur_naf38_libelle": "Construction", "nb_actifs_metier": 13378, "tx_actifs_metier": 76.4, "nb_etablissements_employeurs": 2613, "nb_salaries_prives": 16440, "tx_evolution_salaries_5ans": -2.0, "nb_creations_etablissements": 1469, "tx_evolution_creations_1an": -9.0, "nb_defaillances": 98, "date_debut_defaillances": "2026-01-01", "date_fin_defaillances": "2026-09-30" },
    { "rang": 2, "secteur_naf38_code": "NZ", "secteur_naf38_libelle": "Activités de services administratifs et de soutien", "nb_actifs_metier": 1798, "tx_actifs_metier": 10.3, "nb_etablissements_employeurs": 1642, "nb_salaries_prives": 22464 }
  ]
}
```

### `GET /mesures`

Catalogue des mesures (dictionnaire pour l'application ; `fields` possible) : `{ "items": [ … ], "total": 29 }`, chaque élément portant
`code`, `ressource` (`/indicateurs`, `/secteurs`, `/salaires/secteurs`, `/mobilites` ou `/certifications`), `libelle`, `grain` (§ 3), `definition`, `champs` (noms exposés),
`mailles`, `source`, `millesime`, et la couverture des mesures par métier ou par famille : `nb_rome_couverts` (ROME V3
qui ont au moins une valeur, à une maille au moins) et `tx_rome_couverts` (% des 532 ROME V3) ; `null` pour les mesures
par secteur ou par certification. Ex. : tension 504 ROME (94,7 %), projets de recrutement 513 (96,4 %), compétences des
offres 463 (87 %), insertion des formations au métier 385 (72,4 %).

## 7. Points d'accès de compatibilité

Repris **à l'identique** d'api_entrepot_r3 (mêmes paramètres, mêmes réponses, noms de champs d'origine
`*_lib`). Ils ne suivent pas les conventions du § 3 et évolueront avec l'API d'origine. Le détail est dans `/docs`.

`GET /ressources` a été retiré le 20/10/2026 : ses indicateurs territoriaux de formation sont servis par `/indicateurs`
(mesures `formations_metier` et `insertion_formations_metier`), les mobilités par `/mobilites`.

| Route | Paramètres |
|---|---|
| `GET /sessions_a_venir`, `GET /sessions_en_cours` | `zonage`, `territoire`, `certifinfo` (5 ou 6 chiffres), `page`, `fields` (noms d'origine, ajouté le 21/10/2026) |

## 8. Évolution du contrat

- **Sans préavis (compatible)** : ajout d'un point d'accès, d'un paramètre facultatif, d'un champ dans un objet, d'une
  mesure dans `/mesures` et `/indicateurs`, d'une valeur dans une liste de codes ; mise à jour des données et millésimes.
  Le consommateur doit ignorer les champs qu'il ne connaît pas.
- **Avec version et préavis (incompatible)** : suppression ou renommage d'un champ, changement de type ou de sens,
  paramètre devenu obligatoire, modification des règles de secret statistique.
- Toute évolution des champs passe par `src/Data/ExposedFields.php` : une colonne ajoutée à un script SQL n'est pas
  exposée tant qu'elle n'y est pas déclarée.

## 9. Points ouverts

- Règle de l'écart total − sous-effectif du secret statistique : à valider.
- Compétences et contextes de travail : contenu ROME 4.0 ramené au ROME V3 (au moins une fiche ; part des fiches dans `tx_fiches_rome4`) ; contextes de travail sans regroupement (horaires, lieux, statut, clientèle mêlés), pas de télétravail effectif (seulement « Possibilité de télétravail ») ; pas d'arborescence pour les savoirs ; version et date du référentiel ROME 4.0 non restituées.
- Millésime par document (aujourd'hui porté par `/mesures` et `/indicateurs` seulement).
- InserSup : salaires des promotions 2021-2022 à côté des taux d'emploi de la promotion 2024 ; certification à plusieurs diplômes SISE (27) : salaire du diplôme le plus fourni.
- BMO : millésime 2026 seul, précision des petits volumes (CLPE) : à valider.
- Prospective 2030 : grain FAP 87, métropole seule, déséquilibre national sans les mobilités : à valider.
- Abandons : seulement pour les demandeurs d'emploi formés (France Travail) ; rares (2,1 % en formation certifiante), donc souvent masqués par le secret (1 à 4 abandons). Pas d'abandons InserJeunes / InserSup (« ensemble » − « diplômé » d'InserSup donne les non-diplômés, pas les abandons).
- Offres d'emploi : offres collectées par France Travail seules (partenaires exclus : qualification peu renseignée, volumes instables dans l'entrepôt) ; seuil de 20 offres ; durée d'expérience exigée absente de l'extraction de l'API ; évolution sur un an (Q062) à définir quand deux années seront couvertes ; compétences OEFM 2024 seulement (tables `oefm_*_new` écartées).
- Territoires : pas de code postal ni de population dans l'entrepôt (recherche par nom ou code INSEE, ordre par densité).
- Salaires : seuil de 30 observations, population retenue, maille FAP 225, tranche ouverte au-delà de 50 000 € : à valider.
