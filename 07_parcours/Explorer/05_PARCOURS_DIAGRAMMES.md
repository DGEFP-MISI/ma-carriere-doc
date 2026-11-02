# Explorer V2 — diagrammes de parcours

## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.


**Mise à jour du 2 novembre 2026 — dossier rangé.** Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les 31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.

Alignement L0 — 1er novembre 2026. Les 31 fonctions sont incluses. Ces schémas décrivent les parcours, pas des tests HTTP ou jointures SQL. Les paramètres et chemins JSON exacts sont dans 02/03. Aucun UML de référence sous05_uml n'est modifié.

## Navigation principale — E01/E02/E03/E04/E05/E07/E17/E19/E20/E27/E28

```mermaid
flowchart TD
    A["Explorer : barre unique"] --> B{"Mode choisi"}
    B -->|Métier| C["E01 GET /metiers avec q et page"]
    B -->|Diplôme| D["E02 GET /certifications avec q et page"]
    B -->|Domaine professionnel| E["E03 GET /domaines : arbre, filtre local de libellés"]
    E --> F["Sélection explicite d'un domaine"]
    F --> G["Fiche Domaine"]
    G --> H["E04 GET /metiers avec domaine et page"]
    C --> I["Sélection d'un code ROME V3"]
    H --> I
    I --> J["E05 GET /metiers/{rome} : fiche Métier"]
    J --> J1["Quatre questions : activités, opportunités, salaires, autres pistes"]
    J1 --> J2["Détails accessibles : mobilités, prospective2030, formations, conditions"]
    J --> A
    D --> K["Sélection d'un code Certif Info"]
    K --> L["E17 GET /certifications/{certifinfo}"]
    L --> M["E19 rome_codes[] : métiers associés"]
    M --> I
    J --> N["E20 GET /certifications avec rome"]
    N --> K
    J --> O["E07 métiers proches : codes et libellés reçus"]
    O --> I
    J --> P["E27 ajouter ou retirer une piste : état local"]
    P --> Q["E28 sélectionner deux métiers pour comparer"]
    Q --> J
```

La fiche Domaine précède sa liste de métiers ; elle n'est pas atteinte en requalifiant une sélection déjà métier. Diplôme inclut aussi titres/RS, avec type réel. E27 n'appelle pas un endpoint de sauvegarde.

## Compétences, contextes, transitions — E06/E13/E14/E15/E16/E29

```mermaid
flowchart TD
    A["Fiche métier ou domaine choisi"] --> B["E06 GET /metiers/{rome}/competences"]
    B --> C["Toutes pages utiles et catégories, part des spécialités"]
    C --> D["E13 choisir OGR déjà reçu ou GET /competences"]
    D --> E["E14 GET /metiers : competence et mode_competence"]
    C --> F["E15 contexte référencé ou GET /competences categorie=contexte_travail"]
    F --> G{"Contexte à rechercher ou éviter"}
    G --> H["E16 GET /metiers : contexte"]
    G --> I["E16 GET /metiers : sans_contexte"]
    H --> J["Métiers identifiés : inclusion documentée, pas garantie terrain"]
    I --> J
    E --> J
    A --> K["E29 GET /metiers : toutes les pages du périmètre"]
    K --> L["Filtre local des trois tags de transition"]
    L --> J
```

Les filtres OGR compatibles peuvent se combiner au domaine choisi selon le contrat. Le paramètre domaine de /competences désigne1–6, pas un Domaine professionnel. MC page 1/2 ne prouve pas une liste complète. E29 ne crée pas un paramètre de filtre serveur transition.

## Certification, blocs, thèmes et sessions — E17/E18/E19/E20/E21/E22/E30

```mermaid
flowchart TD
    A["E17 GET /certifications/{certifinfo}"] --> B{"Intention de consultation"}
    B --> C["Je possède : métiers et blocs, sans garantie d'accès"]
    B --> D["Je souhaite obtenir : voies et résultats, sans admission promise"]
    A --> E["Populations nationales séparées : insertion, salaires, inscrits, diplômes, demande"]
    A --> F["E18 blocs RNCP via certifinfo ou fiche"]
    F --> G["Texte compétences et évaluations, jamais OGR inféré"]
    H["E18 recherche q dans les textes des blocs"] --> F
    F --> I["certifinfo_codes[] : sélection de certification"]
    I --> A
    C --> J["E19 rome_codes[] vers fiches Métier"]
    K["Fiche Métier"] --> L["E20 certifications avec rome, acces et validation_partielle"]
    L --> A
    K --> M["E30 GET /formacodes avec rome ou code"]
    M --> N["GET /certifications avec formacode"]
    N --> A
    A --> O["E09 territoire compatible choisi : région, département ou CLPE"]
    O --> P["E21 GET /sessions_a_venir : certifinfo, zonage, territoire"]
    O --> Q["E22 GET /sessions_en_cours : mêmes paramètres"]
    P --> R["Listes datées et modalités ; Onisep séparé si consulté"]
    Q --> R
    R --> S["Recette du filtre et regroupement Q11, pas places disponibles"]
```

Les deux intentions changent l'ordre d'affichage, pas les données. Actives seulement ; ancien diplôme introuvable explicité. Onisep a une date conventionnelle ; ses modes sont exclure/inclure/seulement. Une liste courante n'a pas besoin d'une clé métier stable inventée. Les sessions non certifiantes par Formacode ne sont pas exposées.

## Indicateurs et comparaisons territoriales — E08/E09/E10/E11/E12/E31

