# API DGEFP–RCO — Validation R16 : Territoires → Indicateurs

Date du contrôle : 2026-11-01
Statut : **Validé sur un cas de test réel** (réponses JSON récupérées depuis l'interface API)
Périmètre : **uniquement le fonctionnement de l'API** — aucune hypothèse d'usage.

## Appels effectués

1. `GET /territoires?zonage=commune&code=34172`
   - Fichier preuve : `06_controles/resultats/R16 test/GET_territoires__zonage_commune__code_34172.json`
   - Résultat : `items[0].territoire_code = "34172"`, `items[0].zonage = "commune"`, `items[0].territoire_libelle = "Montpellier"` ; `total = 1`.
   - Correspondances : `clpe_code = "CLPE34003"`, `departement_code = "34"`, `region_code = "76"`.
2. `GET /indicateurs?rome=F1610&zonage=commune&territoire=34172`
   - Fichier preuve : `06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json`
   - Résultat : `rome_code = "F1610"`, `zonage = "commune"`, `territoire = "34172"` ; **14 mesures**.
   - Chaîne de repli dans `territoires` : `com:34172` → `clpe:CLPE34003` → `dep:34` → `reg:76` → `nat:null`.

## Maille réellement renvoyée, par mesure

| Mesure | Grain statistique | Maille réelle | Code du territoire réel | repli | Nb de valeurs |
|---|---|---|---|---|---|
| `tension` | `fap_228` | `dep` | `34` | `true` | 2 |
| `demandeurs_emploi` | `rome` | `clpe` | `CLPE34003` | `true` | 1 |
| `offres_emploi_diffusees` | `rome` | `clpe` | `CLPE34003` | `true` | 1 |
| `offres_emploi_collectees` | `rome` | `clpe` | `CLPE34003` | `true` | 1 |
| `salaires` | `fap_225` | `dep` | `34` | `true` | 1 |
| `projets_recrutement` | `fap_228` | `clpe` | `CLPE34003` | `true` | 2 |
| `metiers_2030` | `fap_87` | `reg` | `76` | `true` | 2 |
| `offres_emploi_caracteristiques` | `rome` | `dep` | `34` | `true` | 1 |
| `offres_emploi_mensuelles` | `rome` | `dep` | `34` | `true` | 12 |
| `competences_offres` | `rome` | `nat` | `None` | `true` | 20 |
| `emploi_secteurs` | `fap_225` | `reg` | `76` | `true` | 13 |
| `statut_emploi` | `rome` | `dep` | `34` | `true` | 1 |
| `formations_metier` | `rome` | `clpe` | `CLPE34003` | `true` | 1 |
| `insertion_formations_metier` | `rome` | `reg` | `76` | `true` | 1 |

Répartition : 5 mesures à la CLPE, 5 au département, 3 à la région, 1 à la France. Dans cet échantillon, toutes les mesures ont `repli: true`.

## Ce qui est confirmé

- Le résultat de `/territoires` fournit bien les valeurs de `zonage` et `territoire_code` transmissibles à `/indicateurs`.
- Le deuxième endpoint accepte ces valeurs et retourne la hiérarchie territoriale attendue.
- Le repli territorial fonctionne sur ce cas : `maille_reelle` et `territoire_code` sont propres à chaque mesure ; les données demandées à la commune ne sont pas nécessairement à la commune.
- Les valeurs sont fournies à des grains différents : `rome`, `fap_228`, `fap_225`, `fap_87`. Une donnée `fap_*` ne doit pas être présentée comme individuelle au métier sans contrôle de `nb_rome_famille`.

## Limites et points d'attention

- La validation porte sur la commune 34172, le ROME F1610 et les deux réponses conservées. Elle **ne prouve pas** le comportement pour toutes les communes ou tous les métiers, ni les jointures SQL physiques.
- Sur la mesure `salaires`, seule une valeur `fap_225_code = B0Z21` apparaît dans l'échantillon, alors que `emploi_secteurs` renvoie notamment `B0Z21` et `B2Z44`. Il faut conserver les codes effectivement retournés, sans en déduire une correspondance 1:1 avec F1610.
- Dans `projets_recrutement`, au moins un `nb_projets_recrutement_saisonniers = 0` coexiste avec un taux `tx_projets_recrutement_saisonniers = 1.7`. La définition des dénominateurs/arrondis mérite confirmation avant tout contrôle d'égalité arithmétique.
- Les valeurs `null` et `secret_stat` sont distinctes et ne doivent pas être assimilées à zéro.

## Décision de cartographie

- **Relation R16 : VALIDÉE sur un appel réel**.
- Preuves : les deux fichiers JSON listés ci-dessus.
- Niveau de validation : correspondance de paramètres + réception de réponse + contrôle des règles de repli sur échantillon ; aucune validation des jointures internes.

## Suivi

R17 a été testé ensuite : voir `06_controles/VALIDATION_R17_territoires_secteurs_V2.md` (filtre métier toujours à clarifier).
