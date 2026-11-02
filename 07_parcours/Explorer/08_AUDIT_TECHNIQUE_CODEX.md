# Explorer V2 — Audit technique et fonctionnel

## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.


**Mise à jour du 2 novembre 2026 — dossier rangé.** Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les 31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.

Date : 1er novembre 2026. Révision après décision produit : **les 31 fonctionnalités E01–E31 constituent le périmètre cible confirmé d'Explorer V2**. Aucun développement applicatif ni nouvel appel HTTP effectué. Les sept livrables sont désormais actualisés en place par le lot L0 ; leurs anciennes recommandations de réduction, de report ou d'exclusion sont supprimées de 01–07. Les sources de référence restent conservées.

Une absence de JSON est une preuve à collecter, pas une impossibilité ni une raison de retirer une fonction. Le statut de preuve ne détermine pas l'appartenance au produit. Les lots sont des séquences techniques couvrant toute la cible. Une anomalie fournisseur ouvre un chantier de résolution et un critère de recette : elle n'efface pas l'ID. Les compléments exploitables sont rattachés aux IDs existants dans le plan 09, sans inventer d'accès ou de données.

## 1. Diagnostic

La cible complète dispose de routes documentées pour la consultation Métier / Certification / Domaine, les compétences/contextes, les mobilités, la prospective détaillée 2030, les salaires sectoriels, les indicateurs et les comparateurs. Les recherches OGR et les contextes disposent de preuves ciblées R23/R24. Les travaux de conception et la préparation des adaptateurs peuvent s'appuyer sur le contrat même lorsqu'un exemple manque. Les validations à organiser portent notamment sur `/domaines`, les pages de compétences, les règles du comparateur et les champs d'insertion Certification. Ces travaux sont intégrés à la réalisation de chaque fonction.

Les classements doivent conserver chaque famille FAP séparément. Ni une ligne par métier, ni une ligne par territoire ne constitue un modèle général correct. La valeur de salaire `null` a une exception documentée importante : la tranche ouverte supérieure. Les sessions ont répondu dans la campagne antérieure, mais le rattachement de chaque ligne au Certif Info n'est pas vérifiable indépendamment. Le filtre ROME de `/secteurs` présente un écart reproduit, pas une simple absence de preuve.

Lors de l’audit du 1er novembre, le dossier inspecté contenait des sources, des JSON, des UML, des documents et des contrôles Python/PowerShell. La maquette HTML a été ajoutée ensuite ; le constat historique était : aucun projet applicatif identifié : pas de `package.json`, de sources d'interface, de point d'entrée applicatif, de configuration de serveur ou de tests de produit. `.vscode` et les lanceurs servent aux contrôles documentaires. Aucun framework, projet ou composant logiciel n'a été créé.

## 2. Sources et portée des preuves

Les chemins de cette section partent de la racine du dossier de référence. Les alias ci-dessous permettent de retrouver les preuves des tableaux.

| Référence | Source consultée | Ce qu'elle permet d'affirmer |
|---|---|---|
| C | `01_sources/contrat_interface_2026-10-19.md`, version 0.1.0, notamment §2–6 et §9 | Sens des champs, règles, erreurs, grains, recherche, repli, authentification et limites |
| O | `01_sources/openapi/docs_json_interface.json` | Export officiel fourni, 21 GET, paramètres, schémas disponibles ; aucune actualisation distante pendant l'audit |
| CAT | `03_catalogue/routes_openapi.csv`, `champs_observes_tous_endpoints.csv`, `modele_valeurs_par_mesure.csv` | Index de lecture à recouper avec les sources ; pas un contrat indépendant |
| ANA | `03_catalogue/A_LIRE_COMPLEMENTS.md`, `modeles_reponses/*.schema.json`, `docs_json_ENRICHI_NON_OFFICIEL.json` | Modélisation complémentaire non officielle ; ne valide pas le fournisseur |
| M | `02_reponses_observees/metiers/response_metiers-rome.json` | Fiche F1610 observée |
| MC | `02_reponses_observees/metiers/response_metiers{rome}competences.json` | F1610, 100 compétences reçues sur 144, page 1/2 |
| CL / CD / CB | `02_reponses_observees/certifications/response_certifications.json`, `response_certifications-certifinfo.json`, `response_certificationsblocs.json` | Liste de 15 certifications ; détail 112561/RNCP36101 ; 4 blocs associés par leurs codes |
| FC | `02_reponses_observees/certifications/response_formacode.json` | Formacode observé, filtre effectif non tracé par ce seul fichier |
| T | `02_reponses_observees/territoires/response_regions.json`, `response_departement.json`, `response_clpe.json`, `response_Commune.json` | Structures des territoires et codes parents |
| BMO | `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`, variantes département et CLPE | Classements FAP228 observés, plusieurs familles possibles |
| SAL | `02_reponses_observees/indicateurs/salaires/response_regions.json`, `response_departement.json` | Classements FAP225 observés ; unités annuelles et mensuelles différentes |
| MES | `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json` | 29 entrées, plusieurs ressources, attribut `source` du catalogue |
| IND | `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json` | Structure des 14 mesures ; ne remplace pas la preuve R16 plus récente |
| MOB | `02_reponses_observees/indicateurs/mobilites/response_origine.json`, `response_destination.json` et variantes par âge | Deux sens de mobilité FAP225, structures distinctes |
| PRO | `02_reponses_observees/indicateurs/prospectiveregions/*.json`, `prospective_regions/response_1793525580226.json`, `ProspectiveMetier/*.json` | Classements FAP87, variantes de tri et association plurielle aux ROME |
| SS | `02_reponses_observees/indicateurs/response_salairessecteurs.json` | Salaires sectoriels FAP225 × NAF38, `maille` et `repli` par ligne |
| REL | `04_relations/matrice_statuts_apres_tests.csv`, `matrice_liens_controles.csv`, `CHAINES_APPELS_API.md`, `PREUVES_ET_LIMITES.md`, `STATUTS_EN_COURS.md` | 24 relations ; la matrice après tests prime sur les anciens statuts |
| UML | Les trois `.puml` de `05_uml/00_modele_global/` et les quatre de `05_uml/sequences_api/` | Modèles d'objets exposés et transferts de paramètres ; aucune preuve SQL ni recette HTTP |
| R16–R24 | Rapports `06_controles/VALIDATION_R*.md` et JSON `06_controles/resultats/R16 test/`, `R17 test/`, `R18 test/`, `R19/`, `R23 test/`, `R24/` | Résultats de la campagne fournie, limités aux cas conservés ; deux rapports R23 complémentaires |

