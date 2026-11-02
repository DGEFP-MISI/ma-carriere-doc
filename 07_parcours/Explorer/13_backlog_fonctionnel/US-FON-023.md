# US-FON-023 — Comprendre les changements de situation professionnelle observés

**Rattachement :** E23 · alias historique US-E23. **Lot :** L5.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05);[US-FON-009](US-FON-009.md) (E09);[US-FON-031](US-FON-031.md) (E31).

**État constaté au 2 novembre 2026 :** Les filtres sont documentés et des JSON F1610 couvrent les deux sens et les six tranches d'âge au niveau France. Ces observations et les contrôles locaux ne prouvent pas les variantes régionales ou de futurs appels HTTP ; les dépendances de test restent incluses sans retirer les mobilités.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comprendre les changements de situation professionnelle observés, pour voir d'où venaient et où sont allées les personnes de la famille de métiers étudiée, pour élargir ma réflexion sans confondre une statistique collective avec mon avenir personnel. Je veux comprendre les origines et destinations professionnelles observées.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comprendre les changements de situation professionnelle observés, afin de voir d'où venaient et où sont allées les personnes de la famille de métiers étudiée, pour élargir ma réflexion sans confondre une statistique collective avec mon avenir personnel.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre la question d'où viennent et où vont les personnes qui exercent ce métier. | Présente d'abord le nom de la famille professionnelle et la période janvier 2022-janvier 2023, avec une explication du périmètre de l'observation. |
| 2 | Choisit la situation un an avant ou un an après. | Traduit le choix en sens=origines ou sens=destinations et adapte ensemble les titres, libellés de situation et définition de la population. |
| 3 | Choisit France ou une région et une tranche d'âge. | Utilise region lorsqu'une région est choisie et age dans l'enum, encode le plus de 60+ et garde la tranche explicitement sélectionnée sans l'inférer de la personne. |
| 4 | Lit le classement des situations observées. | Sépare les familles, affiche leurs libellés, parts, rangs et éventuel repli, puis distingue même famille, autre famille et situations hors emploi. |
| 5 | Ouvre le tableau et l'explication des données manquantes. | Rend les mêmes parts avec le sens, l'âge, la population et la source ; explique le top quinze et les parts omises sous secret, sans total artificiel. |
| 6 | Souhaite découvrir des métiers concrets ou comparer. | Propose les relations de métiers proches déjà documentées ou la comparaison de métiers explicitement choisis, sans transformer une destination de famille en lien métier déduit. |

## 5. Scénarios alternatifs

- Une région se replie sur la France pour une famille : nommer ce repli dans le groupe concerné, sans appliquer la même géographie à toutes les familles.
- Certaines situations ou parts sont absentes : expliquer publication partielle et secret, sans compléter à cent pour cent ni fabriquer une catégorie autres.
- Une situation est chômage, études, apprentissage, retraite ou autre : conserver sa nature et ne pas la présenter comme un métier cible.
- Un filtre n'a pas de réponse observée dans la maquette : conserver le choix et annoncer que cette combinaison n'est pas encore disponible dans les preuves locales, sans afficher les chiffres d'une autre tranche.
- Erreur ou changement rapide de sens et d'âge : ignorer les réponses périmées, maintenir le contexte demandé et permettre la reprise ciblée.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Pour les origines, la population exerce en janvier 2023 et l'âge est celui de 2023 ; pour les destinations, elle exerce en janvier 2022 et l'âge est celui de 2022. Les deux sens ne sont pas interchangeables.
- Les parts concernent des FAP225, non des flux directs de ROME à ROME ; tag_meme_metier signifie même famille et tag_en_emploi distingue les situations de métier.
- Le fournisseur publie des parts sans effectifs, quinze situations au plus par famille et des omissions liées au secret ; ni renormalisation, volume, probabilité personnelle ou Sankey exhaustif n'est construit.
- Le paramètre est age, le champ lisible tranche_age_libelle ; sens emploie les pluriels origines/destinations et les clés origine_* ou destination_* correspondent au sens demandé.
- maille et repli sont propres aux lignes ; aucune correspondance de destination FAP vers ROME n'est déduite d'un libellé ou d'un code ressemblant.

