# Intégration DSFR Chart dans Explorer

2 novembre 2026. Intégration réalisée dans le code existant, sans nouvelle application et sans retrait d’une des 31 fonctionnalités E01–E31.

La [page HTML actuelle](12_maquette_html/index.html) embarque les composants officiels. Elle reste ouvrable par double-clic. Les graphiques fonctionnent à partir des réponses JSON réellement présentes dans le dossier. **Le fournisseur de données existant reste local : cette livraison ne constitue pas un branchement HTTP en production.** Aucun test statique ou navigateur n’est présenté comme une nouvelle validation réseau de l’API.

## Références prises en compte

Les huit fichiers du référentiel commun ont été lus : analyse de DSFR Chart, catalogue des indicateurs, matrice V01–V25, conception UX, composants partagés, règles statistiques/RGAA, intégration dans les parcours et prompt d’intégration. L’instruction actuelle autorise la réalisation directement ; la consigne antérieure d’attendre une validation contenue dans le prompt ne l’interrompt pas.

Les documents Explorer 01–10, le contrat du 19 octobre, les OpenAPI, les JSON observés, la matrice API, les UML et les preuves R16–R24 restent les références fonctionnelles et techniques. Le dossier demandé `API_DGEFP_RCO_REFERENCE_V3_PROPRE` est disponible sous forme d’archive dans Downloads : les **146 fichiers techniques comparés sont identiques** à ceux de ce workspace. Voir [la comparaison conservée](99_archives/2026-11-02_dsfr_chart/COMPARAISON_REFERENCE_PROPRE.json).

Les 31 lignes de conception sont conservées, sans changement de périmètre ni conversion de leurs dépendances en report fonctionnel. Les interfaces de recherche, compétences/contextes, domaines, certifications, sessions, comparaison et Mes pistes sont préservées.

## Installation et architecture effectivement utilisées

| Élément | Réalisation |
|---|---|
| Bibliothèque | `@gouvfr/dsfr-chart` **2.1.1**, paquet officiel installé par npm |
| Socle | `@gouvfr/dsfr` **1.15.4**, compatible avec la plage DSFR déclarée par cette version de Chart |
| Construction | Node **24.22.2**, installation locale au dossier partagé ; aucun changement du PATH système |
| Dépendances | Archives officielles vérifiées SHA-512, `package-lock.json`, installation locale hors ligne ; aucun script de paquet exécuté |
| Code partagé | [commun_datavisualisation](../commun_datavisualisation/README.md), réutilisable par les futurs parcours |
| Distribution HTML | Distributions officielles précompilées, ressources CSS embarquées, assemblage Python existant conservé |
| Composants utilisés | `data-box`, `bar-chart`, `line-chart`, `map-chart`, `table-chart` |
| Interface générale | Styles DSFR officiels ; champs `fr-input`, sélecteurs `fr-select`, boutons `fr-btn` ; navigation existante conservée |
| Chargement | Graphiques créés seulement à l’ouverture de leur section ; aucun appel distant requis pour les consulter |