Les sept documents Explorer ont été lus intégralement, y compris les 31 lignes E01–E31 du CSV. Les 57 JSON historiques et les 16 JSON de la campagne, dont deux corps d'erreur R24, ont été parcourus par analyse locale. Une lecture de fichier ou une concordance de codes n'est jamais promue en test HTTP.

**Niveaux employés :**

- **D — Documenté dans le contrat** : route, paramètre ou champ décrit par C/O ; appel complet à tester.
- **J — Observé dans un JSON** : structure ou valeur effectivement conservée ; URL et statut HTTP souvent absents.
- **V — Testé et validé sur le cas fourni** : rapprochement avec les requêtes décrites dans la campagne R16/R23/R24. Aucun nouveau test réseau dans cet audit, aucune généralisation à tous les codes.
- **T — À confirmer / à tester** : preuve insuffisante, chaîne incomplète ou écart ouvert.
- **NC — Non couvert** : besoin sans restitution ou opération prévue dans les 21 GET. Une interaction purement locale n'est pas pour autant impossible.

Une fonction peut être D+J sans être V. Les intitulés « CONFIRMÉ » des documents initiaux doivent être lus à cette granularité. Les rapports de campagne citent des exports Swagger fournis par l'utilisatrice ; ils ne constituent pas tous une capture de transport avec statut HTTP, URL effective et horodatage.

## 3. Tableau de synthèse des 31 fonctionnalités

Priorités techniques de l'audit : **P0** = résolution à engager en priorité pour sécuriser le bloc ; **P1** = contrôle nécessaire à sa recette ; **P2** = approfondissement et validation du bloc prévu dans la cible. Ces niveaux n'autorisent aucun retrait ou report hors produit et ne sont pas un découpage MVP. Les 31 IDs restent à réaliser ; les anomalies Axx sont détaillées ensuite. Le plan 09 précise pour chacun solution, test et clarification.

