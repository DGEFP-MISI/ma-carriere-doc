# US-FON-026 — Comprendre les secteurs employeurs et l'économie du territoire

**Rattachement :** E26 · alias historique US-E26. **Lot :** L7.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05);[US-FON-009](US-FON-009.md) (E09);[US-FON-008](US-FON-008.md) (E08);[US-FON-031](US-FON-031.md) (E31).

**État constaté au 2 novembre 2026 :** R16 démontre la restitution familiale et R17 la liaison territoriale sans métier ; l'appel métier-territoire attendu est affecté par une anomalie fournisseur reproduite, cause inconnue. Les deux lectures locales ne constituent pas un contournement équivalent ; Q14 et la recette HTTP après réponse fournisseur restent ouverts.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de comprendre les secteurs employeurs et l'économie du territoire, pour distinguer où travaillent les personnes de la famille de métiers et comment évoluent les secteurs économiques du territoire, pour situer les opportunités sans attribuer tous les emplois locaux à mon métier. Je veux distinguer les secteurs d'emploi de la famille et le contexte économique territorial.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite comprendre les secteurs employeurs et l'économie du territoire, afin de distinguer où travaillent les personnes de la famille de métiers et comment évoluent les secteurs économiques du territoire, pour situer les opportunités sans attribuer tous les emplois locaux à mon métier.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre quels secteurs emploient les personnes de cette famille. | Lit la mesure emploi_secteurs de /indicateurs pour le métier et le lieu, en regroupant les résultats par famille et en indiquant la région ou la France réellement mesurée. |
| 2 | Parcourt les principaux secteurs d'emploi. | Présente les actifs occupés et leurs parts du recensement 2021, avec les rangs, la couverture partielle et les noms des familles. |
| 3 | Ouvre que se passe-t-il dans l'économie du territoire. | Interroge /secteurs sans filtre métier pour le contexte local et affiche séparément établissements, salariés privés, créations et défaillances selon leurs sources et périodes. |
| 4 | Choisit un secteur reçu pour détailler son contexte. | Utilise son code NAF38 dans le filtre naf autorisé, conserve la maille réelle et distingue la référence ensemble des lignes sectorielles. |
| 5 | Demande le détail secteur-métier prévu dans le parcours. | Exécute l'appel /secteurs avec rome quand l'environnement est connecté ; garde le résultat attendu et signale l'indisponibilité reproduite R17 sans la convertir en absence d'employeur. |
| 6 | Compare les lectures et poursuit vers salaire, territoire ou fiche métier. | Explique les différences de populations et de lieux, réutilise les données compatibles et préserve toutes les actions sans créer de jointure d'effectifs locaux au métier. |

## 5. Scénarios alternatifs

- Filtre métier vide comme R17 alors que le contexte et emploi_secteurs sont renseignés : afficher les deux lectures disponibles et l'indisponibilité du détail attendu, sans annoncer aucun employeur.
- Champ SIDE null à la CLPE : expliquer la maille départementale au plus fin du champ ; ne pas fabriquer un chiffre de proximité.
- Plusieurs familles ou secteurs partiels : conserver leurs groupes et parts publiées, sans total métier ou secteur résiduel.
- Données privées URSSAF peu représentatives de l'administration publique : préciser cette population au lieu d'étendre les comptes à tout l'emploi.
- Erreur d'un des appels : garder les lectures déjà disponibles avec leur source et date, afficher un état partiel et reprendre uniquement l'appel en échec.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. R17 vide = anomalie/indisponibilité de ce résultat, pas aucun employeur. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- emploi_secteurs concerne les actifs salariés et non-salariés des FAP225, au recensement 2021, région ou France ; /secteurs décrit les activités NAF38 d'un territoire via SIDE, URSSAF et BODACC à d'autres dates.
- Ne pas sommer les familles, attribuer les comptes d'un secteur local au seul ROME ou présenter le contexte sans filtre comme l'équivalent du résultat métier attendu.
- Conserver maille_reelle/repli pour le contexte et metier_maille pour les parts métier ; certains champs sont départementaux au plus fin malgré un contexte servi à la CLPE.
- Distinguer unités légales, établissements, établissements employeurs, salariés privés et entreprises défaillantes ; les défaillances pour mille ne sont pas des pourcentages, et aucune fermeture ou liste d'employeurs nominatifs n'est inventée.
- Q14 suit l'anomalie /secteurs avec rome reproduite à deux mailles pour F1610 ; la fonction métier-territoire reste dans le périmètre jusqu'à correction ou explication contractuelle et recette de clôture.

