# US-FON-030 — Passer d'un thème de formation aux certifications puis aux sessions

**Rattachement :** E30 · alias historique US-E30. **Lot :** L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05) ou [US-FON-017](US-FON-017.md) (E17);[US-FON-020](US-FON-020.md) (E20) pour chaîne;[US-FON-021](US-FON-021.md) (E21)/[US-FON-022](US-FON-022.md) (E22) pour sessions.

**État constaté au 2 novembre 2026 :** Contrat, référentiel Formacode et JSON observés ; la chaîne complète thème-certifications-détail-sessions reste à capturer avec des GET tracés. Le besoin de sessions non certifiantes par thème est réellement non couvert par les 21 GET et n'est pas comblé par une autre source.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de passer d'un thème de formation aux certifications puis aux sessions, pour explorer les thèmes liés à un métier ou une certification et suivre les formations certifiantes publiées jusqu'aux sessions disponibles dans les données. Je veux passer d'un thème de formation aux certifications puis aux sessions exposées.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite passer d'un thème de formation aux certifications puis aux sessions, afin d’explorer les thèmes liés à un métier ou une certification et suivre les formations certifiantes publiées jusqu'aux sessions disponibles dans les données.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Le thème, la certification et la session restent des objets distincts ; les liens utilisent les identifiants reçus.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis un métier ou une certification, ouvre les thèmes de formation associés, ou recherche un thème par son nom. | Interroge /formacodes avec le code, le métier, le domaine Formacode ou q adaptés à l'entrée et affiche les libellés reçus. |
| 2 | Choisit un thème et consulte son contexte. | Présente son sous-domaine, son domaine et ses marqueurs documentés, avec les nombres de certifications reçus lorsqu'ils sont renseignés. |
| 3 | Demande les certifications de ce thème. | Appelle /certifications avec le formacode_code sélectionné, affiche les résultats paginés et ne remplace pas les résultats par une certification d'exemple. |
| 4 | Choisit une certification. | Ouvre son détail par certifinfo_code, conserve le thème de départ et les actions de retour, puis expose voies, blocs et résultats disponibles. |
| 5 | Souhaite voir les sessions publiées pour cette certification et choisit un lieu compatible. | Utilise le Certif Info choisi avec /sessions_a_venir ou /sessions_en_cours, les paramètres de zonage compatibles et la gestion Onisep documentée. |
| 6 | Revient au thème ou explore une autre certification. | Restaure les choix et pages utiles, garde les pistes métier et distingue toujours thème, certification et ligne de session. |

## 5. Scénarios alternatifs

- Thème sans certification retournée : conserver son information et expliquer qu'aucune certification n'est publiée dans ce résultat, sans créer une session directement depuis le thème.
- Recherche de thème ambiguë : afficher sous-domaines et domaines nommés pour choisir explicitement, sans fusion de codes homonymes.
- Certification sans session pour le lieu retenu : garder la fiche et permettre de modifier le territoire ou la vue, sans remplacer le thème par une offre externe.
- Données de rattachement ou nombres absents : afficher ce qui est reçu sans déduire un total depuis une page partielle.
- Erreur d'un maillon : conserver les étapes déjà choisies et reprendre ce GET, sans sauter vers une fiche ou une session supposée correspondante.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Le Formacode est un thème de formation ; son domaine n'est ni un domaine professionnel ROME ni un domaine de compétences, malgré le paramètre domaine homonyme.
- Utiliser uniquement les associations et codes renvoyés : Formacode vers /certifications?formacode=, puis Certif Info vers fiche et sessions ; aucune relation thème-session directe n'est inventée.
- Les nombres nb_certifications et nb_certifications_formacode_principal sont documentés et distincts ; ne pas déduire un nombre complet de certifications depuis une première page.
- Les thèmes non certifiants peuvent être mentionnés dans le référentiel, mais les 21 GET n'exposent pas de recherche de sessions non certifiantes par Formacode ; conserver et expliquer ce besoin non couvert.
- Les sessions conservent leurs précautions de regroupement, lieu, temporalité, Onisep et Q11 ; un thème n'atteste ni admission, ni financement, ni compétence personnelle.

