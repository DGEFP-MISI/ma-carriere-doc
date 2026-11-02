# US-FON-015 — Choisir des conditions de travail

**Rattachement :** E15 · alias historique US-E15. **Lot :** L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-006](US-FON-006.md) (E06) ou recherche catalogue directe.

**État constaté au 2 novembre 2026 :** Choix locaux et R24 disponibles ; catalogue et combinaisons HTTP à compléter.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de choisir des conditions de travail, pour exprimer les contextes à examiner ou à éviter. Je veux choisir des conditions de travail référencées.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite choisir des conditions de travail, afin d’exprimer les contextes à examiner ou à éviter.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les contextes sélectionnés proviennent de la catégorie contexte_travail.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre les conditions du guide | Explique références et absence de garantie poste par poste. |
| 2 | Recherche ou parcourt les contextes | Demande /competences?categorie=contexte_travail. |
| 3 | Choisit une condition | Conserve son nom et son identifiant reçus. |
| 4 | Choisit Je recherche, Je préfère éviter ou Pas de préférence | Actualise le critère distinct d’une compétence. |
| 5 | Lance la recherche | Prépare contexte et sans_contexte pour E16. |

## 5. Scénarios alternatifs

- Référence absente : pas de garantie d’absence de la condition.
- Pas de préférence : aucun filtre pour cette condition.
- Contexte non disponible : ne pas en inventer un.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- contexte_travail n’est pas envoyé en filtre competence.
- Une condition ne peut être simultanément incluse et exclue dans l’interface.
- Aucune adéquation personnelle ou garantie de poste n’est déduite.

**Règles héritées conservées :** Catégorie contexte_travail, arborescence non applicable selon contrat ; pas de préférence libre convertie en OGR.

**Traitements :** `/competences?categorie=contexte_travail&q=...` ou réemploi de la catégorie métier ; Catégorie contexte_travail, arborescence non applicable selon contrat ; pas de préférence libre convertie en OGR.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Catégorie contexte_travail, arborescence non applicable selon contrat ; pas de préférence libre convertie en OGR.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** OGR ; grain contexte ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/competences`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `q` | query | Facultatif Swagger | `string ; défaut API null ; minLength=2 ; maxLength=100` | 2–100 caractères facultatif |
| `categorie` | query | Facultatif Swagger | `string ; valeurs savoir_faire, savoir, savoir_etre, contexte_travail ; défaut API null` | contexte_travail |
| `code` | query | Facultatif Swagger | `string ; défaut API null` | OGR exact ou 1–10 facultatifs |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].categorie_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].categorie_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].macro_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].macro_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].enjeu_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].enjeu_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_competence_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_competence_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_metiers` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_coeur_metier_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [06_controles/resultats/R23 test/GET_competences__code_103659__page_1.json](<../../../06_controles/resultats/R23 test/GET_competences__code_103659__page_1.json>); [06_controles/resultats/R23 test/R23 GET competencescode=125416&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET competencescode=125416&page=1.json>).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [06_controles/VALIDATION_R24_contextes_metiers.md](../../../06_controles/VALIDATION_R24_contextes_metiers.md); [03_catalogue/routes_openapi.csv](../../../03_catalogue/routes_openapi.csv).

**Contrôle local déjà rapporté :** Contrôles de présence des filtres et sélection locale ; catalogue HTTP non couvert. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E15 : Capturer catalogue de contextes, vérifier catégorie et sélection ; pas d'alias arbitraire.

**Points RCO associés :** Q02/Q05 : recherche de contexte ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-015-CA-01** — **Étant donné** une condition choisie, **Quand** je préfère l’éviter, **Alors** elle alimente sans_contexte et non competence.

**US-FON-015-CA-02** — **Étant donné** une condition active, **Quand** je choisis Pas de préférence, **Alors** elle ne filtre plus.

**US-FON-015-CA-03** — **Étant donné** une référence absente d’une fiche, **Quand** je lis la condition, **Alors** aucune absence terrain garantie n’est annoncée.

**US-FON-015-CA-04** — **Étant donné** le catalogue reçu, **Quand** je choisis, **Alors** code et libellé correspondent à la même entrée.

**US-FON-015-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-015-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Aucun texte libre arbitraire transmis comme code ; Contextes libellés et explicites avant filtrage ; conserver distinction contextes/compétences ; Capturer catalogue de contextes, vérifier catégorie et sélection ; pas d'alias arbitraire ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E15` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : recherche/listes, radios par condition, critères et aide.
- Groupes nommés ; modifications annoncées sans reconstruire le formulaire entier.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Choix de contextes OGR ; Contextes libellés et explicites avant filtrage ; conserver distinction contextes/compétences ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Conditions accessibles simultanément aux savoir-faire ; trois choix exclusifs par contexte.

**SEO / validation conservés :** Proposition à valider D10 : Taxonomie interne. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-015 — scénario, interactions et alternatives](svg/US-FON-015.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-015.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