| ID de conception | Fonctionnalité | Faisabilité API | Preuve | Anomalie éventuelle | Correction recommandée | Priorité |
|---|---|---|---|---|---|---|
| E01 | Recherche métier | D ; recherche `q` à tester | C §3–4, O `/metiers`, R23/R24 pour d'autres filtres | Pas de preuve de qualité de recherche libre, A12 | `q` 2–100 caractères, sélection d'un `items[].rome_code`, pagination ; tester préfixes et ambiguïtés | P1 |
| E02 | Recherche diplôme/certification | D+J ; `q` à tester | O, CL, relation R10 statique | « Diplôme » ne décrit pas toutes les certifications RNCP/RS ; actifs seulement, A07 | Identifier par Certif Info chaîne ; afficher type/répertoire ; traiter certification ancienne introuvable | P1 |
| E03 | Navigation Domaine | D ; T pour réponse réelle | C §4 `/domaines`, O description, ANA | Aucun JSON collecté ; `q` et `page` non acceptés ; champ laissé indéfini, A01 | Mapper l'arbre contractuel ; obtenir un export réel ; navigation, pas recherche API libre de domaine | P0 |
| E04 | Métiers d'un domaine | D+J ciblé ; chaîne complète T | O `/metiers`, R24 : 13 ROME F16 répartis entre deux filtres | R24 ne prouve pas `/domaines` → sélection → liste non filtrée | Tester `domaine=F16&page=1`, cohérence des codes et pages | P1 |
| E05 | Fiche métier | D+J | M, O, UML | Aucun champ `activites` ; définitions multiples, A10 | Rendre `definitions[]`, appellations et contexte sans inventer une rubrique alimentée par un champ absent | P1 |
| E06 | Compétences et contextes | D+J partiel | MC : total 144, page 1, last_page 2 | Page 2 absente ; page 1 = 80 savoir-faire et 20 savoirs, A02 | Compléter les pages ou demander `categorie=contexte_travail` ; préserver part des spécialités et booléens nullables | P0 |
| E07 | Métiers proches | D+J pour codes ; ouverture des cibles T | M `metiers_proches_codes[]`, REL | Une seule fiche détaillée conservée ; proximité distincte d'un flux observé | Réutiliser codes/libellés parallèles, charger la cible sélectionnée ; tester 404 | P1 |
| E08 | Indicateurs territoriaux | V sur F1610/34172, avec précautions | R16 et son JSON, IND, C §6 | Mesures hétérogènes à organiser avec E24/E26 sans double compte, A03/A08 | Restituer les mesures par questions et types, avec détail de chaque famille, source et maille ; réutiliser les données dans les autres vues | P0 |
| E09 | Choix de territoire | D+J ; V sur code 34172, `q` T | T, R16, O | France absent du référentiel `/territoires` ; zonages différents selon appel, A06 | France comme choix d'interface documenté pour les seules routes compatibles ; conserver code+zonage et parents | P1 |
| E10 | Projets BMO / territoires | D+J, chaîne R05 non retestée HTTP | BMO, C, REL R05, R16 pour mesure locale | 35 lignes régionales ne sont pas 35 régions ; rang par FAP228, A03/A06 | Groupes par famille et périmètre ; `/indicateurs` pour un territoire, `/recrutements` pour classer | P0 |
| E11 | Salaires / territoires | D+J, chaîne R06 non retestée HTTP | SAL, C méthode salaires, REL | 25 lignes régionales ; cas `null` en tranche ouverte non traité, A03/A04 | Une comparaison par FAP225 ; conserver rang et tranche ; médiane mensuelle séparée des quartiles annuels | P0 |
| E12 | Comparabilité et définitions | D+J, décision de comparaison à spécifier | MES, C, BMO/SAL | Catalogue seul insuffisant pour base/unité/population de chaque résultat, A03/A09 | Croiser métadonnées de réponse, famille, territoire réel, période et définition ; aucune agrégation | P0 |
| E13 | Choix de compétences OGR | V sur `code=125416` et `103659` ; `q` T | R23, O `/competences` | Confirmation des codes ne valide pas la recherche libre ni la pertinence de tous les rattachements | Choix explicite, catégorie correcte, limites 1–10, conserver codes et libellés | P1 |
| E14 | Recherche multicompétences | V sur deux codes, avec précautions | R23 complémentaire + JSON toutes/au_moins_une | Champs de match absents du schéma 200 statique et du mode `toutes`, A05 | Champs conditionnels ; conserver ordre API et nombre de macro-compétences ; aucun score personnel | P1 |
| E15 | Référentiel des contextes | D ; sélection globale T | C/O `categorie=contexte_travail`, M pour code 300782 | R24 ne teste pas `/competences?q=...&categorie=contexte_travail` | Utiliser cette valeur exacte de catégorie ; obtenir fixture dédiée ; réutiliser les contextes déjà reçus | P1 |
| E16 | Avec / sans contexte | V sur F16/300782 sans `fields` | R24 et deux JSON | Incident `fields` singulier/pluriel d'origine non établie, A05 | Tester filtres combinés et plusieurs codes ; éviter `fields` litigieux ; expliquer exclusion au niveau du parent V3 | P1 |
| E17 | Fiche Certification, deux intentions | D+J pour détail ; couverture fonctionnelle partielle | CD 112561/RNCP36101, C/O | Insertion, statut, dates, populations promis mais incomplets dans la table ; titres anciens non couverts, A07 | Ajouter spécification des champs par population, méthodologie MES, actifs/404 ; bascule d'affichage locale | P0 |
| E18 | Blocs RNCP | D+J pour quatre blocs ; filtre exact T | CB, CD, REL R11–R13 | Concordance RNCP/Certif Info statique ; compétences = texte, pas liste OGR | `certifinfo` OU `fiche` documenté ; RNCP uniquement ; conserver texte et `rang_bloc` | P1 |
| E19 | Certification → métiers | D+J statique, chaîne T | CD `rome_codes=[F1610]`, M, REL | Cas multi-ROME non démontré par le détail fourni | Parcourir `rome_codes[]`, pas seul `rome_code` nullable ; aucune garantie d'accès à l'emploi | P1 |
| E20 | Métier → certifications | D+J statique, filtre T | CL, REL R02, C/O | Pas de trace de requête complète pour ce JSON | Tester `rome=F1610`, pagination et cohérence des `rome_codes[]` ; pas de diplôme obligatoire déduit | P1 |
| E21 | Sessions à venir | D+J, appel antérieur partiel ; T pour rattachement individuel | R18 : 10 lignes région 76, Certif Info demandé 112561 | Pas d'ID session/Certif Info dans les lignes ; Onisep et zonages à cadrer, A06/A11 | Réaliser liste et filtres contractuels ; tester le filtrage sur certifications distinctes et demander la garantie RCO ; recette du rattachement tracée, sans places promises | P0 |
| E22 | Sessions en cours | D+J partiel ; T pour rattachement | R19 : 8 lignes, même filtre | Même limite que E21 ; aucune admission démontrée | Réaliser vue en cours et temporalité avec E21 ; validation fournisseur commune, sans promesse d'admission | P1 |
| E23 | Mobilités observées | D+J, appel avec filtres à tester | MOB, C, REL R07 | Origine et destination ne sont pas deux champs toujours simultanés ; codes FAP/hors emploi | Modèles selon `sens`, `maille/repli` par ligne ; pas de lien fiche ROME depuis une FAP non résolue | P2 |
| E24 | Prospective 2030 détaillée | D+J, filtres à tester | PRO, C, REL R04/R22 | Multi-FAP87, métropole, agrégats ; cohérence à organiser avec E08, A08 | Deux entrées métier/région avec tous les champs documentés, effectifs et taux fournis, croissance/départs/jeunes/déséquilibre explicités | P1 |
| E25 | Salaires par secteur économique | D+J, filtre à tester | SS, C | NAF38 × FAP225 ; repli par ligne et seuils ; rien à voir avec Domaine | Respecter `maille`, `repli`, famille ; parts non nécessairement exhaustives | P2 |
| E26 | Secteurs qui emploient le métier | D ; anomalie fournisseur sur les cas R17 ; restitution familiale J via E08 | R17 : 35 sans ROME, 0 avec F1610 à deux mailles ; R16 `emploi_secteurs` | Filtre métier non conforme ; les comptes locaux et parts familiales ne décrivent pas la même population | Réaliser le volet familial depuis `emploi_secteurs` et le contexte économique territorial séparé ; résoudre/tester R17 pour le résultat métier-territoire contractuel, sans fusion inventée | P0 |
| E27 | Mes pistes | Faisable en état local ; NC pour sauvegarde API | O : 21 GET, M pour réaffichage | Aucune persistance distante ; session et plafond à arbitrer | Réutiliser le cache métier, aucun nouvel appel à l'ajout ; durée de vie explicite | P1 |
| E28 | Comparateur deux métiers | D pour données ; T pour comparaison complète | MC, M, SAL/BMO, C `depuis` | Une seule fixture de compétences incomplète ; statistiques multi-familles ; certifications absentes de ses dépendances, A02/A03/A08 | Comparateur complet par questions : OGR sur jeux complets, descriptions et certifications via E05/E20, familles statistiques séparées ; accès aux volets détaillés | P0 |
| E29 | Exploration des transitions | D+J pour tags ; parcours de liste à tester | M, O `/metiers` | Aucun filtre transition serveur ; classement de croissance non déductible des tags | Badges et filtre local explicite sur le catalogue métier paginé complet ; conserver booléens inconnus ; aucun paramètre API inventé | P1 |
| E30 | Thèmes Formacode | D+J, chaîne complète T | FC, C, REL R03/R14/R15 | Thème → certifications prévu ; thème → sessions non certifiantes NC | Rester sur `/certifications?formacode=...` ; ne pas reprendre la source hors API citée dans le contrat | P2 |
| E31 | Catalogue méthodologique | D+J | MES : total 29 ; C/O `/mesures` | Catalogue global, pas disponibilité propre à un métier ; recouvrement E12, A09 | Charger une fois ; joindre `items[].code` à `items[].mesure` ; disponibilité lue dans la réponse métier | P1 |

## 4. Anomalies de l'audit et corrections intégrées au lot L0

Les constats et formulations « à corriger » ci-dessous sont conservés comme historique de l'audit ; les corrections documentaires ont été intégrées dans 01–07 pendant L0. Ils ne sont pas des recommandations de réduction ni une nouvelle liste d'audit à recommencer. Les tests HTTP et réponses fournisseur non acquis restent ouverts dans le triage courant de06, repris dans 10.

### A01 — Domaine : structure documentée, preuve réelle absente

`/domaines` accepte **uniquement** `grand_domaine`. Il ne faut pas tester un hypothétique `q` pour décider si la recherche libre est supportée : ce paramètre ne figure pas dans O. L'arbre est décrit par C : `items[].grand_domaine_code`, `grand_domaine_libelle`, `nb_metiers`, puis `items[].domaines[].domaine_code`, `domaine_libelle`, `nb_metiers`. `total` compte les grands domaines retournés ; pas de pagination. Le domaine conserve son parent dans l'état applicatif ; on n'invente pas un champ parent dans chaque sous-objet JSON.

À corriger après accord : remplacer le texte « non observé dans le CSV » de E03 par ces chemins, en marquant **D et non J** ; retirer l'hypothèse `/domaines?q` de 01 et 06. Le schéma `domaines.schema.json` est analytique, pas officiel. Une recherche locale éventuelle dans les libellés reçus doit rester une décision produit explicite, sans promesse de recherche API ou sémantique.

