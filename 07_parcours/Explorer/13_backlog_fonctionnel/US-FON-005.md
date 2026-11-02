# US-FON-005 — Comprendre une fiche métier

**Rattachement :** E05 · alias historique US-E05. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-001](US-FON-001.md) (E01)/[US-FON-004](US-FON-004.md) (E04)/[US-FON-019](US-FON-019.md) (E19)/[US-FON-007](US-FON-007.md) (E07) selon entrée.

**État constaté au 2 novembre 2026 :** F1610 et fiches connues consultables ; contenus supplémentaires et 404 HTTP à tester.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comprendre une fiche métier, pour comprendre le travail avant d’examiner mes possibilités. Je veux comprendre ce que recouvre un métier.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comprendre une fiche métier, afin de comprendre le travail avant d’examiner mes possibilités.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre un métier depuis une recherche ou un lien | Valide le code et charge ou réutilise /metiers/{rome}. |
| 2 | Lit la présentation | Affiche définitions, appellations et repères reçus avec leur source. |
| 3 | Choisit une question sur travail, emploi, salaire ou autres pistes | Ouvre le volet sans imposer de tunnel ni supprimer les approfondissements. |
| 4 | Garde, compare ou consulte les conditions | Utilise l’identité de cette fiche et montre l’état de l’action. |
| 5 | Revient à la recherche ou à une autre fiche | Conserve mode, saisie pertinente, territoire et pistes. |

## 5. Scénarios alternatifs

- Identifiant inconnu ou 404 : message et retour à la recherche.
- Champ absent : ne pas rédiger une activité ou reprendre un autre métier.
- Fiche partielle : garder ses informations disponibles avec leurs limites.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Nom métier public, ROME V3 interne ; aucun code métier ROME 4.0 restitué.
- Exploiter definitions[] ; ne pas inventer de champ activites.
- Un tag réglementé, cadre ou transition ne garantit ni accès ni emploi.

**Règles héritées conservées :** Définitions[] et libellés reçus ; pas de champ activites, aucun texte métier fabriqué.

**Traitements :** `/metiers/{rome}` ; Définitions[] et libellés reçus ; pas de champ activites, aucun texte métier fabriqué.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Définitions[] et libellés reçus ; pas de champ activites, aucun texte métier fabriqué.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3 ; grain ROME V3 ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/metiers/{rome}`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | path | Requis Swagger | `string` | chemin code ROME V3 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.grand_domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.grand_domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.appellations` | array | Type OpenAPI officiel ; chemin observé |
| `$.definitions` | array | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_numerique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_demographique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_emploi_reglemente` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_emploi_cadre` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.metiers_proches_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.metiers_proches_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.savoir_etre_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.contexte_travail_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.contexte_travail_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.fap228_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.formacode_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.formacode_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/metiers/response_metiers-rome.json](../../../02_reponses_observees/metiers/response_metiers-rome.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/metiers/response_metiers-rome.json](../../../02_reponses_observees/metiers/response_metiers-rome.json).

**Contrôle local déjà rapporté :** Missions 002/003/005 ; quatre questions et actions de fiche. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E05 : Deux fiches supplémentaires et 404 ; rendre listes/valeurs absentes sans texte généré.

**Points RCO associés :** Q01 : stabilité/version du référentiel ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-005-CA-01** — **Étant donné** un métier choisi, **Quand** la fiche s’ouvre, **Alors** nom, contenu et actions concernent le même identifiant.

**US-FON-005-CA-02** — **Étant donné** une définition absente, **Quand** je lis la fiche, **Alors** aucun texte métier inventé ne la remplace.

**US-FON-005-CA-03** — **Étant donné** une action Garder ou Comparer, **Quand** je l’active, **Alors** le métier courant est utilisé, pas un métier fixé en dur.

**US-FON-005-CA-04** — **Étant donné** les quatre questions principales, **Quand** j’en ouvre une, **Alors** mobilités, prospective, certifications et autres volets restent accessibles.

**US-FON-005-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-005-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** N’affiche pas de valeur si absente; nom métier visible ; identifiant ROME V3 interne ; Définitions, appellations, domaine, savoir-être et contextes référencés ; actions vers tous les volets détaillés ; Deux fiches supplémentaires et 404 ; rendre listes/valeurs absentes sans texte généré ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E05` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : titre, cartes de questions, détails, tags justifiés et actions hiérarchisées.
- Un seul bouton principal dans le groupe ; état gardé, retrait et retour explicites.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Fiche métier ; Définitions, appellations, domaine, savoir-être et contextes référencés ; actions vers tous les volets détaillés ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Première lecture par quatre questions ; mobilités, prospective2030, formations et conditions détaillées restent accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Titre et résumé depuis API. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-005 — scénario, interactions et alternatives](svg/US-FON-005.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-005.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
