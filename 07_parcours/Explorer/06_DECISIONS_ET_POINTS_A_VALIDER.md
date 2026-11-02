# Explorer V2 — décisions, points de validation et suivi opérationnel L0

## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.


**Mise à jour du 2 novembre 2026 — dossier rangé.** Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les 31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.

Alignement L0 — 1er novembre 2026. Dossier documentaire de la cible complète, sans développement. D01 confirmée par instruction produit : **E01–E31 inclus, périmètre définitif.** Les paramètres/champs sont dans 02/03, les tests T-E01–T-E31 dans 03/04, les lots dans 09. Les références Q01–Q14 sont conservées et triées ci-dessous ; aucune demande n'est envoyée au RCO.

## A. Décisions actées

- Une recherche, trois modes **Métier / Diplôme ou titre / Domaine professionnel** dans la maquette citoyenne ; domaine de métiers et secteur d’activité économique restent distincts. Les identifiants et sigles techniques ne sont pas des intitulés publics.
- Trois fiches, questions utilisateur avant chiffres ; préférer « Ce qu'il faut savoir avant de choisir » à toute promesse de compatibilité individuelle.
- *Mes pistes* sans compte (2–3 métiers), comparaison de deux métiers, suggestions contextuelles après recherche.
- Deux intentions sur la fiche certification, sans dupliquer le modèle de données.
- Deux lectures territoriales séparées, recrutements et salaires, sans score d'attractivité.


- D01 : la cible entière est validée, incluant mobilités, prospective détaillée2030, salaires sectoriels, secteurs d'emploi, sessions, compétences/contextes, transitions et Formacodes. Les lots ne réduisent pas le produit.
- Les tests manquants et anomalies sont des travaux de réalisation/recette, pas des arbitrages de suppression. Pas de statistique, source, score, correspondance ou accès SQL inventé.

## B. Arbitrages d'exécution D02–D10

Les recommandations d'inclusion sont closes ; les choix ci-dessous concernent les modalités. Trois pistes restent une proposition de plafond, pas une nouvelle décision de stockage.

| ID | Décision d'exécution attendue | Proposition compatible avec la cible complète | Validation attendue | IDs / lots concernés |
|---|---|---|---|---|
| D02 | Libellé public et interaction Domaine | Conserver la barre unique ; navigation d'arbre et filtre local des libellés reçus pour ce mode ; présenter le domaine professionnel sans sigle technique et le distinguer du secteur d’activité des entreprises. Choisir wording et présentation, pas un hypothétique `q` serveur | Produit + métier + UX | E03/E04, L2 |
| D03 | Présentation de l'intention Certification et des titres introuvables | Maintenir les deux intentions et expliquer les certifications actives RNCP/RS ; choisir le message pour un diplôme ancien absent, sans promettre archives/équivalences. Afficher le type réel des résultats | Produit + métier + UX | E02/E17/E19, L2 |
| D04 | Organisation des compétences et contextes | Inclusion acquise. Choisir ordre des catégories, présentation macro-compétences/cœur de métier, périmètre Domaine et formulation avec/sans contexte ; expliquer spécialités et absence de garantie terrain | Produit + métier + UX | E06/E13–E16, L2/L3 |
| D05 | Organisation du comparateur complet | Couvrir descriptions, contextes, compétences, certifications et statistiques ; choisir onglets/sections et présentation des familles communes/différentes. Tester `depuis` et le formuler comme relation entre métiers, jamais comme maîtrise personnelle | Produit + métier/Data + UX/technique | E28 et dépendances, L9 |
| D06 | Présentation territoriale, géographies différentes et salaire ouvert | Choisir les périmètres depuis les parents du lieu sélectionné ; afficher rang par famille, maille réelle et tranche annuelle ouverte ; séparer médiane mensuelle et distribution annuelle, sans score de territoire | Métier/Data + produit/UX | E08–E12/E25, L4/L7 |
| D07 | Hiérarchie des résultats d'insertion | Toutes les populations documentées restent accessibles ; choisir synthèse puis détails par population/horizon avec période/secret, sans fusionner les taux. Questions fournisseur en Q06/Q07/Q09, non par recalcul consommateur | Métier/Data + produit/UX | E17/E08/E12/E31, L2/L4 |
| D08 | Plafond et durée de conservation de Mes pistes | Trois pistes et deux métiers comparés proposés ; choisir mémoire ou stockage de session et comportement au rechargement/fermeture. Fonction sans compte conservée ; pas de sauvegarde distante inventée | Produit + technique ; interlocuteur confidentialité selon politique du produit | E27/E28, L9 |
| D09 | Critère de recette des sessions et présentation Onisep | E21/E22 inclus. Valider la preuve combinant requêtes tracées, tests contrastés et garantie RCO du filtre Certif Info malgré son absence par ligne ; choisir présentation séparée d'Onisep et défaut de vue. Une liste dans l'appel courant ne nécessite pas de fiche session stable | Métier/Data + technique + produit/UX, avec réponse RCO Q11 | E21/E22, L8 |
| D10 | Application d'accueil, accès API et publication | Identifier dépôt/hébergement/conventions et responsable du jeton ; passage serveur proposé pour un jeton confidentiel partagé, quota commun et cache. Choisir rendu/SEO et publication conformes au contrat, attribution RCO comprise | Responsable technique + produit ; interlocuteur habilité pour le cadre fournisseur | L1/L10, transversal |

