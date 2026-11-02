# Explorer V2 — spécification fonctionnelle

## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.


**Mise à jour du 2 novembre 2026 — dossier rangé.** Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les 31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.

**Version :** alignement L0 — 1er novembre 2026. **Statut :** périmètre complet validé, E01–E31 conservés. **Source unique :** API DGEFP–RCO, 21 GET, ROME V3. La table `03_TABLE_CONCEPTION.csv` fait foi pour les appels, champs, tests et lots ; 02 décrit tous les indicateurs. Les modalités d'exécution encore ouvertes sont en06/10 et ne rouvrent pas le périmètre.

## 1. Cible complète validée

Les 31 fonctionnalités E01–E31 sont conservées. Les lots L0–L10 organisent les dépendances techniques ; aucune fonction n'est une extension facultative ou écartée pour complexité/manque d'exemple. Une preuve manquante ouvre un test ; une anomalie fournisseur ouvre une résolution ; une véritable impossibilité est exposée avec sa preuve, sans suppression automatique d'ID.

**Principes de parcours conservés :** une barre, trois modes Métier / Diplôme / Secteur, sélection explicite avant fiche, trois fiches spécialisées, questions avant chiffres, comparaison de deux métiers, Mes pistes sans compte, deux intentions Certification. L’entrée Domaine regroupe des métiers ; les secteurs d’activité décrivent les entreprises qui emploient. Cette distinction doit être expliquée sans afficher les codes ni les sigles des référentiels. La maquette emploie « Un domaine professionnel » ; l’interaction et les modalités de stockage restent à préciser, pas l’inclusion des fonctions.

Les mobilités professionnelles E23, la prospective détaillée2030 E24, les salaires sectoriels E25, les secteurs d'emploi E26, les compétences/contextes E06/E13–E16 et le comparateur E28 sont des éléments de la même cible. Pas de score, de classement composite de territoire, d'inférence de maîtrise personnelle ni de probabilité d'accès à l'emploi.

## 2. Parcours écran par écran

### A. Recherche
1. Écran « Explorer par vous-même » : modes Métier, Diplôme, Secteur ; barre unique et bouton rechercher. Aucun affichage de huit portes d'entrée. Suggestions *contextuelles* uniquement après premier résultat ou sur fiche.
2. Une saisie déclenche l'appel correspondant `GET /metiers?q=...`, `/certifications?q=...`, ou une navigation `GET /domaines`. Le mode Secteur repose sur les codes de domaines ROME ; l'API /domaines n'accepte pas q ; navigation arborescente et proposition de filtre local explicite des libellés reçus, dans la barre unique. Le contrat décrit l'arbre ; le JSON réel est à collecter dans L2, sans retirer cette entrée.
3. Résultats paginés : nom du métier ou de la certification, domaine et type compréhensible ; identifiants et noms des référentiels conservés dans les traitements internes ; la saisie brute ne crée jamais de fiche. Gestion explicite 0 résultat, erreur, charge, page suivante, mot approximatif non trouvé ; ne pas inventer de correction orthographique côté API.

### B. Fiche Métier (ROME V3)
**Entête :** intitulé ROME, définition, domaine, contexte de consultation. **Quatre questions :** « Que fait-on dans ce métier ? » (définitions reçues, savoir-faire, compétences et contextes référencés ; aucun champ activités inventé) ; « Où sont les opportunités ? » (BMO, tension seulement si mesure documentée, géographie) ; « Combien gagne-t-on ? » (médiane mensuelle et distribution annuelle FAP225 séparées, source et unité) ; « Quelles autres pistes ? » (métiers proches, recherche par OGR, ajout aux pistes). **Pour aller plus loin :** mobilités, prospective détaillée, salaires sectoriels, secteurs d'emploi, certifications et sessions, tous prévus avec chargement à la demande.

**Actions :** Ajouter aux pistes (plafond de3 proposé, modalité D08 à finaliser), comparer 2 métiers, rechercher autres métiers avec compétence, contextes de travail à rechercher ou éviter, consulter certifications associées, changer le territoire. La phrase « Ce métier me correspond-il ? » est exclue comme promesse de profilage personnalisé ; retenir « Ce qu'il faut savoir avant de choisir ».

