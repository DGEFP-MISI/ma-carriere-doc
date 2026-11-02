# Prompt Codex — réaliser Explorer V2 complet après autorisation

## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.


**Mise à jour du 2 novembre 2026 — dossier rangé.** Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les 31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.

Ce prompt décrit la future réalisation. **Le lot L0 est terminé. Une maquette HTML de conception a été autorisée et réalisée ; l’application connectée à l’API ne doit pas être démarrée sans instruction explicite de la maîtrise d’ouvrage.** La cible E01–E31 est définitivement conservée. Ne pas refaire un audit pour proposer une réduction, ni classer une fonction comme extension facultative à cause d'un test ou exemple manquant.

## 1. Lis dans cet ordre, sans sauter les annexes
1. `07_parcours/Explorer/01_EXPLORER_V2_FONCTIONNEL.md` ;
2. `07_parcours/Explorer/06_DECISIONS_ET_POINTS_A_VALIDER.md` ;
3. `07_parcours/Explorer/03_TABLE_CONCEPTION.csv` (UTF-8 BOM, séparateur `;`) ;
4. `07_parcours/Explorer/02_SPECIFICATIONS_API.md` ;
5. `07_parcours/Explorer/04_BACKLOG_USER_STORIES.md` ;
6. `07_parcours/Explorer/05_PARCOURS_DIAGRAMMES.md` ;
7. `01_sources/contrat_interface_2026-10-19.md` et `01_sources/openapi/docs_json_interface.json` ;
8. `03_catalogue/routes_openapi.csv`, `03_catalogue/champs_observes_tous_endpoints.csv`, `03_catalogue/modeles_reponses/` ;
9. `04_relations/CHAINES_APPELS_API.md`, `04_relations/PREUVES_ET_LIMITES.md`, `04_relations/STATUTS_EN_COURS.md` et `04_relations/matrice_statuts_apres_tests.csv` si présent ;
10. `06_controles/VALIDATION_R16_territoires_indicateurs.md`, `VALIDATION_R17_territoires_secteurs_V2.md`, `VALIDATION_R18_certifications_sessions_a_venir.md`, `VALIDATION_R19_certifications_sessions_en_cours.md`, `VALIDATION_R23_competences_metiers.md`, `VALIDATION_R23_recherche_multicompetences.md`, `VALIDATION_R24_contextes_metiers.md` ;
11. Exemples JSON dans `02_reponses_observees/` + preuves JSON propres dans `06_controles/resultats/` si présents.

Si un chemin n'existe pas, documente-le dans le rapport, cherche l'équivalent dans l'arborescence existante, et **n'invente pas les preuves**. Inspecte le dépôt avant de choisir framework, arborescence, scripts ou conventions.

Les documents08–10 donnent l'audit et la décision validés ;01–07 sont désormais alignés. 03 fait foi pour les besoins/fonctions, 31 lignes, colonnes de pilotage et Appels_GET_detail ;02 couvre les 29 mesures et tous les champs du catalogue ;06 contient le triage des 14 questions, sans réinterroger le fournisseur sur des réponses déjà documentées.

## 2. Réalise tous les lots techniques

L0 est exécuté pour l'alignement documentaire ; aucun développement n'est réalisé ici. Au démarrage autorisé, identifier le dépôt d'accueil, ses conventions et la gestion du jeton ; ne pas initialiser spontanément une application dans le dossier de référence. Produire à partir du CSV le suivi de réalisation, pas une nouvelle version concurrente des spécifications. La table ci-dessous reprend les lots de09, tous nécessaires à la cible complète.