## C. État des preuves et anomalies techniques

1. R16 : V ciblé F1610/34172, 14 mesures, mailles par mesure ; pas validation générale des lieux.
2. R23/R24 : V sur jeux OGR fournis ; la recherche libre et les combinaisons supplémentaires restent à tester.
3. R17 : anomalie reproduite sur filtre ROME ; E26 maintenu. Réaliser emploi_secteurs familial et contexte économique territorial séparément, puis résoudre le résultat métier-territoire attendu sans jointure locale inventée.
4. R18/R19 : réponses réelles cohérentes ; rattachement individuel non vérifiable par identifiant dans chaque ligne. Tests contrastés + garantie RCO du filtre courant nécessaires, sans exiger un champ non contractuel.
5. R24 projection :422du corps citant contexte_travail_code singulier ; URL effective absente ; pas défaut général prouvé de fields. Utiliser réponses complètes documentées, retester le pluriel.
6. R01–R15/R20–R22 : correspondances historiques statiques, non HTTP retestées par leur seule concordance.
7. MC :100 compétences sur 144, page 1/2 ; collecterpage2 et autre métier complet avant comparaison exhaustive. /domaines : structureC démontrée documentairement, réponse réelle encore à collecter.
8. Salaires : tranche ouverte null documentée, pas exemple réel ; rangAPI conservé, pas null traité en zéro. Statistiques multiFAP et périodes/populations séparées.

## D. Plan de validation transversal, IDs conservés

| ID | Contrôle à mener | Preuve attendue | Responsable proposé |
|---|---|---|---|
| V01 | Recherche depuis les trois modes ; Domaine via arbre/filtre local, sans q serveur | Captures q pour ressources compatibles, 0/multiples/pages ; arbre réel | Data/UX/Dev |
| V02 | Domaine→métiers et certification↔métier/blocs/Formacodes | Requêtes exactes, codes concordants, pages nécessaires | Data/Dev |
| V03 | Comparateur deux métiers, familles communes/différentes et géographies distinctes | Jeux complets, observations familiales identifiées, pas de delta/score inventé | Métier/Data/QA |
| V04 | R23/R24 autres codes et combinaisons, projection plurielle | Captures request/status/body, catégories exactes, erreurs qualifiées | Dev/Data |
| V05 | R16 autre métier/territoire, DOM et mesure sans valeur | Maille/grain/repli et états par mesure | Data/QA |
| V06 | R18/R19 et3 modesOnisep, certifications contrastées | Requêtes tracées, dates/pagination et garantie RCO Q11 | Dev/Data/RCO pour garantie |
| V07 | R17 filtreROME | Reproduction et correction/explication validée puis test de clôture, sans retraitE26 | Dev/Data/RCO |
| V08 | Accessibilité RGAA/DSFR | Parcours clavier, focus, lecteur d'écran, tableaux et graphiques lisibles | UX/QA |
| V09 | Mobilités deux sens/âges/mailles | Variantes MOB et nouvelles captures ciblées, parts non normalisées | Data/QA |
| V10 | Prospective2030 complète et deux entrées | Champs/tris, agrégats, référenceFrance, chaîne ROME, limites géographiques | Data/QA |
| V11 | Salaires sectoriels et contexteéconomique | Famille/NAF, ensemble, repli, seuils/tranches, aucune attribution locale inventée | Data/QA |
| V12 | Transitions/Formacodes et filtres accès/blocs | Pages complètes, codes réels, chaînes et filtres documentés | Dev/Data |
| V13 | Compétences complètes et depuis | Page2MC, seconde fiche, cœur/catégories, comparaison directionnelle fournie | Dev/Data |
| V14 | Couverture documentaire et recette31 IDs | CSV31 lignes, US31, diagrammes/lots alignés, aucun ID écarté | Produit/Tech/QA |