### A02 — Compétences : exhaustivité non acquise

MC indique `total=144`, `page_size=100`, `page=1`, `last_page=2`. Les 100 éléments reçus ne couvrent que `savoir_faire` (80) et `savoir` (20). La seconde page n'est pas conservée. Le jeu ne démontre donc pas la lecture complète des savoir-être/contextes et ne peut prouver une intersection exhaustive pour E28.

À corriger dans 02/03/04/07 : qualifier cette fixture de **partielle**, ajouter le critère « toutes les pages de chaque catégorie comparée sont présentes ». Une erreur de page doit produire « liste incomplète », jamais « compétence absente ». Deux métiers complets sont nécessaires pour tester le comparateur. `tag_coeur_metier=null` n'est pas `false`. `tx_fiches_rome4` et `nb_fiches_rome4_metier` servent à expliquer que le ROME V3 couvre des spécialités ; ils ne mesurent pas la maîtrise personnelle et n'exposent pas de codes métier V4.

### A03 — Unité de comparaison : famille + période + territoire réel

BMO régional comporte 35 lignes ; SAL régional en comporte 25. Une même zone peut apparaître dans plusieurs familles. Dans R16, tension et BMO portent `B1X34` (1 ROME) et `B6X73` (26 ROME) ; salaires porte `B0Z21` (8 ROME) ; prospective porte `B0Z` (15 ROME) et `B2Z` (9 ROME). Ces codes et `nb_rome_famille` doivent faire partie du modèle d'affichage et des clés de lignes, alors qu'ils sont omis des champs E10/E11/E28.

À corriger dans 01–04 et 07 : une ligne statistique est identifiée par la mesure, le grain, le code famille, la période et le territoire effectif. Deux ROME rattachés à la même famille partagent une observation ; montrer explicitement « même donnée de famille ». Deux familles différentes peuvent être décrites côte à côte avec leurs populations, sans en tirer une supériorité individuelle du métier. Si l'unité, la période ou la maille diffèrent, ne pas produire d'écart chiffré ni de classement commun. Aucun taux, delta, somme ou score supplémentaire proposé ici.

Le rang retourné est propre à une famille. Ne pas classer toutes les FAP ensemble ni sommer leurs BMO pour « le métier ». Une union de codes OGR est une opération de navigation sur identifiants déjà présents, pas une mesure de compatibilité ; son affichage doit être arbitré.

### A04 — `null` salarial : règle générale insuffisante

C, « Salaires : méthode », documente une médiane non chiffrable dans la tranche ouverte au-delà de 50 000 euros annuels. `salaire_net_*_median=null` peut alors coexister avec `tranche_salaire_median_libelle="50 000 euros et plus"`. Le classement contractuel peut placer cette médiane `null` en tête. Ce cas n'est pas représenté dans les fixtures SAL observées.

La règle de 01/02/05/07 « null → donnée non disponible » doit donc être spécialisée : afficher la tranche annuelle si elle est renseignée, sans inventer de médiane ni de conversion mensuelle. Ne pas supprimer mécaniquement cette ligne du classement et ne pas la trier comme zéro. Les autres `null` restent indisponibles selon la définition du champ. Les quartiles annuels ne constituent pas une dispersion de la médiane mensuelle : présenter un bloc annuel cohérent, ou seulement la médiane mensuelle. Publication salariale à partir de 30 observations de l'échantillon, non 30 salariés pondérés.

### A05 — Swagger partiel et incident R24

O ne contient aucun schéma de réponse 200 pour dix routes : `/domaines`, `/indicateurs`, `/mesures`, `/recrutements`, `/salaires`, `/salaires/secteurs`, `/mobilites`, `/prospective/metiers`, `/prospective/regions`, `/secteurs`. Les schémas analytiques ne comblent pas cette lacune à titre normatif. Le schéma statique `/metiers` n'inclut pas les trois champs conditionnels du mode `au_moins_une`, pourtant décrits dans le paramètre et observés dans R23. Le schéma de compétences omet aussi l'enveloppe contextuelle `rome_code/rome_libelle` observée et la synthèse `comparaison` décrite avec `depuis`.

De plus, l'inventaire O marque facultatifs `rome` et certains paramètres de contexte statistique que C impose fonctionnellement. L'inventaire de 02 est fidèle aux drapeaux O, mais il ne suffit pas comme validation de requête. Le client doit envoyer `rome` sur les statistiques métier et le couple territorial requis sur `/indicateurs` et `/secteurs`. Signaler la divergence au fournisseur ; ne pas qualifier les paramètres absents de supportés au motif qu'ils ne sont pas `required` dans O.

Les deux JSON d'erreur R24 portent `code=422`, `propertyPath=fields`, et citent le singulier `contexte_travail_code`, alors que le pluriel est autorisé. L'URL effectivement envoyée n'est pas dans les fichiers. **Aucune preuve d'un défaut général du paramètre `fields` ou des filtres de contexte.** Les tests sans projection sont concluants sur le cas fourni. Corriger la portée du blocage dans 06/07 et conserver l'incident historique séparément. Tout re-test devra tracer la requête réellement encodée. Le développement des filtres utilise les réponses complètes documentées et n'attend pas cette optimisation.

### A06 — Territoire demandé et signature des classements

| Usage | Requête prévue | Ce qui ne doit pas être transmis |
|---|---|---|
| Mesure d'un métier sur un territoire | `/indicateurs?rome=...&zonage=...&territoire=...` ; territoire omissible pour France | Pas de code mesure comme paramètre ; `fields` porte sur les champs de valeur |
| Classement BMO | `/recrutements?rome=...&zonage={zonage}` avec région, département ou CLPE ; `region` pour département/CLPE, `departement` pour CLPE | Pas de `territoire`, pas de commune, pas de périmètre incompatible avec le zonage |
| Classement salaires | `/salaires?rome=...&zonage={zonage}` avec région ou département ; `region` seulement pour département | Pas de `territoire`, de commune ou de CLPE |
| Sessions | `/sessions_*?certifinfo=...&zonage={zonage}&territoire=...` avec région, département ou CLPE | Commune et France exclus de l'enum O ; ne pas utiliser la mention contradictoire « france » de la description comme autorisation |

Les parents de la sélection commune peuvent proposer un autre périmètre de classement, à condition de l'annoncer et de le faire choisir. Ce n'est pas le repli automatique d'une mesure `/indicateurs`. `/territoires` ne propose pas `zonage=france`. Le choix France est construit dans l'interface uniquement pour les appels qui le documentent ; `code=null` dans la chaîne nationale ne signifie pas erreur.

