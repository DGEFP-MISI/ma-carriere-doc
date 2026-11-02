# API DGEFP–RCO — Contrôle R17 : Territoires → Secteurs

Date : 2026-11-01  
Statut : **PARTIELLEMENT VALIDÉ — ÉCART SUR LA RESTITUTION DES SECTEURS DU MÉTIER**  
Périmètre : API uniquement, sans hypothèses d'utilisation par un produit.

## 1. Réponse réelle contrôlée

Appel communiqué : `GET /secteurs?rome=F1610&zonage=commune&territoire=34172`  
Preuve fournie : `R17GET secteurs.json` (sortie de l'interface API).

- Paramètres restitués : `zonage="commune"`, `territoire="34172"`, `rome_code="F1610"`.
- Hiérarchie : `com:34172` → `clpe:CLPE34003` → `dep:34` → `reg:76` → `nat:null`.
- Données territoriales effectives : `maille_demandee="com"`, `maille_reelle="clpe"`, `territoire_code="CLPE34003"`, `repli=true`.
- Données « tous secteurs » : objet `ensemble` renseigné, avec notamment `nb_etablissements_employeurs=24543`, `nb_salaries_prives=227013`, `nb_creations_etablissements=20064`, `nb_defaillances=519`, `secteur_naf38_code="ENS"`.
- **Données du métier par secteur : `metier_maille=null`, `items=[]`, `total=0`.**

Les dates et millésimes de la réponse : SIDE 2024-2025, URSSAF 2025, BODACC 2026. Les absences (`null`) dans `ensemble` sont à conserver telles quelles ; elles ne correspondent pas à zéro.

## 2. Confrontation au contrat d'interface

Le `contrat_interface(1).md` au § `GET /secteurs` indique :

- Avec `rome`, seuls les secteurs qui emploient le métier doivent figurer ; `metier_maille` indique `reg` ou `nat`.
- `nb_actifs_metier` et `tx_actifs_metier` sont issus du recensement 2021, à la maille de la région demandée ou à défaut France.
- **L'exemple du contrat utilise exactement les paramètres du test** (`rome=F1610`, `zonage=commune`, `territoire=34172`) et présente `metier_maille="reg"` et des `items` non vides (FZ, NZ, etc.).

La réponse réelle diffère donc de **l'exemple documentaire pour ce jeu de paramètres**. L'exemple ne prouve pas à lui seul qu'il s'agit d'un défaut du service, mais motive un contrôle ciblé.

Le `/docs.json` plus récent précise par ailleurs qu'avec `rome`, le service devrait restituer au plus les **dix premiers secteurs** employant le métier, et que les établissements employeurs représentent des employeurs **potentiels** du métier, sans liste d'entreprises nominatives.

## 3. Contre-vérification croisée : `/indicateurs`

La réponse observée et conservée pour :
`GET /indicateurs?rome=F1610&zonage=commune&territoire=34172`
contient la mesure `emploi_secteurs` :

- `grain="fap_225"`, `maille_reelle="reg"`, `territoire_code="76"` ;
- `valeurs` contient **13 entrées**, dont le secteur FZ « Construction » pour les FAP `B0Z21` et `B2Z44`.

**Attention :** `/indicateurs` et `/secteurs` ne restituent pas nécessairement les mêmes objets ou règles de calcul ; ces 13 entrées ne peuvent pas être présentées comme l'équivalent direct d'`items` dans `/secteurs`. En revanche, ce constat contredit l'hypothèse générale selon laquelle aucune répartition par secteur pour les familles FAP liées à F1610 ne serait disponible.

## 4. Conclusion sur la relation R17

| Composante du contrôle | Statut | Preuve |
|---|---|---|
| Code territorial issu de `/territoires` accepté en entrée | **Confirmé** | `territoire=34172` restituté, hiérarchie cohérente |
| Repli territoire `commune` → `CLPE` | **Confirmé sur ce cas** | `maille_reelle=clpe`, `territoire_code=CLPE34003`, `repli=true` |
| Valeurs générales `ensemble` | **Confirmé sur ce cas** | Objet présent avec ses champs |
| Association `rome=F1610` → secteurs employeurs | **Non démontrée / anomalie à examiner** | `metier_maille=null`, `items=[]`, `total=0` |
| Jointures SQL internes | **Non vérifiées** | Le JSON ne donne pas accès au schéma physique |

**R17 : PARTIELLEMENT VALIDÉE.** Ne pas classer comme « validée » la restitution des secteurs du métier.

## 5. Deux appels complémentaires recommandés dans l'interface API

**Test A — conserver le métier, interroger directement la région** :
`GET /secteurs?rome=F1610&zonage=region&territoire=76`

**Test B — conserver le territoire, retirer le métier** :
`GET /secteurs?zonage=commune&territoire=34172`

Conserver les deux réponses complètes ainsi que les paramètres saisis et, si l'interface l'affiche, le code HTTP.

### Interprétation attendue des tests

- Si A donne des secteurs et que le test initial reste vide : vérifier le comportement du filtre `rome` et de la remontée régionale lorsqu'un territoire communal est demandé.
- Si A reste vide, mais que B fournit des secteurs : le catalogue territorial fonctionne, mais le rapprochement avec `rome=F1610` reste à investiguer.
- Si A et B restent vides : vérifier aussi la disponibilité de la ventilation NAF 38 et les filtres/paramètres acceptés.

Aucune conclusion sur le code applicatif ou les jointures SQL n'est possible sans accès au fournisseur.
