# Livraison et recette UX/UI — Explorer V2

**Statut au 2 novembre 2026 :** conception initiale conservée pour les preuves et la structure. Pour la présentation actuelle, consulter [le HTML citoyen](../12_maquette_html/index.html) et [sa règle éditoriale](../12_maquette_html/documentation/REDACTION_CITOYENNE.md). Les visuels initiaux et les constats Figma de ce document ne prouvent pas l'état actuel de l'interface HTML.

## Ouvrir la proposition

**[Figma — Explorer V2](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav)**, compte « Figma », organisation sg.social.gouv.fr. Fichier natif Design,17 vues desktop1440px. Commencer par [F1610 — l'essentiel](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-2354).

Pour le mobile local, ouvrir [le sommaire](archives/conception_initiale/mobile/menu.svg), puis les liens de texte vers chaque vue. Les SVG sont des objets vectoriels éditables ; leur import éventuel dans Figma ne recréera pas les composants DSFR ou les contraintes d'auto-layout natifs. La structure source [ECRANS_STRUCTURE.json](ECRANS_STRUCTURE.json) permet de reconstruire ces mises en page.

| Vue | Desktop Figma | Mobile local |
|---|---|---|
| essentiel | [essentiel — Pose et restauration de couvertures](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-2354) | [essentiel.svg](archives/conception_initiale/mobile/essentiel.svg) |
| competences | [competences — Quelles compétences et conditions de travail ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-2603) | [competences.svg](archives/conception_initiale/mobile/competences.svg) |
| recrutements | [recrutements — Quels recrutements, quelles tensions ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-2795) | [recrutements.svg](archives/conception_initiale/mobile/recrutements.svg) |
| salaires | [salaires — Combien gagne-t-on, selon la famille et le secteur ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-2975) | [salaires.svg](archives/conception_initiale/mobile/salaires.svg) |
| territoires | [territoires — Où explorer les opportunités ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-3145) | [territoires.svg](archives/conception_initiale/mobile/territoires.svg) |
| mobilites | [mobilites — D'où viennent et où vont les personnes ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-3335) | [mobilites.svg](archives/conception_initiale/mobile/mobilites.svg) |
| prospective | [prospective — Quelles perspectives d'ici 2030 ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-3523) | [prospective.svg](archives/conception_initiale/mobile/prospective.svg) |
| secteurs | [secteurs — Dans quels secteurs travaille-t-on ?](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-3714) | [secteurs.svg](archives/conception_initiale/mobile/secteurs.svg) |
| formations | [formations — Se former, se certifier et découvrir d'autres pistes](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=7-3873) | [formations.svg](archives/conception_initiale/mobile/formations.svg) |
| recherche | [recherche — Explorer votre avenir professionnel](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-817) | [recherche.svg](archives/conception_initiale/mobile/recherche.svg) |
| resultats | [resultats — Choisissez un métier identifié](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1024) | [resultats.svg](archives/conception_initiale/mobile/resultats.svg) |
| certification | [certification — Titre professionnel couvreur-zingueur](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1163) | [certification.svg](archives/conception_initiale/mobile/certification.svg) |
| domaine | [domaine — Explorer le Second œuvre](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1370) | [domaine.svg](archives/conception_initiale/mobile/domaine.svg) |
| guide | [guide — Explorer avec des compétences et des conditions](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1497) | [guide.svg](archives/conception_initiale/mobile/guide.svg) |
| resultats-ogr | [resultats-ogr — Des métiers portent les compétences choisies](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1650) | [resultats-ogr.svg](archives/conception_initiale/mobile/resultats-ogr.svg) |
| comparateur | [comparateur — Comparer deux métiers, point par point](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1765) | [comparateur.svg](archives/conception_initiale/mobile/comparateur.svg) |
| pistes | [pistes — Mes pistes, pour poursuivre l'exploration](https://www.figma.com/design/qXuSLKPN4Cm0iannATmsav?node-id=9-1931) | [pistes.svg](archives/conception_initiale/mobile/pistes.svg) |

Compléments : [Formacodes](archives/conception_initiale/mobile/formacodes.svg), [transitions](archives/conception_initiale/mobile/transitions.svg), [sources et états des valeurs](archives/conception_initiale/mobile/sources.svg). Ces compléments couvrent E30, E29 et E31 ; ils n'ajoutent aucun endpoint.

Supports de revue :
- [Architecture des17 vues](archives/conception_initiale/ARCHITECTURE_EXPERIENCE.svg).
- [Planche des29 visualisations](archives/conception_initiale/PLANCHE_VISUALISATIONS.svg).
- [Quinze états et erreurs](archives/conception_initiale/ETATS_ET_ERREURS.svg).
- [Matrice des29 mesures et241 occurrences de champs](MATRICE_VISUALISATIONS.csv).
- [Conception, couvertureE01–E31 et règles d'interaction](CONCEPTION_UX_UI.md).
- [Journal Figma et nœuds](ETAT_FIGMA.json).

## Ce qui est effectivement vérifié

Les9 vues métier ont été inspectées structurellement dans Figma : textes Marianne, instances réutilisées et aucune image aplatissant l'écran. Une capture native de l'essentiel F1610 a été examinée visuellement : hiérarchie, espacement, lisibilité de la navigation et visibilité des périmètres. Ce contrôle a révélé le texte de marque provisoire décrit ci-dessous. Les8 autres écrans ont été créés et leurs dimensions/identifiants retournés ; ils n'ont pas tous fait l'objet d'une inspection visuelle finale.

Le mobile SVG essentiel a été rendu localement avec Arial en repli et examiné pour la géométrie générale ; des aperçus supplémentaires du guide et du comparateur sont conservés dans apercus_controle. Ces images sont des contrôles géométriques produits par controle_apercus.ps1, pas des exports Figma ni des captures navigateur. Les bordures ne sont pas toutes rendues par cet outil simplifié ; les SVG restent la source visuelle.

Les vérifications locales portent sur la couverture31IDs, les29codes du catalogue et leurs champs, les liens SVG internes, la syntaxe XML/JSON, l'absence de raster externe et l'intégrité des175fichiers préexistants. Résultats dans RECETTE_CONCEPTION.json. Elles ne valent ni tests HTTP ni recette d'accessibilité navigateur.

## Blocage Figma et travail restant précis

L'outil a renvoyé : **limite d'appels Figma MCP atteinte pour le siège Collab du plan Enterprise**. L'appel de création mobile a été rejeté avant création. Il ne s'agit pas d'une permission refusée par la revue automatique de sécurité.

En conséquence :
-17frames desktop créées ;0frame mobile Figma créée ;
-181destinations de navigation préparées, **aucune réaction de prototype appliquée** ;
-page responsive et page des passerelles créées mais non remplies ; les planches locales portent leur contenu ;
-composants locaux carte d'indicateur, information et ligne de tableau présents, avec variables sémantiques ;
-ce fichier est une proposition visuelle inspectable, pas un prototype entièrement fonctionnel.

À finaliser lorsque l'accès d'écriture Figma sera de nouveau disponible, dans **le même fichier** :
1. Remplacer le texte hérité « Intitulé Officiel » de la marque d'en-tête par le libellé correct de la République française, en conservant l'asset officiel DSFR ; contrôler le reflow et la version mobile. Ne pas livrer le placeholder.
2. Créer les17vues mobiles et les compléments à partir de la structure locale, avec les composants natifs DSFR et Marianne ; comparer390 et320px. Remplir les pages d'architecture/états ou les renommer pour refléter leur contenu.
3. Câbler les liens préparés d'après ETAT_FIGMA.json. Contrôler les retours, le lieu et les sélections. Les liens dessinés ne constituent pas un prototype cliquable aujourd'hui.
4. Corriger les actions « Thèmes de formation » et « Explorer les thèmes » : elles doivent ouvrir un écran Formacode distinct, pas la fiche DomaineROME. La destination est corrigée dans les SVG/structure locale. Ne pas présenter la certification112561 comme un résultat prouvé d'un filtre Formacode non testé.
5. Remplacer les tableaux de choix du guide par des puces retirables et des contrôles DSFR. Pour chaque contexte, trois choix mutuellement exclusifs. Les tableaux de données restent des tableaux.
6. Détailler les panneaux que les vues initiales représentent par un accès/accordéon : toutes les mesures de la matrice, les variantes régionales de prospective, les horizons d'insertion, les séries d'offres et l'ensemble des rubriques du comparateur. Ne pas masquer leur absence derrière une apparence de prototype fini.
7. Mettre les notes de test/référence et les hypothèses de conception dans les annotations destinées à l'équipe ; garder dans l'interface les explications utiles à l'utilisateur. Définir le libellé Domaine/Secteur selon D02.
8. Intégrer le véritable logo d'attribution RCO ; le texte d'attribution est déjà prévu, aucun logo n'est inventé.
9. Vérifier visuellement chaque frame et état, composants actifs/désactivés/erreur/focus, contrastes, dimensions et débordements ; tester les scénarios au clavier/zoom/lecteur d'écran sur l'interface développée.

## Preuves de données utilisées

Références normatives : contrat_interface_2026-10-19.md, OpenAPI docs_json_interface.json et les paramètres/champs explicités dans02/03. Les modèles enrichis non officiels ne deviennent pas le contrat.

| Objet | Preuve du dossier | Ce que la preuve autorise |
|---|---|---|
| F1610 | 02_reponses_observees/metiers/response_metiers-rome.json | Intitulés, spécialités, définitions, contextes, tags, codes proches et Formacodes reçus. |
| Compétences | 02_reponses_observees/metiers/response_metiers{rome}competences.json | Extrait100/144 ; aucune exhaustivité présumée. |
| F1613 | 06_controles/resultats/R24, réponse sans_contexte300782 | Intitulé/domaine/contextes de la fiche reçue ; pas de liste de compétences ou statistiques inventée. |
| OGR | R23 et R24, comptes rendus et JSON associés | Tests ciblés sur les codes125416/103659 et contexte300782 ; pas toutes les combinaisons futures. |
| Statistiques territoriales | R16 F1610/commune34172 |14mesures, familles et mailles effectives ; aucune validation générale de tous les lieux. |
| Salaires, secteurs, mobilités, prospective | JSON sous02_reponses_observees/indicateurs et comptes rendus08/09 | Valeurs observées, périodes et familles ; filtres complémentaires à tester. |
| Certification112561 / RNCP36101 | JSON certification détail/blocs et listes sous02_reponses_observees/certifications | Textes, voies, populations et résultats reçus. Les absences null restent visibles. |
| Sessions | JSON sessions et R18/R19 | Dates/lieux/modalités des listes ; pas de places ni preuve individuelle de rattachement absente. |
| Contexte économique | R17 sansROME ; emploi_secteurs R16 | Deux lectures distinctes ; l'anomalie du filtreROME demeure ouverte. |
| Catalogue | response_mesures.json |29codes/241occurrences de champs ; pas la présence de toutes les valeurs dans chaque fiche. |

Les nombres représentés sont des données de ces échantillons. Ils ne sont pas annoncés comme actualisés au jour de consultation, ni comme résultats de requêtes exécutées pendant la conception.

## Tests à prévoir avant recette produit

Conserver les tests T-E01–T-E31 des livrables harmonisés ; compléter par :
- navigation complète recherche→métier→certification→sessions→retour, domaine→métier et OGR→résultats ;
- recherches q, catalogue Domaine réel, paginationMC complète et seconde fiche, depuis dans les deux sens ;
- variantes mobilités, âge60+ encodé correctement, région/France, deux sens et situations hors emploi ;
- prospective deux entrées, référenceFrance, familles, négatifs/null, Corse/DOM selon contrat ;
- salaires sectoriels avec région et France, tranches ouvertes, seuils, référenceensemble ;
- comparateur même famille, familles différentes, périodes/mailles différentes et données partielles ;
- sessions avec certifications/territoires contrastés, modesOnisep et les deux routes ;
- erreur partielle, réseau,429/503, zéro/null/secret et annulation de requête périmée ;
- tâches utilisateur décrites dans CONCEPTION_UX_UI.md, puis recette RGAA sur l'implémentation.

Fournisseur : Q01 environnement/divergences documentaires, Q06 secret, Q07 précisionBMO, Q11 traçabilité sessions, Q14 anomalieR17. Les autres questions sont d'abord des tests avec les GET existants ; Q05 n'est fournisseur que si reproduite sur une URL conforme.

## Conditions pour passer au développement

Validation UX des modalités D02–D09, application d'accueil et accès API D10, gestion du jeton/quota, collecte des jeux manquants et prise en charge des anomalies identifiées. Les réponses fournisseur peuvent bloquer la recette de leur comportement précis ; elles ne retirent aucune des31fonctions. Les maquettes demandent encore une passe de finalisation Figma, explicitée ci-dessus, avant d'être présentées comme un prototype complet validé.

Aucun contrat, JSON source, UML de référence ou livrable01–10 n'a été modifié pendant cette conception.