### C. Fiche Certification
Même ressource API, **bascule de présentation** « Je possède ce diplôme / Je souhaite l'obtenir ». Pour la première intention : métiers associés (ROME V3), blocs RNCP si présents, autres pistes ; pour la seconde : certification, statut, voies d'accès documentées, insertion par population, sessions publiées à venir et en cours, avec recette du filtre et suivi R18/R19 ; modalités et dates, jamais places disponibles ou admission garantie. La fiche conserve toutes les mesures Certification documentées : voies, tension des FAP associées, insertion, poursuite d'études, salaires InserSup, inscrits, diplômés, résultats d'examen et demande/capacité Affelnet-Parcoursup, chacune à son horizon. Ne jamais mélanger population scolaire, apprentissage, InserSup et demandeurs d'emploi ; ne jamais dire qu'un rattachement ROME garantit l'accès au métier.

Les données de la fiche sont nationales et les certifications actives seulement : un ancien diplôme détenu peut être introuvable. Aucun accès aux archives ou équivalence individuelle n'est inventé. Les blocs RNCP sont des textes, pas des OGR ; le RS n'a pas de blocs. Les thèmes Formacode mènent aux certifications puis aux sessions via Certif Info.

### D. Fiche Secteur (domaine ROME)
Grand domaine → domaine professionnel → métiers. Liste progressive, filtre par compétences et contextes référencés. Aucune statistique agrégée inventée au niveau du domaine ; comparaison au niveau des métiers avec rappel du grain statistique des familles.

### E. Comparaison et Mes pistes
L'utilisateur peut conserver des codes ROME V3 temporaires sans compte (**plafond proposé : trois**, stockage/durée D08 à finaliser) ; deux sélectionnables pour un comparateur. Vue questionnelle : définitions et contextes, compétences OGR communes et spécifiques sur listes complètes, salaires, projets BMO, certifications, accès aux mobilités/prospective/secteurs détaillés. Aucun score, delta ou taux supplémentaire calculé ; valeurs côte à côte avec bases/unités/périodes explicites. Deux ROME partageant une FAP partagent une observation, indiquée comme telle ; plusieurs familles restent plusieurs groupes. Si l'un des métiers manque d'une mesure, montrer l'absence, jamais un zéro.

### F. Territoire
Choisir via `/territoires`, mémoriser `{zonage, territoire_code}`. Lire le repli renvoyé par l'API pour chaque mesure via sa `maille_reelle` propre, jamais substituer silencieusement au territoire demandé. Afficher séparément les territoires avec le plus de projets BMO et ceux avec les salaires médians observés les plus élevés. Le classement doit rester dans un jeu de données homogène ; la pertinence métier dépend du grain FAP, pas du seul code ROME de filtre.

### G. Mobilités, prospective et secteurs : détail accessible
- **E23 Mobilités :** choisir origines/destinations, âge et France/région ; groupes FAP225, situations hors emploi et parts reçues, période2022–2023 observée. Top15 au plus, parts secrètes omises : pas de total artificiel à100 ni de lien FAP→ROME supposé.
- **E24 Prospective2030 :** entrée métier→régions et entrée région→familles→métiers V3 via rome_codes[]. Voir emploi2019, créations nettes, départs, postes, jeunes et déséquilibre avec leurs taux, part d'emploi/spécificité régionales et référence France. Conserver les négatifs, agrégats et limites métropole/Corse ; projection distincte de BMO, aucun recalcul.
- **E25 Salaires sectoriels :** groupes FAP225×NAF38, référence ensemble, salaires mensuels/annuels distincts, parts des salariés, seuils et maille/repli par ligne. Une médiane null en tranche ouverte est affichée comme tranche annuelle.
- **E26 Secteurs employeurs :** parts d'emploi familiales RP2021 via emploi_secteurs et contexte NAF territorial via /secteurs sans rome affichés séparément. Le résultat contractuel métier-territoire avec rome reste à résoudre R17, sans retrait de fonction ni somme FAP ou compte local attribué au métier.
- **E29 Transitions :** badges de fiche et exploration locale des tags écologie/numérique/démographie après toutes les pages du catalogue. Aucun filtre transition serveur ni rang de croissance inventé.
- **E30 Formacodes :** thèmes → certifications filtrées → fiches → sessions par Certif Info. Un thème n'est pas une session ; formations non certifiantes par Formacode non exposées.

