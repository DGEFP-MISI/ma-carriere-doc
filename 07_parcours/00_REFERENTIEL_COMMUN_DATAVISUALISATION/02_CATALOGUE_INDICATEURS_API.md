# Catalogue API des indicateurs — inventaire réel

Source principale : `API_DGEFP_RCO_REFERENCE_V3_PROPRE.zip`, `03_catalogue/routes_openapi.csv`, `03_catalogue/champs_observes_tous_endpoints.csv`, `02_reponses_observees/`, contrat du 19 octobre 2026.

## Exhaustivité des 21 GET
| Endpoint | Paramètres facultatifs spécifiés au catalogue | Chemins JSON recensés |
|---|---|---|
| `GET /certifications` | `q,rome,repertoire,formacode,acces,validation_partielle,fields,page` | 113 chemins catalogués |
| `GET /certifications/blocs` | `q,certifinfo,fiche,rome,fields,page` | 20 chemins catalogués |
| `GET /certifications/{certifinfo}` | `fields` | 107 chemins catalogués |
| `GET /competences` | `q,categorie,rome,domaine,enjeu,macro_competence,code,fields,page` | 0 chemins catalogués |
| `GET /formacodes` | `q,rome,domaine,code,fields,page` | 23 chemins catalogués |
| `GET /indicateurs` | `rome,zonage,territoire,fields,onisep` | 136 chemins catalogués |
| `GET /mesures` | `fields` | 22 chemins catalogués |
| `GET /metiers` | `grand_domaine,domaine,competence,contexte,sans_contexte,mode_competence,q,fields,page` | 0 chemins catalogués |
| `GET /metiers/{rome}` | `fields` | 33 chemins catalogués |
| `GET /metiers/{rome}/competences` | `categorie,coeur_metier,depuis,fields,page` | 26 chemins catalogués |
| `GET /domaines` | `grand_domaine` | 0 chemins catalogués |
| `GET /mobilites` | `rome,sens,region,age,fields` | 26 chemins catalogués |
| `GET /prospective/metiers` | `region,tri,fields` | 30 chemins catalogués |
| `GET /prospective/regions` | `rome,tri,fields` | 48 chemins catalogués |
| `GET /recrutements` | `rome,zonage,region,departement,tri,fields` | 32 chemins catalogués |
| `GET /salaires` | `rome,zonage,region,fields` | 34 chemins catalogués |
| `GET /salaires/secteurs` | `rome,region,fields` | 37 chemins catalogués |
| `GET /secteurs` | `zonage,territoire,naf,rome,fields` | 38 chemins catalogués |
| `GET /sessions_a_venir` | `onisep,page,fields` | 20 chemins catalogués |
| `GET /sessions_en_cours` | `onisep,page,fields` | 20 chemins catalogués |
| `GET /territoires` | `q,zonage,region,departement,clpe,code,fields,page` | 24 chemins catalogués |

## Catalogue orienté décision
### V01 — Comparer les rémunérations médianes entre régions
- GET `/salaires` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `territoire_code`, `territoire_libelle`, `salaire_net_mensuel_median`, `maille_reelle`.
- Chemins présents au catalogue : `$.items[].territoire_code`, `$.items[].territoire_libelle`, `$.france[].salaire_net_mensuel_median`, `NON OBSERVÉ : maille_reelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **FAP225** ; période : **2023** ; restitution : map-chart + bar-chart horizontal. Limite : Une carte et le tableau donnent les mêmes valeurs; codes géographiques adaptés et contrôlés.

### V02 — Voir dispersion de la rémunération dans une famille
- GET `/salaires` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `salaire_net_annuel_q1`, `salaire_net_annuel_median`, `salaire_net_annuel_q3`.
- Chemins présents au catalogue : `$.france[].salaire_net_annuel_q1`, `$.france[].salaire_net_annuel_median`, `$.france[].salaire_net_annuel_q3`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/response_salairessecteurs.json`.
- Grain : **FAP225** ; période : **2023** ; restitution : tableau Q1 médiane Q3 + repère horizontal. Limite : Q1 Q3 ne définissent pas un salaire minimum ou maximum.