R16 montre cinq mesures à la CLPE, cinq au département, trois à la région et une à la France. `repli=true` sur les quatorze. Les sorties `/salaires/secteurs` et `/mobilites` utilisent `items[].maille`, pas un `items[].maille_reelle` imaginaire. `/secteurs` a sa maille territoriale en tête et `metier_maille` pour les parts métier. Les comparaisons doivent porter sur la géographie réelle et distinguer les replis identiques obtenus depuis deux communes.

### A07 — Certification : couverture réelle et spécification incomplète

E17 liste les identifiants, quelques voies d'accès et le niveau ; la fonction 01 et le diagramme 05 promettent aussi statut, insertion et résultats par population. Les données existent pour partie dans C/O/CD/CL, mais elles ne sont pas mappées dans E17, et E17 ne dépend pas de MES pour sa méthodologie. Proposition de complément de E17, sans nouveau besoin ni nouvel endpoint :

| Bloc annoncé | Chemins sur `/certifications/{certifinfo}` | Types et règles |
|---|---|---|
| Identité et validité | `certifinfo_code`, `certifinfo_libelle`, `repertoire_code`, `fiche_code`, `etat_certifinfo_libelle`, `type_certification_libelle`, `date_fin_enregistrement` | Chaînes, date ISO ou valeur absente/null selon exposition ; ne pas calculer un statut personnel à partir de la date seule |
| Voies d'accès | `tag_acces_formation_initiale`, `tag_acces_apprentissage`, `tag_acces_formation_continue`, `tag_acces_contrat_professionnalisation`, `tag_acces_candidature_individuelle`, `tag_acces_vae` | Booléens nullables selon schéma ; voie décrite ≠ admission individuelle |
| InserJeunes scolaire | `nb_ij_scolaire_sortants`, `nb_ij_scolaire_emploi_12m`, `tx_ij_scolaire_emploi_12m` | Effectifs et taux national ; cumul 2023–2024 ; ne pas fusionner avec apprentissage |
| InserJeunes apprentissage | `nb_ij_apprentissage_sortants`, `nb_ij_apprentissage_emploi_12m`, `tx_ij_apprentissage_emploi_12m` | Même horizon, autre population ; taux déjà fourni |
| InserSup | `promotion_insersup_libelle`, `nb_insersup_diplomes`, `nb_insersup_emploi_salarie_12m`, `tx_insersup_emploi_salarie_12m` | Promotion explicitée ; champs null dans CD ne prouvent pas une insertion nulle |
| Demandeurs d'emploi formés | `nb_de_sortants`, `nb_de_acces_emploi_6m`, `tx_de_acces_emploi_6m` | Accès à 6 mois, sortants 2024 ; population/horizon différents des deux précédents |
| Bloc RNCP | `nb_blocs_competences`, `bloc_competences_codes[]`, `tag_validation_partielle` | Null/absence de bloc publié ≠ aucune compétence ; aucun bloc RS |

Les effectifs/taux concernés admettent **nombre ou `"secret_stat"` ou `null`**. Les taux sont numériques (entiers ou décimaux), non nécessairement des entiers. MES permet de documenter les millésimes ; pas de champ fictif `millesime` uniforme sur la fiche. Les salaires InserSup ont leurs propres promotions/horizons et ne sont pas les salaires FAP225 de la fiche métier. Les indicateurs sont nationaux ; aucun filtre territoire sur cette route.

Autre limite fonctionnelle majeure : seules les certifications actives sont exposées. « Je possède » peut désigner un ancien diplôme absent de `/certifications`, ou un code qui retourne 404. Il n'existe pas de recherche d'archives ni de résolution de successeur en endpoint : le rattachement de sources anciennes au successeur est une règle interne décrite, pas une opération accessible. Ni éligibilité VAE individuelle, ni reconnaissance d'équivalence ne sont démontrées. À arbitrer : message et périmètre de la bascule, pas ajout de données.

### A08 — Documents, diagrammes et dépendances ne décrivent pas exactement le même produit

| Documents concernés | Incohérence | Proposition de correction |
|---|---|---|
| 01, 04, 07 | 01 recommande compétences/contextes au MVP mais 06 les soumet à arbitrage ; 07 phase 1 ordonne leur construction | Décision actuelle : inclusion acquise des compétences et contextes ; définir leur réalisation et recette sans rouvrir leur inclusion |
| 01, 04, 07 | E21 « MVP sous réserve » dans 01/04/CSV ; 07 le place en phase 2 | E21/E22 inclus ; un chantier commun sessions avec validation de traçabilité et deux temporalités |
| 01, E08, 07 | Anciennes recommandations de report de la prospective/mobilités/secteurs ; `/indicateurs` contient déjà des résultats utilisables | Ces recommandations sont caduques ; réutiliser la réponse entre synthèse, détail et comparateur dans la cible complète |
| 01, E28, 04 | Comparaison des activités/contextes/certifications annoncée, mais E28 cite surtout les compétences et dépend de E27/E06/E10/E11 | Ajouter E05 pour descriptions et E20 pour certifications ; référencer E08/E09/E12/E31 pour statistiques locales et définitions, avec accès aux détails E23–E25 |
| 05 navigation principale | Domaine → liste métiers → sélection typée Domaine : ce flux sélectionne déjà un métier et ne donne pas un accès clair à la fiche Domaine | Placer la sélection du domaine avant sa fiche, puis la liste de ses métiers |
| 05 certification | `GET /certifications certifinfo` ressemble à un filtre liste inexistant | Écrire le chemin `/certifications/{certifinfo}` |
| 05 territoire | Des flèches communes suggèrent une signature identique vers indicateurs, recrutements et salaires | Représenter l'adaptation explicite des paramètres et les périmètres supportés |
| 05 états | `secret_stat` représenté au même niveau que `[]` ou « réponse » ; cas salaire tranche ouverte absent | Distinguer enveloppe/collection et état de chaque champ, en consultant la définition |
| 06 et sources R24 | Le vieux rapport d'incident porte encore « à retester » ; le rapport final confirme les filtres sans `fields` | Lire les deux chronologiquement ; seul l'incident de projection reste non expliqué |
| 07 | Nom de rapport d'implémentation `08_RAPPORT_IMPLEMENTATION.md` et consignes de développement | Ne pas exécuter ce prompt avant arbitrage ; conserver le présent audit comme livrable 08 demandé |

La décision produit formulée dans la conversation confirme désormais le périmètre complet E01–E31 et la recherche de couverture maximale dans les 21 GET. Elle remplace les recommandations de réduction des documents antérieurs. Les modalités de stockage, de présentation des comparaisons et de publication restent des choix d'exécution ; elles ne peuvent servir à retirer une fonction. Les faits de preuve et les impossibilités contractuelles restent distincts de cette validation produit.

