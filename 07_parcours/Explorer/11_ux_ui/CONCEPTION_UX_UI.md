# Explorer V2 — conception UX/UI

**Évolution courante :** la navigation de première lecture utilise désormais quatre questions et une recherche persistante ; les neuf vues détaillées décrites historiquement restent accessibles. Voir [la structure mise à jour](../12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md). Les premiers visuels Figma/SVG ne sont pas annoncés mis à jour à distance.

**Statut au 2 novembre 2026 :** conception initiale conservée pour les preuves et la structure. Pour la présentation actuelle, consulter [le HTML citoyen](../12_maquette_html/index.html) et [sa règle éditoriale](../12_maquette_html/documentation/REDACTION_CITOYENNE.md). Les visuels initiaux et les constats Figma de ce document ne prouvent pas l'état actuel de l'interface HTML.

Proposition du 2 novembre 2026, fondée sur les documents01–10 harmonisés et les preuves du dossier observées au 1er novembre. **E01–E31 sont conservées.** Il s'agit de conception et de maquettes, sans application ni nouvel appel HTTP. Les choix d'interface ci-dessous sont proposés à validation ; ils ne clôturent pas D02–D10.

[Ouvrir Figma](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav) · [Architecture visuelle](archives/conception_initiale/ARCHITECTURE_EXPERIENCE.svg) · [Mobile F1610](archives/conception_initiale/mobile/essentiel.svg) · [Menu des questions](archives/conception_initiale/mobile/menu.svg) · [États](archives/conception_initiale/ETATS_ET_ERREURS.svg) · [Visualisations](archives/conception_initiale/PLANCHE_VISUALISATIONS.svg)

## Livraison et niveau de finalisation

17 vues desktop éditables ont été créées dans le compte « Figma », organisation **sg.social.gouv.fr**, avec des composants DSFR importés, des textes Marianne, des mises en page automatiques et des composants locaux de données. Aucun écran n'est une image aplatie.

Le quota MCP du siège Collab a interrompu la création au début du mobile. **Il n'y a pas de prototype Figma câblé, ni de mobile Figma livré.** Les17 vues mobiles correspondantes, trois compléments (Formacodes, transitions, sources) et le sommaire sont livrés en21 SVG locaux éditables et liés entre eux. Les SVG représentent les formulaires et les onglets ; ils n'exécutent pas leurs filtres. Leur longueur correspond au contenu défilant, pas à une hauteur d'écran fixe. Le viewport cible est390×844.

Les points précis à finaliser dans Figma sont recensés dans [LIVRAISON_ET_RECETTE.md](LIVRAISON_ET_RECETTE.md). Ils incluent le libellé provisoire du bloc de marque, deux destinations de liens Formacode et la distinction entre contrôles dessinés et interactions réelles. La conception ne doit pas être présentée comme une interface RGAA auditée ou un produit déjà connecté.

## Architecture de l'expérience

L'entrée Explorer propose trois modes dans une même zone de recherche : **Métier**, **Diplôme ou certification**, **Secteur · domaine professionnel ROME**. Le troisième libellé articule le vocabulaire public acté « Secteur » et le besoin d'éviter la confusion avec les secteurs économiques NAF. Les maquettes affichent « Domaine professionnel » : cette proposition de wording relève de D02, elle ne remplace pas la décision actée.

Le résultat identifié conduit à une fiche, jamais directement à un score. Depuis chaque fiche, conserver la recherche, ses filtres, sa page et le lieu demandé pour permettre le retour sans recommencer. Le territoire est un contexte de consultation, pas un filtre qui ferait disparaître les descriptions ou les compétences.

La navigation principale comporte Explorer et Mes pistes. La fiche Métier comporte un sommaire de neuf questions, un accès au comparateur et à la sélection temporaire. Une action principale par section invite à approfondir ; les autres informations restent accessibles dans la même section, par détail progressif. L'information utile à l'interprétation d'un chiffre — famille, lieu réel, période — reste immédiatement visible.

Trois niveaux de lecture :
1. **Se repérer** : activité, spécialités et quelques données contextualisées. Aucun classement personnel.
2. **Comprendre** : sections thématiques, familles séparées, indicateurs complets, populations distinctes.
3. **Vérifier** : source, définition, catalogue, bases, limites, listes complètes et liens entre objets identifiés.

### Les passerelles

