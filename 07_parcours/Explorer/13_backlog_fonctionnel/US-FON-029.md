# US-FON-029 — Explorer les métiers concernés par les transitions

**Rattachement :** E29 · alias historique US-E29. **Lot :** L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** catalogue [US-FON-001](US-FON-001.md) (E01)/[US-FON-004](US-FON-004.md) (E04) et [US-FON-005](US-FON-005.md) (E05).

**État constaté au 2 novembre 2026 :** Les tags sont documentés et observés sur des fiches ; la collecte de tout le catalogue et les combinaisons locales restent à valider. Un prototype filtré sur quelques JSON ne démontre pas la couverture exhaustive du catalogue HTTP ; les modalités de combinaison locale ne créent aucun filtre API.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de explorer les métiers concernés par les transitions, pour repérer des métiers signalés comme concernés par les transitions écologique, numérique ou démographique, puis comprendre concrètement leur contenu et leurs perspectives. Je veux explorer les métiers selon les transitions décrites par leurs tags.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite explorer les métiers concernés par les transitions, afin de repérer des métiers signalés comme concernés par les transitions écologique, numérique ou démographique, puis comprendre concrètement leur contenu et leurs perspectives.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis la recherche ou un domaine, choisit découvrir les métiers concernés par une transition. | Présente les trois thèmes disponibles et explique qu'ils reposent sur des marqueurs documentaires du métier, sans prédiction de recrutement. |
| 2 | Choisit un thème et éventuellement un domaine professionnel. | Collecte les pages de /metiers dans ce périmètre et applique localement le marqueur reçu ; n'ajoute aucun paramètre serveur transition. |
| 3 | Consulte les résultats pendant puis après la collecte. | Distingue une liste encore incomplète de la liste complète du périmètre ; conserve les valeurs true, false etnull et annonce le contexte de filtrage. |
| 4 | Ouvre un métier du résultat. | Affiche sa fiche avec le marqueur et ses activités, compétences et données réelles, plutôt qu'un contenu déduit de la seule transition. |
| 5 | Examine ses perspectives ou thèmes de formation. | Propose les volets documentés et conserve leurs populations et limites ; le marqueur ne devient ni un taux de croissance ni une garantie de salaire. |
| 6 | Change de transition, retire le filtre ou garde une piste. | Réutilise le catalogue complet compatible en cache, actualise la lecture locale et préserve les autres sélections. |

## 5. Scénarios alternatifs

- Catalogue partiellement chargé : montrer l'incomplétude et la reprise, sans annoncer un nombre exhaustif ou aucun métier concerné.
- Marqueur null : le garder distinct de false et expliquer une information non renseignée, sans affirmer que le métier n'est pas concerné.
- Aucun résultat après collecte complète du périmètre : indiquer aucun marqueur positif publié dans ce périmètre et proposer de changer de thème ou domaine.
- Plusieurs transitions choisies : afficher explicitement la règle de combinaison locale retenue ; ne pas la présenter comme un mode de recherche serveur documenté.
- Erreur de collecte d'une page : préserver les fiches déjà reçues et empêcher les conclusions d'exhaustivité jusqu'à reprise.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Utiliser les tags métier tag_transition_ecologique, tag_transition_numerique et tag_transition_demographique reçus ; ne pas les confondre avec les tags de certification.
- Le filtrage est local sur toutes les pages du catalogue ou du périmètre de domaine choisi ; aucun paramètre transition, score ou tri de croissance n'existe sur /metiers.
- Un marqueur positif peut venir d'au moins une spécialité consolidée vers le ROME V3 ; il n'affirme pas que toutes les situations de travail du métier ont les mêmes caractéristiques.
- false etnull gardent leur sens distinct ; l'absence de marqueur ne démontre ni absence de contribution réelle à une transition ni absence d'évolution du métier.
- La combinaison éventuelle de thèmes est une interaction locale explicitée et à stabiliser ; les perspectives, salaires et compétences viennent de leurs propres réponses et non du marqueur.

**Règles héritées conservées :** Tags booléens et null distincts ; filtre local sur catalogue complet, pas classement de croissance ni paramètre transition serveur.

