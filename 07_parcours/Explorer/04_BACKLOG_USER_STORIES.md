# Backlog fonctionnel — Explorer

Les **31 fonctionnalités E01 à E31 sont conservées**. Ce fichier est le point d’entrée du backlog fonctionnel : une US détaillée et un schéma SVG par fonctionnalité, complétés par quatre US transversales nécessaires à leur recette. Les 35 US appliquent les dix rubriques du modèle demandé.

**Référentiel au 2 novembre 2026.** Les scénarios décrivent la cible de réalisation. Les états constatés distinguent ce qui est documenté, observé dans un JSON, contrôlé localement et encore à tester. Aucune US n’est déclarée livrée ou validée en HTTP sur la seule base de ce backlog.

[Modèle commun MaCarrière](../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md) · [Table de conception et pilotage](03_TABLE_CONCEPTION.csv) · [Plan de réalisation](09_PLAN_DE_REALISATION.md) · [Décisions à arbitrer](10_DECISIONS_A_ARBITRER.md)

## Utiliser le backlog

Chaque lien ouvre l’US complète : objectif, User Story, préconditions, scénario nominal en tableau, alternatives, règles, API et preuves, critères Étant donné / Quand / Alors, composants accessibles et schéma SVG. Les anciens identifiants `US-E01` à `US-E31` restent des alias ; les IDs E et T-E sont conservés.

Pour alimenter un outil de développement, importer la matrice des US, puis reprendre le Markdown complet comme description et ses critères `US-FON-NNN-CA-NN` comme cas de recette. Les lots sont des dépendances de réalisation, sans retrait ni report de périmètre. Les sous-scénarios de mesures restent dans leur US propriétaire et peuvent être découpés en tâches techniques sans les perdre.

Les US transversales 032–035 s’appliquent à chaque US métier. Une fiche ne peut pas être déclarée terminée si ses données sont correctes mais que la navigation, le langage, les états d’erreur ou les alternatives accessibles ne le sont pas.

## Les 31 fonctionnalités décidées

