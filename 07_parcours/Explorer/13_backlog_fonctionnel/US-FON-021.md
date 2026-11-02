# US-FON-021 — Consulter les sessions de formation publiées à venir

**Rattachement :** E21 · alias historique US-E21. **Lot :** L8.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-017](US-FON-017.md) (E17);[US-FON-009](US-FON-009.md) (E09).

**État constaté au 2 novembre 2026 :** JSON R18 observé pour la certification 112561 et l'Occitanie, avec dix lignes ; ce cas ne prouve pas le rattachement indépendant de chaque groupe. La consultation locale est possible avec ces preuves, la production HTTP et la garantie Q11 restent à valider sur certifications/territoires/pages/modes contrastés.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de consulter les sessions de formation publiées à venir, pour repérer des sessions publiées pour la certification retenue, comprendre leur lieu, leurs dates et leurs modalités avant de poursuivre mon projet. Je veux consulter les sessions publiées à venir pour une certification.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite consulter les sessions de formation publiées à venir, afin de repérer des sessions publiées pour la certification retenue, comprendre leur lieu, leurs dates et leurs modalités avant de poursuivre mon projet.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Une certification et un zonage région/département/CLPE sont choisis. Depuis une commune, le parent est reçu et choisi explicitement.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis une certification choisie, ouvre les sessions à venir. | Conserve son Certif Info et propose les territoires compatibles avec la route, sans appeler les sessions avec un code de métier ou de fiche RNCP. |
| 2 | Choisit une région, un département ou un bassin local pour l'emploi proposé. | Si le point de départ est une commune, fait choisir explicitement un parent reçu de /territoires ; appelle /sessions_a_venir avec certifinfo, zonage, territoire et le mode onisep. |
| 3 | Parcourt les sessions publiées. | Affiche les villes, organismes, dates, modalités et voies réellement reçus ; distingue le nombre de groupes retournés et nb_sessions sans promettre de places. |
| 4 | Ouvre les informations d'une ligne. | Déplie les informations de l'appel courant, avec présentiel, mixte ou distance et les données manquantes signalées, sans créer de fiche session à identifiant stable fictif. |
| 5 | Choisit d'examiner aussi les offres de formation initiale sans session datée. | Utilise le mode onisep choisi et présente séparément les offres marquées tag_onisep avec leur date conventionnelle expliquée. |
| 6 | Change de territoire, passe à la page suivante ou revient à la certification. | Relance le bon appel, garde les choix et annule les réponses périmées ; permet le passage aux sessions en cours sans perte du contexte. |

## 5. Scénarios alternatifs

- Aucune session retournée : indiquer aucun résultat publié pour cet appel et proposer de modifier le territoire ou le mode d'offre, sans conclure qu'aucune formation n'existe.
- Commune ou France sélectionnée dans Explorer : ne pas envoyer ces zonages interdits à la route ; proposer un choix compatible ou expliquer l'absence de parent exploitable.
- Dates ou modalités manquantes : garder les autres informations, montrer ce qui n'est pas renseigné et ne pas fabriquer une date ou une disponibilité.
- Erreur API ou échec d'une page : conserver la certification, le lieu et les résultats déjà lus, afficher l'incomplétude et proposer une reprise ciblée.
- Dates d'une preuve historique devenues anciennes : conserver la date de collecte et signaler le caractère observé des données ; ne pas reclasser cette preuve en disponibilité actuelle démontrée.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Les paramètres certifinfo, zonage et territoire sont requis ; seuls region, departement, clpe sont admis par l'enum officiel. Le code transmis doit correspondre au zonage choisi.
- Les lignes peuvent être regroupées ; nb_sessions n'est ni un nombre de places ni une garantie d'inscription, et total désigne le nombre d'éléments de la liste paginée.
- Aucun ID stable de session ni Certif Info n'est renvoyé par ligne ; ne pas transformer SIRET, organisme ou dates en preuve d'identité ou de rattachement indépendant.
- onisep=exclure est le défaut documenté ; inclure et seulement existent, avec tag_onisep et dates conventionnelles de rentrée à distinguer des sessions datées.
- La fonctionnalité reste complète dans le périmètre ; Q11 suit la garantie du filtre de certification et du regroupement, à valider par requêtes contrastées et réponse fournisseur sans exiger un nouveau GET.

**Règles héritées conservées :** Ligne agrégée et nb_sessions distincts des places ; Onisep à date conventionnelle ; date de collecte connue ; pas d'ID stable inventé.

