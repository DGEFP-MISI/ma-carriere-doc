# US-FON-031 — Comprendre les chiffres, leurs sources et leurs limites

**Rattachement :** E31 · alias historique US-E31. **Lot :** L4.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** aucune.

**État constaté au 2 novembre 2026 :** Catalogue de vingt-neuf entrées observé et contrat disponibles ; la liaison documentaire et les restitutions locales ne prouvent pas une valeur pour chaque métier ou territoire. Les variantes de catalogue, la disponibilité HTTP et les règles de secret Q06 restent à tester ou clarifier ; aucune nouvelle entrée n'est assimilée automatiquement à un indicateur opérationnel.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comprendre les chiffres, leurs sources et leurs limites, pour retrouver une définition simple des indicateurs et savoir qui est compté, où et quand, pour interpréter les résultats sans être spécialiste des données. Je veux retrouver les définitions et limites des mesures effectivement reçues.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comprendre les chiffres, leurs sources et leurs limites, afin de retrouver une définition simple des indicateurs et savoir qui est compté, où et quand, pour interpréter les résultats sans être spécialiste des données.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis un chiffre ou une visualisation, choisit comprendre ce chiffre. | Ouvre l'aide de la mesure réellement reçue et relie son code à l'entrée correspondante du catalogue /mesures lorsque la relation est documentée. |
| 2 | Consulte la définition en langage courant. | Présente le libellé et la définition en conservant le sens du champ, l'unité, la population et les limites, sans ajouter de score ou de taux pour vulgariser. |
| 3 | Demande qui est compté et sur quel lieu. | Utilise les métadonnées du résultat pour montrer le grain effectif, le nom de la famille si nécessaire, le nombre de métiers partageant l'observation et le territoire réel avec son repli. |
| 4 | Consulte la source et la période. | Distingue la source du résultat des métadonnées du catalogue, affiche la date ou le millésime reçu et explique ce qui ne permet pas une datation plus précise. |
| 5 | Ouvre le tableau ou les limites de comparaison. | Présente les mêmes données et états que le graphique, avec avertissements sur secret, null, zéro, publication partielle et dimensions incompatibles. |
| 6 | Parcourt les autres mesures disponibles ou retourne à son exploration. | Affiche le catalogue documenté sans présumer sa disponibilité locale, indique les mesures réellement reçues et restaure la section ainsi que le focus d'origine. |

## 5. Scénarios alternatifs

- Catalogue indisponible mais résultat présent : garder le résultat et ses propres métadonnées, signaler l'aide manquante sans inventer une définition ou bloquer toute la fiche.
- Nouvelle entrée de catalogue ou code inconnu du rendu : conserver la donnée et le code dans la traçabilité technique, demander son adaptation et ne pas fabriquer une visualisation ou une unité.
- Mesure cataloguée sans valeur pour le métier ou le lieu : indiquer la disponibilité effective de cet appel, sans attribuer automatiquement la couverture globale du catalogue à ce cas.
- Écart de source, période ou famille entre deux valeurs : expliquer les différences dans le contexte de comparaison et ne pas les masquer derrière un libellé commun.
- Champ absent après projection ou variante de réponse : distinguer ce cas d'un null documenté et tracer un écart éventuel avant d'en tirer une conclusion métier.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Le catalogue observé comporte vingt-neuf mesures sur plusieurs ressources ; seules quatorze relèvent de /indicateurs dans la définition observée. Une entrée de catalogue ne garantit pas une valeur locale.
- La relation est items[].code du catalogue vers items[].mesure des résultats d'indicateurs ; code de mesure n'est pas un paramètre de recherche mesure ou code inventé sur /indicateurs.
- source dans le catalogue et source_libelle des résultats ont des fonctions distinctes ; les unités viennent des champs et définitions, sans champ unite universel supposé.
- La méthode explique le caractère familial, la population, la période, le repli et les états ; deux métiers d'une famille partagent une observation, et aucun calcul ne révèle une valeur secret_stat.
- Le langage citoyen emploie noms et explications plutôt que codes ou sigles imposés, tout en conservant les sources et la précision ; les trois niveaux statique, JSON observé et HTTP testé restent distincts dans la preuve technique.