### A09 — Le catalogue global n'est pas la disponibilité par métier

MES expose 29 entrées de plusieurs ressources, alors que R16 en renvoie 14 dans `/indicateurs`. Un catalogue de mesure ou `nb_rome_couverts` ne prouve pas une valeur pour le métier et le lieu choisis. E31 « Quelles mesures existent pour ce métier ? » doit devenir une explication du catalogue et des résultats effectivement reçus, en distinguant `valeurs=[]` d'une mesure omise par `fields`. `source` est l'attribut du catalogue ; `source_libelle` celui des réponses statistiques. L'unité n'est pas un champ uniforme : la tirer de la définition et du champ documenté, jamais supposer `items[].unite`.

### A10 — Activités, absences et intitulés

Il n'existe pas de champ `activites` dans l'objet métier O/M. Les savoir-faire peuvent être présentés comme tels ; les `definitions[]` comme définitions ; on ne génère pas d'activités ou de texte métier à partir d'inférences. Les champs de proximité et de contexte possèdent déjà leurs libellés parallèles ; conserver les codes comme identifiants. Le code OGR `038055` doit rester une chaîne avec zéro initial, comme les codes région/département ; ne pas convertir ces identifiants en nombres.

`tag_transition_*` permet des badges de fiche, sans filtre dédié de recherche. « Secteur » au sens Domaine ROME et « secteur économique » NAF38 doivent rester distinguables, y compris dans un comparateur. « Diplôme » mérite une aide indiquant que les résultats incluent titres et certifications RS.

### A11 — Sessions : garde réelle, Onisep et temporalité

R18 et R19 sont des réponses réelles cohérentes, pas des appels jamais testés. Leurs 10 et 8 lignes portent toutes `tag_onisep=false` dans le périmètre indiqué `onisep=exclure`. Il manque cependant dans chaque ligne un identifiant stable de session et un identifiant de certification ; ni le SIRET ni `(SIRET,date_debut)` ne sont démontrés comme uniques. Aucune déduplication métier ou fiche session stable à inventer.

O précise déjà `presentiel_distantiel` : 0 présentiel, 1 mixte, 2 distanciel. Le point « signification à confirmer » du rapport R19 est donc résolu documentairement pour cet enum, sans nouveau test. O précise aussi que les offres Onisep ont une date de rentrée conventionnelle et ne sont pas des sessions datées ordinaires. Laisser le défaut explicite `exclure` dans les scénarios actuels ; toute activation d'Onisep nécessite une présentation séparée à arbitrer. Les dates de ces fixtures sont évaluées au 1er novembre 2026, jamais réinterprétées comme résultats actuels lors d'une future démonstration.

### A12 — Préparation technique transversale absente ou insuffisante

C §2 exige un jeton (`Authorization: Bearer` ou `X-API-Token`), prévoit 40 requêtes/seconde/jeton, interdit la transmission des identifiants et données à des tiers et demande le logo RCO sur les supports affichant les données. Les documents Explorer ne traduisent pas complètement ces obligations dans leur architecture. Aucune URL de serveur dans le champ `servers` de O ; environnement, URL de base, politique d'accès navigateur/CORS et gestion du jeton de réalisation restent à préciser. Ne pas publier un jeton dans une interface cliente ou un dépôt.

La recherche a un contrat de préfixes, normalisation et 2–100 caractères ; les fautes approximatives ne sont pas démontrées. Les erreurs contractuelles comprennent 400, 401, 404, 422, 429 et 503 : 429/503 manquent dans les scénarios les plus visibles du brief. Annulation des résultats périmés, erreurs partielles, reprise bornée et déduplication des appels sont à prévoir. L'indexation SEO n'est pas une capacité offerte par ces 21 GET : elle dépend de l'application d'accueil, des modalités de publication et de son rendu, encore inconnus.

## 5. Règles de valeur à inscrire dans la recette

| Situation | Lecture et traitement proposé |
|---|---|
| Nombre `0` | Afficher zéro avec définition/unité ; ne pas le remplacer par « absent » |
| `null` | Inconnu/non disponible selon le champ ; exception documentée des tranches salariales ouvertes à traiter avant le message générique |
| `"secret_stat"` | Valeur existante non diffusable ; ni coercition numérique, ni déduction à partir d'autres effectifs/taux, ni retrait silencieux d'un calcul |
| Clé absente | Omission possible par `fields`, variante conditionnelle ou écart de contrat ; distinguer ces causes sans inventer une valeur |
| `items=[]` | Aucun résultat pour cet appel ; ne démontre ni absence d'employeur ni absence de formation réelle |
| `valeurs=[]` | Mesure reçue sans valeurs ; ne pas fabriquer un zéro ; contrôler `maille_reelle` et les métadonnées |
| `maille_reelle=null` | Aucune maille renseignée pour cette mesure ; ne pas créer un territoire réel depuis la sélection utilisateur |
| `repli=false` | À interpréter avec la présence de valeurs et la maille ; ne prouve pas à lui seul une donnée locale disponible |
| `tag_*=null` | Non renseigné/non applicable ; ne pas afficher un « Non » |
| Mois absent dans `offres_emploi_mensuelles` | Ne pas remplir par zéro : le contrat indique qu'un mois sans offre peut être absent |
| Part de mobilité / secteur non exhaustive | Ne pas compléter à 100 ni renormaliser ; top N et seuils de diffusion documentés |

R16 contient trois occurrences de `secret_stat` dans `formations_metier.valeurs[0]` (`nb_de_sortants`, `nb_de_acces_emploi_6m`, `tx_de_acces_emploi_6m`). CL en contient 22. Ces cas réels permettent une recette du masquage. R16 contient aussi BMO saisonnier `nb=0` et `tx=1.7` sur B1X34 ; conserver les valeurs reçues et demander l'explication des arrondis/dénominateurs avant de créer un test d'égalité arithmétique.

## 6. Compléments exploitables à intégrer à la conception complète

Ces compléments sont rattachés aux IDs existants dans le plan 09. Leur conception est prévue ; leur comportement réseau reste à vérifier lorsqu'aucun exemple ne le démontre. Les modalités de restitution à valider n'annulent pas les 31 fonctionnalités.

