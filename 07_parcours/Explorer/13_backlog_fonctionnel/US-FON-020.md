# US-FON-020 — Explorer les certifications associées à un métier

**Rattachement :** E20 · alias historique US-E20. **Lot :** L2/L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05).

**État constaté au 2 novembre 2026 :** Filtrage par métier et voies documenté ; liste de certifications observée, mais tous les filtres et leurs combinaisons ne sont pas validés par traces HTTP. Les résultats locaux doivent rester rattachés aux requêtes et réponses disponibles, sans supposer une recherche générale opérationnelle.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de explorer les certifications associées à un métier, pour comprendre quelles certifications sont associées à un métier et repérer les voies d'accès ou la validation partielle qui répondent à mon projet. Je veux explorer les certifications associées à un métier et leurs voies d'accès.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite explorer les certifications associées à un métier, afin de comprendre quelles certifications sont associées à un métier et repérer les voies d'accès ou la validation partielle qui répondent à mon projet.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis une fiche métier, ouvre les diplômes et titres associés. | Recherche /certifications avec le ROME V3 de cette fiche et affiche les résultats actifs exposés, leurs intitulés, types et niveaux lorsqu'ils sont renseignés. |
| 2 | Choisit une voie d'accès ou une possibilité de validation partielle. | Traduit seulement les choix disponibles en acces et validation_partielle contractuels, avec le filtre repertoire si demandé, et réinitialise la pagination. |
| 3 | Parcourt les résultats filtrés et leurs pages. | Conserve les filtres visibles, charge les pages correspondantes et ne mélange pas les résultats d'anciennes requêtes. |
| 4 | Ouvre une certification. | Utilise son certifinfo_code exact, conserve le métier de départ et propose les deux intentions de consultation de la fiche Certification. |
| 5 | Examine les blocs, les résultats ou les sessions publiées. | Ouvre les volets existants de la certification sans présenter l'association au métier comme une obligation de diplôme ou une admission personnelle. |
| 6 | Revient aux certifications du métier ou change de filtre. | Restaure le bon métier, la liste et les filtres ; les pistes et le territoire restent disponibles. |

## 5. Scénarios alternatifs

- Aucun résultat après combinaison de filtres : afficher ce périmètre et permettre d'en retirer un, sans affirmer que le métier est inaccessible.
- Niveau absent, notamment pour certaines certifications RS : conserver la certification et annoncer niveau non renseigné, sans niveau inventé à partir de son titre.
- Une voie ou la validation partielle est inconnue : distinguer l'inconnu du refus, et ne pas construire une décision d'éligibilité.
- Erreur de requête ou de page : conserver le métier et les choix, expliquer l'état et proposer une reprise du seul appel concerné.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Le rattachement est fourni par /certifications?rome= ; ne pas rechercher des diplômes par ressemblance du nom du métier pour compléter la liste.
- acces utilise les seules voies documentées : formation_initiale, apprentissage, formation_continue, contrat_professionnalisation, candidature_individuelle et vae.
- validation_partielle est un booléen de filtre, distinct du détail des blocs ; repertoire distingue RNCP et RS sans les transformer en niveaux de qualité.
- Une certification associée n'est pas nécessairement obligatoire pour exercer et une voie déclarée ne garantit ni admission, financement ni disponibilité locale.
- Conserver la pagination, les états de données et les identifiants distincts Certif Info/fiche ; les résultats sont présentés par leurs noms plutôt que codes.

**Règles héritées conservées :** Association active, pas diplôme obligatoire ni éligibilité individuelle ; validation_partielle et acces sont filtres documentés.

**Traitements :** `/certifications?rome=...&page=...` ; compléments `acces`, `validation_partielle` ; Association active, pas diplôme obligatoire ni éligibilité individuelle ; validation_partielle et acces sont filtres documentés.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Association active, pas diplôme obligatoire ni éligibilité individuelle ; validation_partielle et acces sont filtres documentés.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Certif Info ; grain certification ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/certifications`

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

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [04_relations/CHAINES_APPELS_API.md](../../../04_relations/CHAINES_APPELS_API.md); [02_reponses_observees/certifications/response_certifications.json](../../../02_reponses_observees/certifications/response_certifications.json).

**Contrôle local déjà rapporté :** Liste locale et liens ; filtres d’accès/validation partielle HTTP à compléter. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E20 : ROME exact + filtres d'accès/validation, pages et RNCP/RS ; ne pas transformer en diplôme obligatoire.

**Points RCO associés :** Q09/Q10 : filtrage et validation partielle ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-020-CA-01** — **Étant donné** la personne consulte un métier choisi, **Quand** elle ouvre les certifications associées, **Alors** le GET utilise ce ROME exact et aucun résultat d'un autre métier n'est conservé sous le nouveau titre.

**US-FON-020-CA-02** — **Étant donné** la voie VAE et la validation partielle sont choisies, **Quand** la recherche est relancée, **Alors** les paramètres acces=vae et validation_partielle=true sont transmis avec rome et la pagination repart à un.

**US-FON-020-CA-03** — **Étant donné** une certification RS n'a pas de niveau renseigné, **Quand** les résultats sont présentés, **Alors** son intitulé reste ouvrable sans niveau déduit ni exclusion arbitraire.

**US-FON-020-CA-04** — **Étant donné** les filtres combinés ne donnent aucun résultat, **Quand** la liste est affichée, **Alors** un état explicite propose de modifier les filtres sans déclarer le métier inaccessible.

**US-FON-020-CA-05** — **Étant donné** une fiche a été ouverte depuis la liste filtrée, **Quand** la personne revient à la liste, **Alors** le métier, les filtres et la position utile sont restaurés.

**US-FON-020-CA-06** — **Étant donné** un rattachement métier-certification est publié, **Quand** le texte d'accompagnement est affiché, **Alors** il ne présente ni cette certification comme diplôme obligatoire ni la voie comme éligibilité individuelle.

**US-FON-020-CA-07** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-020-CA-08** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Pas de promesse de diplôme requis ; Certifications associées au métier, voies et validation partielle filtrables ; accès aux blocs/fiches/sessions ; ROME exact + filtres d'accès/validation, pages et RNCP/RS ; ne pas transformer en diplôme obligatoire ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E20` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : filtres nommés, liste de certifications, pagination, liens vers les fiches/blocs/sessions et retour métier ; états chargement, résultats, aucun résultat, liste partielle et erreur.
- Les filtres restent utilisables au clavier et sur mobile ; annoncer le nombre de résultats natif et les modifications sans recharger arbitrairement le focus ; aucun graphique nécessaire pour la liste documentaire.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Certifications associées au métier ; Certifications associées au métier, voies et validation partielle filtrables ; accès aux blocs/fiches/sessions ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Liens certifications. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-020 — scénario, interactions et alternatives](svg/US-FON-020.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-020.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