- Métier → ses compétences/contextes → sélection OGR → métiers associés → nouvelle fiche ou comparaison.
- Métier → métiers proches reçus → fiche cible ; cette relation ne représente pas un flux de mobilité.
- Métier → certifications filtrées par ROME → fiche Certif Info → blocs RNCP et sessions publiées.
- Certification → codes ROME associés → fiches ; l'intention « je possède ce diplôme » change l'ordre de lecture, pas les relations disponibles.
- Métier → Formacodes reçus → certifications filtrées par Formacode → fiche → sessions. **Un Formacode ne conduit pas à l'arbre des domaines ROME.**
- Domaine professionnel → métiers du domaine → compétences/contextes/transitions → fiche ; aucune statistique de domaine agrégée localement.
- Fiche/fiche territoire → Mes pistes → choix de deux métiers → comparateur ; retour sur chaque fiche sans perdre les autres critères.

## F1610 — neuf questions pour décider quoi approfondir

| Vue | Question | Composition et restitution |
|---|---|---|
| essentiel | Que fait-on dans ce métier ? | Titre ROME V3, appellations et définitions par spécialité. Avertissement sur les spécialités. Synthèse BMO, tension, salaire familial et transition ; chacun porte son propre périmètre. |
| competences | Quelles compétences et conditions ? | Recherche/catégories, cœur, part des spécialités si reçue, savoir-être et conditions. Listes sélectionnables ; pas de jauge de maîtrise. Bloc distinct des compétences citées dans les offres. |
| recrutements | Est-ce que ce métier recrute ? | BMO par FAP228, tension catégorielle et sept composantes, offres diffusées/collectées séparées, contrats et caractéristiques, série mensuelle, statut d'emploi. |
| salaires | Quels salaires, et dans quels secteurs ? | Médiane mensuelle familiale en carte. Q1/médiane/Q3 annuels en tableau. Salaires sectoriels par FAP225/NAF38, parts, effectif de base et référence ensemble. |
| territoires | Où regarder les opportunités ? | Lieu identifié ; deux lectures indépendantes recrutement/salaire, familles et mailles explicites ; classement tabulaire avant toute carte. |
| mobilites | Quelles mobilités sont observées ? | Deux sens, région/France, âge, famille. Barres0–100 et table de situations ; même famille, emploi et hors emploi distingués. Pas de parcours individuel déduit. |
| prospective | Quelles perspectives à2030 ? | Cinq composantes par FAP87 en table effectif/taux ; emploi2019, poids, spécificité et tension de départ en détail. Entrées régions et métiers d'une région. |
| secteurs | Quels secteurs emploient et évoluent ? | Parts/effectifs d'actifs par FAP225×NAF38. Contexte économique territorial séparé : établissements, employeurs, salariés, créations, évolutions et défaillances datées. État spécifique R17. |
| formations | Comment se former et explorer d'autres pistes ? | Certifications, voies, sessions, thèmes Formacode, insertion des formations, métiers proches et accès à la comparaison directionnelle. |

### Lecture des valeurs réellement observées

La synthèse montre26 projets pour les Couvreurs du bassin de Montpellier en2026 et une tension extrême en Hérault en2024. Le salaire1690€ est celui de la famille B0Z21,8 métiers, Hérault,2023 ; il ne doit pas devenir « salaire des couvreurs de Montpellier ».

Le bloc sectoriel affiche séparément les salaires **France** reçus, dont1750€ pour B0Z21 Construction et2090€ pour B2Z44 Construction. Le contexte économique Construction du bassin de Montpellier (2613 établissements employeurs,16440 salariés privés) ne mesure pas l'effectif de F1610.

La prospective présente B0Z et B2Z séparément. Les créations nettes négatives et les déséquilibres signés sont conservés. Le tableau n'impose pas d'identité arithmétique entre composantes arrondies ou définies différemment.

Pour les mobilités,55,3% dans la même famille B0Z21 ne veut pas dire55,3% dans le même poste. Les situations publiées sont partielles ; ne pas compléter le total à100, ni transformer la destination FAP en fiche ROME.

## Autres écrans et interactions attendues

### Recherche et résultats

Mode Métier/Certification : libellé de champ explicite, aide courte, minimum de deux caractères, état de chargement et annulation des réponses périmées. Une suggestion sélectionnée porte un identifiant ; la saisie seule n'en tient pas lieu. Déclencher la recherche sur validation ou après délai raisonnable à mesurer, pas sur chaque frappe sans contrôle.