| Possibilité dans les 21 GET | Intérêt | Preuve et garde |
|---|---|---|
| `/metiers/{cible}/competences?depuis={origine}` | Comparaison directionnelle déjà prévue par l'API : tags communs/voisins et synthèse | C et description O ; aucun JSON `depuis` observé dans la campagne ; tester avant usage. « Acquise » signifie portée par un métier, jamais maîtrisée par la personne. Aucun score personnel à ajouter |
| `coeur_metier=true`, `tx_fiches_rome4`, arborescence macro/enjeu/domaine | Réduire la surcharge et expliquer les spécialités | C/O, MC pour les attributs ; filtre `coeur_metier` à tester ; ne pas cacher les autres catégories comme absentes |
| `/competences?code=...,...` | Résoudre jusqu'à 10 codes en un appel et réutiliser les libellés/catégories | C/O, tests R23 unitaires seulement ; pas une intersection multicompétences par lui-même |
| `/certifications/blocs?q=...` puis `certifinfo_codes[]` | Retrouver des certifications par le texte publié d'un bloc | C/O et CB pour structure ; recherche et enchaînement à tester ; aucun rapprochement automatique texte RNCP ↔ OGR |
| `/certifications?acces=...&validation_partielle=true` | Navigation plus utile pour l'intention d'obtention | C/O ; filtres à tester ; voie possible ≠ droit personnel |
| `/indicateurs` : `emploi_secteurs` | Décrire les secteurs où travaillent les familles, malgré le blocage `/secteurs?rome` | R16 : 13 valeurs régionales observées ; ne remplace pas les employeurs locaux de E26, ne joint pas des comptes locaux, ne somme pas les familles |
| `/indicateurs` : tension, caractéristiques d'offres, statut d'emploi | Répondre aux questions sur conditions du marché sans nouvel endpoint | C + R16 ; taux/populations/seuils à respecter ; pas d'offres nominatives ni de durée d'expérience exigée exposée |
| `/prospective/metiers?region=...` puis `items[].rome_codes[]` | Découverte de familles et navigation vers leurs métiers, complément de E24/E19 | C/O/PRO, REL R22 statique ; tester la chaîne, pas de classement personnel |
| `/mesures` : couverture et définitions | Expliciter les limites de diffusion et les familles | MES ; couverture globale, aucune garantie sur le métier/territoire sélectionné |

## 7. Besoins non couverts à signaler

Dans les 21 GET, aucun dispositif de compte/favoris serveur, sauvegarde de profil, évaluation individuelle de compétences, score d'adéquation, équivalence RNCP–OGR, réservation/inscription ou disponibilité de places, liste nominative d'employeurs, recherche d'offres individuelles, statistiques agrégées du Domaine ROME, résolution métier ROME depuis une simple destination FAP de mobilité, recherche territoriale par code postal/distance/population, archive consultable des diplômes ou sessions non certifiantes filtrées par Formacode n'est prévu. La source documentaire peut citer des producteurs et des mécanismes internes ; cela ne crée aucun accès supplémentaire autorisé.

## 8. Vérifications effectuées et limites restantes

- Vérification locale des 31 endpoints de conception contre les 21 routes O ; aucun endpoint étranger détecté. Tous les chemins de `Preuve_reference` du CSV existent. Le texte placeholder E03 reste à remplacer ; les champs conditionnels E14 sont décrits/observés malgré leur omission du schéma statique.
- Lecture structurée de 73 JSON : 57 historiques, 16 sous `06_controles/resultats`, incluant deux erreurs R24. Analyse des identifiants, enveloppes, types observés, pagination, champs de secret et grains. Elle ne valide pas toutes les valeurs ni les réponses non collectées.
- Exécution des six scripts de contrôle existants avec Python 3.13, via `runpy.run_path(..., run_name='__main__')`. Pour respecter la conservation des preuves, `Path.open` en écriture a été remplacé temporairement par un tampon `io.StringIO`/`BytesIO`, et `Path.mkdir` neutralisé ; lectures conservées, `-B` utilisé. Les cinq sorties CSV ont donc été détournées en mémoire. Les messages « Rapport/Rendu dans… » sont les messages d'origine des scripts et ne signifient pas que ces fichiers ont été réécrits.

| Script | Résultat local |
|---|---|
| `verifier_contrat.py` | 21 routes dans chaque export comparé |
| `verifier_echantillons.py` | 57 JSON analysés ; 45 associés à une route sans schéma 200 officiel |
| `verifier_schemas_complementaires.py` | 57 JSON, aucun champ non décrit par les modèles enrichis ; résultat non normatif et non validation complète de types |
| `verifier_relations_api.py` | 24 relations, 18 correspondances statiques, 6 sans correspondance testable ; aucun test HTTP |
| `verifier_uml_global.py` | 21 GET, 24 relations, 3 UML de référence ; vérification textuelle, pas rendu graphique |
| `verifier_preuves_directes.py` | Cohérence des fixtures R16/R23/R24 ; R17 toujours partiel ; limites R18/R19 conservées |

Les six scripts se terminent sans échec dans ce mode. Leurs assertions sont plus étroites que le présent audit : elles ne valident pas une interface ni une comparaison statistique complète. Une tentative de copie de contrôle isolée a rencontré un refus d'accès à un répertoire temporaire ; l'exécution sans écriture décrite ci-dessus a permis de réaliser les contrôles. Le dossier temporaire vide créé dans le workspace a été nettoyé.

Les validations réseau nouvelles restent **NON EFFECTUÉES** : recherche libre, `/domaines`, pages manquantes, nouveaux codes, filtres et chaînes Certification, `depuis`, CORS, authentification, débit et erreurs de transport. La conservation d'un corps `code:422` ne prouve pas à elle seule le statut de transport HTTP. Les versions des sources consultées restent celles du dossier ; aucune source externe, accès SQL ou donnée supplémentaire n'a été utilisé.

Les corrections documentaires ci-dessus sont intégrées dans les sept livrables existants, table commune03 comprise. Le backlog, les diagrammes de parcours et le prompt sont alignés ; aucun UML de référence ni JSON source n'est modifié. Le plan proposé est dans `09_PLAN_DE_REALISATION.md` ; les choix nécessitant validation sont isolés dans `10_DECISIONS_A_ARBITRER.md`.

## Annexe — Vérification des chemins et types de la table de conception

Notation : `$` désigne la racine de la réponse. Dans une même cellule, les accolades regroupent des noms de champs au même niveau ; elles ne sont pas une syntaxe de requête API. `string[]` signifie une liste de chaînes. Les types observés restent limités aux fichiers reçus ; les nullabilités contractuelles sont à conserver même lorsqu'aucun `null` n'apparaît dans l'échantillon. Les chaînes d'identifiants ne sont pas des entiers. L'inventaire des paramètres de 02 concorde avec O ; ses limites fonctionnelles et divergences `required` sont détaillées en A05/A06 et dans le plan 09.

