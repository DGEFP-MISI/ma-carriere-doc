# US-FON-028 — Comparer les différences utiles entre deux métiers choisis

**Rattachement :** E28 · alias historique US-E28. **Lot :** L9.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05);[US-FON-006](US-FON-006.md) (E06);[US-FON-008](US-FON-008.md) (E08);[US-FON-009](US-FON-009.md) (E09);[US-FON-010](US-FON-010.md) (E10);[US-FON-011](US-FON-011.md) (E11);[US-FON-012](US-FON-012.md) (E12);[US-FON-017](US-FON-017.md) (E17);[US-FON-020](US-FON-020.md) (E20);[US-FON-023](US-FON-023.md) (E23);[US-FON-024](US-FON-024.md) (E24);[US-FON-025](US-FON-025.md) (E25);[US-FON-026](US-FON-026.md) (E26);[US-FON-031](US-FON-031.md) (E31) ; [US-FON-027](US-FON-027.md) (E27) entrée facultative, comparaison directe possible.

**État constaté au 2 novembre 2026 :** Comparateur local de métiers choisis et contrôles navigateur disponibles ; la comparaison complète HTTP, les deux listes intégrales et les variantes depuis dans les deux sens restent à valider. La synthèse directionnelle est documentée par le contrat malgré des omissions dans le schéma OpenAPI ; son absence de fixture n'autorise ni son invention ni sa suppression.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comparer les différences utiles entre deux métiers choisis, pour mettre en regard deux métiers qui m'intéressent pour comprendre leurs activités, compétences, conditions, certifications et données d'emploi sans qu'un score décide à ma place. Je veux comparer deux métiers sur leurs contenus, certifications et données statistiques.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comparer les différences utiles entre deux métiers choisis, afin de mettre en regard deux métiers qui m'intéressent pour comprendre leurs activités, compétences, conditions, certifications et données d'emploi sans qu'un score décide à ma place.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Deux métiers reconnus peuvent être choisis directement ; les avoir gardés dans Mes pistes est facultatif.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Choisit un premier puis un second métier depuis résultats, fiches ou Mes pistes. | Conserve deux identités explicites A et B avec leurs noms ; ne complète pas une sélection manquante par un métier d'exemple et refuse un doublon non pertinent. |
| 2 | Ouvre la comparaison et choisit le lieu de lecture. | Charge ou réutilise les données propres à A et B avec les paramètres territoriaux compatibles de chaque ressource ; conserve la géographie réelle de chaque mesure. |
| 3 | Compare ce que l'on fait et dans quelles conditions. | Présente côte à côte les contenus reçus et recueille les pages complètes de compétences/contextes avant de conclure à des éléments communs ou spécifiques. |
| 4 | Choisit examiner ce qui est partagé du métier A vers le métier B. | Interroge le métier cible B avec depuis=A ; explique les tags et la synthèse comparaison fournis comme relations de référentiels métiers, pas comme acquis de la personne. |
| 5 | Ouvre les salaires, recrutements, mobilités, perspectives 2030, secteurs ou certifications. | Présente les deux côtés par question avec sources, bases, unités, périodes et familles ; rend les détails complets accessibles et avertit des observations partagées ou non comparables. |
| 6 | Inverse A et B ou remplace un métier. | Met à jour les titres et les données de la bonne identité ; réévalue la comparaison directionnelle et annule les requêtes périmées sans simple échange trompeur de tags depuis. |
| 7 | Garde ou retire une piste et revient à une fiche ou à la recherche. | Applique le même état local de pistes et les retours explicites, sans score global, recommandation automatique ou perte du contexte d'exploration. |

## 5. Scénarios alternatifs

