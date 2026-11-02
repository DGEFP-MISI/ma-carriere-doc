# US-FON-003 — Découvrir un domaine professionnel

**Rattachement :** E03 · alias historique US-E03. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** aucune.

**État constaté au 2 novembre 2026 :** Fiche Domaine locale testée à partir des métiers ; réponse réelle /domaines encore à collecter.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de découvrir un domaine professionnel, pour commencer sans connaître le nom d’un métier. Je veux découvrir un domaine professionnel sans connaître un métier.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite découvrir un domaine professionnel, afin de commencer sans connaître le nom d’un métier.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- L’arbre /domaines est une source contractuelle distincte de la liste locale issue des métiers.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Choisit Domaine professionnel | Explique le regroupement de métiers, distinct d’un secteur économique. |
| 2 | Parcourt les grands domaines ou saisit des mots | Charge /domaines et, si recherché, filtre localement ses libellés. |
| 3 | Sélectionne un grand domaine | Affiche ses domaines et les nombres de métiers fournis. |
| 4 | Ouvre un domaine | Conserve domaine_code et propose ses métiers. |
| 5 | Poursuit vers un métier ou revient | Ouvre la référence choisie et préserve les retours. |

## 5. Scénarios alternatifs

- Arbre non collecté localement : identifier les domaines issus des seules fiches disponibles, sans fausse réponse /domaines.
- Aucun libellé filtré : proposer de parcourir l’arbre ou retirer le filtre.
- Nombre absent : ne pas le calculer sur une liste partielle.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Arbre non paginé, total grands domaines. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- /domaines accepte grand_domaine, sans q, page ni fields.
- total compte les grands domaines retournés, pas les métiers ou emplois.
- Le mode public est Domaine professionnel ; secteur économique NAF est une autre notion.

**Règles héritées conservées :** nb_metiers du contrat conservé ; aucun agrégat d'emploi par Domaine, total compte les grands domaines retournés.

**Traitements :** `/domaines?grand_domaine=...` ou arbre complet ; nb_metiers du contrat conservé ; aucun agrégat d'emploi par Domaine, total compte les grands domaines retournés.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. nb_metiers du contrat conservé ; aucun agrégat d'emploi par Domaine, total compte les grands domaines retournés.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3 ; grain domaine ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/domaines`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `grand_domaine` | query | Facultatif Swagger | `string ; défaut API null` | facultatif lettre A–N |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.total` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].grand_domaine_code` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].grand_domaine_libelle` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_metiers` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].domaines[].domaine_code` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].domaines[].domaine_libelle` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].domaines[].nb_metiers` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |

**Réponses natives utilisées pour vérifier les chemins :** aucun JSON natif enregistré pour cet endpoint dans les jeux chargés ; contrat à compléter par un test GET ciblé.

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [03_catalogue/routes_openapi.csv](../../../03_catalogue/routes_openapi.csv); [03_catalogue/modeles_reponses/domaines.schema.json](../../../03_catalogue/modeles_reponses/domaines.schema.json).

**Contrôle local déjà rapporté :** Mission 007 sur la liste locale de domaines ; ce n’est pas une capture de /domaines. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E03 : Collecter l'arbre, vérifier codes/nombres/types contractuels ; tester sélection du sous-domaine.

**Points RCO associés :** Q03 : export réel et règle `nb_metiers` ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-003-CA-01** — **Étant donné** un arbre reçu, **Quand** je choisis un grand domaine, **Alors** seuls ses sous-domaines sont proposés.

**US-FON-003-CA-02** — **Étant donné** des mots saisis, **Quand** je filtre les domaines, **Alors** le filtre est local et aucun q n’est envoyé à /domaines.

**US-FON-003-CA-03** — **Étant donné** nb_metiers absent, **Quand** je lis la fiche, **Alors** aucun total local ne le remplace.

**US-FON-003-CA-04** — **Étant donné** un domaine choisi, **Quand** je poursuis, **Alors** son code reçu est utilisé par E04.

**US-FON-003-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-003-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Le libellé public est Domaine professionnel, distinct du secteur économique ; Grand domaine → domaine → fiche ; filtre local des libellés reçus comme proposition pour conserver une barre unique sans `q` serveur ; Collecter l'arbre, vérifier codes/nombres/types contractuels ; tester sélection du sous-domaine ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E03` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : arbre/listes hiérarchisées, recherche locale, cartes et fil d’Ariane.
- Sélection clavier ; aucun graphique d’emploi agrégé au Domaine.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Arbre et fiche Domaine ; Grand domaine → domaine → fiche ; filtre local des libellés reçus comme proposition pour conserver une barre unique sans `q` serveur ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Mode Domaine dans la barre persistante ; adaptateur arborescent selon contrat, réponse réelle à collecter ; liste locale issue des domaines observés sans faux effectif.

**SEO / validation conservés :** Proposition à valider D10 : Libellé domaine et métiers liés. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-003 — scénario, interactions et alternatives](svg/US-FON-003.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-003.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