## E. Triage Q01–Q14 : documentation, GET autonomes et fournisseur

Les réponses déjà démontrées ne sont pas redemandées. Le manque d'une fixture appelle d'abord un GET de validation, non une redéfinition du contrat. Les traces sont expurgées des jetons. **Dossiers réellement ouverts à RCO : Q01, Q06, Q07, Q11, Q14** ; Q05 seulement si l'erreur est reproduite avec une requête conforme. Les autres Q sont des validations GET autonomes, avec escalade uniquement sur écart démontré. Aucun de ces tests HTTP n'est réalisé pendant L0.

| Q | IDs | Déjà démontré (contrat / JSON / campagne) | Tests réalisables avec les GET | Réelle demande RCO restante | Anomalie / limite | Suivi |
|---|---|---|---|---|---|---|
| Q01 | Transversal, E05/E07/E29/E31 | C §2 : authentification, 40req/s/jeton, erreurs, logo ; O expose21 GET ;10schémas200 absents et required divergents constatés | Contrôler accès/base URL une fois environnement fourni ; tester formes de réponses contre C/O | URL/version de l'environnement et clarification des divergences schémas/obligations constatées ; ne pas redemander les règles déjà écrites | Écarts documentaires avérés, comportement réseau à établir | OUVERT FOURNISSEUR — contrat/outillage |
| Q02 | E01/E02/E09/E13/E15 | C/O : q2–100, préfixes, accents/casse/pluriels, pertinence ; /domaines n'a pas q | Tester préfixes/ambiguïtés/0résultat/pages, annulation des résultats périmés ; T-E01/E02/E09/E13/E15 | Aucune demande à ce stade ; remonter seulement un écart reproductible aux règles documentées | Aucune anomalie générale prouvée | TEST GET AUTONOME |
| Q03 | E03/E04/E09 | C décrit arbre/grands domaines/sous-domaines/nb_metiers ; O paramètres grand_domaine et domaine ; parents territoriaux C/T/R16 | Capturer /domaines et grand_domaine=F puis /metiers?domaine=F16 ; tester code/parents et pages des listes | Aucune question de structure à reposer ; JSON manquant à collecter par GET existant | Aucun défaut fournisseur démontré | DOCUMENTÉ + TEST GET |
| Q04 | E06/E13/E14/E28 | C/O : catégories, cœur, depuis, macro-compétences ; R23 V ciblé ; MC100/144 page 1/2 | Collecter page 2, seconde fiche complète, catégories/cœur ; depuis F1613←F1610 et inverse, classement autre jeu OGR | Aucune sémantique déjà documentée à redemander ; enveloppe schéma manquante suivie Q01 | Pas d'anomalie de comparaison démontrée | DOCUMENTÉ + TEST GET |
| Q05 | E04/E15/E16 | Catégorie contexte_travail et inclusion/exclusion C/O ; R24 V sur 300782/F16 sans fields ;422 citait singulier, provenance URL inconnue | Tester catalogue contexte et filtres multiples/combinés ; tracer requête fields plurielle exacte | Seulement si422reproduit avec URL conforme : transmettre requête/réponse. Sinon retrouver la trace de saisie initiale, sans attribuer un défaut à RCO | Incident de projection non attribué, pas anomalie fournisseur établie | TEST GET ; DEMANDE CONDITIONNELLE |
| Q06 | E08/E09/E12/E28/E31 | Repli par mesure, grains, nb_rome_famille et états définis C ; R16 V au cas fourni | Autres ROME/lieux, DOM/valeurs vides, mailles et familles, secret ; T-E08/E12/E28/E31 | Clore le point ouvert C §9 sur la validation de la règle de secret par écart total–sous-effectif ; aucune redéfinition consommateur | Point contractuel signalé ouvert, pas erreur de calcul à présumer | OUVERT FOURNISSEUR — secret |
| Q07 | E08/E10 | BMO2026/FAP228, projets et tris documentés ; R16 B1X34 nb_saisonniers0 et tx1.7 observés | Tracer classements région/département/CLPE et tris ; conserver nombres/taux reçus | Expliquer arrondis/dénominateurs de ce couple0/1.7 et la précision des petits volumes signalée ouverte C §9 | Incohérence apparente à expliquer, cause non démontrée | OUVERT FOURNISSEUR — valeurs |
| Q08 | E11/E25 | C décrit population BTS2023, 30 observations, annuel/mensuel, tranche ouverte et rangnull, repli sectoriel ; SS/SAL structures J | Collecter cas tranche ouverte et repli partiel ; tester France/région/familles/seuils dans GET salaires et salaires/secteurs | Aucune demande de définition déjà dans C ; demander un exemple seulement si les tests ne permettent pas de couvrir ce cas, sans bloquer conception | Aucune anomalie salariale démontrée | DOCUMENTÉ + TEST GET |
| Q09 | E02/E17/E19/E20 | C/O : actives seules, RNCP/RS, voies, promotions, horizons nationaux ; CD/CL observés ; pas d'archive route | Tester RS, multiROME, 404inactif, filtres accès/ROME, cohortes/secret avec MES | Aucune question sur cycle actif/horizons déjà décrits ; remonter seulement incohérence d'une réponse tracée | Pas d'anomalie générale de certification démontrée | DOCUMENTÉ + TEST GET |
| Q10 | E18/E20/E30 | C/O : blocsRNCP, textes, q, fiche/certifinfo, validation_partielle ; Formacode→certifications documenté | Tracer filtres blocsRNCP36101, texte, q, Formacode renvoyé→certification→fiche ; pagination | Aucune nouvelle source ou équivalence OGR à demander ; seulement un écart reproductible aux relations prévues | Concordances statiques ≠ requêtes filtrées testées | DOCUMENTÉ + TEST GET |
| Q11 | E21/E22 | O : zonages, paramètres, 13 champs, sans IDstable/Certif Info par ligne ; présentiel0/mixte1/distanciel2 ; Onisep conventionnel ; R18/R19 J partiels | Contraster certifications/territoires, les 2 routes, temps, pages et3 modesOnisep ; capturer URL/statut/corps, pas de faux identifiant | Garantie opératoire et moyen de vérification du rattachement de chaque groupe via le filtre existant ; règle de regroupement nb_sessions et traçabilité dans les champs actuels. Ne pas exiger de nouveau champ comme préalable | Limite de traçabilité, pas échec prouvé du filtre | OUVERT FOURNISSEUR — garantie/traçabilité |
| Q12 | E23 | C/O : deux sens, âge selon début/fin période, top 15, parts sous secret omises, FAP225, mailles ; MOB J | Tester région/France, tousâges, repli, origine/destination et hors emploi ; encoder60+ en60%2B | Aucune redéfinition des sens/âges/parts ; demander uniquement si résultats contredisent C | Pas d'anomalie générale démontrée | DOCUMENTÉ + TEST GET |
| Q13 | E24 | C/O : champs, tris, FAP87, métropole/France, agrégats Corse et différences région/national ; PRO J | Tester2 routes, chaîne rome_codes[], tris, négatifs/null, Corse/DOM ; pas de recalcul | Aucune demande sur couverture/tris déjà décrits ; remonter un écart capturé ou obtenir clarification ciblée si une valeur reste inexpliquée | Aucune anomalie générale démontrée | DOCUMENTÉ + TEST GET |
| Q14 | E26 | C attend résultat métier-territoire ; R17=35sansROME et0avecF1610 à2mailles ; R16 emploi_secteurs13 lignes régionales | Rejouer avec/sans ROME, autrescodes etmailles ; test de clôture après réponse/correction ; maintenir2 lectures accessibles distinctes | Cause et correction/explication contractuelle du filtre ROME, metier_maille et nb_actifs_metier/tx_actifs_metier attendus | ANOMALIE FOURNISSEUR REPRODUITE sur casR17, cause inconnue | OUVERT FOURNISSEUR — correction R17 |

