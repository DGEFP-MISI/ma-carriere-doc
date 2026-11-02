# US-FON-009 — Choisir le lieu de mon exploration

**Rattachement :** E09 · alias historique US-E09. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** aucune.

**État constaté au 2 novembre 2026 :** Sélection locale et absence de transposition testées ; filtres, parents et pagination HTTP à compléter.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de choisir le lieu de mon exploration, pour comprendre où les chiffres sont réellement disponibles. Je veux choisir un territoire précis et comprendre ses périmètres disponibles.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite choisir le lieu de mon exploration, afin de comprendre où les chiffres sont réellement disponibles.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Active Changer de lieu | Ouvre un dialogue nommé avec le lieu courant. |
| 2 | Recherche un nom et un type | Interroge /territoires avec les filtres admis et propose des lieux identifiés. |
| 3 | Sélectionne le lieu | Conserve zonage, code et parents documentés. |
| 4 | Valide | Actualise les vues dépendantes ; chaque mesure montre sa maille réelle. |
| 5 | Change encore ou revient au périmètre disponible | Conserve métier et pistes, annonce le changement et restitue le focus. |

## 5. Scénarios alternatifs

- Homonymes : demander une sélection identifiée, pas une chaîne libre.
- Aucun lieu ou choix vide : message associé au champ.
- Chiffre non disponible : garder le choix, expliquer l’absence ou le repli réel.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Pas de géolocalisation automatique requise.
- Les parents d’une commune sont reçus de /territoires, jamais inventés.
- Choisir une commune ne rend pas toutes les statistiques communales.
- Codes des cartes explicitement adaptés ; aucune carte CLPE/communes fabriquée.

**Règles héritées conservées :** Territoire de sélection distinct du territoire effectivement mesuré ; pas de population ou distance inférée.

**Traitements :** `/territoires?q=...&zonage=...&page=...` → code, zonage et parents ; Territoire de sélection distinct du territoire effectivement mesuré ; pas de population ou distance inférée.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Territoire de sélection distinct du territoire effectivement mesuré ; pas de population ou distance inférée.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Référentiel territoires ; grain territoire ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/territoires`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `q` | query | Facultatif Swagger | `string ; défaut API null ; minLength=2 ; maxLength=100` | facultatif 2–100 caractères |
| `zonage` | query | Facultatif Swagger | `string ; valeurs region, departement, clpe, commune ; défaut API null` | region/departement/clpe/commune facultatif |
| `region` | query | Facultatif Swagger | `string ; défaut API null` | filtre parent |
| `departement` | query | Facultatif Swagger | `string ; défaut API null` | filtre parent |
| `clpe` | query | Facultatif Swagger | `string ; défaut API null` | filtre communes CLPE |
| `code` | query | Facultatif Swagger | `string ; défaut API null` | code exact facultatif |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].zonage` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].territoire_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].territoire_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].region_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].region_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].departement_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].departement_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].clpe_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].clpe_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].commune_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_communes` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].zone_emploi_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].zone_emploi_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].epci_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].epci_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].densite_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/territoires/response_clpe.json](../../../02_reponses_observees/territoires/response_clpe.json); [02_reponses_observees/territoires/response_Commune.json](../../../02_reponses_observees/territoires/response_Commune.json); [02_reponses_observees/territoires/response_departement.json](../../../02_reponses_observees/territoires/response_departement.json); [02_reponses_observees/territoires/response_regions.json](../../../02_reponses_observees/territoires/response_regions.json); [06_controles/resultats/R16 test/GET_territoires__zonage_commune__code_34172.json](<../../../06_controles/resultats/R16 test/GET_territoires__zonage_commune__code_34172.json>).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/territoires/response_regions.json](../../../02_reponses_observees/territoires/response_regions.json).

**Contrôle local déjà rapporté :** Mission 008 : sélection et absence de transposition de Montpellier. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E09 : Homonymes, commune/CLPE/Corse/DOM ; absence de parent et incompatibilité de zonage ; pas de recherche code postal.

**Points RCO associés :** Q03/Q06 : référentiel territorial et parents ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-009-CA-01** — **Étant donné** des lieux homonymes, **Quand** je choisis un résultat, **Alors** son identité géographique exacte est conservée.

**US-FON-009-CA-02** — **Étant donné** un lieu sans chiffres correspondants, **Quand** je valide, **Alors** aucun chiffre d’un autre lieu ne lui est attribué.

**US-FON-009-CA-03** — **Étant donné** une sélection invalide, **Quand** je valide, **Alors** un message associé et le focus permettent de corriger.

**US-FON-009-CA-04** — **Étant donné** un repli publié, **Quand** je lis la mesure, **Alors** lieu demandé et lieu réel restent distincts.

**US-FON-009-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-009-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Choix explicite; France sans code si admis ; Choix explicite ; proposer les périmètres autorisés dans chaque volet en nommant le parent ; France pour routes compatibles ; Homonymes, commune/CLPE/Corse/DOM ; absence de parent et incompatibilité de zonage ; pas de recherche code postal ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E09` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : dialogue, champ, type, liste, validation et erreur associée.
- Libellés nom/type lisibles ; focus d’entrée, validation et fermeture utiles.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Sélection territoriale ; Choix explicite ; proposer les périmètres autorisés dans chaque volet en nommant le parent ; France pour routes compatibles ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Choix territorial identifié dans un sélecteur filtrable ; garder le lieu demandé et annoncer le lieu mesuré ; ne pas copier les chiffres de Montpellier.

**SEO / validation conservés :** Proposition à valider D10 : URLs canonisées sans indexation massive. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-009 — scénario, interactions et alternatives](svg/US-FON-009.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-009.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