Mode Domaine : charger l'arbre documenté, puis filtrer localement ses libellés. Montrer chemin parent/enfant ; garder le contexte lorsque l'utilisateur ouvre la liste métier. Ne pas afficher un total non reçu.

Les résultats affichent intitulé, type d'objet et référence. Pagination actionnable au clavier ; « Charger la suite » annonce le nombre d'éléments ajoutés si disponible. Les alternatives du domaine restent un bloc distinct d'une recherche q, tant que celle-ci n'est pas prouvée.

### Certification

Les intentions « Je souhaite l'obtenir / Je possède ce diplôme » sont deux entrées d'une même fiche. Dans la première : accès, blocs, sessions, résultats. Dans la seconde : métiers associés en premier, puis exploration des contenus et possibilités d'accès complémentaires. Aucun diagnostic d'éligibilité ou d'équivalence personnelle.

Les résultats sont répartis par population : InserJeunes scolaire/apprentissage, InserSup, demandeurs d'emploi, inscrits, examens et capacité/demande. Chaque carte ou ligne porte sa promotion, son horizon et son dénominateur. Le68,5% d'emploi salarié à12mois des apprentis et le51,4% d'accès à l'emploi à6mois des demandeurs d'emploi ne sont pas comparés comme deux performances équivalentes. Les champs absents restent expliqués, sans disparition de leur rubrique.

Les blocs RNCP sont des textes avec modalités d'évaluation, distincts des OGR. Les sessions sont des listes à venir/en cours avec territoire, dates, lieu, organisme et modalité reçue. « Présentiel » vient du code0 documenté ; les places disponibles et l'inscription ne sont pas promises. Le rattachement individuel reste Q11. La présentation Onisep est séparée conformément aux variantes contractuelles.

### Exploration guidée

Étape1 : chercher et sélectionner des compétences OGR, regroupement lisible par catégorie ; puces retirables avec bouton nommé, pas seulement une croix. Étape2 : groupe radio « au moins une / toutes », domaine facultatif, puis chaque contexte avec « Indifférent / Rechercher / Éviter ». Les valeurs sont des codes en chaînes, zéros initiaux conservés. Les deux états avec/sans d'un même contexte sont mutuellement exclusifs.

Étape3 : action « Voir les métiers associés ». Résultats avec les compétences effectivement trouvées et l'ordre reçu ; aucun pourcentage de compatibilité. Les codes103659 et125416 illustrent R23 ; les correspondances surprenantes reçues ne sont pas corrigées par invention. Le contexte300782 illustre R24. Toute combinaison supplémentaire a son propre test.

### Comparateur

Deux emplacements de métiers remplaçables, lieu demandé commun, identité complète de chaque observation. Quatre familles de lecture : Comprendre, Compétences/conditions, Marché/territoires, Se former. Marché ouvre recrutements, salaires et salaires sectoriels, mobilités, prospective et secteurs ; aucune de ces rubriques n'est supprimée.

Les compétences communes/spécifiques exigent les pages complètes des deux listes ; le rapprochement directionnel depuis est une relation entre métiers, jamais une évaluation des acquis. Tant que F1613 n'est pas chargé, « Données non chargées » ; pas de nombre de compétences communes d'exemple.

Deux valeurs de même source, période, population, unité, grain et géographie peuvent être lues côte à côte. Si les métiers partagent la même FAP, montrer « Observation familiale partagée », pas deux résultats indépendants. Si les familles ou les mailles diffèrent, conserver les deux descriptions avec « Périmètres différents ». Ne pas calculer de delta, score ou gagnant. Aucune fusion des classes FAP87/225/228.

### Mes pistes

Ajout explicite et annonce accessible ; retrait réversible dans la session de consultation proposée. Deux métiers sélectionnés activent le comparateur. La limite de trois et la durée de conservation restent une proposition D08, pas une décision acquise. Distinguer mémoire de page, stockage de session et sauvegarde distante : l'API ne fournit pas de favoris persistants.

## Visualisations : choix et garde-fous

[MATRICE_VISUALISATIONS.csv](MATRICE_VISUALISATIONS.csv) conserve les **29 codes de /mesures et241 occurrences de champs**. Une occurrence n'est pas forcément un champ unique ni une valeur effectivement publiée pour F1610. Le catalogue et le résultat restent deux sources de preuve distinctes. La matrice donne pour chaque mesure ressource, appel de consultation, paramètres, champs de catalogue, grain, mailles, source, millésime, composant, IDs et précautions.