## F. Conditions d'entrée dans le développement

- Identifier l'application/dépôt d'accueil et ses conventions ; ce dossier ne contient pas d'application à démarrer spontanément.
- Désigner responsable technique, accèsURL/environnement/jeton et mode serveur pour un jeton confidentiel partagé ; quota global40 requêtes/s/jeton et attributionRCO.
- Planifier les choix d'exécution D02–D10 au plus près des tâches concernées ; ils n'annulent pas D01. Ne pas attendre une réponse à toutes les questions pour préparer les chantiers indépendants.
- Pour chaque intégration, établir ses captures de recette et tests d'erreur ; les schémas manquants se traitent d'après C/O et preuves, sans transformer l'enrichi en contrat officiel.
- Engager tôt les cinq dossiers fournisseur ; une erreur deR17 peut bloquer sa recette précise sans bloquer toutes les autres fonctions. La cible complète n'est pas déclarée finie par masquage d'une fonction.
- Autorisation explicite de passer au développement attendue après cet alignement. Aucun code applicatif ou projet neuf créé dans L0.

## G. Traçabilité et bilan L0

Preuves conservées : `03_catalogue/routes_openapi.csv`, `champs_observes_tous_endpoints.csv`, `04_relations/PREUVES_ET_LIMITES.md`, `STATUTS_EN_COURS.md`, `matrice_statuts_apres_tests.csv`, rapports `06_controles/VALIDATION_R*.md` et JSON associés. Les chemins complets de preuve par ID restent dans 03. Niveaux distincts : D contrat, J JSON, V campagne ciblée, T restant à faire ; aucun test statique ne vaut HTTP.

