# Complément de modélisation des réponses — VERSION NON OFFICIELLE

## Contenu

- `docs_json_ENRICHI_NON_OFFICIEL.json` : **COPIE ANALYTIQUE** du dernier `GET /docs.json`, dans laquelle les 10 schémas de réponse HTTP 200 absents ont été complétés avec les exemples JSON et le contrat d’interface.
- `modeles_reponses/*.schema.json` : un modèle JSON par endpoint initialement non décrit.
- `champs_observes_tous_endpoints.csv` :  observations des chemins JSON exacts, types constatés et nombres d’occurrences.
- `modele_valeurs_par_mesure.csv` : structures des `valeurs[]` présentes dans le seul échantillon `/indicateurs` ; les mesures vides sont distinguées.

## Ce que cela ne prouve pas

- L'API fournisseur **n'a pas été modifiée**. Les fichiers d'origine restent intacts dans `01_sources/`.
- Les types inférés d'échantillons sont **partiels** (exemple : une valeur `null` seule ne donne pas le type d’origine).
- Les `items` de `/secteurs` sont **toujours vides dans les quatre échantillons** ; leur modèle provient uniquement des règles du contrat, pas de l'observation.
- `/domaines` n'a **aucune réponse JSON collectée** ; son schéma est basé sur l'exemple du contrat uniquement.
- Les `valeurs[]` de `/indicateurs` ont des formes **différentes selon la mesure** ; voir le CSV dédié. Il ne faut pas interpréter la somme de tous les attributs comme une seule structure obligatoire.
- L'analyse est statique (sans jeton, sans appel HTTP, sans base SQL). Elle ne valide pas les clés étrangères ni tous les filtres.
- Une documentation enrichie ne doit pas être présentée comme `/docs.json` officiel ni livrée à un consommateur sans validation du fournisseur.

## Lancer le contrôle dans VS Code (Python déjà installé)

Depuis la racine du dossier :

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" scripts\verifier_schemas_complementaires.py
```

Voir le rapport `06_controles/resultats/comparaison_schemas_complementaires.csv`.