| Lot | IDs / résultat concret | Dépendances | Critère de sortie |
|---|---|---|---|
| L0 — Alignement et chantier fournisseur | Réalisé : alignement01–07 en place, 31 lignes/31 stories, 29 mesures détaillées ; Q01–Q14 triées entre acquis, GET et fournisseur | Périmètre confirmé ; suivi des captures et rôles proposés dans 06/10, demandes non envoyées | Six contrôles hors ligne réussis, cohérence documentaire et intégrité vérifiées ;31 IDs maintenus ; aucune fonction supprimée ni application démarrée |
| L1 — Intégration dans l'application d'accueil | Transport GET, auth, adaptateurs pour les familles de réponses, erreurs, cache et provenance | D10, URL et jeton gérés, conventions connues | Tests de transport/variantes ; preuve HTTP réelle distincte des tests sur fixtures ; aucun jeton dans le client public |
| L2 — Navigation, fiches et certifications | E01–E07, E09, E17–E20 | L1, décisions de présentation D02/D03 ; collecte Domaine et pages dans ce lot | Trois fiches et chaînages accessibles ; compétences complètes ; insertion par populations et blocs RNCP ; limites explicites |
| L3 — Exploration OGR, transitions et thèmes | E06/E13–E16/E18/E29/E30 ; complément cœur de métier/arborescence et recherche de blocs | L1/L2 utiles ; D04 ; données de catalogue complètes pour filtres locaux | Recette R23/R24, tags locaux sans paramètre fictif, thème → certifications ; recherches additionnelles documentées |
| L4 — Indicateurs et territoires | E08/E10/E11/E12/E31 | L1/L2, D06/D07, modèles multi-FAP | Mesures locales et classements complets, mailles/secret/tranches/horizons exacts ; méthodologie réutilisée par tous les lots |
| L5 — Mobilités professionnelles | E23 | L1 et sélection métier/territoire ; composant de provenance L4 réutilisable sans attendre sa recette complète | Deux sens, âges, France/région, familles et hors emploi, repli et parts non exhaustives ; tests dédiés |
| L6 — Prospective détaillée 2030 | E24, complément découverte par région → métiers | L1, sélection métier/région, dictionnaire et familles | Effectifs et taux reçus, croissance/départs/postes/jeunes/déséquilibre, spécificité/part, tris et référence France ; limites géographiques testées |
| L7 — Secteurs économiques et salaires sectoriels | E25/E26 | L1, E08 pour parts familiales, résolution R17 engagée dès L0 | Salaires FAP×NAF et contexte territorial distincts ; recette du résultat métier-territoire après clarification/correction R17. E26 reste ouvert tant que celle-ci manque |
| L8 — Sessions à venir et en cours | E21/E22 | L1, E17/E09, D09 et validations RCO préparées dès L0 | Deux temporalités et modalités, filtres et pagination testés, garantie de rattachement établie ; pas de places/admission promises |
| L9 — Pistes et comparateur complet | E27/E28, réutilisation E05/E06/E08/E10/E11/E17–E25/E31 | Cache L1, décisions D05/D08 ; vues descriptives et statistiques alimentées progressivement par les autres lots | Deux métiers, compétences/contextes complets, certifications, familles communes identifiées et volets détaillés ; aucun score ou calcul inventé |
| L10 — Recette intégrée et publication | Parcours complet E01–E31, accessibilité et preuves | Tous les lots ; D10 pour modalités de publication | Matrice de 31 recettes ; aucun ID écarté pour obtenir artificiellement un résultat complet ; livré/simulé/testé HTTP/bloqué distingués |

Les lots L3–L8 avancent selon leurs dépendances, pas comme fonctions facultatives. Une fixture manquante se collecte et se teste dans le lot ; une anomalie fournisseur se résout et reste ouverte dans le suivi. Les travaux indépendants continuent. Ne pas déclarer 31 fonctions livrées si une capacité contractuelle reste bloquée.

## 3. Contrats et interdits


- Consommer **uniquement les 21 GET** listés dans `03_catalogue/routes_openapi.csv`. Aucune API tierce, accès SQL, Octopilot ou récupération directe France Travail/CDC.
- Codes métiers **ROME V3 uniquement**, y compris dans les routes et résultats. Codes OGR autorisés pour compétences/contextes ; données éventuellement consolidées depuis ROME4 restent exposées sur le ROME V3 parent.
- Types statiques et runtime guards pour réponses et états ; respecter les paramètres réels `q`, `page`, `competence`, `mode_competence`, `contexte`, `sans_contexte`, `zonage`, `territoire` selon chaque endpoint (ne pas les interpoler sur endpoints qui ne les acceptent pas).
- Pas de champ ou de score inventé ; pas d'indicateur agrégé artificiel ou de recommandation personnalisée.
- Ne pas confondre salaire FAP225, recrutements FAP228, perspective FAP87 ; afficher la maille et le grain réels ; ne jamais utiliser « salaire de ce métier précis » lorsque l'API donne une FAP.
- `null`, `0`, `[]`, champ absent, `secret_stat` : comportements différents. Pour `/indicateurs` appliquer `maille_reelle` **par mesure**. Ne pas faire disparaître une donnée masquée dans un calcul.
- R18/R19 : listes et temporalités à réaliser, tests contrastés et garantie RCO du filtre en recette, aucune place/admission promise. R17 : E26 maintenu, lectures accessibles séparées et résolution fournisseur du résultat métier-territoire ; pas de compte local reconstruit. R24 : sans fields fonctionne sur le cas fourni, projection plurielle à retester sans présumer un défaut général.
- Le formulaire d'ajout aux pistes et les filtres restent accessibles au clavier, sans dépendance à la couleur. Respect DSFR et RGAA.


- Salaires : null avec tranche ouverte50 000 EUR et plus n'est pas zéro ou une médiane inconnue à reconstruire ; médiane mensuelle et quartiles annuels séparés. Comparaisons côte à côte sans delta/score inventé.
- Compétences : MC page 1/2, 144annoncées. Compléter les pages avant absence/commun/spécifique. depuis décrit une relation de métiers, jamais maîtrise personnelle ; conserver les taux API sans recalcul.
- Domaine : arbre non paginé, grand_domaine seul ; filtrelocal explicite pour la recherche de libellés. Transitions : local sur catalogue complet, aucun paramètre transition serveur.
- Mobilités : deux sens, âge etFAP225/hors emploi, parts non renormalisées. Prospective : deux routes, tous champs et tris documentés, FAP87/agrégats/géographie. Secteurs salariaux : ensemble, FAP×NAF, maille/repli par ligne, parts sous seuil non exhaustives.
- Certification : toutes mesures nationales disponibles par population/horizon/promotion, blocsRNCP textes, pas archives ni équivalences ; Formacode→certifications→sessions, aucune source de formation hors API.
- Authentification/quotas/attribution : jeton confidentiel non exposé au client public, 40 requêtes/s/jeton, reprise bornée, logo RCO et cadre fournisseur.

