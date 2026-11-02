# US-FON-017 — Comprendre une certification et ses résultats

**Rattachement :** E17 · alias historique US-E17. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-002](US-FON-002.md) (E02)/[US-FON-020](US-FON-020.md) (E20)/[US-FON-030](US-FON-030.md) (E30) selon entrée;[US-FON-031](US-FON-031.md) (E31).

**État constaté au 2 novembre 2026 :** Détail et statistiques documentés, avec JSON observés ; la maquette utilise ces observations et ne démontre pas la disponibilité HTTP générale des certifications, des populations ou des promotions. Les tests RNCP/RS, multi-métiers, null/secrets et introuvables restent nécessaires ; aucune réduction de la fiche cible.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comprendre une certification et ses résultats, pour examiner un diplôme ou un titre, que je le possède déjà ou souhaite l'obtenir, pour comprendre ses voies d'accès, les métiers associés et les résultats des populations suivies. Je veux examiner une certification selon que je la possède ou souhaite l'obtenir.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comprendre une certification et ses résultats, afin d’examiner un diplôme ou un titre, que je le possède déjà ou souhaite l'obtenir, pour comprendre ses voies d'accès, les métiers associés et les résultats des populations suivies.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- La certification est reconnue par certifinfo_code ; l’intention de consultation est distincte de cette identité.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre la certification choisie depuis les résultats, un métier ou un thème de formation. | Charge le détail avec le certifinfo_code sélectionné et affiche son intitulé, son type, le certificateur, son état et les informations d'enregistrement réellement reçues. |
| 2 | Indique je possède cette certification ou je souhaite l'obtenir. | Adapte les questions et les actions proposées à cette intention sans changer de certification ni inventer des données personnelles, de nouvelles associations ou des droits. |
| 3 | Consulte les voies d'accès et les possibilités de validation partielle. | Présente les voies déclarées avec leur état renseigné ou inconnu, les blocs publiés lorsqu'ils existent, et les liens vers leur détail. |
| 4 | Choisit les résultats qui correspondent à la population qu'elle souhaite comprendre. | Distingue scolaire, apprentissage, supérieur et demandeurs d'emploi, puis emploi, poursuite d'études, réussite, effectifs et demande de formation, avec les bases et périodes propres. |
| 5 | Ouvre les salaires après un diplôme du supérieur. | Affiche les quartiles et médianes mensuels disponibles à douze, dix-huit et trente mois, en distinguant les promotions et la base réellement fournie à douze mois. |
| 6 | Poursuit vers un métier, un bloc, un thème ou des sessions publiées. | Utilise les identifiants de la certification courante pour ouvrir la bonne ressource et conserve l'intention, le lieu choisi et la navigation de retour. |

## 5. Scénarios alternatifs

- Certification introuvable ou inactive : conserver la recherche et les sélections, expliquer que cette fiche n'est pas disponible et ne pas substituer une certification de même nom ou une archive non exposée.
- Une seule population statistique est renseignée : afficher ses résultats avec leur périmètre ; les autres volets restent identifiables comme non renseignés sans valeur de remplacement.
- Un résultat vaut secret_stat, null, zéro ou est absent : appliquer le sens propre à chaque état et le conserver dans l'alternative tabulaire.
- Changement d'intention ou de certification pendant un chargement : annuler la réponse devenue périmée et ne jamais afficher les résultats de la fiche précédente sous le nouveau titre.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. 404 peut concerner certification inactive, aucune archive présumée. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Les deux intentions sont des modes de consultation : posséder une certification ne prouve ni maîtrise de toutes les compétences ni droit automatique d'exercer, et souhaiter l'obtenir ne démontre pas une admission ou un financement.
- Les certifications accessibles sont celles exposées par les GET existants ; utiliser l'état reçu et ne pas déduire seul le statut actif d'une date de fin d'enregistrement.
- Les résultats nationaux gardent source, population, base, millésime et horizon ; InserJeunes scolaire/apprentissage, InserSup et accès à l'emploi des demandeurs d'emploi restent distincts.
- Les salaires InserSup à douze et dix-huit mois concernent les diplômés 2022 et ceux à trente mois les diplômés 2021 dans le catalogue observé ; ne pas tracer une progression individuelle ou réutiliser la promotion des taux d'emploi.
- Les métiers, blocs et thèmes proviennent des listes associées reçues ; aucun résultat national de certification n'est attribué à une session ou à un organisme local.

**Règles héritées conservées :** Toutes mesures nationales par population : IJ scolaire/apprentissage distincts, InserSup et DE distincts ; emploi12m/acces6m/poursuite/réussite/salaires/admissions non fusionnés ; millésimes MES propres, secrets et promotions conservés.

