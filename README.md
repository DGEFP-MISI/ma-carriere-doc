# MaCarrière — documentation et Explorer

Ce dépôt rassemble le dossier de référence de l’API DGEFP–RCO, les parcours MaCarrière et la version actuelle d’Explorer. Les 31 fonctionnalités restent dans le périmètre ; les US, données observées, composants et résultats de tests sont conservés avec leurs limites de validation.

## Consulter Explorer

Après avoir cloné le dépôt ou téléchargé puis décompressé son ZIP, ouvrir **[`07_parcours/Explorer/12_maquette_html/index.html`](07_parcours/Explorer/12_maquette_html/index.html)** dans un navigateur. Le fichier est autonome : aucune installation ni aucun serveur ne sont nécessaires. GitHub affiche le code HTML ; il faut ouvrir le fichier téléchargé pour utiliser l’interface.

Explorer utilise les réponses JSON enregistrées dans le dossier. Il ne réalise pas encore d’appels HTTP à l’API ; les tests locaux ne constituent pas une validation générale des données ou de la conformité RGAA.

| Point d’entrée | Contenu |
|---|---|
| [Guide Explorer](07_parcours/Explorer/README.md) | Organisation et état actuel |
| [Backlog fonctionnel](07_parcours/Explorer/04_BACKLOG_USER_STORIES.md) | 31 fonctionnalités, 4 US transversales, scénarios, critères et SVG |
| [Table de conception](07_parcours/Explorer/03_TABLE_CONCEPTION.csv) | Pilotage métier, API, UI, développement, SEO et validation |
| [Direction artistique et maquettes](07_parcours/Explorer/14_direction_artistique/README.md) | Audit, SVG ordinateur/mobile, composants intégrés et recette |
| [Composants partagés](07_parcours/commun_datavisualisation/README.md) | DSFR, DSFR Chart et compositions MaCarrière réutilisables |
| [Consignes de contribution](AGENTS.md) | Contraintes de données et méthode de travail |

## Reconstruire les fichiers

Prérequis pour modifier et reconstruire : **Node.js 24 ou ultérieur** et **Python 3**. Les paquets officiels nécessaires sont conservés dans `07_parcours/commun_datavisualisation/vendor/` avec leurs licences et leur provenance. Les dépendances installées, caches et outils Node portables restent locaux.

Depuis la racine :

```powershell
npm --prefix 07_parcours/commun_datavisualisation ci --offline --ignore-scripts --no-audit --no-fund
npm --prefix 07_parcours/commun_datavisualisation run build
npm --prefix 07_parcours/commun_datavisualisation test
python -B 07_parcours/Explorer/12_maquette_html/sources/construire.py
```

Les [guides du composant partagé](07_parcours/commun_datavisualisation/README.md) et de la [maquette HTML](07_parcours/Explorer/12_maquette_html/README.md) détaillent les lanceurs Windows et les contrôles navigateur. La documentation, les sources, les archives de décisions et les preuves sont versionnées ; `.gitattributes` conserve les octets pour préserver les empreintes SHA-256.

## Dossier de référence API DGEFP–RCO — ROME V3

**Version consolidée : 1er novembre 2026.** Ce dossier remplace l'archive de travail antérieure après vérification des contrôles locaux.

## Périmètre impératif

- **Uniquement les 21 routes `GET`** décrites dans `01_sources/openapi/docs_json_interface.json`. Aucune autre API, base ou source à interroger.
- **ROME V3 exclusivement** pour les codes métier. Compétences / contextes en codes OGR issus du ROME 4.0 **consolidés au ROME V3 parent** ; `nb_fiches_rome4` et `tx_fiches_rome4` sont seulement des attributs statistiques exposés.
- Tout objet représenté dans l'UML est un **champ JSON / résultat d'API**, jamais une table, une clé étrangère ou une jointure SQL supposée.
- **Ne rien déduire à partir des données absentes** : conserver les significations distinctes de `null`, `0`, `[]`, `secret_stat`, `maille_reelle`, `repli` et des grains FAP.

## Où commencer dans VS Code ?