| ID conception / alias | US fonctionnelle | Lot | Mesures / visualisations |
|---|---|---|---|
| <a id="us-e01"></a>E01 · US-E01 | [US-FON-001 — Rechercher un métier par son nom](13_backlog_fonctionnel/US-FON-001.md) | L2 | 0 mesures propriétaires ;  |
| <a id="us-e02"></a>E02 · US-E02 | [US-FON-002 — Rechercher un diplôme ou un titre](13_backlog_fonctionnel/US-FON-002.md) | L2 | 0 mesures propriétaires ;  |
| <a id="us-e03"></a>E03 · US-E03 | [US-FON-003 — Découvrir un domaine professionnel](13_backlog_fonctionnel/US-FON-003.md) | L2 | 0 mesures propriétaires ; V17 |
| <a id="us-e04"></a>E04 · US-E04 | [US-FON-004 — Explorer les métiers d’un domaine](13_backlog_fonctionnel/US-FON-004.md) | L2 | 0 mesures propriétaires ; V17, V19 |
| <a id="us-e05"></a>E05 · US-E05 | [US-FON-005 — Comprendre une fiche métier](13_backlog_fonctionnel/US-FON-005.md) | L2 | 0 mesures propriétaires ;  |
| <a id="us-e06"></a>E06 · US-E06 | [US-FON-006 — Consulter les compétences et conditions du métier](13_backlog_fonctionnel/US-FON-006.md) | L2/L3 | 0 mesures propriétaires ; V18 |
| <a id="us-e07"></a>E07 · US-E07 | [US-FON-007 — Découvrir des métiers proches](13_backlog_fonctionnel/US-FON-007.md) | L2 | 0 mesures propriétaires ; V18 |
| <a id="us-e08"></a>E08 · US-E08 | [US-FON-008 — Lire tous les repères d’emploi et de formation du métier](13_backlog_fonctionnel/US-FON-008.md) | L4 | 13 mesures propriétaires ; V02, V05, V09, V11 |
| <a id="us-e09"></a>E09 · US-E09 | [US-FON-009 — Choisir le lieu de mon exploration](13_backlog_fonctionnel/US-FON-009.md) | L2 | 0 mesures propriétaires ; V01, V04, V06, V21, V24 |
| <a id="us-e10"></a>E10 · US-E10 | [US-FON-010 — Comparer les intentions de recrutement selon les lieux](13_backlog_fonctionnel/US-FON-010.md) | L4 | 0 mesures propriétaires ; V04, V05, V06, V22 |
| <a id="us-e11"></a>E11 · US-E11 | [US-FON-011 — Situer les salaires et leur dispersion](13_backlog_fonctionnel/US-FON-011.md) | L4 | 0 mesures propriétaires ; V01, V02, V06, V22 |
| <a id="us-e12"></a>E12 · US-E12 | [US-FON-012 — Comprendre si des chiffres peuvent être comparés](13_backlog_fonctionnel/US-FON-012.md) | L4 | 0 mesures propriétaires ; V01, V06, V13, V22, V25 |
| <a id="us-e13"></a>E13 · US-E13 | [US-FON-013 — Choisir des compétences à retrouver dans un métier](13_backlog_fonctionnel/US-FON-013.md) | L3 | 0 mesures propriétaires ;  |
| <a id="us-e14"></a>E14 · US-E14 | [US-FON-014 — Trouver les métiers liés à plusieurs compétences](13_backlog_fonctionnel/US-FON-014.md) | L3 | 0 mesures propriétaires ;  |
| <a id="us-e15"></a>E15 · US-E15 | [US-FON-015 — Choisir des conditions de travail](13_backlog_fonctionnel/US-FON-015.md) | L3 | 0 mesures propriétaires ; V19 |
| <a id="us-e16"></a>E16 · US-E16 | [US-FON-016 — Chercher avec ou sans les conditions choisies](13_backlog_fonctionnel/US-FON-016.md) | L3 | 0 mesures propriétaires ; V19 |
| <a id="us-e17"></a>E17 · US-E17 | [US-FON-017 — Comprendre une certification et ses résultats](13_backlog_fonctionnel/US-FON-017.md) | L2 | 11 mesures propriétaires ; V12, V13, V14, V15, V23 |
| <a id="us-e18"></a>E18 · US-E18 | [US-FON-018 — Comprendre les blocs et retrouver une certification par ses compétences publiées](13_backlog_fonctionnel/US-FON-018.md) | L2/L3 | 0 mesures propriétaires ; V16 |
| <a id="us-e19"></a>E19 · US-E19 | [US-FON-019 — Découvrir les métiers associés à une certification](13_backlog_fonctionnel/US-FON-019.md) | L2 | 0 mesures propriétaires ;  |
| <a id="us-e20"></a>E20 · US-E20 | [US-FON-020 — Explorer les certifications associées à un métier](13_backlog_fonctionnel/US-FON-020.md) | L2/L3 | 0 mesures propriétaires ; V15 |
| <a id="us-e21"></a>E21 · US-E21 | [US-FON-021 — Consulter les sessions de formation publiées à venir](13_backlog_fonctionnel/US-FON-021.md) | L8 | 0 mesures propriétaires ;  |
| <a id="us-e22"></a>E22 · US-E22 | [US-FON-022 — Consulter les sessions de formation publiées en cours](13_backlog_fonctionnel/US-FON-022.md) | L8 | 0 mesures propriétaires ;  |
| <a id="us-e23"></a>E23 · US-E23 | [US-FON-023 — Comprendre les changements de situation professionnelle observés](13_backlog_fonctionnel/US-FON-023.md) | L5 | 2 mesures propriétaires ; V07, V08 |
| <a id="us-e24"></a>E24 · US-E24 | [US-FON-024 — Explorer les perspectives d'emploi à 2030](13_backlog_fonctionnel/US-FON-024.md) | L6 | 0 mesures propriétaires ; V09, V10, V21 |
| <a id="us-e25"></a>E25 · US-E25 | [US-FON-025 — Comparer les salaires selon le secteur économique](13_backlog_fonctionnel/US-FON-025.md) | L7 | 1 mesures propriétaires ; V02, V03, V11 |
| <a id="us-e26"></a>E26 · US-E26 | [US-FON-026 — Comprendre les secteurs employeurs et l'économie du territoire](13_backlog_fonctionnel/US-FON-026.md) | L7 | 2 mesures propriétaires ; V11 |
| <a id="us-e27"></a>E27 · US-E27 | [US-FON-027 — Conserver et reprendre jusqu'à trois pistes de métiers](13_backlog_fonctionnel/US-FON-027.md) | L9 | 0 mesures propriétaires ;  |
| <a id="us-e28"></a>E28 · US-E28 | [US-FON-028 — Comparer les différences utiles entre deux métiers choisis](13_backlog_fonctionnel/US-FON-028.md) | L9 | 0 mesures propriétaires ; V18, V20, V22 |
| <a id="us-e29"></a>E29 · US-E29 | [US-FON-029 — Explorer les métiers concernés par les transitions](13_backlog_fonctionnel/US-FON-029.md) | L3 | 0 mesures propriétaires ;  |
| <a id="us-e30"></a>E30 · US-E30 | [US-FON-030 — Passer d'un thème de formation aux certifications puis aux sessions](13_backlog_fonctionnel/US-FON-030.md) | L3 | 0 mesures propriétaires ;  |
| <a id="us-e31"></a>E31 · US-E31 | [US-FON-031 — Comprendre les chiffres, leurs sources et leurs limites](13_backlog_fonctionnel/US-FON-031.md) | L4 | 0 mesures propriétaires ; V25 |

## Exigences transversales

| US | Objet | Application |
|---|---|---|
| [US-FON-032](13_backlog_fonctionnel/US-FON-032.md) | Retrouver ses choix pendant l’exploration | E01, E02, E03, E04, E05, E09, E17, E19, E27, E28, E30 |
| [US-FON-033](13_backlog_fonctionnel/US-FON-033.md) | Explorer au clavier, sur mobile et avec une alternative aux graphiques | E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31 |
| [US-FON-034](13_backlog_fonctionnel/US-FON-034.md) | Comprendre les données et leurs sources sans connaître les référentiels | E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31 |
| [US-FON-035](13_backlog_fonctionnel/US-FON-035.md) | Poursuivre malgré une attente, une donnée manquante ou une erreur | E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31 |

## Contrôler qu’aucun besoin ne disparaît

- [Matrice de couverture des 35 US](13_backlog_fonctionnel/MATRICE_COUVERTURE_US.csv) : rattachements, lots, dépendances, tests et clarifications.
- [Matrice des 29 mesures](13_backlog_fonctionnel/MATRICE_MESURES.csv) : champs, grain, mailles, millésime, unité, population, composant, règles et preuve pour chacune.
- [Matrice des 25 visualisations V01–V25](13_backlog_fonctionnel/MATRICE_VISUALISATIONS.csv) : chacune est reliée à ses US, y compris les deux populations sectorielles distinctes.
- [Matrice des 21 GET](13_backlog_fonctionnel/MATRICE_GET.csv) : couverture et paramètres officiels, sans endpoint ajouté.
- [Matrice des champs JSON et types](13_backlog_fonctionnel/MATRICE_CHAMPS_JSON.csv) : schéma officiel, observation et champs restant à confirmer distingués.
- [Matrice des critères d’acceptation](13_backlog_fonctionnel/MATRICE_CRITERES_ACCEPTATION.csv) : IDs stables et colonnes Étant donné / Quand / Alors, prêtes pour le suivi de recette.
- [Résultat du contrôle documentaire et d’intégrité](13_backlog_fonctionnel/CONTROLE_COMPLETUDE.md).

E08 détaille les 14 mesures territoriales, dont `emploi_secteurs` partagé avec E26 qui en conserve le pilotage. E17 détaille les 11 mesures de certification ; E23 les deux sens des mobilités ; E25 les salaires sectoriels ; E26 les secteurs employeurs et la dynamique économique. E24 approfondit la prospective et ses cinq composantes ; E28 réutilise les indicateurs pour deux métiers avec un contrôle de comparabilité. E12 inclut l’export fidèle des données, qui reste à réaliser lorsque l’action DataBox est désactivée.

## Preuves, tests et dépendances

**Documenté** signifie présent au contrat/Swagger ; **observé** signifie présent dans un JSON identifié ; **testé localement** concerne le comportement du prototype sur ce jeu ; **validé HTTP** nécessite une requête réelle avec paramètres, statut et réponse conservés. La rédaction des US ne crée aucune preuve HTTP nouvelle.

Les priorités de réalisation sont celles des lots L1 à L10. Les disponibilités partielles ou anomalies fournisseur restent attachées aux fonctionnalités incluses. Q01, Q06, Q07, Q11 et Q14 restent les principaux points fournisseur ; Q05 dépend d’une reproduction avec les champs pluriels corrects. Consulter le tri Q01–Q14 de [06](06_DECISIONS_ET_POINTS_A_VALIDER.md) : les autres points commencent par un GET autonome et ne déclenchent pas une demande RCO inutile.

La recette complète reste à réaliser sur HTTP réel, pagination, autres métiers/lieux/cohortes, protection statistique et réponses invalides. Le rechargement natif Ctrl+R/F5, le zoom navigateur 200/400 %, les lecteurs d’écran et la conformité RGAA ne sont pas déclarés validés. Les autres parcours MaCarrière ne sont pas simulés : les pistes sont portables, leur raccordement sera branché lorsque les destinations seront fournies.

Le [suivi des travaux restant dans le prototype](BACKLOG_EXPLORER_RESTANT.md) est un tableau d’exécution partiel, complémentaire à ce backlog fonctionnel exhaustif.

## Maintenance et conservation

Les 31 lignes et les colonnes de pilotage de la table sont conservées, avec liens US/SVG et état local courant. La version précédente de ce fichier et de la table est conservée dans [l’archive avant enrichissement](99_archives/2026-11-02_backlog_fonctionnel/ETAT_AVANT.zip). Contrat, Swagger, JSON natifs, UML et référentiel commun de datavisualisation restent intacts.

Les données de rédaction dans `13_backlog_fonctionnel/donnees/` et le script `outils/construire_backlog.py` permettent de reconstruire les descriptions et matrices. Pour une évolution, mettre à jour ces sources et la table avant régénération, puis contrôler les différences ; ne pas régénérer après une édition manuelle d’US sans la reporter dans les données de rédaction.