Privilégier :
- une carte quand une valeur contextualisée suffit ;
- un tableau pour plusieurs dimensions, les quartiles, composantes2030, horizons et populations ;
- des barres horizontales avec origine zéro pour les parts réellement reçues ;
- une série mensuelle uniquement pour les mois fournis, sans courbe lissée ;
- des liens identifiés pour les compétences, thèmes et relations entre objets ;
- une explication textuelle pour les états non numériques, limites et tranches ouvertes.

Pas de radar de compétences, jauge de tension synthétique inventée, score territorial, Sankey de mobilités partielles ou cascade2030 supposant des sommes. Une carte géographique n'est pas retenue par défaut : aucun fond/cartographie externe ni géométrie API non démontrée n'est introduit. Les tableaux de classement permettent de comparer les territoires avec les seuls GET disponibles.

La période affichée est celle du résultat. Le millésime du catalogue est un repère méthodologique ; il ne doit pas remplacer une période effective plus précise, notamment pour les offres, sessions ou défaillances. Les unités ne proviennent pas d'un champ unite uniforme supposé.

## Responsive, DSFR et accessibilité

Desktop1440 : contenu organisé autour d'un sommaire de240px et de sections larges. Tablet768 : sommaire repliable au-dessus du contenu, cartes sur une ou deux colonnes selon longueur des libellés. Mobile390 et cible de reflow320 : une colonne, marges proposées24px puis16px à320, pas de barre d'actions fixe masquant les contenus ; boutons sur plusieurs lignes si nécessaire.

Le comparateur mobile se lit par critère, avec intitulé des deux métiers répété. Les tableaux statistiques transposés en fiches conservent les libellés de colonnes. Pour une table réellement bidimensionnelle, garder une version tabulaire accessible et un défilement horizontal local annoncé ; aucun débordement horizontal de la page. Les figures ont toujours une alternative tabulaire.

Les maquettes Figma utilisent les composants importés DSFR (en-têtes, boutons, navigation, onglets, champs et accordéons) et Marianne. Les cartes de données sont des composants locaux à fondations sémantiques : texte, texte secondaire, action, surface, bordure et espacement. Le bleu d'action distingue les liens/contrôles ; les titres ordinaires restent sombres. Les SVG locaux sont des interprétations vectorielles, avec Marianne si disponible et Arial en repli, pas des instances DSFR exportées.

À réaliser et vérifier dans l'interface :
- lien d'évitement, landmarks, h1 unique, hiérarchie des titres et langue française ;
- boutons/liens sémantiques ; onglets et accordéons avec nom, rôle, état, clavier et focus ;
- cibles d'au moins44px proposées, focus visible et non masqué ; aucune information sur la seule couleur ou au seul survol ;
- labels permanents et erreurs rattachées aux champs ; suggestions accessibles sans perte de focus ;
- annonce discrète des résultats/erreurs/retraits ; pas d'annonce de chaque frappe ;
- texte redimensionné, zoom200/400%, reflow320, contraste réel de tous les états et table lisible ;
- en-têtes de tableau associés aux cellules ; ordre de lecture métierA/métierB conservé ;
- sources et bases accessibles sans infobulle obligatoire ; graphiques nommés avec données équivalentes ;
- pas d'animation obligatoire, respect de réduction du mouvement.

Ce sont des exigences de conception et de recette, **pas une certification RGAA**. Références de conception : [composants DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/composants), [onglets DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/onglet/design-de-l-onglet), [critères et tests RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/). Ces références servent à l'interface ; aucune donnée métier externe n'est ajoutée.

## États, données et sobriété

[ETATS_ET_ERREURS.svg](archives/conception_initiale/ETATS_ET_ERREURS.svg) illustre quinze familles d'états. null, clé absente, secret_stat, zéro et liste vide restent distincts. Ne jamais effacer une valeur inconnue pour rendre une figure plus jolie. Une liste partielle ne permet pas de conclure à une absence.

La page affiche d'abord le titre et les définitions ; puis charge les sections nécessaires à la lecture. Réutiliser les résultats par identifiant et paramètres exacts, conserver catalogue et référentiels en cache selon politique à définir. Réutiliser une réponse familiale commune dans le comparateur en la signalant. Annuler les recherches périmées ; gérer erreurs par section. Ne pas précharger tous les métiers, sessions et combinaisons de filtres à l'ouverture.

Aucune photographie décorative, carte lourde ou animation n'est nécessaire ici. Les diagrammes et barres peuvent être rendus nativement. Les informations restent disponibles sans visualisation complexe. L'attribution RCO est visible ; le véritable asset de logo RCO reste à intégrer, sans logo inventé.