**Traitements :** `/sessions_a_venir?certifinfo=...&zonage=...&territoire=...&onisep=...&page=...` ; Ligne agrégée et nb_sessions distincts des places ; Onisep à date conventionnelle ; date de collecte connue ; pas d'ID stable inventé.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Ligne agrégée et nb_sessions distincts des places ; Onisep à date conventionnelle ; date de collecte connue ; pas d'ID stable inventé.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** RCO/Onisep selon réponse ; grain session agrégée ; période période courante. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/sessions_a_venir`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `certifinfo` | query | Requis Swagger | `string` | code choisi requis |
| `zonage` | query | Requis Swagger | `string ; valeurs region, departement, clpe` | region/departement/clpe requis |
| `territoire` | query | Requis Swagger | `string` | code requis |
| `onisep` | query | Facultatif Swagger | `string ; valeurs exclure, inclure, seulement ; défaut API "exclure"` | exclure/inclure/seulement, défaut exclure |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].code_insee` | string | Type OpenAPI officiel ; chemin observé |
| `$.items[].date_debut` | string | Type OpenAPI officiel ; chemin observé |
| `$.items[].date_fin` | string | Type OpenAPI officiel ; chemin observé |
| `$.items[].formation_apprentissage` | boolean | Type OpenAPI officiel ; chemin observé |
| `$.items[].formation_continue_conventionnee` | boolean | Type OpenAPI officiel ; chemin observé |
| `$.items[].formation_contrat_pro` | boolean | Type OpenAPI officiel ; chemin observé |
| `$.items[].formation_initiale` | boolean | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_sessions` | integer | Type OpenAPI officiel ; chemin observé |
| `$.items[].presentiel_distantiel` | integer | Type OpenAPI officiel ; chemin observé |
| `$.items[].raison_sociale` | string | Type OpenAPI officiel ; chemin observé |
| `$.items[].siret_formateur` | string | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_onisep` | boolean | Type OpenAPI officiel ; chemin observé |
| `$.items[].ville` | string | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/sessions/response_sessions_a_venir.json](../../../02_reponses_observees/sessions/response_sessions_a_venir.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [06_controles/VALIDATION_R18_certifications_sessions_a_venir.md](../../../06_controles/VALIDATION_R18_certifications_sessions_a_venir.md); [02_reponses_observees/sessions/response_sessions_a_venir.json](../../../02_reponses_observees/sessions/response_sessions_a_venir.json).

**Contrôle local déjà rapporté :** Vue locale sessions à venir ; Q11 ne vaut pas filtre HTTP validé. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E21 : Tests contrastés de certifications et territoires, temporalité, pagination, trois modes Onisep ; confirmation du filtre sans identifiant par ligne.

**Points RCO associés :** Q11 : garantie et traçabilité contractuelle ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-021-CA-01** — **Étant donné** la personne part d'une certification et d'une commune, **Quand** elle ouvre les sessions à venir, **Alors** un choix explicite de territoire parent compatible est proposé et aucun code communal n'est envoyé sous un zonage différent.

**US-FON-021-CA-02** — **Étant donné** un territoire compatible est choisi, **Quand** la requête est lancée, **Alors** certifinfo, zonage, territoire, page et le mode onisep utile appartiennent au contexte courant.

**US-FON-021-CA-03** — **Étant donné** une ligne contient nb_sessions supérieur à un, **Quand** son détail est consulté, **Alors** le nombre publié reste nommé sessions et aucun nombre de places, inscription ouverte ou identifiant stable n'est déduit.

**US-FON-021-CA-04** — **Étant donné** presentiel_distantiel vaut zéro, un ou deux, **Quand** la modalité est affichée, **Alors** la correspondance présentiel, mixte, distanciel est respectée par un libellé compréhensible.

**US-FON-021-CA-05** — **Étant donné** le mode Onisep inclure ou seulement est choisi, **Quand** les résultats sont affichés, **Alors** les offres marquées sont distinguées et leur date conventionnelle n'est pas présentée comme début d'une session réelle.

**US-FON-021-CA-06** — **Étant donné** une réponse ne contient pas le Certif Info par ligne, **Quand** la recette de rattachement est évaluée, **Alors** le test ne prétend pas avoir vérifié isolément chaque ligne et conserve la dépendance Q11 sans retirer la fonctionnalité.

**US-FON-021-CA-07** — **Étant donné** une page échoue après une première page lue, **Quand** la personne reprend sa consultation, **Alors** les lignes acquises restent disponibles et la liste est explicitement incomplète.

**US-FON-021-CA-08** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-021-CA-09** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Liste des sessions à venir avec paramètres tracés, dates et modalités ; filtres contrastés et garantie RCO de rattachement ; aucune place disponible promise ; Tests contrastés de certifications et territoires, temporalité, pagination, trois modes Onisep ; confirmation du filtre sans identifiant par ligne ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E21` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : sélection de territoire compatible, choix du type d'offre, onglets temporels, liste ou tableau des dates/lieux/organismes, dépliage local et pagination ; états chargement, publié, vide, partiel et erreur.
- Les dates et modalités sont écrites en toutes lettres ; les lignes sont accessibles au clavier sans clic unique ambigu, avec état déplié annoncé et version mobile lisible ; aucune action d'inscription ou fiche session fictive.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Sessions à venir ; Sessions publiées à venir, dates, lieu, organisme, modalités ; mode Onisep séparé si consulté ; aucune place/inscription promise ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Noindex listes volatiles. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-021 — scénario, interactions et alternatives](svg/US-FON-021.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-021.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