- Un seul métier choisi : demander explicitement le second et garder le premier sans afficher une comparaison préremplie.
- Pages de compétences manquantes : rendre la liste partielle lisible et suspendre seulement les conclusions de commun/spécifique non démontrables, sans retirer le volet.
- Même famille statistique sur les deux métiers : expliquer qu'il s'agit d'une même observation partagée, sans simuler deux enquêtes ou une différence propre aux métiers.
- Périodes, populations ou géographies incompatibles : garder les données et leurs explications séparées, sans calcul de delta ni classement comparatif abusif.
- Erreur sur un côté ou un indicateur : conserver l'autre côté, le nom du métier en échec et une reprise ciblée ; ne jamais dupliquer ses chiffres pour remplir l'autre colonne.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Page manquante = liste incomplète, jamais compétence absente. null avec tranche ouverte = afficher tranche, pas salaire inventé. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- A et B restent les métiers effectivement choisis ; identité, appels et résultats sont rattachés au même code, au même contexte de paramètres et à la bonne colonne.
- Les compétences communes/spécifiques sont des relations sur des identifiants reçus et listes complètes ; une page absente ou un champ non renseigné ne prouve pas une compétence manquante.
- depuis est directionnel : cible dans le chemin, départ dans depuis ; tag_acquise et les comptes/taux comparaison sont fournis par l'API et décrivent les références des métiers, jamais une maîtrise, un manque personnel ou un score inventé.
- Chaque statistique garde sa famille FAP225/FAP228/FAP87, sa population, son unité, sa période et son lieu réel ; même famille égale observation commune, autres familles comparables seulement avec les autres dimensions expliquées et compatibles.
- Tous les volets restent accessibles, y compris mobilités, détail 2030, salaires sectoriels, secteurs, certifications et contextes ; aucune synthèse ne calcule un score global, gain personnel, projection annuelle ou substitut d'une valeur absente.

**Règles héritées conservées :** Listes complètes pour commun/spécifique ; depuis=relation directionnelle de métiers, jamais maîtrise ; chaque statistique conserve FAP/population/maille/période ; aucun score/delta calculé.

**Traitements :** Réemploi des fiches, compétences, certifications et statistiques ; complément `/metiers/{cible}/competences?depuis={origine}` ; Listes complètes pour commun/spécifique ; depuis=relation directionnelle de métiers, jamais maîtrise ; chaque statistique conserve FAP/population/maille/période ; aucun score/delta calculé.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Listes complètes pour commun/spécifique ; depuis=relation directionnelle de métiers, jamais maîtrise ; chaque statistique conserve FAP/population/maille/période ; aucun score/delta calculé.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3/OGR ; grain ROME V3 ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

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

### Appel 2 — GET `/metiers/{rome}`

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

### Appel 3 — GET `/metiers/{rome}/competences`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | path | Requis Swagger | `string` | cible V3 chemin |
| `depuis` | query | Facultatif Swagger | `string ; défaut API null` | métier de départ V3 |
| `categorie` | query | Facultatif Swagger | `string ; valeurs savoir_faire, savoir, savoir_etre, contexte_travail ; défaut API null` | savoir_faire/savoir/savoir_etre ou omis selon besoin |
| `coeur_metier` | query | Facultatif Swagger | `boolean ; défaut API null` | booléen facultatif |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 jusqu'à last_page |

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
| `$.comparaison.rome_code_depuis` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.rome_libelle_depuis` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_competences` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_acquises` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_a_acquerir` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_a_acquerir_meme_macro_competence` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.tx_acquises` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_coeur_metier` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_coeur_metier_acquises` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_coeur_metier_meme_macro_competence` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_macro_competences` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.nb_macro_competences_communes` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.comparaison.tx_macro_competences_communes` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/metiers/response_metiers{rome}competences.json](../../../02_reponses_observees/metiers/response_metiers{rome}competences.json).