```mermaid
flowchart TD
    A["E09 GET /territoires : choisir zonage, code et parents"] --> B["E08 GET /indicateurs : rome, zonage, territoire"]
    B --> C["Par mesure : valeurs, grain, famille, maille réelle et repli"]
    A --> D["Choisir périmètre de classement compatible et explicite"]
    D --> E["E10 GET /recrutements : zonage, region ou departement selon signature"]
    D --> F["E11 GET /salaires : region ou departement, filtre region si départements"]
    E --> G["Rangs BMO par FAP228 et référence France"]
    F --> H["Rangs salaires par FAP225 ; tranche ouverte et unités séparées"]
    I["E31 GET /mesures : dictionnaire global"] --> J["E12 définitions, sources, périodes et comparabilité"]
    C --> J
    G --> J
    H --> J
```

/recrutements et /salaires n'acceptent pas territoire. Un périmètre de classement choisi n'est pas le repli automatique d'une mesure. Les 29 entrées de /mesures ne sont pas29valeurs disponibles pour le métier ; les 14 mesures d'indicateurs ont leurs formes propres. France est un choix spécifique aux routes compatibles, non un zonage de /territoires.

## Mobilités, prospective détaillée et secteurs — E23/E24/E25/E26

```mermaid
flowchart TD
    A["Fiche métier et territoire de consultation"] --> B["E23 GET /mobilites : sens, age, region ou France"]
    B --> C["Origines ou destinations par FAP225, hors emploi et parts reçues"]
    A --> D["E24 GET /prospective/regions : rome et tri"]
    D --> E["Familles FAP87, détail2030 et référence France"]
    F["Choix explicite de région ou France"] --> G["E24 GET /prospective/metiers : region et tri"]
    G --> H["Familles et rome_codes[]"]
    H --> I["Ouvrir une fiche ROME V3"]
    A --> J["E25 GET /salaires/secteurs : rome, region ou France"]
    J --> K["Groupes FAP225 et NAF38, ensemble et maille par ligne"]
    A --> L["E26 depuis E08 : emploi_secteurs familial régional ou national"]
    A --> M["E26 GET /secteurs sans rome : contexte territorial"]
    L --> N["Deux lectures distinctes, aucun compte local attribué au métier"]
    M --> N
    A --> O["E26 GET /secteurs avec rome : résultat contractuel attendu"]
    O --> P["R17 reproduit : chantier fournisseur Q14 et test de clôture"]
    P --> Q["Indisponibilité explicite tant que le défaut subsiste, E26 conservé"]
```

Mobilités : top 15 au plus et parts sous secret omises, pas normalisation à100. Prospective : créations/déséquilibres négatifs conservés, taux fournis, métropole/France et agrégats expliqués, pas de somme BMO. Salaires sectoriels : mensuel/annuel distincts et références tous secteurs, pas de score. Les lectures accessibles d'E26 ne valent pas clôture de R17.

## Comparateur complet — E28 avec E05/E06/E08–E12/E17/E20/E23–E25/E27/E31

```mermaid
flowchart TD
    A["E27 deux codes métier choisis"] --> B["E28 réutiliser détails, certifications et cache"]
    B --> C["E06 toutes les pages pour les catégories comparées"]
    C --> D["Codes OGR communs et spécifiques : pas maîtrise personnelle"]
    C --> E["GET /metiers/{rome}/competences avec depuis : synthèse API directionnelle à tester"]
    B --> F["E08 et volets détaillés : indicateurs, mobilités,2030,salaires sectoriels"]
    F --> G["Chaque famille et géographie/période/population conservée"]
    G --> H{"Même observation de famille"}
    H -->|Oui| I["Signaler la donnée partagée, pas deux observations indépendantes"]
    H -->|Non| J["Valeurs côte à côte avec limites de comparaison"]
    D --> K["Vue par questions, sans score ni delta inventé"]
    E --> K
    I --> K
    J --> K
```

## États et tests indispensables

```mermaid
flowchart TD
    A["Réponse API"] --> B{"Erreur de transport ou enveloppe"}
    B -->|Oui| C["Erreur par bloc, reprise bornée ;401/422sans boucle,429quota"]
    B -->|Non| D{"Collection ou champ reçu"}
    D --> E["Liste vide : aucun résultat de cet appel"]
    D --> F["Champ absent : projection, variante ou écart à qualifier"]
    D --> G["secret_stat : non diffusable, aucun calcul"]
    D --> H["Zéro numérique : afficher zéro avec unité"]
    D --> I{"null"}
    I --> J["Salaire avec tranche ouverte : afficher tranche annuelle"]
    I --> K["Autre null : inconnu ou indisponible selon définition"]
    D --> L["Valeur valide : source,grain,période,population et lieu effectif"]
    D --> M["Pagination incomplète : ne pas conclure absence de compétence"]
```

## Couverture et lots techniques

| Diagramme | IDs couverts | Lots |
|---|---|---|
| Navigation principale | E01, E02, E03, E04, E05, E07, E17, E19, E20, E27, E28 | L2, L9 |
| Compétences/contextes/transitions | E06, E13, E14, E15, E16, E29 | L2, L3 |
| Certification/blocs/thèmes/sessions | E17, E18, E19, E20, E21, E22, E30 | L2, L3, L8 |
| Indicateurs/territoires/méthode | E08, E09, E10, E11, E12, E31 | L2, L4 |
| Mobilités/prospective/secteurs | E23, E24, E25, E26 | L5, L6, L7 |
| Comparateur | E28 et réutilisation des contenus référencés | L9 |
| États/accessibilité et recette intégrée | Tous E01–E31, T-E01–T-E31 et V01–V14 | L1, L10 |

L0 aligne les livrables et prépare les validations ; L1 fournit l'intégration partagée ; L2–L9 réalisent toute la cible ; L10 couvre sa recette. Une erreur ou un manque de preuve ne retire aucun ID.