**Traitements :** `/certifications/{certifinfo}`, MES pour définitions/périodes ; Toutes mesures nationales par population : IJ scolaire/apprentissage distincts, InserSup et DE distincts ; emploi12m/acces6m/poursuite/réussite/salaires/admissions non fusionnés ; millésimes MES propres, secrets et promotions conservés.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Toutes mesures nationales par population : IJ scolaire/apprentissage distincts, InserSup et DE distincts ; emploi12m/acces6m/poursuite/réussite/salaires/admissions non fusionnés ; millésimes MES propres, secrets et promotions conservés.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Certif Info/France compétences et producteurs par mesure du catalogue MES ; grain certification ; période Par mesure MES et promotion, pas de millésime uniforme. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/certifications/{certifinfo}`

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

### Appel 2 — GET `/mesures`

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

**Références conservées de la conception :** [02_reponses_observees/certifications/response_certifications-certifinfo.json](../../../02_reponses_observees/certifications/response_certifications-certifinfo.json); [02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json).

**Contrôle local déjà rapporté :** Recette certification et indicateurs locaux ; plusieurs cohortes ont des valeurs null. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E17 : Cas RNCP/RS, multi-ROME, champs null/secrets, anciennes certifications introuvables ; tests des populations et promotions.

**Points RCO associés :** Q09 : cycle actif, périodes/coverage insertion ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

### Couverture détaillée des 11 mesures rattachées à cette US

Chaque mesure est un sous-scénario de cette US. Ses champs, sa population et ses critères sont conservés même si aucune valeur n’est publiée dans le jeu local.

#### `tension_fap228_principale` — Tension de la FAP principale

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `fap_228`. **Mailles du catalogue :** nat. **Millésime observé :** 2024.

**Producteur :** Certif Info (RCO) ; DARES - France Travail. **Unité et population :** Indice de tension sans unité et niveaux discrets publiés ; nombres de familles ; aucune unité en pourcentage.

**Définition source :** Tension nationale (indice et niveau discret 1 à 5.2) de la FAP 228 principale de la certification : FAP atteinte par le plus de ROME V3 de la certification compatibles avec son niveau, puis plus fort emploi moyen.

**Champs nécessaires :** `$.fap228_principale_code`, `$.fap228_principale_libelle`, `$.fap228_methode_libelle`, `$.indice_tension_fap228_principale`, `$.tension_discret_fap228_principale`, `$.tension_niveau_max`, `$.nb_fap228_tension_4_et_plus`, `$.tension_discret_par_fap228`.

**Présentation attendue :** DSFR : encadré explicatif de la famille principale et tableau des niveaux des familles associées ; pas de jauge de chance personnelle.

- Afficher fap228_principale_libelle, fap228_methode_libelle, indice_tension_fap228_principale et tension_discret_fap228_principale avec leur signification nationale et le millésime 2024 observé.
- La FAP principale est choisie par les rattachements ROME compatibles avec le niveau, puis l'emploi moyen ; ne pas la présenter comme l'unique métier accessible grâce à la certification.
- Les niveaux discrets1,2,3,4,5.1,5.2 sont des catégories ; tension_niveau_max et nb_fap228_tension_4_et_plus ne doivent pas devenir une probabilité d'emploi.
- Lire tension_discret_par_fap228 selon son format contractuel code:niveau séparé par virgules ; ne pas inventer un nom de famille absent ni une relation famille-vers-ROME.
- Distinguer cet indicateur national de certification des tensions territoriales d'un métier ; ne pas projeter son niveau sur une session locale.

**Dépendance / tests :** Catalogue observé : fap_228, 2024, nat. Champs à la racine de /certifications/{certifinfo} ou sous items[] de /certifications. Les libellés de catégories doivent s'appuyer sur le contrat, pas sur une échelle créée pour l'interface.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `insertion_inserjeunes` — Taux d'emploi à 12 mois et poursuite d'études (InserJeunes)

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** Cumul 2023-2024.

**Producteur :** DEPP - DARES, InserJeunes. **Unité et population :** Effectifs de sortants en emploi salarié à douze mois et d'inscrits en année terminale poursuivant leurs études ; pourcentages sur leurs bases respectives.

**Définition source :** Part des sortants en emploi salarié 12 mois après la sortie, et part des inscrits en année terminale qui poursuivent leurs études l'année suivante (inscrits = poursuivants + sortants), voie scolaire et apprentissage, agrégées au niveau national.

**Champs nécessaires :** `$.nb_ij_scolaire_sortants`, `$.nb_ij_scolaire_emploi_12m`, `$.tx_ij_scolaire_emploi_12m`, `$.nb_ij_apprentissage_sortants`, `$.nb_ij_apprentissage_emploi_12m`, `$.tx_ij_apprentissage_emploi_12m`, `$.nb_ij_scolaire_annee_terminale`, `$.nb_ij_scolaire_poursuite_etudes`, `$.tx_ij_scolaire_poursuite_etudes`, `$.nb_ij_apprentissage_annee_terminale`, `$.nb_ij_apprentissage_poursuite_etudes`, `$.tx_ij_apprentissage_poursuite_etudes`.

**Présentation attendue :** DSFR Chart DataBox et barres scolaires/apprentis séparées par objectif emploi ou études ; tableau DSFR des effectifs, bases et taux.

- Présenter séparément voie scolaire et apprentissage, au niveau national pour la certification, cumul 2023-2024 observé.
- Le taux d'emploi salarié à douze mois utilise les sortants ; le taux de poursuite d'études utilise les inscrits en année terminale, qui regroupent poursuivants et sortants.
- Conserver les douze champs nb_ij_* et tx_ij_* disponibles, sans moyenne des voies ni complément calculé entre emploi et études.
- Les effectifs et taux peuvent être secret_stat ; aucune différence ou conversion en nombre sur cent ne reconstitue une valeur protégée.
- Un résultat national historique de certification ne mesure ni la qualité d'un organisme local, ni les résultats d'une session, ni la chance individuelle d'obtenir un emploi.

**Dépendance / tests :** Catalogue observé : certification, Cumul 2023-2024, nat. Couverture de la voie professionnelle définie par InserJeunes ; ne pas compléter une absence avec InserSup ou un taux demandeurs d'emploi. Tester RNCP/RS, populations disponibles et secrets.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `insertion_insersup` — Taux d'emploi salarié à 12 mois et poursuite d'études (InserSup)

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2025_S2 (diplômés 2024).

**Producteur :** SIES, InserSup. **Unité et population :** Diplômés, diplômés sortants en emploi salarié à douze mois et diplômés poursuivants ; pourcentages sur les populations propres à chaque résultat.

**Définition source :** Part des diplômés sortis des études en emploi salarié 12 mois après le diplôme, et part des diplômés qui poursuivent leurs études (diplômés = sortants + poursuivants), toutes populations, niveau national (lignes « National » de la source ; plusieurs diplômes SISE d'une même certification additionnés). Promotion 2024, ou cumul 2023/2024 pour un diplôme de moins de 20 sortants (`promotion_insersup_libelle`).

**Champs nécessaires :** `$.promotion_insersup_libelle`, `$.nb_insersup_diplomes`, `$.nb_insersup_emploi_salarie_12m`, `$.tx_insersup_emploi_salarie_12m`, `$.nb_insersup_diplomes_ensemble`, `$.nb_insersup_poursuivants`, `$.tx_insersup_poursuite_etudes`.

**Présentation attendue :** DSFR Chart DataBox et deux lectures distinctes emploi et poursuite d'études ; tableau DSFR avec promotion_insersup_libelle et bases.

- Conserver promotion_insersup_libelle : promotion 2024 ou cumul 2023/2024 pour un diplôme de moins de vingt sortants, selon le catalogue 2025_S2 observé.
- nb_insersup_diplomes désigne les sortants hors poursuivants et sert de base à l'emploi salarié à douze mois ; nb_insersup_diplomes_ensemble inclut sortants et poursuivants pour la poursuite d'études.
- Les données sont nationales et peuvent additionner plusieurs diplômes SISE d'une certification côté source ; ne pas les recalculer depuis d'autres certifications ni attribuer ce total à une session.
- Préserver les effectifs et taux reçus, y compris secret_stat et null ; ne pas calculer taux d'emploi, taux de poursuite ou complément manquant.
- Ne pas confondre cette promotion avec celles des salaires InserSup à douze, dix-huit et trente mois, ni comparer les voies comme une même cohorte.

**Dépendance / tests :** Catalogue observé : certification, 2025_S2 (diplômés 2024), nat ; promotion réelle lue dans le champ reçu. Q09 : variantes à tester, définitions déjà documentées ; Q06 pour règle du secret.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `salaires_insersup` — Salaire des diplômés (InserSup)

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2025_S2 (diplômés 2021 et 2022).

**Producteur :** SIES, InserSup. **Unité et population :** Euros nets par mois pour les quartiles et médianes ; diplômés en emploi salarié pour la base de salaire à douze mois.

**Définition source :** Quartiles et médiane du salaire mensuel net des diplômés en emploi salarié, 12 et 18 mois après le diplôme (promotion 2022) et 30 mois après (promotion 2021), niveau national. Diplômes de l'enseignement supérieur suivis par InserSup (licence, licence professionnelle, master, ingénieur, écoles de management) ; publiés à partir de 20 diplômés en emploi. Une certification couvrant plusieurs diplômes SISE prend celui qui compte le plus de diplômés en emploi salarié.

**Champs nécessaires :** `$.nb_insersup_salaire_base_12m`, `$.salaire_insersup_q1_12m`, `$.salaire_insersup_median_12m`, `$.salaire_insersup_q3_12m`, `$.salaire_insersup_q1_18m`, `$.salaire_insersup_median_18m`, `$.salaire_insersup_q3_18m`, `$.salaire_insersup_q1_30m`, `$.salaire_insersup_median_30m`, `$.salaire_insersup_q3_30m`.

**Présentation attendue :** DSFR : tableau de quartiles mensuels par horizon avec promotions explicites ; DSFR Chart DataBox et barres de médianes séparées par cohorte, sans courbe de progression individuelle.

- Afficher les Q1/médiane/Q3 à douze et dix-huit mois pour les diplômés 2022, et à trente mois pour les diplômés 2021, d'après la diffusion 2025_S2 observée.
- Ces montants sont mensuels nets, distincts des quartiles annuels BTS des métiers ; aucun passage annuel/mensuel n'est calculé.
- Population : diplômés en emploi salarié des diplômes du supérieur suivis par InserSup ; publication à partir de vingt diplômés en emploi.
- Si une certification couvre plusieurs diplômes SISE, la source choisit celui ayant le plus de diplômés en emploi salarié ; ne pas agréger les salaires des diplômes côté consommateur.
- nb_insersup_salaire_base_12m est la base à douze mois, pas une base démontrée aux autres horizons ; Q1/Q3 ne sont ni minimum/maximum ni une trajectoire de la même personne.

**Dépendance / tests :** Catalogue observé : certification, 2025_S2 (diplômés 2021 et 2022), nat. Les promotions de salaires diffèrent de l'insertion 2024 ; conserver toute la dispersion disponible, sans donnée personnalisée.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `insertion_demandeurs_emploi` — Accès à l'emploi à 6 mois et abandons des demandeurs d'emploi formés

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2024.

**Producteur :** France Travail, sortants de formation. **Unité et population :** Demandeurs d'emploi sortis de formation, ayant accédé à l'emploi dans les six mois, ou ayant abandonné ; taux publiés en pourcentage.

**Définition source :** Part des demandeurs d'emploi sortis de formation ayant accédé à l'emploi dans les 6 mois, et part de ceux qui ont abandonné la formation avant son terme.

**Champs nécessaires :** `$.nb_de_sortants`, `$.nb_de_acces_emploi_6m`, `$.tx_de_acces_emploi_6m`, `$.nb_de_abandons`, `$.tx_de_abandons`.

**Présentation attendue :** DSFR Chart DataBox et barres distinctes accès à l'emploi et abandon ; tableau DSFR avec effectifs, base nb_de_sortants et taux reçus.

- Population nationale de demandeurs d'emploi sortis de formation en 2024 observée ; utiliser nb_de_sortants, nb_de_acces_emploi_6m et tx_de_acces_emploi_6m.
- L'accès à l'emploi dans les six mois ne signifie pas être en emploi salarié exactement au sixième mois ; ne pas l'assimiler à l'emploi InserJeunes/InserSup à douze mois.
- Conserver nb_de_abandons et tx_de_abandons séparément de l'accès à l'emploi ; les deux résultats ne constituent pas deux catégories complémentaires à additionner.
- Traiter les effectifs et taux secret_stat sans calcul de complément ni taux reconstitué ; null n'est pas zéro ni absence d'accès à l'emploi.
- Une observation de certification nationale ne renseigne ni une session actuelle ni une probabilité d'insertion personnelle.

**Dépendance / tests :** Catalogue observé : certification, 2024, nat. Tester secrets et absence par certification ; conserver les cinq champs natifs et le libellé de population. Q06 porte sur les règles du secret.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `inscrits` — Inscrits en formation

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** Rentrée 2023 (DEPP), rentrée 2024 (SIES, DREES), 2025 (France Travail).

**Producteur :** DEPP ; SIES ; DREES ; France Travail, entrées en formation. **Unité et population :** Personnes inscrites par voie, ou entrées en formation de demandeurs d'emploi ; aucun pourcentage commun.

**Définition source :** Inscrits dans la formation, au niveau national, par voie : voie scolaire et apprentissage (toutes années de la formation), enseignement supérieur, formations sanitaires et sociales, entrées en formation des demandeurs d'emploi. Les effectifs d'une version archivée de la certification sont rattachés à la version active (filiation Certif Info).

**Champs nécessaires :** `$.nb_inscrits_voie_scolaire`, `$.nb_inscrits_apprentissage`, `$.nb_inscrits_enseignement_sup`, `$.nb_inscrits_sanitaire_social`, `$.nb_entrees_formation_de`.

**Présentation attendue :** DSFR : tableau par filière avec millésime et source ; cartes de chiffres ou barres DSFR Chart à lecture séparée, sans total toutes filières.

- Conserver les inscrits scolaire et apprentissage(DEPP,rentrée 2023), supérieur(SIES,rentrée 2024), sanitaire-social(DREES,rentrée 2024) et entrées de demandeurs d'emploi(FranceTravail,2025), selon le catalogue observé.
- Les inscrits scolaire/apprentissage couvrent toutes les années de formation ; les entrées DE sont des entrées en formation et ne sont pas un stock d'inscrits de même nature.
- Les effectifs sont nationaux, par certification ; ne pas les distribuer entre organismes, territoires ou sessions ni additionner des années/populations différentes.
- La filiation Certif Info rattache les effectifs de versions archivées à la version active ; ne pas inventer une route d'archive ni additionner une ancienne et une nouvelle version.
- secret_stat reste non diffusable ; chaque valeur nulle ou absente est expliquée selon la couverture, sans inventer un effectif manquant.

**Dépendance / tests :** Catalogue observé : certification, rentrée 2023 DEPP/rentrée 2024 SIES-DREES/2025 FranceTravail, nat. Les grandes différences de volume ne classent pas la qualité de la certification ; tester la filiation sans créer de consultation d'archive.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `diplomes` — Diplômés et réussite aux examens

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** Session 2023 (DEPP, SIES), 2024 (DREES).

**Producteur :** DEPP, résultats aux examens ; SIES ; DREES. **Unité et population :** Candidats présents, admis et diplômés selon la filière ; taux de réussite en pourcentage des présents pour les examens concernés.

**Définition source :** Présents, admis et taux de réussite aux examens de l'Éducation nationale (CAP, bac professionnel, BTS…, toutes situations de candidats) et aux diplômes sanitaires et sociaux ; diplômés de l'enseignement supérieur. Niveau national ; filiation Certif Info appliquée.

**Champs nécessaires :** `$.nb_examen_presents`, `$.nb_examen_admis`, `$.tx_examen_reussite`, `$.nb_diplomes_enseignement_sup`, `$.nb_sanitaire_social_presents`, `$.nb_diplomes_sanitaire_social`, `$.tx_sanitaire_social_reussite`.

**Présentation attendue :** DSFR : tableau par population d'examen ; DSFR Chart DataBox et barres des taux fournis, avec bases et sessions distinctes.

- Séparer examens Éducation nationale : nb_examen_presents, nb_examen_admis, tx_examen_reussite ; supérieur : nb_diplomes_enseignement_sup ; sanitaire-social : nb_sanitaire_social_presents, nb_diplomes_sanitaire_social, tx_sanitaire_social_reussite.
- Les sessions observées sont 2023 pour DEPP/SIES et 2024 pour DREES, nationales ; ne pas fusionner les années et populations en un taux global.
- Les examens de l'Éducation nationale couvrent toutes situations de candidats, dont scolaire, apprentissage, formation continue et individuel ; ce n'est pas une cohorte de seuls inscrits de la mesure inscrits.
- Conserver les taux de réussite reçus, sans calcul d'abandon, de rendement diplômés/inscrits ou de taux du supérieur non fourni.
- Respecter secret_stat et la filiation Certif Info appliquée par la source ; un diplômé compté n'est ni une admission future ni un accès automatique au métier.

**Dépendance / tests :** Catalogue observé : certification, Session 2023(DEPP,SIES),2024(DREES), nat. Tester les certifications ne couvrant qu'une des sources et les groupes protégés ; ne pas comparer ces résultats aux inscrits d'une autre rentrée.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `attractivite` — Attractivité de la formation

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** Rentrée 2025 (Affelnet), session 2025 (Parcoursup).

**Producteur :** DGESCO, Affelnet ; MESR, Parcoursup. **Unité et population :** Places, vœux de rang un, candidatures et admis ; indice Affelnet en vœux de rang un par place ; indice Parcoursup en candidatures par place, sans unité en pourcentage.

**Définition source :** Demande rapportée aux places : vœux de rang 1 par place dans Affelnet (voie scolaire après la 3e) et candidatures par place dans Parcoursup (un candidat compte dans chaque formation où il postule). Niveau national ; filiation Certif Info appliquée.

**Champs nécessaires :** `$.nb_affelnet_places`, `$.nb_affelnet_voeux_1`, `$.indice_affelnet_pression`, `$.nb_parcoursup_places`, `$.nb_parcoursup_candidatures`, `$.nb_parcoursup_admis`, `$.indice_parcoursup_candidatures_par_place`.

**Présentation attendue :** DSFR : deux encadrés Affelnet/Parcoursup avec définitions et tableau des nombres/indices ; DSFR Chart DataBox et barres seulement sur une même nature d'indice.

- Distinguer Affelnet(voie scolaire après la troisième) : nb_affelnet_places, nb_affelnet_voeux_1, indice_affelnet_pression ; Parcoursup : nb_parcoursup_places, nb_parcoursup_candidatures, nb_parcoursup_admis, indice_parcoursup_candidatures_par_place.
- Les indices reçus sont des rapports de demandes par place, pas des pourcentages ni une probabilité personnelle d'admission ; ne pas recalculer le rapport avec d'autres effectifs.
- Un candidat Parcoursup compte dans chaque formation où il postule ; candidatures n'est pas un nombre de personnes uniques.
- Conserver le niveau national et les références observées rentrée 2025 Affelnet/session 2025 Parcoursup ; ne pas attribuer ces places à des sessions locales actuellement disponibles.
- Ne pas fusionner les indices Affelnet et Parcoursup ni les transformer en score de popularité ou de qualité ; la filiation des versions est celle appliquée par la source.

**Dépendance / tests :** Catalogue observé : certification, Rentrée 2025 Affelnet/session 2025 Parcoursup, nat. Aucun calcul de sélectivité individuelle ni mécanisme d'inscription n'est couvert par les 21 GET. Tester sources absentes et présentation des indices sans signe%.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `voies_acces` — Voies d'accès, VAE et validation partielle

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2026.

**Producteur :** France compétences, RNCP et RS (via Certif Info). **Unité et population :** Voies déclarées et validation partielle sous forme de booléens nullables ; nombre de blocs et listes d'intitulés ; aucune grandeur statistique commune.

**Définition source :** Voies d'accès déclarées dans la fiche France compétences (formation initiale, apprentissage, formation continue, contrat de professionnalisation, candidature individuelle, VAE) ; blocs de compétences RNCP (chaque bloc est évalué et validé séparément, détail dans /certifications/blocs) ; validation partielle : RNCP avec blocs, ou fiche RS qui la déclare.

**Champs nécessaires :** `$.tag_acces_formation_initiale`, `$.tag_acces_apprentissage`, `$.tag_acces_formation_continue`, `$.tag_acces_contrat_professionnalisation`, `$.tag_acces_candidature_individuelle`, `$.tag_acces_vae`, `$.nb_blocs_competences`, `$.bloc_competences_codes`, `$.bloc_competences_libelles`, `$.tag_validation_partielle`.

**Présentation attendue :** DSFR : liste de voies d'accès avec libellés explicites et accordéons de blocs ; boutons/liens vers les filtres et /certifications/blocs, sans graphique numérique.

- Conserver les six voies tag_acces_formation_initiale, apprentissage, formation_continue, contrat_professionnalisation, candidature_individuelle et vae, avec le sens déclaré dans la fiche.
- true indique une voie déclarée, false une voie non déclarée comme accessible et null une information inconnue ; aucune voie ne démontre l'éligibilité, le financement, l'admission ou les droits individuels de la personne.
- RNCP : nb_blocs_competences, bloc_competences_codes et bloc_competences_libelles donnent les blocs publiés ; leur détail vient de /certifications/blocs?certifinfo= ou ?fiche=.
- tag_validation_partielle correspond à RNCP avec blocs ou à une fiche RS qui la déclare ; null peut signifier RNCP sans bloc publié et ne doit pas devenir false.
- Les textes de compétences et d'évaluation des blocs ne créent pas de correspondance OGR ; pas de blocs RNCP inventés pour une fiche RS.

**Dépendance / tests :** Catalogue observé : certification, 2026, nat. E18/E20 réutilisent ces champs ; conserver leur caractère documentaire, distinct des modalités effectivement proposées par une session. Tests des filtres acces/validation_partielle et blocs à tracer.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `formacodes` — Formacodes de la certification

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2026.

**Producteur :** Certif Info (RCO) ; Centre Inffo, Formacode V14. **Unité et population :** Thèmes de formation nommés et listes d'identifiants ; aucune unité numérique ou pourcentage.

**Définition source :** Formacodes V14 liés à la certification (Formacode principal en premier), pour retrouver les formations du même thème, certifiantes ou non (cf. /formacodes).

**Champs nécessaires :** `$.formacode_principal_code`, `$.formacode_principal_libelle`, `$.formacode_codes`, `$.formacode_libelles`.

**Présentation attendue :** DSFR : liste de thèmes avec thème principal distingué, liens vers le thème et les certifications ; pas de graphique statistique.

- Afficher formacode_principal_libelle et formacode_libelles dans l'ordre reçu, principal en premier ; les codes servent aux appels sans être imposés comme intitulés publics.
- Conserver le rattachement documentaire Formacode V14 de la certification, sans inventer une équivalence de compétences ou un niveau de maîtrise.
- Navigation : code reçu vers /formacodes?code=, puis /certifications?formacode=, puis détail CertifInfo et sessions par certifinfo ; la pagination et l'absence de certification doivent rester gérées.
- Un thème n'est pas une offre de formation ni une session ; les 21 GET n'exposent pas de recherche de sessions non certifiantes par Formacode.
- Des listes vides ou un thème sans certification visible restent des informations de couverture et ne sont pas complétés par une offre fictive.

**Dépendance / tests :** Catalogue observé : certification, 2026, nat. Le parcours E30 reste couvert ; domaine Formacode distinct du domaine professionnel ROME et du domaine de compétences. Tester chaîne complète et cas sans certification.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `tags` — Tags stratégiques

**Source API :** GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]. Conserver les familles/populations réellement publiées.

**Grain :** `certification`. **Mailles du catalogue :** nat. **Millésime observé :** 2026.

**Producteur :** RCO. **Unité et population :** Marqueurs thématiques booléens nullables et libellés de rénovation énergétique ; aucune grandeur statistique.

**Définition source :** Rénovation énergétique des bâtiments (thématiques REB) et transition écologique (Formacode principal).

**Champs nécessaires :** `$.tag_renovation_energetique_batiment`, `$.thematique_reb_libelle`, `$.tag_transition_ecologique`.

**Présentation attendue :** DSFR : badges textuels expliqués et liste des thématiques ; aucune jauge, score ou graphique de tendance.

- Restituer tag_renovation_energetique_batiment, thematique_reb_libelle et tag_transition_ecologique tels que reçus pour la certification.
- thematique_reb_libelle peut contenir plusieurs thématiques séparées par le caractère| ; les séparer pour la lecture sans fabriquer de nouvelles catégories.
- Distinguer true,false etnull ; une absence de marqueur ne prouve ni l'absence de compétences écologiques ni l'absence de contribution à la transition.
- Le marqueur écologique est lié au Formacode principal selon la définition de la source ; il ne démontre ni croissance d'emploi, ni salaire, ni garantie d'embauche.
- Ne pas inventer de paramètre serveur de transition sur /certifications ; un éventuel filtre local doit porter sur une liste entièrement collectée et être présenté comme tel.

**Dépendance / tests :** Catalogue observé : certification, 2026, nat. Ne pas confondre ces tags de certification avec les trois tags métier d'E29 ; aucun nouveau filtre API ajouté. Tester vrais/faux/null et plusieurs libellésREB.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

## 8. Critères d’acceptation

**US-FON-017-CA-01** — **Étant donné** une certification est choisie dans une liste contenant plusieurs résultats, **Quand** sa fiche est ouverte, **Alors** l'identifiant technique de la requête est celui du résultat choisi et le titre ainsi que les données appartiennent à cette certification.

**US-FON-017-CA-02** — **Étant donné** la fiche est consultée dans l'intention je possède cette certification, **Quand** la personne passe à je souhaite l'obtenir, **Alors** les actions et explications sont adaptées sans modification des données ou attribution d'une éligibilité personnelle.

**US-FON-017-CA-03** — **Étant donné** les populations scolaire, apprentissage et demandeurs d'emploi sont renseignées, **Quand** les résultats d'emploi sont consultés, **Alors** les bases, horizons de douze ou six mois et populations restent séparés sans taux moyen.

**US-FON-017-CA-04** — **Étant donné** des salaires InserSup sont fournis aux trois horizons, **Quand** le détail salarial est ouvert, **Alors** les montants mensuels et quartiles, promotions distinctes et seule base disponible à douze mois sont explicités sans courbe de progression personnelle.

**US-FON-017-CA-05** — **Étant donné** une certification a plusieurs métiers et rome_code est null, **Quand** les métiers associés sont demandés, **Alors** tous les codes et libellés de rome_codes/rome_libelles sont proposés sans dépendre du champ singulier.

**US-FON-017-CA-06** — **Étant donné** un résultat statistique est protégé ou indisponible, **Quand** le graphique et le tableau sont rendus, **Alors** la même protection ou indisponibilité est affichée sans zéro artificiel, complément ou taux recalculé.

**US-FON-017-CA-07** — **Étant donné** une certification relève de plusieurs familles et possède une famille principale, **Quand** la personne consulte ses débouchés, **Alors** la méthode de sélection et les niveaux fournis sont expliqués sans limiter les métiers à cette seule famille.

**US-FON-017-CA-08** — **Étant donné** le niveau discret reçu est5.2, **Quand** le niveau est présenté, **Alors** le système conserve la catégorie publiée et ne l'affiche ni comme5,2% ni comme une probabilité de recrutement.

**US-FON-017-CA-09** — **Étant donné** les deux voies ont des bases et des taux différents, **Quand** la personne consulte l'insertion après certification, **Alors** chaque taux indique sa voie, son dénominateur, son horizon et le cumul national, sans fusion.

**US-FON-017-CA-10** — **Étant donné** un effectif d'emploi est protégé, **Quand** la personne ouvre le tableau alternatif, **Alors** la protection figure aussi dans le tableau et ne devient pas une cellule nulle ou un calcul déduit.

**US-FON-017-CA-11** — **Étant donné** promotion_insersup_libelle vaut 2023/2024, **Quand** la personne consulte l'insertion dans le supérieur, **Alors** le cumul de promotions est indiqué avec la base des sortants et l'horizon douze mois.

**US-FON-017-CA-12** — **Étant donné** les bases emploi et poursuite d'études diffèrent, **Quand** les résultats sont présentés, **Alors** chaque résultat conserve sa base et aucune partition complémentaire emploi/études n'est fabriquée.

**US-FON-017-CA-13** — **Étant donné** les salaires à douze, dix-huit et trente mois sont reçus, **Quand** la personne consulte la rémunération après diplôme, **Alors** les promotions 2022 et 2021 sont indiquées et aucune courbe de progression personnelle ne relie ces cohortes.

**US-FON-017-CA-14** — **Étant donné** seule la base nb_insersup_salaire_base_12m est disponible, **Quand** le tableau présente les trois horizons, **Alors** cette base n'est pas répétée comme effectif des horizons dix-huit et trente mois.

**US-FON-017-CA-15** — **Étant donné** un taux d'accès à l'emploi à six mois est disponible, **Quand** la personne consulte les résultats pour les demandeurs d'emploi, **Alors** la formulation conserve accès dans les six mois, la population nationale et le millésime, sans comparaison directe avec emploi salarié à douze mois.

**US-FON-017-CA-16** — **Étant donné** des taux d'abandon et d'accès à l'emploi sont publiés, **Quand** ils sont affichés, **Alors** ils restent deux lectures séparées et aucun complément à cent pour cent n'est calculé.

**US-FON-017-CA-17** — **Étant donné** les cinq voies disposent de valeurs de millésimes différents, **Quand** la personne consulte les effectifs en formation, **Alors** les lignes gardent leur année et leur nature inscrits ou entrées, sans total global.

**US-FON-017-CA-18** — **Étant donné** un effectif d'une voie est secret_stat, **Quand** le tableau est affiché, **Alors** la cellule indique la protection et aucune somme ne permet de reconstruire cet effectif.

**US-FON-017-CA-19** — **Étant donné** des diplômés du supérieur sont disponibles sans nombre de présents correspondant, **Quand** la personne consulte les résultats aux examens, **Alors** l'effectif est affiché et aucun taux de réussite du supérieur n'est calculé.

**US-FON-017-CA-20** — **Étant donné** les résultats Éducation nationale 2023 et sanitaire-social 2024 sont reçus, **Quand** le tableau est présenté, **Alors** les populations et sessions restent séparées et les taux fournis conservent leurs bases.

**US-FON-017-CA-21** — **Étant donné** indice_parcoursup_candidatures_par_place vaut un nombre supérieur à un, **Quand** la personne consulte la demande de formation, **Alors** le nombre est expliqué comme candidatures par place et non comme pourcentage ou chance d'être admis.

**US-FON-017-CA-22** — **Étant donné** des places Parcoursup sont affichées avec une liste de sessions locales, **Quand** la personne passe aux sessions, **Alors** le système ne reprend pas ces places comme capacités disponibles dans les sessions.

**US-FON-017-CA-23** — **Étant donné** tag_acces_vae est true, **Quand** la personne consulte comment accéder à la certification, **Alors** la voie VAE est présentée comme déclarée pour la certification sans conclusion d'éligibilité personnelle.

**US-FON-017-CA-24** — **Étant donné** une certification RS déclare une validation partielle mais n'a pas de blocs RNCP, **Quand** la personne ouvre les modalités, **Alors** la validation partielle déclarée reste visible et aucun blocRNCP ni équivalence de compétence n'est fabriqué.

**US-FON-017-CA-25** — **Étant donné** une certification possède plusieurs thèmes ordonnés, **Quand** la personne consulte les thèmes associés, **Alors** les libellés reçus sont affichés et le thème principal est distingué sans réordonner arbitrairement les associations.

**US-FON-017-CA-26** — **Étant donné** la personne choisit un thème sans certification retournée, **Quand** la recherche de certifications s'achève, **Alors** un état sans résultat est présenté sans promettre de session directement à partir du thème.

**US-FON-017-CA-27** — **Étant donné** une certification possède un marqueur écologique et plusieurs thématiquesREB, **Quand** la personne consulte sa fiche, **Alors** les thématiques reçues sont lisibles et le marqueur est expliqué sans prédiction d'emploi ni score.

**US-FON-017-CA-28** — **Étant donné** le marqueur écologique vautnull, **Quand** le système affiche les thématiques, **Alors** l'information est traitée comme non renseignée et non comme une réponse négative certaine.

**US-FON-017-CA-29** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-017-CA-30** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** La bascule ne modifie aucune donnée ; Deux intentions, statut et voies, insertion scolaire/apprentissage/InserSup/DE séparée, résultats disponibles et masqués ; enrichissements salariaux InserSup à leurs horizons propres ; Cas RNCP/RS, multi-ROME, champs null/secrets, anciennes certifications introuvables ; tests des populations et promotions ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E17` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : titre et résumé d'identité, groupe de choix d'intention, sommaire par questions, accordéons de voies et blocs, tableaux et liens explicites ; états chargement, fiche disponible, résultat partiel, introuvable et erreur.
- DSFR Chart : DataBox et barres uniquement pour les indicateurs adaptés ; quartiles en tableau accessible si aucun composant officiel ne respecte leur sémantique ; sources, dates, populations et alternative tabulaire restent accessibles.
- Au clavier, le changement d'intention n'ouvre pas une autre fiche ni ne déplace arbitrairement le focus ; annoncer les sections actualisées et offrir les mêmes contenus sur petit écran sans dépendre d'une couleur.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Fiche Certification et résultats ; Deux intentions, statut et voies, insertion scolaire/apprentissage/InserSup/DE séparée, résultats disponibles et masqués ; enrichissements salariaux InserSup à leurs horizons propres ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Ouvrir la certification sélectionnée ; séparer champs réellement reçus, absence de détail et données d’une autre certification.

**SEO / validation conservés :** Proposition à valider D10 : Titre officiel et code. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-017 — scénario, interactions et alternatives](svg/US-FON-017.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-017.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