### Appel 4 — GET `/indicateurs`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `zonage` | query | Facultatif Swagger | `string ; valeurs france, region, departement, clpe, commune ; défaut API null` | france/region/departement/clpe/commune requis |
| `territoire` | query | Facultatif Swagger | `string ; défaut API null` | code requis sauf france |
| `onisep` | query | Facultatif Swagger | `string ; valeurs exclure, inclure, seulement ; défaut API "exclure"` | exclure/inclure/seulement pour formations_metier |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.rome_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.zonage` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoire` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoires[].maille` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoires[].code` | chaîne / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoires[].libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].mesure` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].maille_demandee` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].maille_reelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_code` | chaîne / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].repli` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_228_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_228_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_globale` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_intensite_embauche` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_lien_formation_emploi` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_manque_main_oeuvre` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_non_durabilite_emploi` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_conditions_travail_contraignantes` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_inadequation_geographique` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_non_attractivite_salariale` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_demandeurs_emploi` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_emploi_diffusees` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_emploi_collectees` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].salaire_net_annuel_q1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].salaire_net_annuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].salaire_net_annuel_q3` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].salaire_net_mensuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tranche_salaire_median_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_salaries_temps_complet` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_projets_recrutement` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_projets_recrutement_difficiles` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_projets_recrutement_difficiles` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_projets_recrutement_saisonniers` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_projets_recrutement_saisonniers` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_87_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].fap_87_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_emplois_2019` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_part_emploi_region_2019` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].indice_specificite_region_2019` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_creations_nettes_emplois_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_creations_nettes_emplois_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_departs_fin_carriere_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_departs_fin_carriere_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_postes_a_pourvoir_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_postes_a_pourvoir_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_jeunes_debutants_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_jeunes_debutants_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_desequilibre_potentiel_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_desequilibre_potentiel_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tension_niveau_2019` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].periode_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_emploi_base` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_cdi` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_cdd` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_interim` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_saisonnier` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_non_salarie` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_emploi_durable` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_alternance` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_debutant_accepte` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_ouvrier_non_qualifie` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_ouvrier_qualifie` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_employe_non_qualifie` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_employe_qualifie` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_technicien_agent_maitrise` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_cadre` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_niveau_formation_renseigne` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_niveau_formation_infra_bac` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_niveau_formation_bac` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_niveau_formation_bac2` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_niveau_formation_bac3_4` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_niveau_formation_bac5` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].periode_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_emploi_mois` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_postes_offres_emploi_mois` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].rang_competence` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].competence_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].competence_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].competence_type_libelles` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_competence` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_offres_avec_competences` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_offres_competence` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].rang_secteur` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].secteur_naf38_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].secteur_naf38_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_actifs_emploi` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_actifs_secteur` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_actifs_salaries` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_actifs_independants` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_actifs_employeurs` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_actifs_aides_familiaux` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_actifs_salaries` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_actifs_independants` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_actifs_employeurs` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_actifs_aides_familiaux` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_inscrits_voie_scolaire` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_inscrits_apprentissage` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_inscrits_enseignement_sup` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_inscrits_sanitaire_social` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_entrees_formation_de` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_de_sortants` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_de_acces_emploi_6m` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_de_acces_emploi_6m` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_affelnet_places` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_affelnet_voeux_1` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].indice_affelnet_pression` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_parcoursup_places` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_parcoursup_candidatures` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_sessions_a_venir` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_certifications` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_scolaire_sortants` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_scolaire_emploi_12m` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_ij_scolaire_emploi_12m` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_apprentissage_sortants` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_apprentissage_emploi_12m` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_ij_apprentissage_emploi_12m` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_scolaire_annee_terminale` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_scolaire_poursuite_etudes` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_ij_scolaire_poursuite_etudes` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_apprentissage_annee_terminale` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].nb_ij_apprentissage_poursuite_etudes` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].valeurs[].tx_ij_apprentissage_poursuite_etudes` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json](<../../../06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json>).