## Couverture des31 fonctionnalités

| ID | Fonction conservée | Vues / support | Règle d'interaction |
|---|---|---|---|
| E01 | Recherche de métiers | recherche / resultats | Saisie identifiée, choix explicite du résultat ; ne pas promettre une recherche sémantique. |
| E02 | Recherche de certifications | recherche / certification | Mode certification ; référence RNCP/RS et type réel. Intitulé ancien introuvable : explication et nouvelle recherche. |
| E03 | Arbre et fiche Domaine | domaine | Arbre chargé puis filtre local ; sous-domaines et retour parent. Aucun q ajouté à /domaines. |
| E04 | Métiers du domaine | domaine / guide | Liste paginée de métiers du domaine ; conserver le code ROME et les critères en revenant. |
| E05 | Fiche métier | essentiel | Définitions par spécialité, appellations, tags et navigation par questions. |
| E06 | Compétences et contextes complets | competences | Catégories, cœur de métier, savoir-être, contextes ; détail des spécialités. Charger les144 compétences avant conclusion exhaustive. |
| E07 | Métiers proches | formations | Métiers proches issus des codes reçus, distincts des mobilités observées ; fiche cible et comparaison. |
| E08 | Indicateurs territoriaux complets | recrutements / salaires / secteurs / formations / prospective | Les14 familles de mesures /indicateurs ont chacune une restitution dans la matrice, y compris offres mensuelles, statut d'emploi et insertion. |
| E09 | Sélection territoriale | territoires | Recherche et sélection d'un territoire identifié ; géographie demandée distincte de la maille effectivement reçue. |
| E10 | Classements des recrutements BMO | territoires | Classement BMO par famille, mailles et tri disponibles ; projets, difficultés et saisonniers en colonnes séparées. |
| E11 | Classements des salaires | territoires / salaires | Classement salarial indépendant du recrutement ; rang reçu ou absence de rang, médiane ou tranche. |
| E12 | Comparabilité des données | sources / comparateur | Identité source/période/grain/population/unité/mailleeffective avant rapprochement ; pas de delta fabriqué. |
| E13 | Choix de compétences OGR | guide | Recherche OGR, liste de sélection avec retrait individuel ; pas d'autoévaluation personnelle. |
| E14 | Recherche multicompétences | guide / resultats-ogr | Choix explicite « au moins une / toutes », critères conservés ; correspondances OGR reçues, sans score. |
| E15 | Choix de contextes OGR | guide / competences | Contextes OGR identifiés ; groupe radio « indifférent / rechercher / éviter » pour chaque contexte. |
| E16 | Recherche avec/sans contexte | guide / resultats-ogr | Appliquer avec/sans contexte au domaine sélectionné ; expliquer qu'absence référentielle ne garantit pas absence terrain. |
| E17 | Fiche Certification et résultats | certification | Deux intentions, voies, résultats par population, promotions, horizons, inscrits, diplômés, demande/capacité et tension. |
| E18 | Blocs RNCP et recherche textuelle | certification | Quatre blocs RNCP en accordéons avec compétences/modalités textuelles ; recherche q séparée et paginée. |
| E19 | Métiers associés à une certification | certification | Liens ROME reçus ; intention « je possède » met les métiers associés en premier sans inventer équivalence. |
| E20 | Certifications associées au métier | formations / certification | Certifications actives, filtres accès/validation partielle/répertoire ; type réel et pagination. |
| E21 | Sessions à venir | certification | Liste à venir, territoire, dates/organisme/modalité ; pas de disponibilité ou identifiant stable supposé. |
| E22 | Sessions en cours | certification | Onglet en cours conservé ; même protocole de traçabilité et distinction Onisep. |
| E23 | Mobilités professionnelles | mobilites | Origines/destinations, famille, région/France et âge ; barres de parts, pas de Sankey ou lien ROME inventé. |
| E24 | Prospective détaillée 2030 | prospective | Toutes les composantes2030 et repères2019 ; entrée comparer les régions et entrée explorer une région. |
| E25 | Salaires par secteur économique | salaires | FAP225 × NAF38 ; médiane mensuelle, quartiles annuels, part des salariés et référence ensemble. |
| E26 | Secteurs d'emploi et contexte économique | secteurs | Emploi familial, contexte économique territorial, vue métier-territoire attendue et état R17 distinct. |
| E27 | Mes pistes temporaires | pistes | Ajouter/retirer, ouvrir, sélectionner deux métiers ; état local temporaire. Plafond et conservation restent D08. |
| E28 | Comparateur complet de deux métiers | comparateur | Deux métiers, descriptions, compétences communes/spécifiques, contextes, certifications et toutes les statistiques ; états comparables/non comparables. |
| E29 | Exploration des transitions | transitions / essentiel / domaine | Tags vrais/faux/null et thèmes fournis ; distinction avec projection et mobilité. Pas de filtre serveur inventé. |
| E30 | Thèmes Formacode et certifications | formacodes / formations / certification | Formacode identifié → certifications filtrées → fiche → sessions ; pas de passage par DomaineROME. |
| E31 | Catalogue et méthodologie des mesures | sources / toutes les sections | Notice de chaque mesure alimentée par /mesures, origine, définition, champs, grain, millésime, secret et limites. |