### V03 — Comparer salaires entre secteurs employeurs
- GET `/salaires/secteurs` ; paramètres candidats `rome;region`.
- Champs à vérifier : `secteur_naf38_libelle`, `salaire_net_mensuel_median`, `tx_salaries_secteur`.
- Chemins présents au catalogue : `$.items[].secteur_naf38_libelle`, `$.ensemble[].salaire_net_mensuel_median`, `$.items[].tx_salaries_secteur`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/Secteurs/response_Departement.json`.
- Grain : **FAP225 × NAF38** ; période : **2023** ; restitution : bar-chart horizontal + tableau. Limite : Garder secteurs distincts des métiers précis et vérifier ensemble exhaustif.

### V04 — Territoires avec plus de projets de recrutement
- GET `/recrutements` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `territoire_code`, `nb_projets_recrutement`, `maille_reelle`.
- Chemins présents au catalogue : `$.items[].territoire_code`, `$.france[].nb_projets_recrutement`, `NON OBSERVÉ : maille_reelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **FAP228** ; période : **selon JSON** ; restitution : map-chart + bar-chart. Limite : Projets BMO ne sont pas embauches.

### V05 — Comprendre la difficulté anticipée de recrutement
- GET `/recrutements` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `nb_projets_recrutement_difficiles`, `tx_projets_recrutement_difficiles`.
- Chemins présents au catalogue : `$.france[].nb_projets_recrutement_difficiles`, `$.france[].tx_projets_recrutement_difficiles`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **FAP228** ; période : **selon JSON** ; restitution : bar-chart pour taux; texte pour effectifs. Limite : Taux de projets difficiles sans probabilité individuelle.

### V06 — Comparer deux régions sous deux angles sans les fusionner
- GET `/salaires` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `territoire_code`, `salaire_net_mensuel_median`.
- Chemins présents au catalogue : `$.items[].territoire_code`, `$.france[].salaire_net_mensuel_median`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **FAP225** ; période : **2023** ; restitution : 2 graphiques indépendants synchronisés via territoire. Limite : Seconde source /recrutements FAP228; aucune addition ni score.

### V07 — Origines des mobilités observées
- GET `/mobilites` ; paramètres candidats `rome;sens=origine;age`.
- Champs à vérifier : `destination_libelle`, `tx_personnes`, `tranche_age_libelle`.
- Chemins présents au catalogue : `$.items[].destination_libelle`, `$.items[].tx_personnes`, `$.items[].tranche_age_libelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/mobilites/response_destination 15-29 ans.json`, `02_reponses_observees/indicateurs/mobilites/response_destination 30-39 ans.json`.
- Grain : **FAP225** ; période : **2022–2023 exemple** ; restitution : bar-chart horizontal + tableau. Limite : Vérifier signification direction et base de taux.

### V08 — Destinations des mobilités observées
- GET `/mobilites` ; paramètres candidats `rome;sens=destination;age`.
- Champs à vérifier : `destination_libelle`, `tx_personnes`, `tag_en_emploi`.
- Chemins présents au catalogue : `$.items[].destination_libelle`, `$.items[].tx_personnes`, `$.items[].tag_en_emploi`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/mobilites/response_destination 15-29 ans.json`, `02_reponses_observees/indicateurs/mobilites/response_destination 30-39 ans.json`.
- Grain : **FAP225** ; période : **2022–2023 exemple** ; restitution : bar-chart horizontal + tableau. Limite : Aucune probabilité personnalisée de reconversion.

### V09 — Emplois créés vs départs à horizon 2030
- GET `/prospective/regions` ; paramètres candidats `rome;tri=postes_a_pourvoir`.
- Champs à vérifier : `nb_creations_nettes_emplois_2030`, `nb_departs_fin_carriere_2030`, `nb_postes_a_pourvoir_2030`.
- Chemins présents au catalogue : `$.france[].nb_creations_nettes_emplois_2030`, `$.france[].nb_departs_fin_carriere_2030`, `$.france[].nb_postes_a_pourvoir_2030`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/ProspectiveMetier/response_Tx_postes_a_pourvoir.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_creations_nettes_emplois.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_departs_fin_carriere.json`.
- Grain : **FAP87** ; période : **2019–2030** ; restitution : bar-chart groupé si séries mêmes familles et territoire. Limite : Pas courbe temporelle; pas somme calculée si mesure déjà fournie.

### V10 — Comparaison des projections par familles
- GET `/prospective/metiers` ; paramètres candidats `region;tri`.
- Champs à vérifier : `nb_postes_a_pourvoir_2030`, `nb_creations_nettes_emplois_2030`.
- Chemins présents au catalogue : `$.items[].nb_postes_a_pourvoir_2030`, `$.items[].nb_creations_nettes_emplois_2030`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/ProspectiveMetier/response_Tx_postes_a_pourvoir.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_creations_nettes_emplois.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_departs_fin_carriere.json`.
- Grain : **FAP87** ; période : **2019–2030** ; restitution : bar-chart horizontal + tableau. Limite : Contrôler champs observés de cette route avant usage.

### V11 — Répartition sectorielle des salariés
- GET `/salaires/secteurs` ; paramètres candidats `rome;region`.
- Champs à vérifier : `secteur_naf38_libelle`, `tx_salaries_secteur`.
- Chemins présents au catalogue : `$.items[].secteur_naf38_libelle`, `$.items[].tx_salaries_secteur`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/Secteurs/response_Departement.json`.
- Grain : **FAP225×NAF38** ; période : **2023** ; restitution : bar-chart horizontal; donut seulement si parts exhaustives. Limite : Vérifier dénominateur et total, ne pas renormaliser sans preuve.

