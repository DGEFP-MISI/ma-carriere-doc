# US-FON-006 — Consulter les compétences et conditions du métier

**Rattachement :** E06 · alias historique US-E06. **Lot :** L2/L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05).

**État constaté au 2 novembre 2026 :** Page 1 observée et lecture locale testée ; page 2, catégories et seconde fiche complète à collecter.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de consulter les compétences et conditions du métier, pour comprendre les exigences sans les confondre avec mon niveau. Je veux consulter toutes les catégories de compétences et les contextes référencés.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite consulter les compétences et conditions du métier, afin de comprendre les exigences sans les confondre avec mon niveau.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- La pagination et la catégorie de la liste de compétences sont connues ; une page isolée n’est pas exhaustive.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre Savoir-faire et conditions | Montre catégories et couverture de la liste. |
| 2 | Choisit catégorie ou cœur de métier | Demande /metiers/{rome}/competences avec les filtres admis. |
| 3 | Parcourt la hiérarchie | Affiche les noms, macro-compétences, enjeux et domaines reçus. |
| 4 | Demande les pages suivantes | Suit page et last_page et distingue liste partielle et complète. |
| 5 | Explore ou compare à partir d’un élément | Transmet son code documenté sans maîtrise personnelle déduite. |

## 5. Scénarios alternatifs

- Page manquante : liste incomplète, jamais compétence absente.
- tag_coeur_metier null : non renseigné, pas faux.
- Hiérarchie manquante : liste simple sans parent inventé.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Page manquante = liste incomplète, jamais compétence absente. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Les quatre catégories restent distinctes : savoir_faire, savoir, savoir_etre, contexte_travail.
- coeur_metier est utilisé seulement dans son périmètre contractuel.
- tx_fiches_rome4 décrit les spécialités consolidées au V3, pas la maîtrise.
- Aucune compétence spécifique ou absente conclue sur une page partielle.

**Règles héritées conservées :** tx_fiches_rome4 décrit la part des spécialités V3, pas la maîtrise ; cœur nullable ; listes complètes pour comparaison.

**Traitements :** `/metiers/{rome}/competences?categorie=...&page=...`, complément `coeur_metier=true` ; tx_fiches_rome4 décrit la part des spécialités V3, pas la maîtrise ; cœur nullable ; listes complètes pour comparaison.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. tx_fiches_rome4 décrit la part des spécialités V3, pas la maîtrise ; cœur nullable ; listes complètes pour comparaison.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3 et OGR ; grain ROME V3 parent ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/metiers/{rome}/competences`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | path | Requis Swagger | `string` | chemin V3 |
| `categorie` | query | Facultatif Swagger | `string ; valeurs savoir_faire, savoir, savoir_etre, contexte_travail ; défaut API null` | savoir_faire/savoir/savoir_etre/contexte_travail ou omis |
| `coeur_metier` | query | Facultatif Swagger | `boolean ; défaut API null` | booléen facultatif pour savoir-faire/savoirs |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1, jusqu'à last_page |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].categorie_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].categorie_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_coeur_metier` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].macro_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].macro_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].enjeu_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].enjeu_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_fiches_rome4` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_fiches_rome4_metier` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tx_fiches_rome4` | number ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acquise` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_meme_macro_competence` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.rome_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | integer | Type OpenAPI officiel ; chemin observé |
| `$.page` | integer | Type OpenAPI officiel ; chemin observé |
| `$.last_page` | integer | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/metiers/response_metiers{rome}competences.json](../../../02_reponses_observees/metiers/response_metiers{rome}competences.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/metiers/response_metiers{rome}competences.json](../../../02_reponses_observees/metiers/response_metiers{rome}competences.json).

**Contrôle local déjà rapporté :** Missions 003/009 ; page 1 observée, pas validation d’exhaustivité. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E06 : Collecter page 2 F1610 et une seconde fiche complète ; tester chaque catégorie et cœur, `tag_coeur_metier=null`.

**Points RCO associés :** Q04 : exhaustivité et portée des tags ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-006-CA-01** — **Étant donné** F1610 page 1, 100 sur 144 éléments, **Quand** je consulte la liste, **Alors** l’incomplétude est affichée jusqu’aux pages nécessaires.

**US-FON-006-CA-02** — **Étant donné** un tag cœur null, **Quand** je le lis, **Alors** il n’est ni true ni false.

**US-FON-006-CA-03** — **Étant donné** une compétence du métier, **Quand** je la consulte, **Alors** elle n’est pas attribuée à la personne comme acquise.

**US-FON-006-CA-04** — **Étant donné** une nouvelle catégorie, **Quand** je la sélectionne, **Alors** requête et éléments suivent la catégorie choisie.

**US-FON-006-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-006-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Garder codes OGR et ne jamais exposer ROME4 ; Catégories, hiérarchie macro/enjeu/domaine quand reçue, part des spécialités et cœur de métier ; pas de compétence personnelle inférée ; Collecter page 2 F1610 et une seconde fiche complète ; tester chaque catégorie et cœur, `tag_coeur_metier=null` ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E06` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : filtres, listes/accordéons, tags factuels et pagination.
- Pas de jauge personnelle ; hiérarchie et textes utilisables au clavier.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Compétences et contextes complets ; Catégories, hiérarchie macro/enjeu/domaine quand reçue, part des spécialités et cœur de métier ; pas de compétence personnelle inférée ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Contenus seulement présents API. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-006 — scénario, interactions et alternatives](svg/US-FON-006.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-006.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
