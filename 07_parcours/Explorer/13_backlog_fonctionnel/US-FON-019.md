# US-FON-019 — Découvrir les métiers associés à une certification

**Rattachement :** E19 · alias historique US-E19. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-017](US-FON-017.md) (E17).

**État constaté au 2 novembre 2026 :** Association documentée et listes observées dans les JSON de certification ; la chaîne HTTP vers plusieurs fiches doit être capturée. La maquette peut restituer les associations observées et les cibles présentes sans démontrer la disponibilité de toutes les fiches.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de découvrir les métiers associés à une certification, pour identifier les métiers associés à un diplôme ou un titre puis examiner leur contenu avant de retenir une piste. Je veux ouvrir les métiers associés à une certification.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite découvrir les métiers associés à une certification, afin d’identifier les métiers associés à un diplôme ou un titre puis examiner leur contenu avant de retenir une piste.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre la rubrique quels métiers découvrir depuis la certification consultée. | Lit les listes rome_codes et rome_libelles de cette certification, sans dépendre de l'éventuel rome_code singulier. |
| 2 | Parcourt les métiers proposés. | Affiche leurs noms reçus et explique qu'il s'agit de rattachements documentaires, sans promesse d'accès ou de poste disponible. |
| 3 | Choisit un métier. | Réutilise sa fiche en cache compatible ou appelle /metiers/{rome} avec le code ROME V3 associé ; affiche l'état de chargement du seul métier choisi. |
| 4 | Consulte ses activités, conditions et perspectives. | Ouvre la vraie fiche cible avec les autres volets d'Explorer et garde le territoire précédemment choisi sans transférer les statistiques de la certification au métier. |
| 5 | Retient ce métier ou revient à la certification. | Applique les règles communes de Mes pistes et restaure la fiche de certification ainsi que l'intention et les associations parcourues. |

## 5. Scénarios alternatifs

- Plusieurs métiers associés et champ rome_code null : afficher toutes les associations des listes, sans choisir automatiquement un métier principal.
- Listes vides : indiquer qu'aucun rattachement n'est publié dans la réponse, sans conclure que la certification n'a aucun débouché réel.
- Un code associé n'ouvre pas de fiche : garder la certification et les autres liens, signaler la fiche indisponible et conserver l'anomalie pour contrôle.
- Désaccord entre codes et libellés parallèles : ne pas associer arbitrairement un nom à un code ; préserver la preuve et résoudre le nom par la fiche ciblée lorsque disponible.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Toutes les cibles métier sont des ROME V3 reçus ; aucun métier n'est déduit du titre de certification, d'une famille statistique ou d'un texte de bloc.
- Les listes de codes et libellés sont parallèles ; préserver leurs correspondances et leur ordre sans inventer un classement de débouchés.
- Le rattachement ne signifie ni qualification obligatoire, ni habilitation individuelle, ni accès automatique à l'emploi.
- Ne pas appeler chaque fiche pour répéter un libellé déjà reçu ; charger le détail à la sélection et réutiliser les données compatibles en cache.
- Le retour conserve le contexte de certification ; aucune mesure nationale de certification n'est présentée comme un indicateur propre au métier ouvert.

**Règles héritées conservées :** Association rome_codes[] multiple, non-garantie d'accès à l'emploi ; ne pas dépendre de rome_code nullable.

**Traitements :** `rome_codes[]` de la certification → `/metiers/{rome}` ; Association rome_codes[] multiple, non-garantie d'accès à l'emploi ; ne pas dépendre de rome_code nullable.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Association rome_codes[] multiple, non-garantie d'accès à l'emploi ; ne pas dépendre de rome_code nullable.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3 ; grain ROME V3 ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/metiers/{rome}`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | path | Requis Swagger | `string` | chemin de chaque rome_codes[] choisi |

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

**Références conservées de la conception :** [04_relations/CHAINES_APPELS_API.md](../../../04_relations/CHAINES_APPELS_API.md); [02_reponses_observees/certifications/response_certifications-certifinfo.json](../../../02_reponses_observees/certifications/response_certifications-certifinfo.json).

**Contrôle local déjà rapporté :** Navigation depuis certification vers métiers connus dans la recette existante. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E19 : Certification à plusieurs ROME, ouverture des cibles ; ne pas dépendre du seul `rome_code` nullable.

**Points RCO associés :** Q09 si relation contradictoire ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-019-CA-01** — **Étant donné** une certification comporte trois associations et rome_code vaut null, **Quand** la rubrique métiers est ouverte, **Alors** les trois associations publiées sont proposées par leurs noms et aucun métier n'est perdu à cause du champ singulier.

**US-FON-019-CA-02** — **Étant donné** la personne choisit la deuxième association, **Quand** la fiche métier est demandée, **Alors** le code technique sélectionné pilote le GET et le titre correspond au métier réellement choisi.

**US-FON-019-CA-03** — **Étant donné** le nom d'un métier associé est déjà reçu, **Quand** la liste est affichée, **Alors** aucun GET de détail par carte n'est exigé pour rendre ce nom.

**US-FON-019-CA-04** — **Étant donné** une cible est indisponible et les autres sont accessibles, **Quand** la personne tente son ouverture puis revient, **Alors** l'erreur n'efface ni la certification ni les autres associations et aucun autre métier ne lui est substitué.

**US-FON-019-CA-05** — **Étant donné** la fiche métier a été explorée depuis une certification, **Quand** la personne revient à la certification, **Alors** l'intention de consultation, le territoire et les pistes sont conservés sans duplication.

**US-FON-019-CA-06** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-019-CA-07** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Aucune garantie emploi; ouverture réelle fiche ; Tous les métiers associés en liens, sans garantir accès à l'emploi ; réutiliser le cache ; Certification à plusieurs ROME, ouverture des cibles ; ne pas dépendre du seul `rome_code` nullable ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E19` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : liste ou cartes de métiers avec un lien explicite par nom, texte d'explication du rattachement, retour à la certification et action Mes pistes ; chargement ciblé, liste vide et erreur partielle.
- L'ordre de lecture et le parcours clavier suivent les associations ; annoncer le titre de la fiche cible et offrir un retour identifiable sur desktop comme sur mobile.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Métiers associés à une certification ; Tous les métiers associés en liens, sans garantir accès à l'emploi ; réutiliser le cache ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Maillage indexable. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-019 — scénario, interactions et alternatives](svg/US-FON-019.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-019.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