### Appel 5 — GET `/recrutements`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `zonage` | query | Facultatif Swagger | `string ; valeurs region, departement, clpe ; défaut API "region"` | region/departement/clpe |
| `region` | query | Facultatif Swagger | `string ; défaut API null` | seulement département ou CLPE |
| `departement` | query | Facultatif Swagger | `string ; défaut API null` | seulement CLPE |
| `tri` | query | Facultatif Swagger | `string ; valeurs projets, projets_difficiles, tx_difficiles, projets_saisonniers, tx_saisonniers ; défaut API "projets"` | projets/projets_difficiles/tx_difficiles/projets_saisonniers/tx_saisonniers |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_228_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_228_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_projets_recrutement` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_projets_recrutement_difficiles` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_projets_recrutement_difficiles` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_projets_recrutement_saisonniers` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_projets_recrutement_saisonniers` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.perimetre.maille` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.perimetre.code` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.perimetre.libelle` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.france[].fap_228_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].fap_228_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_projets_recrutement` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_projets_recrutement_difficiles` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_projets_recrutement_difficiles` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_projets_recrutement_saisonniers` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_projets_recrutement_saisonniers` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json](<../../../02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json>); [02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json](<../../../02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json>); [02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json](<../../../02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json>).

### Appel 6 — GET `/salaires`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `zonage` | query | Facultatif Swagger | `string ; valeurs region, departement ; défaut API "region"` | region/departement |
| `region` | query | Facultatif Swagger | `string ; défaut API null` | seulement avec zonage=departement |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_q1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_q3` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_mensuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tranche_salaire_median_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_salaries_temps_complet` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].salaire_net_annuel_q1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].salaire_net_annuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].salaire_net_annuel_q3` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].salaire_net_mensuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tranche_salaire_median_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_salaries_temps_complet` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/salaires/response_departement.json](../../../02_reponses_observees/indicateurs/salaires/response_departement.json); [02_reponses_observees/indicateurs/salaires/response_regions.json](../../../02_reponses_observees/indicateurs/salaires/response_regions.json).

### Appel 7 — GET `/certifications`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | code V3 |
| `acces` | query | Facultatif Swagger | `string ; valeurs formation_initiale, apprentissage, formation_continue, contrat_professionnalisation, candidature_individuelle, vae ; défaut API null` | formation_initiale/apprentissage/formation_continue/contrat_professionnalisation/candidature_individuelle/vae facultatif |
| `validation_partielle` | query | Facultatif Swagger | `boolean ; défaut API null` | booléen facultatif |
| `repertoire` | query | Facultatif Swagger | `string ; valeurs RNCP, RS ; défaut API null` | RNCP/RS facultatif |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].certifinfo_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].certifinfo_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].etat_certifinfo_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].type_certification_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].certificateur_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].repertoire_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fiche_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fiche_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].type_enregistrement_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].date_fin_enregistrement` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].niveau_certification_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nsf_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nsf_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_principal_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_principal_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_formation_initiale` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_apprentissage` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_formation_continue` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_contrat_professionnalisation` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_candidature_individuelle` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_acces_vae` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_blocs_competences` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].bloc_competences_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].bloc_competences_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_validation_partielle` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_rome` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].fap228_principale_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fap228_principale_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fap228_methode_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_fap228` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fap228_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].indice_tension_fap228_principale` | number ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tension_discret_fap228_principale` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tension_niveau_max` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_fap228_tension_4_et_plus` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tension_discret_par_fap228` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_ij_scolaire_sortants` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_scolaire_emploi_12m` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_ij_scolaire_emploi_12m` | chaîne / entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_apprentissage_sortants` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_apprentissage_emploi_12m` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_ij_apprentissage_emploi_12m` | chaîne / entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_scolaire_annee_terminale` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_scolaire_poursuite_etudes` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_ij_scolaire_poursuite_etudes` | nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_apprentissage_annee_terminale` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_ij_apprentissage_poursuite_etudes` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_ij_apprentissage_poursuite_etudes` | entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].promotion_insersup_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_insersup_diplomes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_insersup_emploi_salarie_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_insersup_emploi_salarie_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_insersup_diplomes_ensemble` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_insersup_poursuivants` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_insersup_poursuite_etudes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_insersup_salaire_base_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q1_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_median_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q3_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q1_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_median_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q3_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q1_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_median_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].salaire_insersup_q3_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_de_sortants` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_de_acces_emploi_6m` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_de_acces_emploi_6m` | chaîne / entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_de_abandons` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_de_abandons` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tag_renovation_energetique_batiment` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].thematique_reb_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_inscrits_voie_scolaire` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_inscrits_apprentissage` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_inscrits_enseignement_sup` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_inscrits_sanitaire_social` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_entrees_formation_de` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_examen_presents` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_examen_admis` | chaîne / entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_examen_reussite` | chaîne / entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_diplomes_enseignement_sup` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_sanitaire_social_presents` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_diplomes_sanitaire_social` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_sanitaire_social_reussite` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_affelnet_places` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_affelnet_voeux_1` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].indice_affelnet_pression` | entier / nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_parcoursup_places` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_parcoursup_candidatures` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_parcoursup_admis` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].indice_parcoursup_candidatures_par_place` | number ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/certifications/response_certifications.json](../../../02_reponses_observees/certifications/response_certifications.json).

### Appel 8 — GET `/mobilites`

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