| IDs couverts | Chemins vérifiés | Types et portée de preuve |
|---|---|---|
| E01 / E04 / E14 / E16 | `$.items[].{rome_code,rome_libelle,domaine_code}` ; E14 `competences_trouvees_codes`, `nb_competences_trouvees` ; E16 `contexte_travail_codes` | Chaînes ; tableaux de chaînes et entier pour les champs de match ; contexte en `string[]`. O + JSON R23/R24. Match conditionnel et absent en mode `toutes` ; `nb_macro_competences_trouvees` entier également observé |
| E02 / E20 | `$.items[].{certifinfo_code,certifinfo_libelle,repertoire_code,fiche_code}` | Chaînes observées dans CL ; E20 n'utilise pas tous les champs E02. Schéma O autorise des champs nullables ; `q`/filtre ROME non démontrés par la structure seule |
| E03 (D uniquement) | `$.items[].{grand_domaine_code,grand_domaine_libelle,nb_metiers}` et `$.items[].domaines[].{domaine_code,domaine_libelle,nb_metiers}` ; `$.total` | C : codes/libellés chaînes, nombres entiers, `domaines` tableau ; aucune observation JSON. Pas de propriété `page/last_page` documentée |
| E05 / E07 / E19 / E27 | `$.{rome_code,rome_libelle,definitions}` ; E05 `domaine_libelle`, `appellations`, `metiers_proches_codes`, `contexte_travail_codes` | Codes/libellés chaînes, définitions/appellations/codes proches/contextes en `string[]` dans M ; E27 n'exploite que code/libellé. M ne prouve pas l'ouverture de toutes les cibles |
| E06 / E28 | `$.items[].{competence_code,competence_libelle,categorie_competence_libelle,tag_coeur_metier}` | Trois chaînes et booléen ou null dans MC ; catégorie et pagination de l'enveloppe à conserver. Les contextes ne sont pas observés dans cette page de MC |
| E08 | `$.items[].{mesure,grain,valeurs,maille_reelle,repli,millesime}` | Chaînes pour mesure/grain/millésime, tableau d'objets pour valeurs, chaîne ou null pour maille, booléen pour repli. Les valeurs scalaires se trouvent sous `$.items[].valeurs[]`, jamais directement dans la mesure |
| E09 | `$.items[].{territoire_code,territoire_libelle,zonage,region_code,departement_code}` | Chaînes ; parents nullables, notamment département null pour une région. Les deux premiers champs ne sont pas les paramètres de requête de toutes les routes |
| E10 | `$.items[].{nb_projets_recrutement,tx_projets_recrutement_difficiles,territoire_code}` ; `$.{grain,millesime}` | Entier, nombre (entier ou décimal) et chaîne ; grain/millésime chaînes en tête. Compléter par `items[].fap_228_code`, `fap_228_libelle`, `nb_rome_famille`, `rang` (chaînes, entiers). BMO/R16 |
| E11 | `$.items[].{salaire_net_mensuel_median,salaire_net_annuel_q1,salaire_net_annuel_q3}` ; `$.{grain,millesime}` | Entiers observés, null possible selon C ; grain/millésime chaînes en tête. Ajouter code/libellé FAP225, `nb_rome_famille`, rang et tranche. SAL ; cas tranche ouverte documenté seulement |
| E12 / E31 | `$.items[].{code,grain,millesime,definition}` | Chaînes dans MES ; `$.items[].source` chaîne, `champs` et `mailles` tableaux de chaînes. Aucun filtre métier ni paramètre `code` sur `/mesures` |
| E13 / E15 | `$.items[].{competence_code,competence_libelle,categorie_competence_libelle,rome_codes}` | Chaînes et `string[]` dans R23 ; E15 n'utilise pas `rome_codes`. La structure est démontrée pour des savoir-faire ; le résultat d'une recherche du catalogue des contextes reste à collecter |
| E17 | `$.{certifinfo_code,certifinfo_libelle,fiche_code,rome_codes,niveau_certification_code,tag_acces_vae,tag_acces_formation_continue}` | Chaînes, `rome_codes` en `string[]`, deux booléens dans CD ; nullabilités O à conserver, notamment niveau des RS. Les champs d'insertion supplémentaires sont distingués en A07 |
| E18 | `$.items[].{bloc_code,bloc_libelle,competences,modalites_evaluation}` | Quatre chaînes dans CB. `competences` est un texte, non `string[]` et non un tableau d'OGR ; `certifinfo_codes` est bien une liste de chaînes |
| E21 / E22 | `$.items[].{ville,date_debut,date_fin,raison_sociale}` ; E21 `nb_sessions` | Chaînes ; dates ISO documentées, entier pour nombre de sessions. `siret_formateur` et `code_insee` sont des chaînes ; flags de formation booléens ; `presentiel_distantiel` entier enum 0/1/2. R18/R19 + O |
| E23 | `$.items[].destination_libelle` OU `origine_libelle`, `$.items[].tx_personnes` ; `$.{grain,millesime}` | Chaîne selon le sens, nombre (entier ou décimal), chaînes en tête. MOB. `maille/repli` sont sous `items[]` et ne sont pas une maille commune garantie |
| E24 | `$.items[].{nb_creations_nettes_emplois_2030,nb_departs_fin_carriere_2030,nb_postes_a_pourvoir_2030}` ; `$.{grain,millesime}` | Entiers observés, chaînes en tête. PRO ; conserver `items[].fap_87_code`, `fap_87_libelle`, territoire et `nb_rome_famille`. Créations nettes négatives possibles selon C |
| E25 | `$.items[].{secteur_naf38_libelle,salaire_net_mensuel_median,tx_salaries_secteur}` ; `$.grain` | Chaîne, entier et nombre décimal observés ; grain chaîne en tête. SS ; salaires nullables selon C ; FAP, code NAF et `maille/repli` par ligne nécessaires |
| E26 | `$.{items,maille_reelle,repli,grain}` | Tableau vide dans les tests avec F1610, chaîne, booléen, chaîne ; ne prouve pas les champs d'un élément métier-secteur. Les éléments du test sans ROME ne valident pas les parts métier avec filtre |
| E29 | `$.{tag_transition_ecologique,tag_transition_numerique,tag_transition_demographique}` | Booléens observés dans M, nullabilité du schéma à respecter ; pas de paramètre de recherche transition |
| E30 | `$.items[].{formacode_code,formacode_libelle}` | Chaînes dans FC ; chaîne documentaire Formacode → certifications à tester séparément |

Le contrôle SHA-256 de l'audit initial comparait les **172 fichiers préexistants** au relevé pris avant création des rapports : aucun fichier modifié, ajouté ou supprimé dans cet ensemble. Seuls les trois livrables demandés avaient été ajoutés. Le lot L0 suivant actualise les sept livrables01–07 et les mentions de suivi08–10. Ses six contrôles hors ligne sont réexécutés avec succès et son bilan figure en06 ; ils ne sont pas de nouveaux appels HTTP. Le tableau de synthèse conserve les 31 IDs E01–E31.
