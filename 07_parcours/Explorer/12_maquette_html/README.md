# Maquette HTML — présentation citoyenne

**[Ouvrir index.html](index.html)** par double-clic dans le navigateur. Le fichier est autonome et peut être copié seul. Il ne nécessite ni installation ni serveur et n'appelle pas l'API.

La version actuelle ouvre la recherche, qui reste accessible depuis les fiches. La première lecture du métier suit quatre questions, avec les contenus détaillés accessibles ensuite. Noms compréhensibles, explication des chiffres, sources, dates, lieux, unités et limites utiles sont conservés. Les 31 fonctionnalités restent la cible du produit ; la maquette ne constitue pas leur intégration complète à l'API.

## Graphiques officiels

La [direction artistique appliquée](../14_direction_artistique/01_AUDIT_ET_INTENTIONS.md) enrichit les quatre questions de la fiche avec des repères directement issus des réponses natives. Les noms des groupes, leurs sources et le lieu réellement mesuré restent visibles. Les SVG commentés et la recette sont dans [le dossier de conception visuelle](../14_direction_artistique/02_GRAMMAIRE_VISUELLE.md). L’exemple HTML fourni sert uniquement d’intention : ses valeurs et sa carte schématique ne sont pas intégrées.

**DSFR Chart 2.1.1 et DSFR 1.15.4 sont intégrés.** Ouvrir « Voir le graphique et son tableau » pour charger une visualisation. Les chiffres restent consultables directement, avec sources, dates, groupes et territoires. Les filtres permettent aussi de comparer deux régions, sans fusionner les indicateurs de salaire et de recrutement.

[Compte rendu d’intégration](../11_INTEGRATION_DSFR_CHART.md) · [Sources partagées et reconstruction](../../commun_datavisualisation/README.md). Les cas sans données, dont certaines cohortes de certification et le second métier du comparateur, ne sont pas remplis artificiellement.

## Consulter

- [Fiche métier](index.html#essentiel), [recherche](index.html#recherche), [savoir-faire et conditions](index.html#guide).
- [Certification et sessions](index.html#certification), [domaine professionnel](index.html#domaine).
- [Comparateur à deux métiers au choix](index.html#comparateur), [Mes pistes](index.html#pistes), [sources](index.html#sources).
- [Capture ordinateur](apercus/apercu-desktop.png) et [capture mobile](apercus/apercu-mobile.png).

## Ce qui fonctionne et ce qui reste à réaliser

Les 22 vues de navigation et les fiches identifiées sont consultables. Les contrôles portent sur les trois modes de recherche, les pistes, les deux modes multicompétences du cas observé, les intentions de certification, les sessions à venir/en cours, la comparaison libre et les parcours professionnels selon sens et âge disponibles.

La recherche porte sur les fiches embarquées, pas sur tout le catalogue serveur. Une combinaison sans réponse JSON correspondante est signalée, sans résultat fabriqué. Le comparateur porte sur les deux métiers choisis ; les détails de marché restent présents et les données manquantes ne sont pas remplies avec celles d'un autre métier. Le lieu se choisit parmi les territoires observés ; un lieu sans chiffres correspondants reste explicitement sans chiffres.

Les pistes sont conservées dans la session d'onglet lorsque le navigateur le permet ; un fichier de sélection lisible peut être enregistré et repris. Le plafond de trois et le stockage de production restent D08. Les deux autres parcours arriveront plus tard, selon l'instruction de l'utilisatrice : aucun faux lien n'est affiché. Le format de sélection prépare leur raccordement, sans démontrer aujourd'hui un partage interapplications déployées. Voir [l'évolution UX et ses limites](documentation/EVOLUTION_STRUCTURE_UX.md).

Les futures intégrations, variantes manquantes et questions RCO restent suivies dans les documents 03, 06 et 10 du dossier parent. Aucune fonctionnalité n'est supprimée parce que la maquette n'en simule pas tous les états.

## Recette UX ciblée

Les dix missions du brief passent en 1280 et 375 px : 69 et 67 assertions réussies, sans échec sur les vérifications exécutées. La reprise de session après de nouveaux chargements complets est confirmée ; Ctrl+R/F5 natif reste NON TESTÉ dans le pilote, de même que le vrai zoom navigateur et l’audit RGAA complet. Voir [le rapport avant/après](../TESTS_UX_EXPLORER.md) et [les travaux restants](../BACKLOG_EXPLORER_RESTANT.md).

Les savoir-faire ne sont plus précochés. Les deux critères proposés proviennent des réponses observées ; une sélection unitaire ouvre ses liens métier documentés, une sélection double utilise les réponses multicritères. Une combinaison non couverte est explicitement signalée.

## Sources, rédaction et maintenance

| Dossier ou fichier | Rôle |
|---|---|
| sources/interface_citoyenne.js | Écrans, interactions et textes actuels. |
| sources/ameliorations_ux.js et .css | États des pistes, guide explicite, titres et polissage mesuré. |
| sources/experience_exploration.js | Recherche persistante, quatre questions, sélection et comparaison. |
| sources/infographie_explorer.js | Adaptation visuelle des mêmes données et rapprochement des DataBox ; aucun état ou calcul métier ajouté. |
| sources/donnees_exploration.js | Adaptateurs des réponses et source locale observée, sans HTTP. |
| sources/modele.html | Enveloppe HTML et styles, sans ancien script concurrent. |
| sources/construire.py | Assemblage du HTML à partir des fichiers locaux. |
| [Règle éditoriale](documentation/REDACTION_CITOYENNE.md) | Noms publics, explications, portée et limites des chiffres. |
| [Preuves des libellés](preuves/PREUVES_LIBELLES.json) | Correspondance des noms affichables avec les champs et fichiers observés. |
| controles/scripts/ | Vérification navigateur, extraction des résultats et lanceur. |
| controles/resultats/ | Rapports actuels et empreinte d'assemblage. |
| controles/traces/ | Captures DOM brutes, conservées comme preuves. |
| archives/ | Textes et adaptation de libellés antérieurs, à titre historique. |

Après modification des composants partagés, exécuter leur [construction Node](../../commun_datavisualisation/README.md), puis reconstruire le HTML avec Python 3 depuis la racine du dossier API :

```powershell
& "$env:LOCALAPPDATA/Programs/Python/Python313/python.exe" -B 07_parcours/Explorer/12_maquette_html/sources/construire.py
```

Relancer les contrôles locaux dans Edge :

```powershell
& ./07_parcours/Explorer/12_maquette_html/controles/scripts/lancer_controles.ps1
```

Les chemins Python et navigateur sont paramétrables dans le lanceur. Le constructeur utilise seulement la bibliothèque standard Python. Les images, le document de contrôle mobile et les traces ne sont pas nécessaires à l'ouverture d'index.html.

## Validation et limites

Dernière recette : **179 contrôles réussis sur ordinateur et 179 à 320 pixels** : navigation, noms publics, absence de mentions internes, sélection réelle des résultats, comparaison, territoire sans transposition de chiffres, reprise de sélection, réponse périmée et focus. Les détails de marché restent contrôlés. [Rapport ordinateur](controles/resultats/CONTROLE_DESKTOP.json) · [Rapport mobile](controles/resultats/CONTROLE_MOBILE.json).

Ces contrôles ne sont pas des tests HTTP de l'API, des tests avec des utilisateurs ni un audit complet RGAA. Le branchement HTTP à l’API et la recette de production restent nécessaires ; les composants DSFR Chart officiels sont désormais intégrés. Les erreurs fournisseur déjà connues et les validations manquantes ne sont pas déclarées résolues.