**Règles héritées conservées :** FAP225, 2022–2023 ; 15 situations au plus/famille, parts secret omises ; somme possiblement <100, pas de renormalisation ; âge fin période origines/début destinations ; tag_meme_metier=FAP.

**Traitements :** `/mobilites?rome=...&sens=...&region=...&age=...` ; FAP225, 2022–2023 ; 15 situations au plus/famille, parts secret omises ; somme possiblement <100, pas de renormalisation ; âge fin période origines/début destinations ; tag_meme_metier=FAP.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. FAP225, 2022–2023 ; 15 situations au plus/famille, parts secret omises ; somme possiblement <100, pas de renormalisation ; âge fin période origines/début destinations ; tag_meme_metier=FAP.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Source renvoyée ; grain fap_225 ; période 2022-2023 observé, vérifier réponse. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/mobilites`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `sens` | query | Facultatif Swagger | `string ; valeurs origines, destinations ; défaut API "origines"` | origines/destinations |
| `region` | query | Facultatif Swagger | `string ; défaut API null` | code2caractères ou omis=France |
| `age` | query | Facultatif Swagger | `string ; valeurs ensemble, 15-29, 30-39, 40-49, 50-59, 60+ ; défaut API "ensemble"` | ensemble/15-29/30-39/40-49/50-59/60+ ; encoder le + |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tranche_age_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].origine_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].origine_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tag_meme_metier` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tag_en_emploi` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_personnes` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].maille` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].repli` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].destination_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].destination_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.sens` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.region` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.region_libelle` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tranche_age_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/mobilites/response_destination 15-29 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_destination 15-29 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_destination 30-39 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_destination 30-39 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_destination 40-49 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_destination 40-49 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_destination 50-59 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_destination 50-59 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_destination 60 ans ou plus.json](<../../../02_reponses_observees/indicateurs/mobilites/response_destination 60 ans ou plus.json>); [02_reponses_observees/indicateurs/mobilites/response_destination.json](../../../02_reponses_observees/indicateurs/mobilites/response_destination.json); [02_reponses_observees/indicateurs/mobilites/response_origine 15-29 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_origine 15-29 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_origine 30-39 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_origine 30-39 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_origine 40-49 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_origine 40-49 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_origine 50-59 ans.json](<../../../02_reponses_observees/indicateurs/mobilites/response_origine 50-59 ans.json>); [02_reponses_observees/indicateurs/mobilites/response_origine 60 ans ou plus.json](<../../../02_reponses_observees/indicateurs/mobilites/response_origine 60 ans ou plus.json>); [02_reponses_observees/indicateurs/mobilites/response_origine.json](../../../02_reponses_observees/indicateurs/mobilites/response_origine.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/indicateurs/mobilites/response_destination.json](../../../02_reponses_observees/indicateurs/mobilites/response_destination.json); [02_reponses_observees/indicateurs/mobilites/response_origine.json](../../../02_reponses_observees/indicateurs/mobilites/response_origine.json).

**Contrôle local déjà rapporté :** Mission 010 : sens, âge, famille, période, source et focus. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E23 : Tracer région et âges ; valider `maille/repli`, présence d'un seul couple origine/destination et libellés hors emploi.

**Points RCO associés :** Q12 : âges, repli, couverture des parts ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

### Couverture détaillée des 2 mesures rattachées à cette US

Chaque mesure est un sous-scénario de cette US. Ses champs, sa population et ses critères sont conservés même si aucune valeur n’est publiée dans le jeu local.

#### `mobilites_origines` — Origine des personnes qui exercent un métier

**Source API :** GET /mobilites?sens=origines. Conserver les familles/populations réellement publiées.

**Grain :** `fap_225`. **Mailles du catalogue :** reg, nat. **Millésime observé :** 2022-2023.

**Producteur :** DARES, dispositif ForCE et DSN-Sismmo. **Unité et population :** Pourcentage des personnes en emploi dans la famille en janvier 2023, selon leur situation en janvier 2022 ; aucun effectif publié.

**Définition source :** Situation en janvier 2022 des personnes en emploi en janvier 2023 dans la famille professionnelle (FAP 225) rattachée au ROME V3 : même métier, autre métier (FAP 225), demandeur d'emploi, apprenti, sortant d'études, autre situation. Part des personnes en %, par région de travail et tranche d'âge (en 2023). Les 15 situations les plus fréquentes par FAP ; parts sous secret statistique de la source omises.

**Champs nécessaires :** `$.items[].fap_225_code`, `$.items[].fap_225_libelle`, `$.items[].tranche_age_libelle`, `$.items[].origine_code`, `$.items[].origine_libelle`, `$.items[].tag_meme_metier`, `$.items[].tag_en_emploi`, `$.items[].tx_personnes`.

**Présentation attendue :** DSFR Chart DataBox et barres horizontales des situations d'origine ; tableau DSFR rang/libellé/part, filtre d'âge et de région DSFR, sans Sankey donnant une impression d'exhaustivité.

- Appeler /mobilites avec sens=origines, rome et age exact ; age vaut ensemble,15-29,30-39,40-49,50-59 ou60+ et le signe plus est encodé dans l'URL.
- La population est en emploi dans la FAP225 en janvier 2023 et la situation regardée est janvier 2022 ; la tranche d'âge est celle de fin de période, en 2023.
- Conserver les quinze situations les plus fréquentes au plus par famille, avec origine_libelle, rang, tag_meme_metier, tag_en_emploi et tx_personnes ; distinguer autre famille et situation hors emploi.
- Parts sous secret omises par la source : pas de renormalisation, d'effectif calculé ou de catégorie manquante déduite ; la somme publiée peut être inférieure à cent.
- Lire maille/repli par ligne et le nom de la FAP ; les codes de situation ou de famille ne prouvent aucun lien vers un ROME cible et tag_meme_metier signifie même famille.

**Dépendance / tests :** Catalogue observé : fap_225, 2022-2023, reg/nat. Les fixtures de tranche d'âge F1610 sont des observations, pas un nouveau testHTTP. Tester région/repli, plusieurs familles et non-emploi ; ne pas mélanger avec destinations.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `mobilites_destinations` — Devenir des personnes qui exercent un métier

**Source API :** GET /mobilites?sens=destinations. Conserver les familles/populations réellement publiées.

**Grain :** `fap_225`. **Mailles du catalogue :** reg, nat. **Millésime observé :** 2022-2023.

**Producteur :** DARES, dispositif ForCE et DSN-Sismmo. **Unité et population :** Pourcentage des personnes en emploi dans la famille en janvier 2022, selon leur situation en janvier 2023 ; aucun effectif publié.

**Définition source :** Situation en janvier 2023 des personnes en emploi en janvier 2022 dans la famille professionnelle (FAP 225) rattachée au ROME V3 : même métier, autre métier (FAP 225), demandeur d'emploi, retraité, autre situation. Part des personnes en %, par région de travail et tranche d'âge (en 2022). Les 15 situations les plus fréquentes par FAP ; parts sous secret statistique de la source omises.

**Champs nécessaires :** `$.items[].fap_225_code`, `$.items[].fap_225_libelle`, `$.items[].tranche_age_libelle`, `$.items[].destination_code`, `$.items[].destination_libelle`, `$.items[].tag_meme_metier`, `$.items[].tag_en_emploi`, `$.items[].tx_personnes`.

**Présentation attendue :** DSFR Chart DataBox et barres horizontales des situations de destination ; tableau DSFR accessible, avec commandes d'âge et de région et explication de la population.

- Appeler /mobilites avec sens=destinations ; utiliser le paramètre age et non tranche_age, puis afficher tranche_age_libelle reçu et les destination_libelle.
- La population exerce dans la FAP225 en janvier 2022 et la situation de destination est observée en janvier 2023 ; la tranche d'âge est celle du début de période, en 2022.
- Conserver les familles et situations distinctes, y compris demandeur d'emploi, retraité et autres situations ; tag_en_emploi indique une situation métier et tag_meme_metier une stabilité dans la famille.
- Les quinze situations au plus et les parts secrètes omises ne décrivent pas un total exhaustif ; aucune normalisation, catégorie résiduelle calculée, probabilité personnelle ou volume n'est produit.
- Une destination de famille n'est pas un code métier ouvrable ; préserver maille/repli par ligne et n'offrir un accès aux métiers proches que via la relation documentaire distincte.

**Dépendance / tests :** Catalogue observé : fap_225, 2022-2023, reg/nat. Retraite et autres sorties ne sont pas des métiers alternatifs ; afficher le nom de la famille avant les parts, y compris dans E28. Tests de filtres et repli encore distincts des contrôles de fixtures.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

## 8. Critères d’acceptation

**US-FON-023-CA-01** — **Étant donné** la personne choisit les origines pour la tranche 60+, **Quand** l'appel est préparé, **Alors** la route utilise sens=origines et age=60%2B et l'explication situe l'âge en 2023.

**US-FON-023-CA-02** — **Étant donné** la personne passe aux destinations avec le même âge, **Quand** les données sont reçues, **Alors** les libellés destination et la population de départ 2022 sont affichés ensemble sans reste des origines.

**US-FON-023-CA-03** — **Étant donné** plusieurs familles sont liées au métier, **Quand** le classement est affiché, **Alors** chaque famille dispose de son nom, ses rangs et son éventuelle géographie de repli.

**US-FON-023-CA-04** — **Étant donné** les parts restituées totalisent moins de cent, **Quand** le graphique et son tableau sont rendus, **Alors** les valeurs restent inchangées et la publication partielle est expliquée sans solde calculé.

**US-FON-023-CA-05** — **Étant donné** une destination est une famille ou une situation hors emploi, **Quand** la personne consulte les actions associées, **Alors** aucun lien direct vers un métier individuel n'est inventé.

**US-FON-023-CA-06** — **Étant donné** une seule combinaison d'âge et territoire est observée localement, **Quand** une autre combinaison est choisie, **Alors** ses données ne sont pas remplacées par celles de la combinaison connue et le manque de preuve est explicite.

**US-FON-023-CA-07** — **Étant donné** la personne choisit les origines et la tranche60+, **Quand** la requête est préparée, **Alors** le système utilise sens=origines et age=60%2B, et explique que l'âge concerne 2023.

**US-FON-023-CA-08** — **Étant donné** le classement publié est partiel et comprend des situations hors emploi, **Quand** les mobilités sont affichées, **Alors** les catégories sont nommées distinctement sans total forcé, effectif calculé ou lien métier déduit.

**US-FON-023-CA-09** — **Étant donné** la personne passe des origines aux destinations avec une tranche d'âge sélectionnée, **Quand** les nouvelles données sont affichées, **Alors** le sens, l'âge de début de période et les libellés destination sont actualisés ensemble, sans réutiliser la population des origines.

**US-FON-023-CA-10** — **Étant donné** une ligne représente les retraités ou une autre famille professionnelle, **Quand** la personne parcourt le classement, **Alors** la situation est expliquée sans bouton vers une fiche métier déduite du code de destination.

**US-FON-023-CA-11** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-023-CA-12** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Population et âge expliqués ; Deux sens, âge, France/région, tableaux/graphiques par FAP225, situations hors emploi et parts incomplètes ; Tracer région et âges ; valider `maille/repli`, présence d'un seul couple origine/destination et libellés hors emploi ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E23` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : choix de sens par questions, sélecteurs d'âge et de région avec libellés, résumé de contexte au-dessus de chaque groupe ; états de chargement, partiel, repli, aucun résultat et erreur.
- DSFR Chart DataBox et barres horizontales des parts publiées avec tableau alternatif ; texte pour les situations hors emploi et le champ de population, sans dépendre de couleurs ni d'une infobulle au survol.
- Annoncer le sens et la tranche après modification, conserver le focus sur le filtre et donner les mêmes renseignements sur téléphone et au clavier ; l'accès aux métiers proches est nommé comme une autre relation.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Mobilités professionnelles ; Deux sens, âge, France/région, tableaux/graphiques par FAP225, situations hors emploi et parts incomplètes ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Contenu enrichi. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-023 — scénario, interactions et alternatives](svg/US-FON-023.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-023.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
