# Chaînes d’appels API – statut des preuves

Ce dossier ne décrit **aucun produit consommateur**. Les appels sont des possibilités techniques, **pas des enchaînements obligatoires**.

## Clés de liaison explicites

- `rome_code` (ROME V3) : `/metiers/{rome}`, `/metiers/{rome}/competences`, recherche `/certifications?rome=`, `/formacodes?rome=`, `/indicateurs?rome=...` et endpoints de mesures par FAP.
- `competence_code` (OGR) : `/competences` → filtre `/metiers?competence=...`; pour les contextes, `contexte` et `sans_contexte`.
- `certifinfo_code` : `/certifications/{certifinfo}` ; filtre `certifinfo` sur `/certifications/blocs` et `/sessions_*`.
- `fiche_code` : `GET /certifications/blocs?fiche=...` (RNCP uniquement).
- `formacode_code` : recherche `GET /formacodes?code=...` ou filtrage `GET /certifications?formacode=...`.
- `zonage` + `territoire_code` : fournir ensemble les paramètres `zonage` et `territoire` aux endpoints territoriaux. Pour `france`, le paramètre `territoire` peut être omis.
- `items[].mesure` ↔ `GET /mesures` `items[].code` : correspondance *de sorties*, pas paramètre de requête.

## Règles non négociables

1. Les indicateurs à grain `fap_228`, `fap_225`, `fap_87` sont **des résultats de familles** ; ne jamais déduire un fait exclusif à un ROME individuel.
2. Vérifier `maille_reelle` et `repli` pour chaque mesure : le lieu calculé peut différer de la zone demandée.
3. La pagination doit parcourir les pages nécessaires (100 éléments par page, quand applicable).
4. Ne pas confondre `null`, `0`, `[]`, et `secret_stat`.
5. Avec `fields`, certains champs/mesures peuvent ne pas figurer dans la réponse. Les identifiants obligatoirement restitués sont précisés dans le contrat.
6. Pour `/secteurs`, les quatre **échantillons initiaux** ont `items=[]`. Un test R17 ultérieur **sans** filtre `rome` renvoie 35 secteurs ; les tests avec `rome=F1610` renvoient toujours `items=[]` dans les deux mailles testées. Voir `06_controles/VALIDATION_R17_territoires_secteurs_V2.md`.
7. Une correspondance de codes documentée ne prouve **aucune jointure SQL physique**.
8. La documentation est versionnée dans le dossier ; `docs_json_ENRICHI_NON_OFFICIEL.json` est un outil **d’analyse**, pas le contrat officiel du fournisseur.

Voir également `matrice_liens_controles.csv` pour les liens individuels et leur niveau de preuve.