### V12 — Comparer insertion des apprentis selon une certification
- GET `/certifications` ; paramètres candidats `q;rome;fields`.
- Champs à vérifier : `tx_ij_apprentissage_emploi_12m`, `tx_ij_apprentissage_poursuite_etudes`.
- Chemins présents au catalogue : `$.items[].tx_ij_apprentissage_emploi_12m`, `$.items[].tx_ij_apprentissage_poursuite_etudes`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`.
- Grain : **Certification; apprentis** ; période : **millésime par champ** ; restitution : 2 indicateurs ou barres séparées. Limite : Indicateurs non forcément exclusifs ni complémentaires.

### V13 — Comparer les populations après certification
- GET `/certifications` ; paramètres candidats `q;rome`.
- Champs à vérifier : `tx_ij_scolaire_emploi_12m`, `tx_insersup_emploi_salarie_12m`, `tx_de_acces_emploi_6m`.
- Chemins présents au catalogue : `$.items[].tx_ij_scolaire_emploi_12m`, `$.items[].tx_insersup_emploi_salarie_12m`, `$.items[].tx_de_acces_emploi_6m`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`.
- Grain : **Populations distinctes** ; période : **millésimes distincts** ; restitution : onglets par population; tableau. Limite : Ne pas aligner 6 et 12 mois comme équivalents.

### V14 — Salaire observé des diplômés du supérieur
- GET `/certifications` ; paramètres candidats `q;rome`.
- Champs à vérifier : `salaire_insersup_median_12m`.
- Chemins présents au catalogue : `$.items[].salaire_insersup_median_12m`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`.
- Grain : **InserSup** ; période : **selon JSON** ; restitution : data-box chiffre clé. Limite : Ne pas confondre avec INSEE salariés FAP.

### V15 — Comprendre les certifications par modalités
- GET `/certifications` ; paramètres candidats `rome;acces`.
- Champs à vérifier : `tag_acces_vae`, `tag_acces_formation_continue`, `tag_acces_apprentissage`.
- Chemins présents au catalogue : `$.items[].tag_acces_vae`, `$.items[].tag_acces_formation_continue`, `$.items[].tag_acces_apprentissage`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`.
- Grain : **certification** ; période : **statut actuel dans réponse** ; restitution : liste de tags et tableau. Limite : Tags ne prouvent pas éligibilité individuelle.

### V16 — Voir les blocs associés à une certification
- GET `/certifications/blocs` ; paramètres candidats `certifinfo;fiche`.
- Champs à vérifier : `bloc_code`, `bloc_libelle`, `competences`, `modalites_evaluation`.
- Chemins présents au catalogue : `$.items[].bloc_code`, `$.items[].bloc_libelle`, `$.items[].competences`, `$.items[].modalites_evaluation`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certificationsblocs.json`.
- Grain : **bloc RNCP** ; période : **selon fiche** ; restitution : accordéon DSFR + tableau. Limite : Ne pas fabriquer un score de compétences OGR vers bloc.

### V17 — Identifier les familles de métiers d’un domaine
- GET `/metiers` ; paramètres candidats `domaine;page`.
- Champs à vérifier : `rome_code`, `rome_libelle`.
- Chemins présents au catalogue : `NON OBSERVÉ : rome_code`, `NON OBSERVÉ : rome_libelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`.
- Grain : **ROME V3** ; période : **référentiel** ; restitution : liste accessible et choix métier. Limite : Aucun graphique chiffré de recrutement sans requête dédiée.

### V18 — Métiers proches et compétences communes
- GET `/metiers/{rome}/competences` ; paramètres candidats `depuis;categorie`.
- Champs à vérifier : `tag_acquise`, `nb_acquises`, `nb_a_acquerir`, `tx_macro_competences_communes`.
- Chemins présents au catalogue : `$.items[].tag_acquise`, `NON OBSERVÉ : nb_acquises`, `NON OBSERVÉ : nb_a_acquerir`, `NON OBSERVÉ : tx_macro_competences_communes`.
- Échantillons contenant au moins un champ : `02_reponses_observees/metiers/response_metiers{rome}competences.json`.
- Grain : **ROME V3 / OGR consolidé** ; période : **référentiel** ; restitution : liste comparative + badge de relation. Limite : tag_acquise décrit rapprochement métier, pas acquis réel du salarié.

### V19 — Contextes souhaités ou évités
- GET `/metiers` ; paramètres candidats `contexte;sans_contexte;domaine`.
- Champs à vérifier : `rome_code`, `rome_libelle`.
- Chemins présents au catalogue : `NON OBSERVÉ : rome_code`, `NON OBSERVÉ : rome_libelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`.
- Grain : **ROME V3** ; période : **référentiel** ; restitution : cartes de pistes et filtres. Limite : Absence de contexte ne garantit pas absence sur les postes.

### V20 — Comparer des métiers sur des indicateurs distincts
- GET `/indicateurs` ; paramètres candidats `rome;zonage;territoire`.
- Champs à vérifier : `maille_reelle`, `secret_stat`.
- Chemins présents au catalogue : `$.items[].maille_reelle`, `NON OBSERVÉ : secret_stat`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`, `02_reponses_observees/indicateurs/Secteurs/response_Departement.json`.
- Grain : **ROME / FAP selon mesure** ; période : **selon indicateur** ; restitution : tableau comparatif ventilé par grain. Limite : Interdire radar multi-unités et score global.

