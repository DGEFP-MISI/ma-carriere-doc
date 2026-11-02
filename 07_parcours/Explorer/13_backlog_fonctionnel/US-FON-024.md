# US-FON-024 — Explorer les perspectives d'emploi à 2030

**Rattachement :** E24 · alias historique US-E24. **Lot :** L6.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05) ou [US-FON-009](US-FON-009.md) (E09) selon entrée;[US-FON-031](US-FON-031.md) (E31).

**État constaté au 2 novembre 2026 :** Scénario, champs et tris documentés, JSON des deux routes observés. Il reste à tracer les variantes de tri, la chaîne région-famille-métiers, les négatifs et les couvertures particulières ; les fixtures et visualisations locales ne démontrent pas ces appels HTTP. Toutes les composantes détaillées restent dans la cible.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de explorer les perspectives d'emploi à 2030, pour distinguer les créations d'emploi, les renouvellements et les autres composantes des perspectives à 2030, puis examiner les régions et les métiers associés pour éclairer mes choix. Je veux explorer les perspectives détaillées à 2030 par métier et par région.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite explorer les perspectives d'emploi à 2030, afin de distinguer les créations d'emploi, les renouvellements et les autres composantes des perspectives à 2030, puis examiner les régions et les métiers associés pour éclairer mes choix.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis la fiche métier, ouvre que pourrait-il se passer d'ici 2030. | Présente le scénario de référence, les familles professionnelles concernées et la période cumulée 2019-2030 ; charge les perspectives régionales de ce métier. |
| 2 | Consulte les composantes des perspectives. | Affiche créations nettes, départs en fin de carrière, postes à pourvoir, jeunes débutants et déséquilibre potentiel, avec les taux publiés et l'emploi 2019 de référence. |
| 3 | Compare les régions selon la question choisie. | Utilise seulement un tri documenté de /prospective/regions, conserve les rangs par famille et la référence France, puis affiche part régionale et spécificité lorsque disponibles. |
| 4 | Choisit une région pour découvrir les familles dont les perspectives l'intéressent. | Appelle /prospective/metiers avec cette région et un tri documenté, distingue les familles et indique la portée métropolitaine et les regroupements particuliers. |
| 5 | Choisit un métier parmi les associations d'une famille. | Utilise les rome_codes reçus pour ouvrir une fiche ROME V3, avec un nom résolu par les données disponibles ou le GET de détail, sans inférence de famille vers métier. |
| 6 | Consulte le tableau détaillé ou ajoute une piste. | Rend toutes les composantes et métadonnées disponibles, permet l'enregistrement local du métier choisi et garde les possibilités de comparaison et de retour à la région. |

## 5. Scénarios alternatifs

- Créations nettes ou déséquilibre négatifs : conserver le signe et fournir l'explication, sans écrêter les barres à zéro ni déclarer le métier sans avenir.
- Territoire ultramarin : expliquer l'absence de projection régionale dans l'exercice et proposer les données France réellement reçues par repli, sans les attribuer au territoire.
- Familles regroupées en Corse : afficher le périmètre particulier et ne pas classer l'agrégat comme une famille strictement équivalente des autres régions.
- Une composante est null ou une famille n'a pas de cible métier publiée : garder les autres résultats et leurs limites, sans reconstruire la composante ou les associations.
- Tri ou région non observés localement : conserver la fonctionnalité et son test à réaliser, sans réordonner une autre réponse pour simuler une variante HTTP validée.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Les données sont des projections du scénario de référence PMQ, cumulées 2019-2030 au grain FAP87 ; ni recrutement certain, ni offres actuelles, ni série annuelle ne sont fabriqués.
- Conserver les cinq composantes et les taux fournis ; les taux de flux prennent l'emploi 2019 pour base, tandis que part régionale et indice de spécificité ont des sens distincts et que l'indice n'est pas un pourcentage.
- Postes à pourvoir et déséquilibre sont lus dans les champs publiés ; ne pas les recalculer, le déséquilibre régional intégrant notamment le solde des mobilités entre régions.
- Les tris sont limités aux enums des deux routes ; jeunes débutants reste affichable sans tri serveur jeunes inventé ; respecter référence France, rangs par famille, métropole et agrégats corses.
- La passerelle vers une fiche utilise les rome_codes explicites de /prospective/metiers ; aucune somme entre familles, avec BMO ou entre horizons n'est produite.