## 3. Règles transversales et états
- ROME V3 uniquement en entrée/sortie ; les contextes et compétences OGR éventuellement dérivés de ROME 4 restent consolidés sur le parent ROME V3 ; ne jamais présenter un code ROME4.
- `null` = inconnu/indisponible selon le champ ; exception salaire avec tranche ouverte : afficher la tranche annuelle sans inventer de médiane ; `0` = valeur nulle observée ; `[]` = aucun élément retourné ; clé absente = inconnue ou omise par `fields` ; `secret_stat` = masquage statistique. Aucun de ces états n'est interchangeable.
- Pour chaque mesure afficher **source, millésime, définition/unité, grain et géographie réelle/repli suivant les champs de sa route** ; pas de somme entre FAP225/FAP228/FAP87, entre BMO et projection 2030 ni entre salaires mensuels et quartiles annuels.
- Pages : boucler sur `page/last_page` quand nécessaire, selon besoin utilisateur ; états 4xx/5xx, réseau, 422 ; réponses complètes utilisables sans fields ; retester l'URL de projection plurielle R24, dont l'origine singulière n'est pas démontrée comme défaut fournisseur.
- Les contextes **non référencés** ne signifient pas absence garantie de cette condition dans un emploi réel.
- *Mes pistes* : aucune donnée de compte ni enregistrement serveur ; durée de conservation et stockage local à arbitrer (session en mémoire conseillée par défaut).
- RGAA/DSFR : contrôles accessibles, affichages sans code couleur seul, erreurs annoncées, listes accessibles, titres hiérarchisés et texte accompagnant les graphiques.
- SEO : pages métier/certification fondées sur codes stables ; pas d'indexation de recherches vides, variantes de filtres ou pistes personnelles ; contenu textuel provenant de l'API, sans inventer d'indicateurs.

## 4. Critères de succès
Un utilisateur peut chercher, sélectionner un résultat exact, lire une fiche questionnelle, découvrir une alternative via OGR ou ROME, sauvegarder 2 pistes dans la session, ouvrir une comparaison et retourner à ses choix sans recommencer. Les indicateurs n'altèrent pas leurs granularités. Aucun bloc ne plante en cas de null, secret_stat, liste incomplète, tranche salariale ouverte ou changement de maille. Les 31 fonctions restent accessibles par leurs parcours ; leurs erreurs partielles n'effacent pas la fiche. Une capacité bloquée par le fournisseur n'est pas déclarée livrée parce que son bloc est caché. Les résultats statiques/fixtures sont séparés des tests HTTP.

## 5. Index fonctionnel exhaustif et lots

Les besoins détaillés, appels JSON, états et acceptations de chaque ligne sont dans 03 ; les 29 mesures et tous leurs champs dans 02. Lots identiques à09, sans réduction de cible.

| ID | Fonction attendue | Lot |
|---|---|---|
| E01 | Recherche de métiers | L2 |
| E02 | Recherche de certifications | L2 |
| E03 | Arbre et fiche Domaine | L2 |
| E04 | Métiers du domaine | L2 |
| E05 | Fiche métier | L2 |
| E06 | Compétences et contextes complets | L2/L3 |
| E07 | Métiers proches | L2 |
| E08 | Indicateurs territoriaux complets | L4 |
| E09 | Sélection territoriale | L2 |
| E10 | Classements des recrutements BMO | L4 |
| E11 | Classements des salaires | L4 |
| E12 | Comparabilité des données | L4 |
| E13 | Choix de compétences OGR | L3 |
| E14 | Recherche multicompétences | L3 |
| E15 | Choix de contextes OGR | L3 |
| E16 | Recherche avec/sans contexte | L3 |
| E17 | Fiche Certification et résultats | L2 |
| E18 | Blocs RNCP et recherche textuelle | L2/L3 |
| E19 | Métiers associés à une certification | L2 |
| E20 | Certifications associées au métier | L2/L3 |
| E21 | Sessions à venir | L8 |
| E22 | Sessions en cours | L8 |
| E23 | Mobilités professionnelles | L5 |
| E24 | Prospective détaillée 2030 | L6 |
| E25 | Salaires par secteur économique | L7 |
| E26 | Secteurs d'emploi et contexte économique | L7 |
| E27 | Mes pistes temporaires | L9 |
| E28 | Comparateur complet de deux métiers | L9 |
| E29 | Exploration des transitions | L3 |
| E30 | Thèmes Formacode et certifications | L3 |
| E31 | Catalogue et méthodologie des mesures | L4 |

## Règle de présentation citoyenne — décision produit du 2 novembre 2026

Les écrans affichent les noms fournis par l’API, sans codes, noms de référentiels, version du projet ni notes de conception. Les paramètres techniques restent dans le code et la documentation. Expliquer les chiffres en langage courant : sens, personnes concernées, lieu, période, unité et limites. Une information manquante n’est pas zéro ; un projet de recrutement n’est pas une offre ; une projection n’est pas une garantie. Conserver les sources. Ne pas ajouter de score, de taux ou de calcul pour vulgariser. Cette règle s’applique aux31 fonctionnalités et à leurs critères de recette. La ligne éditoriale est [documentée ici](12_maquette_html/documentation/REDACTION_CITOYENNE.md).