Les sept livrables01–07 sont mis à jour en place.31 IDs/31 lignes/31 stories sont consolidés. Corrections principales : cible complète et lots communs ; arbre Domaine et filtrelocal sans q ; fiches Certification et comparateur enrichis ; pagination144 compétences non présumée complète ;29 mesures exhaustives et familles/mailles/unités ; sessions etR17 suivis sans retrait ; demandesRCO triées ; prompt futur aligné sans nouvel audit ou création spontanée d'application.

### Contrôles exécutés pendant L0

Commande utilisée à la racine du dossier (Python3.13 installé) :

```powershell
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONDONTWRITEBYTECODE = '1'
& "$env:LOCALAPPDATA/Programs/Python/Python313/python.exe" -B scripts/verifier_dossier.py
```

Sortie globale : **6 contrôles réussis, code de sortie 0**. Ce sont des contrôles hors ligne, sans appel HTTP.

| Contrôle | Résultat |
|---|---|
| verifier_contrat.py | 21 routes dans chaque export comparé |
| verifier_echantillons.py | 57 JSON analysés ;45associés à une route sans schéma200 officiel |
| verifier_schemas_complementaires.py | 57 JSON, aucun champ non décrit par les modèles enrichis non officiels ; pas validation complète de types |
| verifier_relations_api.py | 24 relations, 18correspondances statiques, 6sans correspondance testable ; pas18testsHTTP |
| verifier_uml_global.py | Carte21 GET, 24 relations, 3UML de référence ; contrôle textuel, pas rendu graphique |
| verifier_preuves_directes.py | Fixtures R16/R23/R24 cohérentes ; R17 toujours ouvert ; limites de rattachement R18/R19 inchangées |

