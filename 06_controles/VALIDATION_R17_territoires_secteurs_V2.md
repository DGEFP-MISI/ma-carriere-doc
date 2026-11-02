# Contrôle R17 — Territoires → Secteurs (mise à jour)

Date : 1er novembre 2026  
Objet : vérification de la relation entre `GET /territoires` et `GET /secteurs`, avec et sans filtre métier.  
Périmètre : API DGEFP–RCO uniquement (sans hypothèse sur une application consommatrice).

## Résultat

**R17 : liaison territoriale validée ; restitution des secteurs du métier `F1610` non conforme à ce qui est décrit par le contrat d'interface et le `/docs.json` actuel. Cause technique non déterminée.**

| Test | Requête | `maille_reelle` | `repli` | `rome_code` | `metier_maille` | `total` | Nombre d'éléments dans `items` |
|---|---|---|---|---|---|---:|---:|
| R17 initial | `/secteurs?rome=F1610&zonage=commune&territoire=34172` | `clpe` | `true` | `F1610` | `null` | 0 | 0 |
| R17-B | `/secteurs?zonage=commune&territoire=34172` | `clpe` | `true` | `null` | `null` | 35 | 35 |
| R17-A | `/secteurs?rome=F1610&zonage=region&territoire=76` | `reg` | `false` | `F1610` | `null` | 0 | 0 |

### Contrôles démontrés

- La chaîne territoriale est cohérente : `34172` (commune Montpellier) → `CLPE34003` (Montpellier) → `34` (Hérault) → `76` (Occitanie) → France.
- La maille communale se replie effectivement sur la CLPE pour les statistiques sectorielles : `maille_reelle = clpe`, `repli = true`.
- Sans filtre ROME, l'API restitue les 35 secteurs NAF38 présents dans l'échantillon de la CLPE ; `ensemble` donne 24 543 établissements employeurs et 227 013 salariés privés.
- Pour `rome=F1610`, `items` reste vide à la CLPE **et** à l'échelle régionale ; `metier_maille` reste `null`.

### Écart avec les sources contractuelles

Le `contrat_interface(1).md`, section `GET /secteurs` (§ 6, autour des lignes 948–989), indique que le filtre `rome` renvoie les secteurs qui emploient le métier et renseigne `metier_maille` à `reg` ou `nat`. Il inclut **un exemple de la même requête** `/secteurs?rome=F1610&zonage=commune&territoire=34172`, qui retourne `metier_maille = reg`, notamment les secteurs `FZ` et `NZ`.

Le Swagger récupéré depuis l'interface `/docs.json` confirme le comportement annoncé : avec `rome`, les dix principaux secteurs employant le métier devraient apparaître, ordonnés par `tx_actifs_metier`, calculés au niveau régional ou national.

Par ailleurs, `GET /indicateurs?rome=F1610&zonage=commune&territoire=34172` contient une mesure `emploi_secteurs` : **13 valeurs** pour les FAP225 liées au ROME, avec `maille_reelle = reg`. Pour le secteur `FZ`, les valeurs par famille FAP225 sont `11 028` (B0Z21) et `2 350` (B2Z44), soit `13 378` au total — valeur également donnée dans l'exemple contractuel de `/secteurs`. Le secteur `NZ` comporte `1 716` et `82`, soit `1 798`, encore conforme à l'exemple. Ces agrégats FAP ne doivent pas être confondus avec une observation propre au seul code ROME lorsque les familles couvrent d'autres métiers.

**Lecture :** les données de secteur métier existent dans la sortie `/indicateurs`, mais ne sont pas restituées dans `/secteurs` avec `rome=F1610` dans les tests réalisés. Cela suggère un problème du traitement conditionnel `rome` dans `/secteurs`, sans pouvoir identifier la cause (filtre, table de passage, index, extraction ou autre) à partir des seules réponses.

## Point à transmettre au développeur API

> Nous avons testé `GET /secteurs` pour le code ROME `F1610` et Montpellier. Sans `rome`, `/secteurs?zonage=commune&territoire=34172` renvoie 35 secteurs. Avec `rome=F1610`, `/secteurs` renvoie `total:0`, `items:[]`, `metier_maille:null`, y compris avec `zonage=region&territoire=76`. Pourtant, `/indicateurs?rome=F1610&zonage=commune&territoire=34172` restitue 13 lignes `emploi_secteurs` à la maille régionale, et le contrat donne un exemple explicite avec des secteurs `FZ` et `NZ` pour le même métier. Pouvez-vous vérifier pourquoi le filtre ROME dans `/secteurs` ne remonte pas les données d'emploi par secteur et confirmer le comportement attendu de `metier_maille` ?

## Statut à inscrire dans la matrice

- **Relation territoriale** : **validée par appels réels**.
- **Filtrage par métier et retour des secteurs employeurs** : **écart contractuel reproduit sur deux mailles** ; confirmation et correction côté API à demander.
- **Relations SQL physiques** : non vérifiées (pas de schéma/base ni de code d'extraction).

## Fichiers de preuve

- `R17GET secteurs.json` : commune, avec métier.
- `R17 verif GET secteurszonage=commune&territoire=34172.json` : commune, sans métier.
- `R17 verif GET secteursrome=F1610&zonage=region&territoire=76.json` : région, avec métier.
- `06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json` : indicateurs, même métier et territoire.
- `contrat_interface(1).md` et `swagge api docs.json` : comportement documentaire attendu.

Limite : preuves fondées sur trois réponses réelles de `/secteurs` et une de `/indicateurs`, pas sur l'exécution SQL ni un test exhaustif de tous les codes ROME.