**Règles héritées conservées :** Catalogue global29entrées historiques, disponibilité locale lue dans valeurs[] ; code↔mesure et ressource ; source du catalogue différent de source_libelle des résultats.

**Traitements :** `/mesures`, dictionnaire par code et ressource ; Catalogue global29entrées historiques, disponibilité locale lue dans valeurs[] ; code↔mesure et ressource ; source du catalogue différent de source_libelle des résultats.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Catalogue global29entrées historiques, disponibilité locale lue dans valeurs[] ; code↔mesure et ressource ; source du catalogue différent de source_libelle des résultats.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Catalogue API ; grain mesure ; période par indicateur. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/mesures`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `fields` | query | Facultatif Swagger | `string ; défaut API null` | facultatif ; omis initialement |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].ressource` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].definition` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].champs` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].mailles` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].source` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_couverts` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_rome_couverts` | entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json).

**Contrôle local déjà rapporté :** Vingt-neuf notices locales ; cela ne démontre pas la disponibilité d’une mesure pour tout métier. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E31 : Vérifier que les 29 entrées historiques ne sont pas présumées toutes présentes sous `/indicateurs` ; nouvelles entrées tolérées.

**Points RCO associés :** Q01/Q06 : schémas et version du catalogue ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-031-CA-01** — **Étant donné** la personne ouvre l'aide d'une mesure reçue, **Quand** la définition est présentée, **Alors** elle correspond à cette mesure et aux unités réellement utilisées dans le résultat, sans score ajouté.

**US-FON-031-CA-02** — **Étant donné** le catalogue contient vingt-neuf entrées, **Quand** les indicateurs du métier sont consultés, **Alors** aucune règle ne suppose vingt-neuf valeurs sous /indicateurs ni une valeur disponible pour chaque entrée.

**US-FON-031-CA-03** — **Étant donné** le résultat s'est replié sur une maille parent, **Quand** la personne demande d'où vient ce chiffre, **Alors** le lieu effectif est nommé distinctement du lieu choisi et le repli est expliqué.

**US-FON-031-CA-04** — **Étant donné** une mesure est familiale et nb_rome_famille est supérieur à un, **Quand** la définition du chiffre est ouverte, **Alors** la population partagée est expliquée par son nom sans présenter l'observation comme exclusive du métier.

**US-FON-031-CA-05** — **Étant donné** le tableau et le graphique montrent une valeur protégée, manquante ou nulle, **Quand** la personne change de présentation, **Alors** le même sens de donnée est conservé et aucune cellule alternative ne révèle ou ne calcule la valeur absente.

**US-FON-031-CA-06** — **Étant donné** un nouveau code de mesure est reçu, **Quand** le rendu ne connaît pas encore sa structure, **Alors** la réponse n'est pas perdue, l'adaptation est tracée et aucun graphique, unité ou disponibilité n'est inventé.

**US-FON-031-CA-07** — **Étant donné** la consultation utilise des JSON observés, **Quand** les preuves de recette sont publiées, **Alors** elles ne sont pas présentées comme nouveaux tests HTTP réels ou comme certification RGAA.

**US-FON-031-CA-08** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-031-CA-09** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Aucune mesure disponible présumée ; Méthodologie commune et disponibilité effective d'après réponses, consultable dans chaque volet ; Vérifier que les 29 entrées historiques ne sont pas présumées toutes présentes sous `/indicateurs` ; nouvelles entrées tolérées ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E31` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : lien comprendre ce chiffre proche de la valeur, aide progressive et tableaux de méthode, sources et limites ; retour au focus d'origine ; textes courts puis détail accessible pour tous les niveaux de familiarité avec les données.
- DSFR Chart DataBox : source, période, explication et alternative tabulaire associées aux visualisations ; mêmes états dans le tableau et le graphique, sans dépendre du survol ou d'une couleur.
- États aide disponible, catalogue en chargement, source partielle, nouvelle mesure et erreur sans blocage général ; conserver une lecture claire sur mobile et au clavier sans exposer de notes internes au citoyen.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Catalogue et méthodologie des mesures ; Méthodologie commune et disponibilité effective d'après réponses, consultable dans chaque volet ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Explication méthodologique. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-031 — scénario, interactions et alternatives](svg/US-FON-031.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-031.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