Sources techniques primaires : [dépôt officiel DSFR Chart](https://github.com/GouvernementFR/dsfr-chart), [paquet officiel 2.1.1](https://www.npmjs.com/package/@gouvfr/dsfr-chart/v/2.1.1). La documentation livrée dans le paquet installé gouverne les attributs réellement utilisés. La provenance exacte et les licences sont conservées dans `../commun_datavisualisation/vendor/`.

Le composant commun assemble une DataBox, son graphique et son TableChart liés par `databox-id` / `databox-type` / `databox-source`. Le tableau autonome reste consultable sans monter le graphique. Les barres CSS dessinées auparavant dans Explorer ont été remplacées par BarChart. Aucun moteur de dessin personnalisé n’a été ajouté.

La distribution DSFR destinée aux anciens navigateurs altérait les collections utilisées par le code existant. L’intégration utilise la distribution moderne officielle, isolée dans une fonction pour protéger les variables globales. La recette confirme la conservation de la recherche et des fiches. Les icônes utiles à Chart sont extraites des règles officielles DSFR et embarquées, afin d’éviter des boutons de bascule sans pictogramme.

## Visualisations opérationnelles sur les JSON disponibles

Les chemins ci-dessous sont relatifs à la réponse de l’endpoint cité. Chaque famille reste une série indépendante. Les noms des métiers et des lieux sont affichés, leurs identifiants restent internes.

| Restitution | Source et champs exploités | Contexte visible et précautions |
|---|---|---|
| Salaire mensuel médian, chiffre clé DataBox | `/indicateurs?rome=F1610&zonage=commune&territoire=34172` ; `items[mesure=salaires].valeurs[].salaire_net_mensuel_median` | Hérault, 2023, salariés à temps complet ; famille de 8 métiers, pas un salaire garanti du seul métier |
| Dispersion annuelle, trois barres + tableau explicatif | Même mesure ; `salaire_net_annuel_q1`, `salaire_net_annuel_median`, `salaire_net_annuel_q3` | 17 400 / 20 300 / 22 000 € nets annuels ; Q1/Q3 ne sont pas des minima/maxima ; aucune division par douze |
| Salaires sectoriels | `/salaires/secteurs?rome=F1610` ; `items[].fap_225_code`, `secteur_naf38_libelle`, `salaire_net_mensuel_median` | France, 2023 ; familles séparées ; les parts et repères annuels restent dans les tableaux existants |
| Salaires régionaux et départementaux | `/salaires?rome=F1610&zonage=region` ou `departement` ; `items[].territoire_code`, `territoire_libelle`, `salaire_net_mensuel_median`, `france[]` | FAP225, 2023 ; barres, cartes officielles et tableaux ; repère national uniquement s’il est publié |
| Projets locaux, difficultés et saisonnalité | Mesure `projets_recrutement` de `/indicateurs` ; nombres et taux publiés, sans les recalculer | FAP228, bassin de Montpellier, 2026 ; catégories susceptibles de se recouper, pas de somme des barres ; intentions ≠ embauches |
| Projets régionaux et départementaux | `/recrutements?rome=F1610&zonage=region&tri=projets`, variante `departement` ; `items[].nb_projets_recrutement`, `france[]` | Barres/cartes par famille, 2026 ; comparaison explicite de deux régions, distincte de la lecture salariale |
| Offres mensuelles et postes annoncés | Mesure `offres_emploi_mensuelles` ; `periode_code`, `nb_offres_emploi_mois`, `nb_postes_offres_emploi_mois` | Deux courbes indépendantes sur les mois réellement publiés ; sinon barres, sans compléter les mois absents |
| Mobilités observées | `/mobilites?rome=F1610&sens=origines` ou `destinations`, `age` ; `origine_libelle` ou `destination_libelle`, `tx_personnes` | France, 2022–2023 ; sens, âge et famille sélectionnables ; liste publiée partielle, sans renormalisation à 100 % |
| Prospective détaillée | Mesure `metiers_2030` ; `nb_creations_nettes_emplois_2030`, `nb_departs_fin_carriere_2030`, `nb_postes_a_pourvoir_2030`, `nb_jeunes_debutants_2030`, `nb_desequilibre_potentiel_2030` | Occitanie, FAP87, 2019–2030 ; négatifs conservés ; pas d’empilement, de cascade ni de série annuelle inventée ; taux et base 2019 conservés dans les tableaux |
| Prospective par région et par famille | `/prospective/regions?rome=F1610&tri=postes_a_pourvoir` ; `/prospective/metiers?tri=postes_a_pourvoir` ; `items[].nb_postes_a_pourvoir_2030` | Barres et cartes régionales, classement par familles avec graphiques de quinze groupes par page et tableau complet conservé ; les valeurs nationales et régionales ne sont pas additionnées |
| Secteurs employeurs | Mesure `emploi_secteurs` ; `fap_225_code`, `secteur_naf38_libelle`, `tx_actifs_secteur`, `nb_actifs_emploi` | Occitanie, 2021 ; tous les secteurs observés du groupe, sans fabriquer un complément ; contexte économique local conservé à part |
| Insertion après certification | `/certifications/112561` ; `tx_ij_apprentissage_emploi_12m`, `tx_ij_apprentissage_poursuite_etudes`, `tx_de_acces_emploi_6m`, `tx_de_abandons` et leurs effectifs | DataBox de chiffres clés, pas un graphique décoratif par taux ; populations et horizons distincts ; 314 sortants apprentis ≠ 452 élèves en année terminale ≠ 105 demandeurs d’emploi sortants |
| Résultats absents après certification | Champs scolaire, InserSup, examens, salaire médian InserSup | États non disponibles explicitement conservés ; aucune barre à zéro créée à partir de `null` ; fonctionnalité maintenue |
| Comparateur de deux métiers | Choix réels dans les deux sélecteurs ; tableaux existants + mêmes composants pour la réponse salariale disponible | Données de F1610 affichées seulement si F1610 fait partie de la sélection ; aucun transfert au second métier, aucune moyenne ou note globale |

Les tableaux de tensions restent qualitatifs : les catégories reçues ne deviennent pas des nombres arbitraires. Les compétences et contextes restent des listes et filtres, sans score de maîtrise personnelle. Les sessions restent un tableau de lieux et dates ; aucun regroupement temporel chiffré ne remplace leurs données.

## Couverture de la matrice commune V01–V25

« Local » signifie fonctionnel avec les JSON observés ; une collecte HTTP supplémentaire reste nécessaire pour généraliser les cas.

| ID | Couverture dans la livraison | Dépendance restante |
|---|---|---|
| V01 | Local : salaires par région, barres/carte/tableau | Autres métiers, valeurs sous secret et replis réels |
| V02 | Local : repères annuels, sans faux minimum/maximum | Tranches ouvertes à couvrir avec une réponse supplémentaire |
| V03 | Local : salaires sectoriels par famille | Variantes régionales et repli partiel |
| V04 | Local : projets par région/département | Autres périmètres et tris HTTP |
| V05 | Local : taux publié de difficultés et effectifs distincts | Q07 sur les arrondis/dénominateurs ; pas de correction côté client |
| V06 | Local : sélecteurs de deux régions et réinitialisation ; lectures salaire/recrutement séparées | Généralisation des données à d’autres métiers |
| V07 | Local : origines, âge, famille | Tests régionaux et 60+ encodé `60%2B` |
| V08 | Local : destinations, âge, famille | Même campagne de variations ; pas de lien FAP→fiche ROME inféré |
| V09 | Local : cinq composantes 2030 et tableau des taux | Autres lieux, négatifs et null supplémentaires |
| V10 | Local : classement des familles prospectives | Navigation vers une fiche seulement via les `rome_codes[]` documentés, jamais via une équivalence inventée |
| V11 | Local : secteurs, parts et effectifs | Ne pas confondre avec les établissements/salariés de tout un secteur |
| V12 | Local pour la certification détaillée observée | Autres certifications/cohortes pour une comparaison effective entre titres |
| V13 | Local : populations et délais séparés | Pas de classement transversal de populations incompatibles |
| V14 | Composant prêt, état absent conservé pour le titre courant | Valeur InserSup non nulle et promotion correspondante à collecter |
| V15 | Voies d’accès conservées en liste/tableau | Pas de graphique pertinent ; éligibilité individuelle non déduite |
| V16 | Blocs et évaluations conservés en accordéons | Tests filtrés/pagination ; pas de correspondance de maîtrise inventée |
| V17 | Domaine et choix de métiers conservés | Réponse `/domaines` à collecter ; les domaines locaux proviennent encore des métiers observés |
| V18 | Alternatives et compétences conservées | Comparaison `depuis`, page 2 et seconde fiche complète à collecter |
| V19 | Filtres de contextes souhaités/évités conservés | Variantes combinées et incident Q05 conditionnel |
| V20 | Deux métiers sélectionnables ; chiffres disponibles seulement pour leur vraie source | Second jeu statistique nécessaire avant un graphique numérique à deux métiers |
| V21 | Local : carte/barres prospectives par région | Cas Corse/DOM et couverture effective selon le contrat |
| V22 | Local : vues BMO et salaires juxtaposées, unités et groupes propres | Aucun indice commun ni causalité calculée |
| V23 | Composant et état absent pour l’examen courant | Réponse non nulle avec population/session |
| V24 | Cartes régionales et départementales ; codes Chart explicités et sélecteur de lieux observés | Les cartes de bassins/communes ne sont pas fabriquées ; validation complémentaire des géographies particulières |
| V25 | Sources, périodes, groupes et limites conservés ; 29 notices accessibles | Audit métier et accessibilité de production, généralisation des cas limites |

## Corrections techniques appliquées par rapport au référentiel

- `sens=origines` et `sens=destinations` sont utilisés au pluriel ; la colonne des origines lit `origine_libelle`, pas `destination_libelle`.
- `secret_stat` est traité comme une **valeur**, pas comme une propriété JSON imaginaire.
- `/indicateurs` expose `maille_reelle` et `repli` par mesure. Les autres réponses sont interprétées selon leur `zonage` et leur éventuel `items[].maille` ; une propriété `maille_reelle` n’y est pas inventée.
- La conversion INSEE→codes de carte est technique, explicite et limitée aux régions documentées par Chart ; les départements gardent leurs codes textuels. Un repli incompatible n’est pas colorié au lieu demandé. Les géométries natives sans valeur sont neutralisées en gris avec une légende explicite : la couleur initiale du SVG ne doit pas suggérer une valeur.
- Les liens de fichiers proposés par certaines lignes de la matrice renvoient à d’autres indicateurs. Le constructeur lit les réponses salariales/recrutement/prospective réellement correspondantes.
- Aucun camembert n’est utilisé pour les mobilités ou les secteurs partiels. Aucune courbe n’est déduite d’un simple horizon 2030.

Ces corrections sont dans le code et ce compte rendu ; les documents communs d’origine ne sont pas réécrits silencieusement.

## Accessibilité, responsive et sobriété

- Source et période sont transmises à DataBox ; unité, population et territoire effectif figurent dans les explications.
- Bascule native graphique/tableau vérifiée avec les valeurs réellement rendues dans le DOM. Tableaux avec légendes et en-têtes ; labels complets conservés.
- Nombres finis seulement dans les graphiques. Zéro distinct de `null`, propriété absente, `secret_stat`, valeur invalide et sélection sans lignes. Une valeur masquée ou absente n’est pas remplacée.
- Les montants, taux et groupes ne sont pas agrégés. Pas d’arrondi métier recalculé ni de conversion annuel/mensuel.
- Aucun débordement de page à 320 px. Les graphiques aux légendes longues disposent d’une zone de défilement ; les repères salariaux utilisent des intitulés courts expliqués et gardent les libellés complets dans les tableaux.
- Les régions graphiques peuvent recevoir le focus ; les sections et contrôles natifs restent accessibles. Cela ne remplace pas une recette clavier/lecteur d’écran complète ni un audit RGAA.
- Les graphes ne sont pas tous montés à chaque navigation. Aucune carte, police ou bibliothèque distante n’est téléchargée à la consultation.
- Plein écran, capture et export CSV natifs sont désactivés. Le CSV de cette version nécessite une adaptation pour les cellules contenant séparateurs/retours à la ligne et leurs métadonnées. Le téléchargement/rechargement de Mes pistes est préservé.

## Fichiers modifiés et ajoutés

| Emplacement | Modification |
|---|---|
| `12_maquette_html/sources/interface_citoyenne.js` | Remplacement des barres CSS, cycle de montage, classes DSFR sur champs/sélecteurs/boutons |
| `12_maquette_html/sources/visualisations_dsfr.js` | Adaptation des réponses natives et compositions par écran ; comparaison régionale ; passerelle vers les salaires du lieu choisi |
| `12_maquette_html/sources/construire.py` | Réponses géographiques observées supplémentaires, embarquement DSFR/Chart et contrôles |
| `12_maquette_html/index.html` | Page autonome reconstruite |
| `../commun_datavisualisation/` | Dépendances, verrou, provenance, licences, adaptateurs, composants et construction réutilisables |
| `12_maquette_html/controles/scripts/verifier_dsfr_chart.js` | Tests des vrais graphiques, cartes, tables et états |
| `12_maquette_html/controles/scripts/verifier_navigateur.js` | Prise en compte des erreurs initiales et lancement des contrôles Chart |
| `12_maquette_html/controles/scripts/capturer_visualisations.ps1` | Captures reproductibles de salaires et cartes |
| `12_maquette_html/controles/scripts/verifier_integration_dsfr.py` | Vérification des empreintes des références et des 31 IDs |
| `12_maquette_html/controles/` | Rapports desktop/mobile, empreinte, preuve d’intégrité et documents de contrôle reconstruits |
| `12_maquette_html/apercus/` | Captures actuelles et captures des visualisations |
| `README.md`, `12_maquette_html/README.md` | Instructions et état des contrôles actualisés |
| `99_archives/2026-11-02_dsfr_chart/` | Inventaire et sauvegarde avant intégration, rapprochement avec PROPRE |

Les livrables 01–10 ne sont pas remplacés par une nouvelle version parallèle. La table de conception conserve exactement E01 à E31. Les sources de référence et les huit fichiers communs restent intacts.

## Vérifications exécutées

| Vérification | Résultat et portée |
|---|---|
| Installation npm et inventaire des dépendances | DSFR Chart 2.1.1 / DSFR 1.15.4 effectivement installés |
| Compilation/assemblage partagé | `scripts/build.mjs` exécuté avec succès ; distributions et ressources locales produites |
| Assemblage HTML | `sources/construire.py` exécuté avec succès ; 29 mesures, 22 vues de navigation ; manifeste SHA-256 |
| Tests purs | **20 réussis, 0 échec** ; vrais JSON et cas limites ; [résultat TAP](../commun_datavisualisation/dist/TESTS_ADAPTATEURS.tap) |
| Recette desktop | **179 réussis, 0 échec**, largeur 1410 px ; [rapport](12_maquette_html/controles/resultats/CONTROLE_DESKTOP.json) |
| Recette mobile | **179 réussis, 0 échec**, largeur 320 px ; [rapport](12_maquette_html/controles/resultats/CONTROLE_MOBILE.json) |
| Rendus effectifs | Canvas barres/courbe, SVG région/département/prospective, TableChart, bascule, icônes, neutralisation des zones sans donnée, données annuelles/négatives/zéro, comparaison régionale et absence de transfert entre métiers |
| Inspection visuelle | Captures salaires et cartes examinées ; adaptation mobile des légendes et des tableaux |
| Contrôles du dossier API | **6 exécutés avec succès** ; ils restent hors ligne, avec leurs limites documentées |
| Intégrité | **155 références protégées inchangées** ; [preuve](12_maquette_html/controles/resultats/INTEGRITE_DSFR_CHART.json) |
| HTTP réel / RGAA complet | Non exécutés ; aucune validation implicite revendiquée |

Captures : [salaires desktop](12_maquette_html/apercus/dsfr-salaires-desktop.png), [salaires mobile](12_maquette_html/apercus/dsfr-salaires-mobile.png), [carte desktop](12_maquette_html/apercus/dsfr-territoires-desktop.png), [carte mobile](12_maquette_html/apercus/dsfr-territoires-mobile.png). Les captures mobiles montrent une fenêtre de 320 px dans son cadre de contrôle.

## Dépendances restantes, sans retrait de fonctionnalités

| Suivi | Travail restant et traitement actuel |
|---|---|
| Q01 | Environnement HTTP et divergences documentaires : connexion, authentification et campagne live à réaliser dans l’environnement prévu. Ne pas assimiler la lecture de fixtures à cette campagne. |
| Q06 | Faire clore la règle de secret signalée ouverte dans le contrat. Le client masque les valeurs reçues sous secret sans reconstituer les effectifs. |
| Q07 | Le couple 0 saisonnier / 1,7 % est conservé tel que reçu et contextualisé ; arrondis/dénominateurs à expliquer par RCO, sans correction inventée. |
| Q11 | Garantie de rattachement/regroupement des sessions ; aucune identité de session ni relation fournisseur n’est reconstruite. |
| Q14 / R17 | Filtre secteur/métier vide sur le cas observé. Le contexte économique du secteur reste distinct de l’emploi du métier ; correction/explication fournisseur suivie. |
| Q05 conditionnelle | Reproduire avec URL conforme avant d’attribuer l’incident à RCO. |
| Tests autonomes | Collecter `/domaines`, page 2 des compétences, `depuis`, autres métiers/lieux, tranches salariales ouvertes, replis, cohortes non nulles, mobilité régionale/60+, filtres de sessions. Utiliser les GET déjà documentés. |
| Comparateur | La deuxième réponse statistique réelle est nécessaire à une comparaison numérique complète. Le composant est réutilisable ; l’écran ne prête pas au second métier les statistiques du premier. |
| Accessibilité | Recette manuelle clavier et lecteur d’écran, agrandissement et audit RGAA de production à mener ; pas de certification automatique. |
| Autres parcours | Les composants sont partagés et prêts à être consommés. Les deux autres parcours n’étant pas fournis, aucun faux raccordement n’est ajouté. |

Tous ces travaux restent dans le périmètre de réalisation. Aucun point ci-dessus ne vaut proposition de suppression ou de passage hors périmètre.