## 4. Jeux de tests obligatoires


- Par mocks JSON **réels**, pas des données chiffrées inventées. Si la fixture manque, spécifier l'état selon le contrat et collecter une preuve réelle ; aucun chiffre ou résultat métier inventé pour remplir la lacune. Les simulations de transport/erreur sont explicitement des tests techniques.
- Tests de validation R23 : `125416,103659` avec `toutes` (1 ROME F1610) et `au_moins_une` (3 ROME) selon fixtures ; vérifier que les champs de match sont optionnels.
- Tests R24 : `domaine=F16`, `contexte=300782` (10 ROME), `sans_contexte=300782` (3 ROME), sans `fields`, sur fixtures conservées.
- Tests R16 : `F1610`, Montpellier ; 14 mesures vérifiées, gestion `maille_reelle` par mesure.
- Tests R17 : résultat métier-territoire attendu non restitué sur les casR17 avec `rome=F1610`, suivi fournisseur et test de clôture, pas de conclusion « aucun employeur ».
- Tests R18/19 : rattachement vérifié selon critèreQ11, temporalités, modalités etOnisep séparés ; résultat vide décrit comme aucun résultat de cet appel, pas « places disponibles ».
- État 0 résultat, paginations, HTTP 422/401/500, timeout, valeurs `null`, zéro, `secret_stat`, champ manquant, `[]`, repli territorial, changement de mode, ajout/suppression de pistes, fermeture/retour, accessibilité.


- Tester chacun des T-E01–T-E31 de03/04 et V01–V14 de06. Mobilités/prospective détaillée/salaires sectoriels/transitions/Formacodes ont leurs tests dédiés, pas un simple lien en attente.
- Séparer résultats statiques, tests sur JSON et HTTP réel avec URL/statut/corps/date expurgés du jeton. Les nombres de fixtures figées ne sont pas des volumes attendus à toute date.

## 5. Critères de livraison et suivi

1. Tracer chaqueID etlot : conception, adaptateur, testsJSON, HTTP, recette, anomalie, prochaine action/preuve ; tous les 31 restent inclus.
2. Réutiliser cache/catalogues/fiches, annuler requêtes périmées, conserver sections utiles sur erreur partielle ; ne pas remplacer l'API par des résultats fictifs en production.
3. Exécuter les tests appropriés, documenter commandes/résultats/limites ; pas de succès réseau déduit de tests statiques. Si accès API absent, marquer intégration HTTP NON TESTÉE et poursuivre les tâches indépendantes.
4. Mettre à jour le suivi dans 09 et les points de validation06, avec liste des fichiers et preuves. Ne pas créer de08_RAPPORT_IMPLEMENTATION parallèle ou remplacer l'audit08 ; respecter le mode de compte rendu demandé au moment de l'implémentation.
5. Préserver contrat, JSON sources et UML de référence ; une nouvelle preuve réseau est ajoutée uniquement selon l'instruction et la convention validées de collecte, jamais substituée à une fixture historique.

Les 31 fonctionnalités sont des engagements de périmètre. Un défaut fournisseur reste visible et ouvert jusqu'à résolution ; une impossibilité contractuelle précise est signalée pour décision explicite, sans suppression automatique ni autre source de données.

## Règle de présentation citoyenne — décision produit du 2 novembre 2026

Les écrans affichent les noms fournis par l’API, sans codes, noms de référentiels, version du projet ni notes de conception. Les paramètres techniques restent dans le code et la documentation. Expliquer les chiffres en langage courant : sens, personnes concernées, lieu, période, unité et limites. Une information manquante n’est pas zéro ; un projet de recrutement n’est pas une offre ; une projection n’est pas une garantie. Conserver les sources. Ne pas ajouter de score, de taux ou de calcul pour vulgariser. Cette règle s’applique aux31 fonctionnalités et à leurs critères de recette. La ligne éditoriale est [documentée ici](12_maquette_html/documentation/REDACTION_CITOYENNE.md).

Pour poursuivre, lire aussi les sources du HTML et EVOLUTION_STRUCTURE_UX.md. Conserver la séparation des vues et des adaptateurs ; remplacer la source locale par les réponses HTTP réelles lors de l’intégration autorisée. Ne pas présenter le catalogue local de domaines comme un JSON /domaines capturé. Ne pas déclarer les autres parcours reliés avant leur intégration réelle.