Les cinq rapports CSV régénérés par ces scripts ont les mêmes empreintes qu'avant exécution. Leurs réussites n'annulent pas les anomalies ou tests restant ouverts.

### Cohérence et intégrité documentaire

- 31 IDs E01–E31 uniques dans 03, 31 colonnes dont toutes les colonnes de pilotage d'origine ; UTF-8 avec BOM et séparateur point-virgule conservés.
- 31 stories et testsT-E01–T-E31, 14 questions Q et validations V01–V14 ; diagrammes et lots couvrent les 31 IDs.
- Les appels détaillés de03 couvrent les 21 GET et uniquement leurs noms de paramètres autorisés dans l'export officiel. Les chemins de preuves référencés existent. Les valeurs/combinaisons restent à tester en HTTP.
- 29 mesures du catalogue et leurs241 occurrences de champs[] présentes dans 02, avec source, grain, millésime, mailles et restitution ; aucune suppression liée à une preuve manquante.
- Empreintes SHA-256 avant/après sur 175 fichiers : seuls les 10 documents Explorer existants sont modifiés (01–07 actualisés, 08–10 synchronisés). Les165 autresfichiers restent identiques, notamment contrat/OpenAPI, JSON sources, JSON de campagne, catalogues, matrices, UML et scripts ; aucun fichier ajouté ou supprimé.
- Les sources de données de référence ne sont ni corrigées ni remplacées pour faire passer un contrôle.

### Reste à exécuter et entrée dans L1

Les testsHTTP T-E01–T-E31 et validations V01–V14 sont préparés, non exécutés ici. Collectes prioritaires : /domaines, page 2MC et second métier, comparaison depuis, filtres et chaînages Certification, autres lieux R16 ; mobilités région/âges, prospective et tris, secteurs salariaux/tranche ouverte ; sessions contrastées/Onisep et test de clôture R17. L'accessibilité sera testée sur l'application effectivement réalisée.

Cinq dossiers RCO réellement ouverts : Q01écarts contractuels/accès, Q06règle du secret à valider, Q07arrondis BMO, Q11traçabilité/regroupement des sessions, Q14anomalieR17. Demandes préparées, non envoyées. Les autres Q n'exigent pas de redemander les définitions déjà connues ; Q05 n'est escaladé que sur reproduction conforme.

**L0 documentaire est terminé.** Entrée en développement : instruction explicite de démarrage, application/dépôt d'accueil identifié, responsable technique et accès API sécurisés, planning des choix d'exécution par lot et responsables du suivi RCO désignés. Ces conditions ne rouvrent pas le périmètre. Aucun projet applicatif n'a été créé ou lancé.

## Décisions de présentation actées le 2 novembre 2026

- **D11 — Noms publics : acté.** Utiliser les libellés effectivement fournis ; conserver les codes et les référentiels dans les traitements internes. Ne pas inventer un nom manquant.
- **D12 — Lecture citoyenne : acté.** Retirer des écrans les mentions de version, de maquette, de tests, de conception et d’intégration. Expliquer les chiffres à proximité de leur valeur, avec leur portée et leurs limites. Les sources restent consultables.

D11/D12 ne rouvrent ni le périmètre D01 ni les questions fournisseur. D02–D10 restent ouverts pour leurs modalités non résolues ; D02 ne peut plus proposer des codes ou sigles comme libellés publics. Les questions RCO ouvertes restent Q01, Q06, Q07, Q11 et Q14 ; Q05 reste conditionnelle. Les 108 contrôles de la maquette sur ordinateur et mobile sont des tests locaux d’interface, sans nouvelle validation HTTP ni certification RGAA. La production connectée reste à préparer.