### V21 — Comparer territoires pour une projection 2030
- GET `/prospective/regions` ; paramètres candidats `rome;tri`.
- Champs à vérifier : `territoire_code`, `nb_postes_a_pourvoir_2030`.
- Chemins présents au catalogue : `$.items[].territoire_code`, `$.france[].nb_postes_a_pourvoir_2030`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/ProspectiveMetier/response_Tx_postes_a_pourvoir.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_creations_nettes_emplois.json`, `02_reponses_observees/indicateurs/ProspectiveMetier/response_departs_fin_carriere.json`.
- Grain : **FAP87** ; période : **2019–2030** ; restitution : map-chart région si codes compatibles; tableau. Limite : Vérifier codes géo et non additivité des vues.

### V22 — Projets BMO et salaires: écarts de lecture
- GET `/recrutements` ; paramètres candidats `rome;zonage=region`.
- Champs à vérifier : `nb_projets_recrutement`, `territoire_code`.
- Chemins présents au catalogue : `$.france[].nb_projets_recrutement`, `$.items[].territoire_code`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **FAP228 vs FAP225** ; période : **selon chacune** ; restitution : juxtaposition barres de recrutement et barres de salaire. Limite : Aucune corrélation ou relation causale induite.

### V23 — Taux de réussite aux examens par certification
- GET `/certifications` ; paramètres candidats `q;repertoire`.
- Champs à vérifier : `tx_examen_reussite`.
- Chemins présents au catalogue : `$.items[].tx_examen_reussite`.
- Échantillons contenant au moins un champ : `02_reponses_observees/certifications/response_certifications-certifinfo.json`, `02_reponses_observees/certifications/response_certifications.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`.
- Grain : **certification / examens** ; période : **selon JSON** ; restitution : indicateur clé + note population. Limite : Le taux ne garantit pas accès à emploi.

### V24 — Territoires selon nomenclature vérifiée
- GET `/territoires` ; paramètres candidats `zonage;code`.
- Champs à vérifier : `territoire_code`, `region_code`, `departement_code`.
- Chemins présents au catalogue : `$.items[].territoire_code`, `$.items[].region_code`, `$.items[].departement_code`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France CLPE projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json`.
- Grain : **territoires** ; période : **référentiel** ; restitution : sélecteur DSFR + cartes liées. Limite : Transcoder codes INSEE vers codes DSFR Chart explicitement.

### V25 — Prévenir les comparaisons non valides
- GET `/mesures` ; paramètres candidats `fields`.
- Champs à vérifier : `code`, `libelle`.
- Chemins présents au catalogue : `$.items[].code`, `$.items[].libelle`.
- Échantillons contenant au moins un champ : `02_reponses_observees/indicateurs/Recrutementregions/response_indicateurs.json`, `02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json`, `02_reponses_observees/indicateurs/Secteurs/response_Departement.json`.
- Grain : **mesure** ; période : **selon dictionnaire** ; restitution : notice méthodologique et tableau. Limite : Vérifier les chemins avant implémentation.

## Règles de preuve
Le catalogue de champs observés établit seulement la présence du champ dans des échantillons, pas la faisabilité de tous les paramétrages ni toutes les relations. Les champs **NON OBSERVÉ** ne doivent pas être traités comme existants sans contrôle dans Swagger / JSON ou tests. Ne pas transposer les champs d'une route vers une autre. Le champ `millesime` de l'enveloppe prévaut sur une année suggérée dans l'interface; les années du tableau sont indicatives des fichiers examinés.
