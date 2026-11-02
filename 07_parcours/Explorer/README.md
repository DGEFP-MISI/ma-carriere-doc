# Explorer — guide du dossier

**État au 2 novembre 2026.** Les 31 fonctionnalités E01–E31 sont conservées. Le cadrage L0 est terminé ; une maquette HTML permet de parcourir la présentation citoyenne. L’application de production connectée à l’API reste à réaliser dans son dépôt d’accueil.

## Pour consulter le parcours

**[Ouvrir la maquette HTML](12_maquette_html/index.html)** — un double-clic suffit, sans installation. Les écrans utilisent des noms compréhensibles, expliquent les chiffres et conservent les sources. Les données embarquées sont des observations du dossier ; la maquette ne fait aucun appel à l’API.

L'ouverture mène à la recherche, conservée sur les fiches. Quatre questions structurent la première lecture du métier ; les rubriques approfondies restent accessibles. La comparaison porte sur deux métiers au choix, le lieu se sélectionne dans les territoires observés et les pistes peuvent être reprises. Les autres parcours seront reliés plus tard. [Évolution UX appliquée](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md).

[Guide de la maquette et limites](12_maquette_html/README.md) · [Règle de rédaction citoyenne](12_maquette_html/documentation/REDACTION_CITOYENNE.md) · [Aperçu ordinateur](12_maquette_html/apercus/apercu-desktop.png) · [Aperçu mobile](12_maquette_html/apercus/apercu-mobile.png).

## Visualisations intégrées

Les composants officiels **DSFR Chart 2.1.1** sont intégrés dans la page existante, avec sources, périodes, graphiques à la demande et alternatives tabulaires. Les salaires, recrutements, cartes, mobilités, projections et résultats après formation exploitent les JSON observés. [Compte rendu et dépendances](11_INTEGRATION_DSFR_CHART.md) · [Composants partagés](../commun_datavisualisation/README.md).

## Améliorations UX appliquées

Le [chantier de langage visuel](14_direction_artistique/01_AUDIT_ET_INTENTIONS.md) applique le brief artistique à l’Explorer existant : [maquettes SVG](14_direction_artistique/02_GRAMMAIRE_VISUELLE.md), repères natifs dans les quatre questions, icônes officielles et DataBox rapprochées des informations concernées. Le [catalogue des composants](14_direction_artistique/03_COMPOSANTS_ET_INTEGRATION.md) et la matrice des 31 fonctions relient la présentation aux US, données et contrôles. Les parcours, données et règles restent ceux du dossier.

Les modes de recherche sont annoncés, les pistes gardées se retirent directement, le comparateur expose A/B et les retours aux fiches, et les savoir-faire se choisissent explicitement avec un compteur. Les dix missions passent à 1280 et 375 px ; le [rapport de recette](TESTS_UX_EXPLORER.md) distingue les tests réussis et les points NON TESTÉS. Le [backlog restant](BACKLOG_EXPLORER_RESTANT.md) conserve les dépendances, sans réduction du périmètre.

## Pour préparer la réalisation

| Fichier | Utilisation |
|---|---|
| [01 — Fonctionnel](01_EXPLORER_V2_FONCTIONNEL.md) | Besoins, parcours et règle de présentation citoyenne. |
| [02 — Spécifications API](02_SPECIFICATIONS_API.md) | 21 GET, paramètres, champs, 29 mesures et précautions statistiques. |
| [03 — Table de conception](03_TABLE_CONCEPTION.csv) | Table commune : 31 lignes, pilotage, appels, preuves, critères et lots. |
| [04 — Backlog fonctionnel](04_BACKLOG_USER_STORIES.md) | 31 fonctionnalités, 4 US transversales, scénarios nominaux, critères vérifiables et 35 schémas SVG. |
| [05 — Diagrammes](05_PARCOURS_DIAGRAMMES.md) | Navigation et chaînes fonctionnelles documentées. |
| [06 — Décisions et validations](06_DECISIONS_ET_POINTS_A_VALIDER.md) | Décisions actées, tests manquants et triage Q01–Q14. |
| [07 — Prompt de réalisation](07_PROMPT_CODEX.md) | Instructions pour la future application, après autorisation. |
| [08 — Audit](08_AUDIT_TECHNIQUE_CODEX.md) | Diagnostic API et preuves, avec contexte historique explicite. |
| [09 — Plan](09_PLAN_DE_REALISATION.md) | Lots techniques et dépendances de toute la cible. |
| [10 — Arbitrages](10_DECISIONS_A_ARBITRER.md) | Modalités restant à valider ; périmètre et ligne citoyenne déjà actés. |

Les noms du projet, codes et référentiels ont leur place dans ces documents techniques, pas dans les écrans destinés aux citoyens. Les appels et leurs identifiants restent indispensables aux traitements.

Le [backlog fonctionnel complet](04_BACKLOG_USER_STORIES.md) applique le [modèle commun MaCarrière](../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md). Les matrices relient les 35 US aux 29 mesures, aux 25 visualisations et aux 21 GET ; les critères disposent d’identifiants et d’un export CSV pour préparer la recette. Les [contrôles de complétude et d’intégrité](13_backlog_fonctionnel/CONTROLE_COMPLETUDE.md) portent sur les documents, sans nouvelle validation HTTP ni modification de l’application.

## Organisation

```text
Explorer/
├── README.md                    point d’entrée
├── 01…10                        livrables de travail, noms conservés
├── 11_ux_ui/                    conception, matrice et état Figma
│   └── archives/                premières maquettes, à titre historique
├── 12_maquette_html/
│   ├── index.html               présentation actuelle à ouvrir
│   ├── README.md                utilisation et maintenance
│   ├── sources/                 interface, gabarit et constructeur
│   ├── documentation/           règle éditoriale citoyenne
│   ├── apercus/                 captures de la version actuelle
│   ├── preuves/                 provenance des noms affichables
│   ├── controles/               scripts, résultats et traces
│   └── archives/                anciens textes et script initial
├── 13_backlog_fonctionnel/      35 US détaillées, SVG et matrices de traçabilité
├── 14_direction_artistique/     audit, maquettes, composants intégrés et recette visuelle
└── 99_archives/                 inventaire et journal du rangement
```

## État des preuves et points ouverts

- Contrat, JSON observé, validation HTTP ciblée et contrôle local restent des preuves distinctes.
- 179 contrôles locaux de la maquette ont réussi sur ordinateur et à 320 pixels ; ils ne valent pas un test HTTP, un test utilisateur ou un audit RGAA.
- Le fichier Figma contient17vues desktop initiales ; le quota du siège a interrompu sa finalisation. Il n’est pas aligné sur toute la rédaction citoyenne actuelle. La maquette HTML est la référence de présentation ; les documents01–10 portent la cible fonctionnelle complète.
- Les questions réellement ouvertes auprès du RCO restent Q01, Q06, Q07, Q11 et Q14 ; Q05 est conditionnelle. Le filtre secteur/métier R17 reste à résoudre. Les tests manquants ne retirent aucune fonctionnalité.
- Aucune donnée, calcul, source externe, table SQL ou relation API supplémentaire n’est introduit.

Les sources de référence hors Explorer sont conservées : contrat/OpenAPI, JSON, UML et matrice API. L’historique des mouvements et les empreintes sont dans [le journal de rangement](99_archives/2026-11-02_nettoyage/README.md). Les anciens visuels ne sont pas des versions concurrentes à utiliser pour le produit.