**Règles héritées conservées :** Formacode V14 thème et non offre/session ; aucune session non certifiante par Formacode exposée.

**Traitements :** `/formacodes?rome=...` ou `code=...` → `/certifications?formacode=...` → détail/session par Certif Info ; Formacode V14 thème et non offre/session ; aucune session non certifiante par Formacode exposée.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Formacode V14 thème et non offre/session ; aucune session non certifiante par Formacode exposée.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Formacode V14 ; grain thème formation ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/formacodes`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | V3 facultatif |
| `code` | query | Facultatif Swagger | `string ; défaut API null` | Formacode3–5chiffres facultatif |
| `domaine` | query | Facultatif Swagger | `string ; défaut API null` | domaine Formacode distinct de Domaine ROME |
| `q` | query | Facultatif Swagger | `string ; défaut API null ; minLength=2 ; maxLength=100` | 2–100 facultatif |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].formacode_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].sous_domaine_formacode_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].sous_domaine_formacode_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_formacode_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_formacode_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_numerique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_sanitaire_social` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_certifications` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_certifications_formacode_principal` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/certifications/response_formacode.json](../../../02_reponses_observees/certifications/response_formacode.json).

### Appel 2 — GET `/certifications`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `formacode` | query | Facultatif Swagger | `string ; défaut API null` | code renvoyé par /formacodes |
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

### Appel 3 — GET `/certifications/{certifinfo}`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `certifinfo` | path | Requis Swagger | `string` | chemin string numérique Certif Info |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.certifinfo_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.certifinfo_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.etat_certifinfo_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.type_certification_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.certificateur_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.repertoire_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.fiche_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.fiche_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.type_enregistrement_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.date_fin_enregistrement` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.niveau_certification_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nsf_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nsf_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.formacode_principal_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.formacode_principal_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.formacode_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.formacode_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_formation_initiale` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_apprentissage` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_formation_continue` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_contrat_professionnalisation` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_candidature_individuelle` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_acces_vae` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_blocs_competences` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.bloc_competences_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.bloc_competences_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.tag_validation_partielle` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_rome` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.rome_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.fap228_principale_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.fap228_principale_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.fap228_methode_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_fap228` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.fap228_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.indice_tension_fap228_principale` | number ou null | Type OpenAPI officiel ; chemin observé |
| `$.tension_discret_fap228_principale` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.tension_niveau_max` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_fap228_tension_4_et_plus` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.tension_discret_par_fap228` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_ij_scolaire_sortants` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_scolaire_emploi_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_ij_scolaire_emploi_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_apprentissage_sortants` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_apprentissage_emploi_12m` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_ij_apprentissage_emploi_12m` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_scolaire_annee_terminale` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_scolaire_poursuite_etudes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_ij_scolaire_poursuite_etudes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_apprentissage_annee_terminale` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_ij_apprentissage_poursuite_etudes` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_ij_apprentissage_poursuite_etudes` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.promotion_insersup_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_insersup_diplomes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_insersup_emploi_salarie_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_insersup_emploi_salarie_12m` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_insersup_diplomes_ensemble` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_insersup_poursuivants` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_insersup_poursuite_etudes` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_insersup_salaire_base_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q1_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_median_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q3_12m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q1_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_median_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q3_18m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q1_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_median_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.salaire_insersup_q3_30m` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_de_sortants` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_de_acces_emploi_6m` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_de_acces_emploi_6m` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_de_abandons` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_de_abandons` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tag_renovation_energetique_batiment` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.thematique_reb_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_inscrits_voie_scolaire` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_inscrits_apprentissage` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_inscrits_enseignement_sup` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_inscrits_sanitaire_social` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_entrees_formation_de` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_examen_presents` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_examen_admis` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_examen_reussite` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_diplomes_enseignement_sup` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_sanitaire_social_presents` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_diplomes_sanitaire_social` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.tx_sanitaire_social_reussite` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_affelnet_places` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_affelnet_voeux_1` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.indice_affelnet_pression` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.nb_parcoursup_places` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_parcoursup_candidatures` | integer ou null | Type OpenAPI officiel ; chemin observé |
| `$.nb_parcoursup_admis` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.indice_parcoursup_candidatures_par_place` | number ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/certifications/response_certifications-certifinfo.json](../../../02_reponses_observees/certifications/response_certifications-certifinfo.json).