Cette table trace la **couverture de conception**. Elle ne signifie pas que tous les panneaux sont dessinés dans tous leurs états, ni que les contrôles Figma sont fonctionnels. Les compléments locaux et la matrice explicitent les rubriques détaillées dont la vue Figma ne montre encore que l'accès.

## Préparation de la réalisation

Ne créer un projet qu'après identification de l'application d'accueil et validation du passage au développement. Le présent dossier n'est pas cette application.

Ordre d'interaction et d'appels :
1. Charger /mesures une fois, puis recherche /metiers, /certifications ou /domaines selon mode ; /territoires pour un lieu sélectionné.
2. À la sélection ROME : /metiers/{rome}, puis /metiers/{rome}/competences avec pagination ; conserver les identifiants reçus.
3. /indicateurs avec rome, zonage et territoire exacts ; afficher le repli renvoyé, pas un repli déduit.
4. À l'ouverture : /recrutements, /salaires, /mobilites, /prospective/regions ou /prospective/metiers, /salaires/secteurs et /secteurs selon leurs signatures distinctes. Les paramètres exhaustifs restent dans02/03 ; ne pas leur ajouter territoire ou page par uniformisation.
5. /certifications?rome=… → /certifications/{certifinfo} → blocs et sessions. Choisir un zonage de session autorisé et son territoire ; pas de commune/France inventé.
6. Sélection OGR → /metiers avec competence, mode_competence, contexte/sans_contexte et domaine si choisis. Le comparateur réutilise les fiches puis charge les deux listes complètes et depuis selon le contrat.

Composants à réaliser : enveloppe/navigation, recherche identifiée, sélecteur territorial, fiche métier/sections, vue de mesure contextualisée, sélecteur familial, table statistique et alternative aux barres, sélecteurs OGR/contextes, fiche certification/blocs/sessions, domaine/arbre, comparateur, pistes et notice sources. Les types numériques/chaînes/null/secret doivent être traités avant le composant graphique.

Conserver les lots L1–L10 existants. La conception prépare tous les lots ; leur ordre ne réduit pas la cible. Les tests T-E01–T-E31 et les questions Q des documents03/06 restent la base de recette. Les questions réellement fournisseur restent Q01, Q06, Q07, Q11 et Q14 ; Q05 conditionnelle après requête conforme reproduisant l'erreur.

## Recherche UX et validation proposée

Aucun entretien utilisateur, test terrain ou test de lecteur d'écran réel n'a été réalisé ici. Les critères sont des hypothèses de conception confrontées au dossier et une revue heuristique, pas des résultats de recherche.

Proposer des séances avec personnes sans métier cible, personnes souhaitant changer de secteur, améliorer leur revenu ou vérifier une contrainte de travail. Tâches :
- expliquer ce que recouvre F1610 et distinguer deux spécialités ;
- retrouver un salaire et expliquer sa population et son lieu ;
- rechercher/éviter la grande hauteur sans conclure à une garantie terrain ;
- distinguer mobilité observée, métier proche et perspective2030 ;
- comparer F1610/F1613 sans prendre une FAP partagée pour deux résultats ;
- trouver une voie et une session sans déduire des places disponibles ;
- revenir aux pistes et modifier le territoire sans perdre ses choix.

Observer réussite autonome, erreurs d'interprétation, détours, compréhension des libellés et charge de lecture ; ne pas inventer de mesures de succès. Faire une passe clavier/lecteur d'écran/zoom sur l'interface développée. Les arbitrages D02–D10 portent sur ces modalités, jamais sur la suppression d'une fonctionnalité.