### Appel 9 — GET `/prospective/regions`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `tri` | query | Facultatif Swagger | `string ; valeurs specificite, part_emploi, postes_a_pourvoir, tx_postes_a_pourvoir, desequilibre_potentiel, tx_desequilibre_potentiel, creations_nettes_emplois, tx_creations_nettes_emplois, departs_fin_carriere, tx_departs_fin_carriere, emplois_2019 ; défaut API "specificite"` | specificite/part_emploi ou tris documentés de /prospective/metiers |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_87_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_87_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_emplois_2019` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_part_emploi_region_2019` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].indice_specificite_region_2019` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_creations_nettes_emplois_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_creations_nettes_emplois_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_departs_fin_carriere_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_departs_fin_carriere_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_postes_a_pourvoir_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_postes_a_pourvoir_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_jeunes_debutants_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_jeunes_debutants_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_desequilibre_potentiel_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_desequilibre_potentiel_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tension_niveau_2019` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].territoire_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].fap_87_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].fap_87_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_emplois_2019` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_part_emploi_region_2019` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].indice_specificite_region_2019` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_creations_nettes_emplois_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_creations_nettes_emplois_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_departs_fin_carriere_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_departs_fin_carriere_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_postes_a_pourvoir_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_postes_a_pourvoir_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_jeunes_debutants_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_jeunes_debutants_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_desequilibre_potentiel_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tx_desequilibre_potentiel_2030` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].tension_niveau_2019` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.france[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/prospectiveregions/response_creations_nettes_emplois.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_creations_nettes_emplois.json); [02_reponses_observees/indicateurs/prospectiveregions/response_departs_fin_carriere.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_departs_fin_carriere.json); [02_reponses_observees/indicateurs/prospectiveregions/response_desequilibre_potentiel.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_desequilibre_potentiel.json); [02_reponses_observees/indicateurs/prospectiveregions/response_emplois_2019.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_emplois_2019.json); [02_reponses_observees/indicateurs/prospectiveregions/response_part_emploi.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_part_emploi.json); [02_reponses_observees/indicateurs/prospectiveregions/response_postes_a_pourvoir.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_postes_a_pourvoir.json); [02_reponses_observees/indicateurs/prospectiveregions/response_specificite.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_specificite.json); [02_reponses_observees/indicateurs/prospectiveregions/response_tx_creations_nettes_emplois.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_tx_creations_nettes_emplois.json); [02_reponses_observees/indicateurs/prospectiveregions/response_tx_departs_fin_carriere.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_tx_departs_fin_carriere.json); [02_reponses_observees/indicateurs/prospectiveregions/response_tx_postes_a_pourvoir.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_tx_postes_a_pourvoir.json); [02_reponses_observees/indicateurs/prospectiveregions/response_x_desequilibre_potentiel.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_x_desequilibre_potentiel.json).

