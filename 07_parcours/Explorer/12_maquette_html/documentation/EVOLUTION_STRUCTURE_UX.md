# Évolution ciblée de l'expérience Explorer

Retour utilisateur du 2 novembre 2026, appliqué au HTML existant. Le socle de restitution des données et les31 fonctionnalités sont conservés. Le retour cite index(1).html et un document UX non joints ; le travail porte sur l'index actuel du dossier et les recommandations effectivement fournies, sans prétendre à une comparaison de fichiers absents.

## Changements réalisés

| Demande | Réalisation dans la maquette | Limite conservée |
|---|---|---|
| Ouvrir Explorer | Sans fragment d'URL, l'entrée ouvre la recherche. Les liens directs vers les fiches restent possibles. | Aucun métier n'est sélectionné à partir d'une simple saisie. |
| Recherche persistante | Barre unique, trois modes, saisie et lieu conservés dans les vues. Barre fixe au défilement sur ordinateur ; repliable sur mobile pour ne pas masquer le contenu. | La saisie est une recherche locale dans les réponses embarquées. |
| Résultats pilotés par les données | Adaptateurs séparés pour métiers, certifications, domaines et territoires ; états de chargement, erreur, aucun résultat et protection contre une réponse périmée. | Aucun serveur API n'est appelé. Les signatures GET sont préparées, pas testées en HTTP. |
| Quatre questions de première lecture | Activités ; opportunités ; salaires ; autres pistes. Les mobilités, la prospective2030, les formations et les conditions détaillées restent accessibles dans « Pour aller plus loin ». | Les vues de données existantes sont réutilisées, sans réduction fonctionnelle. |
| Comparateur libre | Deux métiers choisis dans les résultats ou les pistes, sélecteurs, inversion, avertissement si identiques ; données présentées pour les métiers effectivement choisis. | Pas de copie des statistiques de F1610 sur une autre fiche. Les listes partielles ne permettent pas de compter toutes les compétences communes. |
| Choix territorial | Recherche de libellé, filtre par type, sélection d'un objet territorial observé et conservation du lieu. | Un lieu sans chiffres correspondants affiche une absence ; une observation de Montpellier ne devient pas celle d'un autre lieu. Les noms des lieux mesurés restent visibles. |
| Mes pistes réutilisable | Sélection en session d'onglet sous une clé MaCarrière commune ; export HTML lisible et reprise de sélection validée sur identifiants connus. | Aucune sauvegarde serveur. D08/D10 restent ouverts pour la stratégie de production et l'hébergement commun. |
| Filtres sans étapes | Savoir-faire, mode au moins une/toutes, domaine et conditions sont accessibles ensemble, sans numérotation de parcours. | Les combinaisons sans réponse exacte ne sont pas simulées. |

Les branches détaillées du comparateur conservent les salaires sectoriels, les mobilités dans les deux sens, les composantes2030 et les secteurs d'emploi. Les familles, populations, lieux et périodes restent séparés. Les indications positives de compétences issues de R23 peuvent être affichées ; l'absence dans une réponse partielle ne signifie pas absence du métier.

## Sources et composants

- sources/interface_citoyenne.js : vues de données et événements existants, réutilisés.
- sources/donnees_exploration.js : adaptateurs des réponses et catalogue observé. Les codes restent internes.
- sources/experience_exploration.js : recherche persistante, quatre questions, comparaison libre, lieux et sélection réutilisable.
- sources/construire.py : assemblage autonome ; données supplémentaires issues des JSON existants de certifications et territoires.

Le JSON réel de GET /domaines reste à collecter. La liste locale de domaines vient des domaine_code/libelle des métiers observés. Elle n'est pas une réponse /domaines inventée et aucun nb_metiers n'est reconstruit. L'adaptateur de la réponse arborescente suit le contrat, sans être annoncé validé sur HTTP.

## Continuité avec les autres parcours

L'utilisatrice a explicitement demandé d'avancer sans leurs chemins, qui arriveront plus tard. Aucun faux lien vers « Préparer mon projet » ni écran simulant ce produit n'est créé. Le format de sélection prépare le raccordement : type/version, métiers connus, paire comparée et territoire identifié. Le fichier exporté affiche les noms ; ses identifiants servent à la reprise. Les noms provenant d'un fichier importé ne remplacent pas les libellés de l'API.

Sur le futur site, une origine commune ou une transmission validée sera nécessaire. Le fonctionnement de session d'un fichier local ne prouve pas le partage entre applications déployées. La fermeture de l'onglet, les restrictions du navigateur et le stockage définitif restent des sujets de D08/D10. Le fichier exporté constitue une possibilité de reprise autonome, sans compte ni nouvelle source métier.

## Preuves et recette

Les scénarios réellement exécutés sont dans controles/scripts/verifier_navigateur.js et verifier_exploration.js. Ils couvrent notamment la première page, les trois modes, la sélection effective d'une autre certification, le domaine, la libre comparaison, le maintien des contenus détaillés, un lieu sans chiffres, la reprise de sélection, le rejet d'identifiants inconnus et les réponses asynchrones périmées. Le focus et le lien d'évitement sont également contrôlés dans le navigateur.

Les nombres de contrôles réussis sont ceux des rapports actuels sous controles/resultats. Ces contrôles ne constituent ni un test HTTP des21 GET, ni des tests utilisateurs, ni un audit RGAA. Les composants restent du HTML/CSS inspiré du DSFR ; l'intégration officielle et la recette d'accessibilité de production restent à réaliser. Les notes chiffrées du retour utilisateur ne sont pas des preuves de ces validations.

Les archives avant modification sont sous99_archives/2026-11-02_evolution_ux. Les documents01–10 et la table03 conservent les IDs, les appels et les preuves ; leurs précisions UX sont actualisées en place.