**Règles héritées conservées :** FAP87, 2019–2030, projections ; effectifs et taux fournis base emploi2019, créations/déséquilibre négatifs possibles ; spécificité/part régionales ; agrégats Corse et métropole distincts ; aucune somme BMO.

**Traitements :** `/prospective/regions?rome=...&tri=...` et `/prospective/metiers?region=...&tri=...` → `rome_codes[]` ; FAP87, 2019–2030, projections ; effectifs et taux fournis base emploi2019, créations/déséquilibre négatifs possibles ; spécificité/part régionales ; agrégats Corse et métropole distincts ; aucune somme BMO.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. FAP87, 2019–2030, projections ; effectifs et taux fournis base emploi2019, créations/déséquilibre négatifs possibles ; spécificité/part régionales ; agrégats Corse et métropole distincts ; aucune somme BMO.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Source prospective renvoyée ; grain fap_87 ; période 2019-2030 observé, vérifier réponse. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/prospective/regions`

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

### Appel 2 — GET `/prospective/metiers`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `region` | query | Facultatif Swagger | `string ; défaut API null` | code région métropole ou omis=France |
| `tri` | query | Facultatif Swagger | `string ; valeurs postes_a_pourvoir, tx_postes_a_pourvoir, desequilibre_potentiel, tx_desequilibre_potentiel, creations_nettes_emplois, tx_creations_nettes_emplois, departs_fin_carriere, tx_departs_fin_carriere, emplois_2019 ; défaut API "postes_a_pourvoir"` | postes_a_pourvoir/tx_postes_a_pourvoir/desequilibre_potentiel/tx_desequilibre_potentiel/creations_nettes_emplois/tx_creations_nettes_emplois/departs_fin_carriere/tx_departs_fin_carriere/emplois_2019 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.source_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.grain` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.millesime` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.total` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_87_code` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].fap_87_libelle` | chaîne | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_emplois_2019` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_part_emploi_region_2019` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].indice_specificite_region_2019` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_creations_nettes_emplois_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_creations_nettes_emplois_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_departs_fin_carriere_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_departs_fin_carriere_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_postes_a_pourvoir_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_postes_a_pourvoir_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_jeunes_debutants_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_jeunes_debutants_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_desequilibre_potentiel_2030` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tx_desequilibre_potentiel_2030` | entier / nombre | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].tension_niveau_2019` | chaîne / null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_rome_famille` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rang` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].rome_codes` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.region` | null | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.region_libelle` | null | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/indicateurs/ProspectiveMetier/response_creations_nettes_emplois.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_creations_nettes_emplois.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_departs_fin_carriere.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_departs_fin_carriere.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_desequilibre_potentiel.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_desequilibre_potentiel.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_emplois_2019.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_emplois_2019.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_prospectivemetiers_poste a  pourvoir.json](<../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_prospectivemetiers_poste a  pourvoir.json>); [02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_creations_nettes_emplois.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_creations_nettes_emplois.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_departs_fin_carriere.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_departs_fin_carriere.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_desequilibre_potentiel.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_tx_desequilibre_potentiel.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_Tx_postes_a_pourvoir.json](../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_Tx_postes_a_pourvoir.json).

### Appel 3 — GET `/metiers/{rome}`

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

**Références conservées de la conception :** [02_reponses_observees/indicateurs/prospectiveregions/response_postes_a_pourvoir.json](../../../02_reponses_observees/indicateurs/prospectiveregions/response_postes_a_pourvoir.json); [02_reponses_observees/indicateurs/ProspectiveMetier/response_prospectivemetiers_poste a  pourvoir.json](<../../../02_reponses_observees/indicateurs/ProspectiveMetier/response_prospectivemetiers_poste a  pourvoir.json>).

**Contrôle local déjà rapporté :** Mission 006 et contrôles des projections, négatifs et carte régionale. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E24 : Tracer chaque famille de tri, métropole/DOM/Corse, négatifs et null ; tester la chaîne région → famille → métiers.

**Points RCO associés :** Q13 : agrégats, géographie et taux ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

**Complément obligatoire :** tous les champs de la mesure `metiers_2030`, ses définitions et ses critères sont explicités dans [US-FON-008](US-FON-008.md). Cette US ajoute les classements et comparaisons régionaux détaillés, sans réduire les cinq composantes aux seules créations nettes.

## 8. Critères d’acceptation

**US-FON-024-CA-01** — **Étant donné** les cinq composantes et leurs taux sont disponibles, **Quand** la personne ouvre les perspectives détaillées, **Alors** aucune composante n'est omise et l'emploi 2019, les unités, le scénario et la période cumulée sont visibles.

**US-FON-024-CA-02** — **Étant donné** la création nette ou le déséquilibre est négatif, **Quand** le graphique est rendu, **Alors** le signe et la valeur sont conservés avec une explication sans écrêtage ni jugement automatique sur le projet.

**US-FON-024-CA-03** — **Étant donné** un tri documenté des régions est choisi, **Quand** la requête est préparée, **Alors** le nom exact du tri est utilisé et aucun tri pour les jeunes débutants n'est inventé.

**US-FON-024-CA-04** — **Étant donné** une région et une famille publient des rome_codes, **Quand** la personne ouvre un métier associé, **Alors** le GET de fiche porte sur un code explicitement reçu et le nom de la famille n'est pas utilisé comme correspondance implicite.

**US-FON-024-CA-05** — **Étant donné** la fiche concerne un territoire ultramarin, **Quand** la projection France est disponible par repli, **Alors** le niveau France est explicitement nommé et aucune projection régionale n'est simulée.

**US-FON-024-CA-06** — **Étant donné** un agrégat particulier est reçu pour la Corse, **Quand** les régions sont comparées, **Alors** son périmètre est expliqué et aucun rang comparable à une famille non agrégée n'est fabriqué.

**US-FON-024-CA-07** — **Étant donné** le déséquilibre régional ne se reconstitue pas par les seules autres composantes affichées, **Quand** la personne consulte son explication, **Alors** la valeur fournisseur est conservée et le rôle possible des mobilités interrégionales est précisé sans correction arithmétique.

**US-FON-024-CA-08** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-024-CA-09** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Projection ≠ recrutement certain ; Prospective détaillée par famille et région, effectifs/taux fournis, référence France, navigation vers ROME V3 ; Tracer chaque famille de tri, métropole/DOM/Corse, négatifs et null ; tester la chaîne région → famille → métiers ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire.

**Recette de rattachement :** `T-E24` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : navigation par questions croissance ou renouvellement, choix de région et de tri, explication progressive des cinq composantes et tableau complet ; états projection disponible, partielle, couverture nationale et erreur.
- DSFR Chart DataBox et barres de composantes ou de régions avec négatifs lisibles ; cartes officielles uniquement sur un zonage pris en charge ; pas de courbe annuelle reconstruite ni visualisation qui additionne deux composantes qui se recoupent.
- Les explications du signe, de la base 2019 et du caractère projeté restent visibles sans survol ; tableau, navigation vers les fiches et choix de région utilisables au clavier et sur mobile.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Prospective détaillée 2030 ; Prospective détaillée par famille et région, effectifs/taux fournis, référence France, navigation vers ROME V3 ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles.

**SEO / validation conservés :** Proposition à valider D10 : Contenu explicatif. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-024 — scénario, interactions et alternatives](svg/US-FON-024.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-024.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