### Appel 10 — GET `/salaires/secteurs`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 requis fonctionnellement |
| `region` | query | Facultatif Swagger | `string ; défaut API null` | code région ou omis=France |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].secteur_naf38_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].secteur_naf38_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_salaries_secteur` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_q1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_annuel_q3` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].salaire_net_mensuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tranche_salaire_median_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_salaries_temps_complet` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].maille` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].repli` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].fap_225_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].fap_225_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].salaire_net_annuel_q1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].salaire_net_annuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].salaire_net_annuel_q3` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].salaire_net_mensuel_median` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].tranche_salaire_median_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].nb_salaries_temps_complet` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].maille` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/response_salairessecteurs.json](../../../02_reponses_observees/indicateurs/response_salairessecteurs.json).

### Appel 11 — GET `/mesures`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

Aucun paramètre pour cet appel.

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

**Références conservées de la conception :** [02_reponses_observees/metiers/response_metiers{rome}competences.json](../../../02_reponses_observees/metiers/response_metiers{rome}competences.json); [01_sources/contrat_interface_2026-10-19.md](../../../01_sources/contrat_interface_2026-10-19.md).

**Contrôle local déjà rapporté :** Missions 002/009 ; choix/inversion/retours testés, deuxième série statistique absente. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E28 : Deux jeux complets ; familles identiques/différentes, mailles/périodes différentes ; tester `depuis`, sens inverse et catégories ; aucun score personnel.

**Points RCO associés :** Q04/Q06 : comparaison et métadonnées ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

**Réutilisation des mesures :** reprendre l’ensemble des sous-scénarios pertinents de [US-FON-008](US-FON-008.md), [US-FON-017](US-FON-017.md), [US-FON-023](US-FON-023.md), [US-FON-024](US-FON-024.md), [US-FON-025](US-FON-025.md), [US-FON-026](US-FON-026.md), avec deux réponses identifiées et des populations comparables. Une valeur absente pour B reste absente ; le tableau commun ne lui attribue jamais la valeur de A.

## 8. Critères d’acceptation

**US-FON-028-CA-01** — **Étant donné** les métiers A et B sont choisis depuis deux points d'entrée différents, **Quand** la comparaison est ouverte, **Alors** les titres et requêtes portent sur ces deux métiers et aucun exemple fixe ne remplit un côté.

**US-FON-028-CA-02** — **Étant donné** le métier B est comparé depuis A, **Quand** les compétences transférables sont demandées, **Alors** le GET cible B avec depuis=A et les tags, comptes et taux fournis sont expliqués comme relation entre métiers sans diagnostic personnel.

**US-FON-028-CA-03** — **Étant donné** la personne inverse A et B, **Quand** la comparaison directionnelle est actualisée, **Alors** le sens est inversé dans la requête ou son cache exact et les anciens tags ne sont pas présentés comme résultat du sens inverse.

**US-FON-028-CA-04** — **Étant donné** une fiche de compétences est limitée à une première page, **Quand** les éléments spécifiques sont consultés, **Alors** la liste est annoncée incomplète et aucune absence de compétence n'est affirmée avant collecte des pages nécessaires.

**US-FON-028-CA-05** — **Étant donné** les deux métiers partagent une même famille et une même mesure, **Quand** les statistiques sont affichées, **Alors** le caractère commun de l'observation est expliqué sans différence fabriquée.

**US-FON-028-CA-06** — **Étant donné** les deux valeurs ont des périodes ou lieux effectifs différents, **Quand** la comparaison de cet indicateur est consultée, **Alors** les limites restent visibles et aucune soustraction, variation ou rang global n'est calculé.

**US-FON-028-CA-07** — **Étant donné** un volet détaillé mobilité,2030 ou salaire sectoriel est demandé, **Quand** la personne ouvre son détail, **Alors** les informations natives des deux métiers restent accessibles avec leurs populations et limites, même si elles ne tiennent pas dans la synthèse initiale.

**US-FON-028-CA-08** — **Étant donné** une requête du métier B échoue, **Quand** la vue est rendue, **Alors** A reste lisible, B garde son identité et une erreur ciblée, et aucune donnée de A n'est recopiée sous B.

**US-FON-028-CA-09** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-028-CA-10** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Comparer 2 métiers, source et année de chaque donnée ; Comparateur complet par questions, accès détails mobilité/prospective/secteurs ; compétences communes et spécifiques sur listes complètes ; synthèse API directionnelle expliquée si utilisée ; Deux jeux complets ; familles identiques/différentes, mailles/périodes différentes ; tester `depuis`, sens inverse et catégories ; aucun score personnel ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E28` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : sélection explicite A/B, titres persistants, bouton inverser, navigation par questions et tableaux avec en-têtes de métier ; empilement mobile maintenant les labels A/B et les retours, pas une juxtaposition sans contexte.
- DSFR Chart DataBox et barres ou courbes officielles lorsque les dimensions permettent réellement la comparaison ; mêmes alternatives tabulaires, sources et états manquants des deux côtés ; pas de radar de score personnalisé.
- Changer un métier ou un filtre annonce le contexte actualisé ; commandes et détails restent utilisables au clavier, les informations ne dépendent ni de la couleur A/B ni du survol ; erreur et chargement par côté.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Comparateur complet de deux métiers ; Comparateur complet par questions, accès détails mobilité/prospective/secteurs ; compétences communes et spécifiques sur listes complètes ; synthèse API directionnelle expliquée si utilisée ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Choix libre de deux métiers depuis résultats, fiches ou pistes ; inversion ; comparaison limitée aux données des métiers choisis ; tous les détails restent accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Noindex comparateur personnalisé. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-028 — scénario, interactions et alternatives](svg/US-FON-028.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-028.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