**Traitements :** `/metiers?page=...` complet, `tag_transition_*` ; cache détail partagé ; Tags booléens et null distincts ; filtre local sur catalogue complet, pas classement de croissance ni paramètre transition serveur.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Tags booléens et null distincts ; filtre local sur catalogue complet, pas classement de croissance ni paramètre transition serveur.

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

### Appel 2 — GET `/metiers`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 jusqu'à last_page ; pas de filtre transition serveur |
| `domaine` | query | Facultatif Swagger | `string ; défaut API null` | facultatif |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_numerique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_demographique` | boolean ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [06_controles/resultats/R23 test/R23 GET metierscompetence=125416&mode_competence=toutes&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416&mode_competence=toutes&page=1.json>); [06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json>); [06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json>); [06_controles/resultats/R24/R24 GET metiersdomaine=F16&contexte=300782&page=1.json](<../../../06_controles/resultats/R24/R24 GET metiersdomaine=F16&contexte=300782&page=1.json>); [06_controles/resultats/R24/R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json](<../../../06_controles/resultats/R24/R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json>).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/metiers/response_metiers-rome.json](../../../02_reponses_observees/metiers/response_metiers-rome.json); [01_sources/openapi/docs_json_interface.json](../../../01_sources/openapi/docs_json_interface.json).

**Contrôle local déjà rapporté :** Tags du métier et page thématique ; filtrage général de catalogue à compléter. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E29 : Toutes les pages du catalogue ; true/false/null ; résultats locaux incomplets identifiés jusqu'à fin de collecte.

**Points RCO associés :** Q01 : stabilité des tags et référentiel ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-029-CA-01** — **Étant donné** un thème de transition est choisi, **Quand** la recherche de métiers est préparée, **Alors** seuls les GET et paramètres autorisés sont utilisés et aucun paramètre transition fictif n'est transmis.

**US-FON-029-CA-02** — **Étant donné** le catalogue comporte plusieurs pages, **Quand** le filtrage local démarre, **Alors** le résultat reste annoncé incomplet jusqu'à collecte de toutes les pages du périmètre.

**US-FON-029-CA-03** — **Étant donné** des valeurs true, false etnull existent, **Quand** les résultats sont classés par présence du marqueur, **Alors** null n'est pas converti en false et l'absence d'information n'est pas une exclusion métier prétendument certaine.

**US-FON-029-CA-04** — **Étant donné** un métier possède un marqueur écologique positif, **Quand** la personne ouvre sa fiche, **Alors** le marqueur est expliqué sans lui attribuer une croissance, une rémunération ou un recrutement garanti.

**US-FON-029-CA-05** — **Étant donné** plusieurs thèmes sont sélectionnés, **Quand** le filtre local est appliqué, **Alors** sa règle explicite de combinaison est visible et ne prétend pas être une fonctionnalité de filtrage serveur.

**US-FON-029-CA-06** — **Étant donné** un domaine professionnel limite le périmètre, **Quand** la collecte se termine, **Alors** l'exhaustivité annoncée concerne ce domaine et non l'ensemble du catalogue national.

**US-FON-029-CA-07** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-029-CA-08** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Tag présent n’annonce aucune embauche ; Badges et exploration par tags via filtre local explicitement présenté, combinable avec Domaine ; pas de filtre transition serveur fictif ; Toutes les pages du catalogue ; true/false/null ; résultats locaux incomplets identifiés jusqu'à fin de collecte ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E29` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : choix de thèmes, filtre de domaine, badges textuels et résultats de métiers ; texte sur le filtrage local et les limites, états collecte, complet, partiel, vide et erreur.
- Pas de graphique de croissance produit à partir des tags ; commandes sélectionnées annoncées, règle de combinaison lisible, focus stable et résultats accessibles par noms au clavier comme sur mobile.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Exploration des transitions ; Badges et exploration par tags via filtre local explicitement présenté, combinable avec Domaine ; pas de filtre transition serveur fictif ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Filtre éditorial si justifié. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-029 — scénario, interactions et alternatives](svg/US-FON-029.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-029.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
