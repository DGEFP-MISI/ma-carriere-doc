# Prompt Codex — Vérification d’intégration et réutilisation de DSFR Chart

Tu travailles dans le dépôt MaCarrière. Avant toute modification, lis dans l'ordre :
1. Les 8 fichiers `07_parcours/00_REFERENTIEL_COMMUN_DATAVISUALISATION/`.
2. `API_DGEFP_RCO_REFERENCE_V3_PROPRE.zip` : contrat officiel, OpenAPI, `routes_openapi.csv`, échantillons `02_reponses_observees`, `champs_observes_tous_endpoints.csv`, relations, matrices et contrôles R16–R24.
3. `07_parcours/Explorer/` et `07_parcours/Faire_evoluer_ma_situation/` ; vérifier ce qui existe effectivement dans le code.
4. Documentation DSFR Chart correspondant à la version installée : https://github.com/GouvernementFR/dsfr-chart et https://gouvernementfr.github.io/dsfr-chart/ .

## Phase A — Vérification ciblée de compatibilité, sans coder
- Inspecte la stack, les composants existants, le DSFR, les packages, l’accès API et les contraintes SSR/hydratation. Réutilise les composants officiels DSFR Chart et leurs mécanismes d’accessibilité : **pas d’audit général de conformité de la bibliothèque depuis zéro**.
- Confirme les balises/options et la licence du package installé ; vérifie seulement les points de compatibilité utilisés dans MaCarrière (carte, DataBox, tableau alternatif, événements et intégration DSFR).
- Reproduis les chemins JSON précis pour les lignes CSV; les lignes notées `CHAMPS_PARTIELS_A_TESTER` requièrent contrôle contrat et test.
- Contrôle le transcodage INSEE↔codes cartes. Aucune valeur mock affichée comme donnée métier réelle.
- Distingue les données par FAP225/FAP228/FAP87 et les millésimes; vérifie `maille_reelle`, `secret_stat`, `null`.
- Livrer AUDIT_DSFR_CHART.md, PLAN_ADAPTATEURS.md, MATRICE_ECARTS.md et TESTS_A_EXECUTER.md, avec décisions à faire valider.

## Phase B — Sur validation de l'équipe uniquement
- Créer adaptateurs typés par endpoint; wrappers DataBox, tableau et métadonnées communs.
- Construire d'abord barres et chiffres, puis carte seulement après mapping validé.
- Réutiliser les mêmes composants dans Explorer, Faire évoluer, comparateur et Mes pistes.
- Ne changer aucun contrat API, aucune source ni aucun champ sans preuve. Ne pas réécrire les documents existants silencieusement.
- Écrire les tests unitaires des adaptateurs, territoires, secret statistique, null et unités ; tester l’intégration applicative des composants officiels (libellés, alternatives, navigation clavier dans le contexte MaCarrière, mobile, performances et non-régression). Ne pas réauditer les composants DSFR Chart isolément ni les réimplémenter.

## Principe de réutilisation obligatoire
- Installer ou réutiliser la version officielle de `@gouvfr/dsfr-chart` compatible avec la stack et le DSFR déjà utilisé.
- Ne pas refaire les moteurs graphiques, les interactions et les fonctionnalités d’accessibilité déjà fournies.
- Prioriser les composants documentés ; tout développement graphique spécifique est une **exception à justifier et à faire valider**.
- Contrôler l’accessibilité de **l’assemblage MaCarrière** (titres, descriptions, valeurs alternatives, événements, filtres, messages dynamiques), sans prétendre qu’une bibliothèque officielle dispense de cette vérification.

## Sortie attendue
Rapport des éléments confirmés, documentés, à tester et non couverts, estimation par lots, risques, référentiel des composants testés, puis attente de validation explicite avant intégration de production. La documentation n'autorise pas à développer immédiatement.