### Appel 4 — GET `/sessions_a_venir`

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

### Appel 5 — GET `/sessions_en_cours`

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

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/sessions/response_sessions_en_cours.json](../../../02_reponses_observees/sessions/response_sessions_en_cours.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/certifications/response_formacode.json](../../../02_reponses_observees/certifications/response_formacode.json); [04_relations/CHAINES_APPELS_API.md](../../../04_relations/CHAINES_APPELS_API.md).

**Contrôle local déjà rapporté :** Thèmes disponibles localement ; chaîne filtrée complète à capturer. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E30 : Chaîne complète capturée, pagination et thème sans certification ; pas d'accès sessions non certifiantes par Formacode.

**Points RCO associés :** Q10 : couverture des associations et filtres ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-030-CA-01** — **Étant donné** un thème est choisi depuis un métier, **Quand** les certifications sont demandées, **Alors** le formacode_code réellement reçu est transmis au filtre formacode et non un code de domaine métier.

**US-FON-030-CA-02** — **Étant donné** un thème et un domaine ont des noms voisins, **Quand** les résultats sont affichés, **Alors** les libellés et hiérarchies permettent un choix explicite sans correspondance supposée entre les référentiels.

**US-FON-030-CA-03** — **Étant donné** la liste des certifications est paginée, **Quand** la personne poursuit la consultation, **Alors** les pages restent rattachées au thème choisi et aucun total n'est calculé depuis la seule page reçue.

**US-FON-030-CA-04** — **Étant donné** un thème n'a pas de certification retournée, **Quand** la personne recherche des sessions, **Alors** le besoin non couvert est expliqué et aucune requête sessions par Formacode ou offre fictive n'est créée.

**US-FON-030-CA-05** — **Étant donné** une certification du thème est choisie, **Quand** la personne ouvre ses sessions, **Alors** le Certif Info de cette certification et un territoire compatible pilotent la route existante avec la dépendance Q11 conservée.

**US-FON-030-CA-06** — **Étant donné** la personne revient depuis une certification à son thème, **Quand** le retour est activé, **Alors** le thème, la recherche et les filtres utiles sont restaurés sans perdre les pistes.

**US-FON-030-CA-07** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-030-CA-08** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Ne pas promettre de session à partir du seul thème ; Thèmes de formation → certifications → sessions publiées ; thème distinct d'une offre de formation ; garder les thèmes sans certification visible ; Chaîne complète capturée, pagination et thème sans certification ; pas d'accès sessions non certifiantes par Formacode ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E30` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : recherche de thème, résultats nommés et hiérarchie lisible, liens de certifications, pagination et retours contextuels ; états thème connu, sans certification, sans session, partiel et erreur.
- Pas de graphique obligatoire pour une chaîne documentaire ; parcours clavier et mobile sans code imposé, annonce du contexte à chaque changement et aide expliquant les trois objets thème, certification, session.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Thèmes Formacode et certifications ; Thèmes de formation → certifications → sessions publiées ; thème distinct d'une offre de formation ; garder les thèmes sans certification visible ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Contenu thématique. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-030 — scénario, interactions et alternatives](svg/US-FON-030.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-030.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
