# Contrôle automatique des relations entre endpoints de l'API DGEFP–RCO

Ce travail concerne **uniquement l'API**. Il ne modélise aucun parcours ou usage d'un produit consommateur.

## Objectif

Tester statiquement les 24 relations de `matrice_liens_controles.csv` sur :

1. la présence du **paramètre d'entrée** dans le `/docs.json` original de l'interface ;
2. la présence du **champ de sortie** dans les réponses JSON collectées ;
3. pour 18 relations comparables, la présence d'une **même valeur de code** des deux côtés ;
4. la séparation entre un constat documentaire, une correspondance dans les exemples et une requête effectivement tracée.

## Exécution sous Windows, sans dépendance extérieure

Ouvrir le dossier racine `API_DGEFP_RCO_VSCode` dans VS Code, puis lancer :

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" scripts\verifier_relations_api.py
```

Les rapports sont générés dans `06_controles/resultats` :

- `controle_relations_api.csv` : 24 lignes, une par relation ; statut des paramètres, identifiants observés, réserves ;
- `preuves_correspondances_json.csv` : 18 comparaisons de valeurs, avec leur nombre d'identifiants en commun et quelques exemples.

## Résultats des échantillons disponibles (01/11/2026)

- **24** relations examinées ;
- **21** relations d'appel dont les paramètres sont déclarés dans OpenAPI ; **3** correspondances de sorties sans filtre ;
- **18** relations montrant des identifiants communs dans les JSON collectés ;
- **6** relations sans correspondance directement testable à partir des seuls **exemples initiaux** : R16, R17, R18, R19, R23, R24. **Elles ont fait ensuite l’objet de contrôles API directs**, dont R17 reste partiel. Voir `matrice_statuts_apres_tests.csv`.

**Attention au lien R09 `/metiers` → `/secteurs`** : la correspondance observée est seulement la présence du même `rome_code` dans l'en-tête de deux réponses. Le détail `items[]` des quatre échantillons initiaux est vide : les secteurs employeurs **par métier** ne sont donc pas démontrés par cette correspondance. Les essais R17 supplémentaires renvoient 35 secteurs sans `rome`, mais 0 avec `rome=F1610` sur les deux mailles testées.

## Ce que ces contrôles ne permettent PAS de conclure

- Pas d'appel HTTP exécuté avec l'identifiant relevé : les fichiers JSON ne contiennent pas de trace d'URL/paramètres garantissant la requête ayant produit la réponse.
- Pas de validation de l'ensemble des valeurs possibles ni des pages non collectées.
- Pas de validation du filtre `fields`, du taux `secret_stat`, du repli territorial, du secret statistique, ni des paramètres conditionnels.
- Pas de preuve de clé primaire / étrangère, de tables ou de jointures SQL physiques.
- Pas de preuve que `/secteurs` renvoie effectivement des secteurs liés au métier dans les échantillons fournis.

## Point contractuel à signaler

Dans le `contrat_interface_2026-10-19.md`, le endpoint `/indicateurs` requiert `rome`, `zonage` et `territoire` sauf `zonage=france`. Dans le `docs_json_interface.json`, ces trois paramètres de requête sont marqués `required: false`. Le Swagger décrit les noms et les types, **mais ne transcrit pas complètement l'obligation conditionnelle**. Pour préparer un appel exact, appliquer la règle du contrat et vérifier le comportement effectif de l'API.

## Suite logique

La **validation des appels effectifs** demande de conserver la requête exacte (méthode, chemin, query string sans jeton), la réponse HTTP, la date, les paramètres, et un échantillon de réponse par liaison. Une correspondance de codes seule ne suffit pas pour marquer une relation `TEST DE LIAISON CONFIRMÉ`.