**Règles héritées conservées :** emploi_secteurs=FAP225 actifs occupés RP2021 région/France ; secteurs=NAF38 SIDE/URSSAF/BODACC selon période ; populations et mailles distinctes, pas de somme FAP ni attribution des comptes territoriaux au métier ; R17 ouvert.

**Traitements :** E08 `emploi_secteurs` + `/secteurs?zonage=...&territoire=...` pour contexte ; `/secteurs?zonage=...&territoire=...&rome=...` pour résultat contractuel attendu ; emploi_secteurs=FAP225 actifs occupés RP2021 région/France ; secteurs=NAF38 SIDE/URSSAF/BODACC selon période ; populations et mailles distinctes, pas de somme FAP ni attribution des comptes territoriaux au métier ; R17 ouvert.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. emploi_secteurs=FAP225 actifs occupés RP2021 région/France ; secteurs=NAF38 SIDE/URSSAF/BODACC selon période ; populations et mailles distinctes, pas de somme FAP ni attribution des comptes territoriaux au métier ; R17 ouvert.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** INSEE RP2021 ; SIDE ; URSSAF ; BODACC, périodes distinctes ; grain fap_225 pour emploi_secteurs ; secteur_naf38 pour contexte ; maille territoriale et metier_maille distinctes ; période RP2021 ; SIDE2024-2025 ; URSSAF2025 ; BODACC2026, selon réponse. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/secteurs`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `zonage` | query | Facultatif Swagger | `string ; valeurs france, region, departement, clpe, commune ; défaut API null` | france/region/departement/clpe/commune |
| `territoire` | query | Facultatif Swagger | `string ; défaut API null` | requis sauf france |
| `naf` | query | Facultatif Swagger | `string ; défaut API null` | NAF38 facultatif ; sans rome pour contexte |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.maille_demandee` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.maille_reelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoire_code` | chaîne / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.territoire_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.repli` | booléen | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.metier_maille` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].secteur_naf38_code` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].secteur_naf38_libelle` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_etablissements` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_etablissements_n5` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].tx_evolution_etablissements_5ans` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_unites_legales` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_creations_etablissements` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_creations_etablissements_n1` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].tx_evolution_creations_1an` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_etablissements_employeurs` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_salaries_prives` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_salaries_prives_n5` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].tx_evolution_salaries_5ans` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].nb_defaillances` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].tx_defaillances_1000_unites_legales` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].date_debut_defaillances` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].date_fin_defaillances` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.ensemble.secteur_naf38_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.secteur_naf38_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_etablissements` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_etablissements_n5` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.tx_evolution_etablissements_5ans` | nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_unites_legales` | entier / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_creations_etablissements` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_creations_etablissements_n1` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.tx_evolution_creations_1an` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_etablissements_employeurs` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_salaries_prives` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_salaries_prives_n5` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.tx_evolution_salaries_5ans` | nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.nb_defaillances` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.tx_defaillances_1000_unites_legales` | nombre / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.date_debut_defaillances` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.ensemble.date_fin_defaillances` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/Secteurs/response_clpe.json](../../../02_reponses_observees/indicateurs/Secteurs/response_clpe.json); [02_reponses_observees/indicateurs/Secteurs/response_Departement.json](../../../02_reponses_observees/indicateurs/Secteurs/response_Departement.json); [02_reponses_observees/indicateurs/Secteurs/response_FRANCE.json](../../../02_reponses_observees/indicateurs/Secteurs/response_FRANCE.json); [02_reponses_observees/indicateurs/Secteurs/response_secteurnaf.json](../../../02_reponses_observees/indicateurs/Secteurs/response_secteurnaf.json).

### Appel 2 — GET `/indicateurs`

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

### Appel 3 — GET `/secteurs`

**Déclenchement :** Diagnostic et recette R17 ; aucun compte métier local reconstruit. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `zonage` | query | Facultatif Swagger | `string ; valeurs france, region, departement, clpe, commune ; défaut API null` | france/region/departement/clpe/commune |
| `territoire` | query | Facultatif Swagger | `string ; défaut API null` | requis sauf france |
| `rome` | query | Facultatif Swagger | `string ; défaut API null` | code V3, résultat attendu à résoudre R17 |
| `naf` | query | Facultatif Swagger | `string ; défaut API null` | NAF38 facultatif |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.metier_maille` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_actifs_metier` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].tx_actifs_metier` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].secteur_naf38_code` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |
| `$.items[].secteur_naf38_libelle` | À confirmer sur réponse | Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/Secteurs/response_clpe.json](../../../02_reponses_observees/indicateurs/Secteurs/response_clpe.json); [02_reponses_observees/indicateurs/Secteurs/response_Departement.json](../../../02_reponses_observees/indicateurs/Secteurs/response_Departement.json); [02_reponses_observees/indicateurs/Secteurs/response_FRANCE.json](../../../02_reponses_observees/indicateurs/Secteurs/response_FRANCE.json); [02_reponses_observees/indicateurs/Secteurs/response_secteurnaf.json](../../../02_reponses_observees/indicateurs/Secteurs/response_secteurnaf.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [06_controles/VALIDATION_R17_territoires_secteurs_V2.md](../../../06_controles/VALIDATION_R17_territoires_secteurs_V2.md); [06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json](<../../../06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json>).

**Contrôle local déjà rapporté :** Deux lectures locales distinctes ; anomalie R17 non résolue. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E26 : Reproduire avec/sans ROME sur plusieurs codes/mailles ; conserver 13 lignes R16 et 35 sans filtre comme preuves distinctes ; retester après réponse RCO.

**Points RCO associés :** Q14 : anomalie R17, `metier_maille` et interprétation métier-territoire ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

### Couverture détaillée des 2 mesures rattachées à cette US

Chaque mesure est un sous-scénario de cette US. Ses champs, sa population et ses critères sont conservés même si aucune valeur n’est publiée dans le jeu local.

#### `emploi_secteurs` — Secteurs d'activité qui emploient le métier

**Source API :** GET /indicateurs. Filtrer `items[].mesure` par ce code ; ne pas supposer une forme commune de `valeurs[]`.

**Grain :** `fap_225`. **Mailles du catalogue :** reg, nat. **Millésime observé :** 2021.

**Producteur :** INSEE, recensement de la population. **Unité et population :** Actifs en emploi, salariés et non-salariés ; pourcentage des actifs de chaque famille professionnelle dans le secteur.

**Définition source :** Actifs en emploi de chaque famille professionnelle (FAP 225) rattachée au ROME V3 par secteur d'activité de l'employeur (NAF 38 postes), salariés et non-salariés : les 10 premiers secteurs par FAP (`rang_secteur`), avec la part des actifs de la FAP qui y travaillent (`tx_actifs_secteur`). Estimations du recensement, publiées à partir de 20 actifs. Pour la dynamique de ces secteurs sur le territoire, cf. /secteurs?rome=.

**Champs nécessaires :** `$.items[].valeurs[].fap_225_code`, `$.items[].valeurs[].fap_225_libelle`, `$.items[].valeurs[].rang_secteur`, `$.items[].valeurs[].secteur_naf38_code`, `$.items[].valeurs[].secteur_naf38_libelle`, `$.items[].valeurs[].nb_actifs_emploi`, `$.items[].valeurs[].tx_actifs_secteur`.

**Présentation attendue :** DSFR Chart DataBox et barres classées par secteur_naf38_libelle, séparées par famille FAP225 ; tableau DSFR avec rang_secteur, effectif et part.

- Utiliser /indicateurs, mesure emploi_secteurs : une ligne par FAP225 et secteur NAF38, jusqu'aux dix premiers secteurs de chaque famille, au recensement 2021 observé.
- nb_actifs_emploi inclut salariés et non-salariés ; tx_actifs_secteur est la part des actifs de la famille dans ce secteur et ne doit pas être remplacé par tx_salaries_secteur de 2023.
- Conserver chaque famille et nb_rome_famille ; ne pas sommer les FAP pour fabriquer un effectif propre au seul métier ROME ni renormaliser les dix secteurs à cent pour cent.
- Seuil de publication vingt actifs ; couverture régionale ou nationale, dont le lieu effectif est lu dans la mesure, et non comptages d'employeurs au niveau communal.
- Garder séparée la dynamique économique de /secteurs ; le résultat familial publié ne corrige pas silencieusement l'anomalie R17 du filtre métier.

**Dépendance / tests :** Catalogue observé : fap_225, 2021, reg/nat. R16 contient treize lignes pour F1610 ; /secteurs avec rome reste dépendant Q14. Réutilisable E08/E28 avec les avertissements de famille et de périmètre.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

#### `secteurs` — Dynamique des secteurs d'activité

**Source API :** GET /secteurs. Conserver les familles/populations réellement publiées.

**Grain :** `secteur_naf38`. **Mailles du catalogue :** clpe, dep, reg, nat. **Millésime observé :** SIDE 2024-2025, URSSAF 2025, BODACC 2026.

**Producteur :** INSEE, SIDE ; URSSAF, établissements employeurs et effectifs salariés ; BODACC. **Unité et population :** Établissements, unités légales, salariés privés et entreprises défaillantes ; évolutions en pourcentage ; défaillances pour mille unités légales, pas en pourcentage.

**Définition source :** Par secteur d'activité (NAF 38 postes) et pour l'ensemble des secteurs (`secteur_naf38_code` = ENS) : établissements actifs fin 2024 et évolution sur 5 ans, unités légales (SIDE, département au plus fin) ; créations d'établissements 2025 et évolution sur un an (SIDE) ; établissements employeurs et salariés du privé 2025, évolution des salariés sur 5 ans (URSSAF) ; défaillances d'entreprises (jugements d'ouverture de liquidation, redressement ou sauvegarde publiés au BODACC entre `date_debut_defaillances` et `date_fin_defaillances`, une entreprise comptant une fois) et leur nombre pour 1 000 unités légales. Pas de fermetures d'établissements. Comptages d'établissements seulement, sans liste nominative.

**Champs nécessaires :** `$.items[].secteur_naf38_code`, `$.items[].secteur_naf38_libelle`, `$.items[].nb_etablissements`, `$.items[].nb_etablissements_n5`, `$.items[].tx_evolution_etablissements_5ans`, `$.items[].nb_unites_legales`, `$.items[].nb_creations_etablissements`, `$.items[].nb_creations_etablissements_n1`, `$.items[].tx_evolution_creations_1an`, `$.items[].nb_etablissements_employeurs`, `$.items[].nb_salaries_prives`, `$.items[].nb_salaries_prives_n5`, `$.items[].tx_evolution_salaries_5ans`, `$.items[].nb_defaillances`, `$.items[].tx_defaillances_1000_unites_legales`, `$.items[].date_debut_defaillances`, `$.items[].date_fin_defaillances`.

**Présentation attendue :** DSFR Chart DataBox et barres par indicateur/secteur ; DSFR tableau multicritère regroupé par source et période, référence ensemble séparée ; carte officielle seulement pour un zonage pris en charge.

- Conserver séparément SIDE : établissements actifs fin 2024 et fin 2019, unités légales fin 2024, créations 2025 et 2024 ; URSSAF : établissements employeurs et salariés privés 2025/2020 ; BODACC : dates exactes des jugements publiés.
- tx_defaillances_1000_unites_legales est un nombre pour mille unités légales, et non un taux en pourcentage ; les tx_evolution_* sont des pourcentages reçus, sans recalcul ni tendance interpolée.
- ensemble est un objet tous secteurs ENS, non un secteur à additionner aux lignes ; la source ne fournit ni fermetures d'établissements ni liste nominative d'employeurs.
- Lire maille_reelle/repli pour le contexte économique ; certains champs SIDE sont départementaux au plus fin et null à la CLPE ; metier_maille décrit une autre maille pour les parts du métier avec rome.
- Le filtre rome attendu reste dans le périmètre mais son résultat F1610 vide est une anomalie R17 à résoudre ; il ne signifie aucun employeur et ne permet aucune attribution des comptes locaux au seul métier.

**Dépendance / tests :** Catalogue observé : secteur_naf38, SIDE 2024-2025/URSSAF 2025/BODACC 2026, clpe/dep/reg/nat. Q14 ouvert, cause inconnue ; les tests avec/sans ROME sont nécessaires jusqu'à clôture fournisseur. /indicateurs emploi_secteurs est une lecture familiale distincte.

**Preuve :** [notice native /mesures](../../../02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json) ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.

## 8. Critères d’acceptation

**US-FON-026-CA-01** — **Étant donné** R16 fournit treize lignes emploi_secteurs et R17 trente-cinq secteurs sans filtre métier, **Quand** les deux lectures sont rendues, **Alors** leurs populations, dates et lieux restent séparés sans agrégat ROME fabriqué.

**US-FON-026-CA-02** — **Étant donné** /secteurs avec F1610 retourne une liste vide et metier_maille null comme R17, **Quand** la personne ouvre le détail métier-territoire, **Alors** le système annonce une information indisponible et conserve la dépendance fournisseur sans affirmer aucun employeur.

**US-FON-026-CA-03** — **Étant donné** un compte sectoriel est publié pour un bassin local, **Quand** la personne consulte son explication, **Alors** il est décrit comme contexte du secteur et non comme nombre d'emplois du seul métier étudié.

**US-FON-026-CA-04** — **Étant donné** un champ SIDE est null à la CLPE, **Quand** le tableau est affiché, **Alors** son indisponibilité à cette échelle est indiquée sans conversion en zéro.

**US-FON-026-CA-05** — **Étant donné** un indicateur BODACC est exprimé pour mille unités légales, **Quand** la dynamique économique est ouverte, **Alors** l'unité pour mille et les dates effectives sont visibles sans pourcentage ni nombre de fermetures déduit.

**US-FON-026-CA-06** — **Étant donné** le fournisseur corrige le filtre métier, **Quand** les tests avec et sans ROME sont rejoués, **Alors** la clôture repose sur des réponses HTTP tracées et une interprétation cohérente de metier_maille, nb_actifs_metier et tx_actifs_metier.

**US-FON-026-CA-07** — **Étant donné** deux familles sont présentes dans les secteurs d'emploi de 2021, **Quand** la personne consulte les secteurs employeurs, **Alors** deux groupes avec leurs noms, effectifs, parts et lieu régional sont affichés sans agrégat métier fabriqué.

**US-FON-026-CA-08** — **Étant donné** les salaires sectoriels de 2023 sont également disponibles, **Quand** la personne passe d'un volet à l'autre, **Alors** la population actifs de 2021 reste distincte de la population salariés de 2023 et les champs de part ne sont pas substitués.

**US-FON-026-CA-09** — **Étant donné** /secteurs sans rome contient des lignes et le même appel avec F1610 est vide comme R17, **Quand** la personne consulte les secteurs employeurs, **Alors** le contexte territorial reste lisible et le volet métier est signalé indisponible, sans conclure à l'absence d'employeur.

**US-FON-026-CA-10** — **Étant donné** un nombre de défaillances pour mille unités légales et des dates sont reçus, **Quand** la personne ouvre la dynamique économique, **Alors** l'unité pour mille et la période sont visibles et aucune conversion en pourcentage ou fermeture n'est inventée.

**US-FON-026-CA-11** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-026-CA-12** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** F1610 => vide ne signifie pas absence employeur ; Deux lectures explicitement séparées : où travaillent les familles (région/France) et dynamique NAF territoriale. Le volet métier-territoire attend résolution R17 ; aucun compte local attribué au métier par jointure ; Reproduire avec/sans ROME sur plusieurs codes/mailles ; conserver 13 lignes R16 et 35 sans filtre comme preuves distinctes ; retester après réponse RCO ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E26` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : deux entrées clairement nommées personnes de la famille et économie du territoire, tableaux par source, messages d'indisponibilité partielle et liens de secteur ; aucun écran ne masque la lecture disponible parce qu'un autre appel échoue.
- DSFR Chart DataBox et barres des parts ou indicateurs à population commune ; carte officielle seulement avec zonage compatible ; les sources, dates, unités et limites sont aussi dans le tableau et accessibles au clavier.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Secteurs d'emploi et contexte économique ; Deux lectures explicitement séparées : où travaillent les familles (région/France) et dynamique NAF territoriale. Le volet métier-territoire attend résolution R17 ; aucun compte local attribué au métier par jointure ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Aucun contenu indexé. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-026 — scénario, interactions et alternatives](svg/US-FON-026.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-026.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