1. Ouvrir **ce dossier `API_DGEFP_RCO_REFERENCE_V3`** dans VS Code, pas son dossier parent.
2. Ouvrir **`05_uml/00_modele_global/01_MODELE_LOGIQUE_API_V3.puml`** : modèle des données accessibles.
3. Ouvrir `05_uml/00_modele_global/02_CARTE_21_GET_API.puml` : toutes les routes de l'API ; puis `03_EXEMPLES_CHAINAGES_GET.puml`.
4. Lire `05_uml/00_modele_global/04_INVENTAIRE_EXACT_21_GET.md` et `04_relations/matrice_statuts_apres_tests.csv`.
5. Consulter `06_controles/VALIDATION_R*.md` et les preuves JSON de `06_controles/resultats/`.
6. Exécuter les tests locaux via Python (voir ci-dessous). Aucune connexion ni aucun jeton n'est nécessaire.

## Contrôles automatiques

Dans le terminal PowerShell de VS Code :

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" scripts\verifier_dossier.py
```

Tu peux aussi **double-cliquer sur `LANCER_CONTROLES.cmd`** : il utilise en priorité Python 3.13 installé dans ton profil Windows, puis essaie `python` si disponible. Dans VS Code : `Terminal > Run Task > CONTROLE GLOBAL API (Python)` (la tâche utilise ce même lanceur).

Le script global exécute **les six vérifications** : Swagger, échantillons, schémas analytiques, relations, UML, preuves R16–R24. Des tâches VS Code permettent aussi de lancer le contrôle global et les contrôles partiels.

**Important :** il s'agit de **contrôles hors connexion** (structure et cohérence des réponses reçues), pas d'une batterie de tests HTTP en direct, ni d'une validation générale des données.

## Répertoires

| Dossier | Fonction |
|---|---|
| `01_sources` | Contrat initial et Swagger fournisseur d'origine, intacts |
| `02_reponses_observees` | 57 échantillons historiques inventoriés et comparés aux modèles |
| `03_catalogue` | Dictionnaires et modèles complémentaires **non officiels** |
| `04_relations` | 24 relations et statuts détaillés de preuve |
| `05_uml/00_modele_global` | **3 diagrammes de référence**, strictement API / ROME V3 |
| `05_uml/sequences_api` | Séquences supplémentaires d'appels API |
| `05_uml/_archives_non_reference` | Anciennes représentations, non utilisables comme référence actuelle |
| `06_controles` | 7 rapports directs, preuves JSON, contrôles statiques et historique |
| `scripts` | Vérifications hors ligne Python et 2 contrôles PowerShell historiques |

## Limites réelles

- **R17 ouvert** : `GET /secteurs` sans `rome` a renvoyé 35 secteurs ; `rome=F1610` a renvoyé 0 item dans les deux mailles testées. Ne pas présenter les secteurs employeurs par métier comme validés.
- **R18 / R19** : les listes de sessions répondent selon les filtres, mais leurs objets ne restituent ni `certifinfo` ni identifiant de session ; impossible de valider individuellement la correspondance dans chaque objet.
- **R16, R23 et R24** : validés sur des exemples concrets, pas sur toutes les combinaisons possibles.
- **Swagger enrichi** : `03_catalogue/docs_json_ENRICHI_NON_OFFICIEL.json` est une **hypothèse de modélisation**, pas un contrat fournisseur ; 10 réponses HTTP 200 n'ont pas de schéma dans l'export initial.
- `04_relations/controle_relations_api.csv` et les 18 correspondances initiales sont des vérifications **statiques** ; la campagne directe R16–R24 est distinguée dans la matrice de statuts.

## Où trouver les corrections ?

`JOURNAL_CORRECTIONS_2026-11-01.md` résume la remise en état ; `06_controles/RAPPORT_VERIFICATION_FINALE.md` enregistre les contrôles effectués localement.

**Ne supprime pas ton ancien dossier avant d'avoir décompressé ce ZIP et ouvert le nouveau dans VS Code.** Ce dossier est autonome et ne dépend pas des anciens ZIP complémentaires.
