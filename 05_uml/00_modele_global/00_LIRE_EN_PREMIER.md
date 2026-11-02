# UML — Périmètre STRICTEMENT API DGEFP / RCO

**Règle de conception : le seul accès utilisable est l'API.** Ce dossier décrit uniquement les **21 endpoints GET du Swagger** et les données qu’ils renvoient. Il ne prétend pas décrire l’entrepôt Octopilot, ses tables ni son accès SQL.

**ROME V3 exclusivement :** les identifiants métier exposés `rome_code` / `rome_codes` sont des codes **ROME V3**. Des compétences et contextes OGR dérivés de ROME 4.0 sont regroupés par ROME V3 parent. L’API peut renvoyer `tx_fiches_rome4`, `nb_fiches_rome4` et `nb_fiches_rome4_metier` : ces **agrégats numériques** ne sont pas des identifiants métiers ROME V4.

### Les fichiers

1. `01_MODELE_LOGIQUE_API_V3.puml` — classes des **données exposées** et relations d’appels/identifiants.
2. `02_CARTE_21_GET_API.puml` — carte **exhaustive des 21 routes GET** et des chaînages possibles.
3. `03_EXEMPLES_CHAINAGES_GET.puml` — trois séquences d’appels d'exemple, avec des données effectivement testées.
4. `04_INVENTAIRE_EXACT_21_GET.md` — toutes les routes et paramètres extraits de `/docs.json` ; **gras** = champ obligatoire selon Swagger.

### Comment lire les diagrammes

- Les boîtes UML sont des **objets de réponse JSON** ou des **routes API**, **jamais des tables SQL**.
- Les flèches indiquent un passage de **paramètre d'appel** ou la comparaison d'un **code retourné**, jamais une clé étrangère SQL.
- On ne peut utiliser que les **paramètres et champs effectivement documentés / observés** ; l'API ne donne pas accès aux tables `octopilot.data_rco`, `octopilot.public` ou à SQL.
- Le code `certifinfo` est un **filtre** des routes `sessions_*`, et non un attribut retourné dans les JSON de test ; ne pas fabriquer un `id_session`.
- Les mesures FAP225/FAP228/FAP87/NAF38 peuvent être de granularité différente du ROME ; le `grain`, la `maille_reelle`, le `repli` et le secret statistique doivent être conservés.
- Le contrôle R17 (`/secteurs` filtré par `rome`) est **ouvert** : ne pas représenter comme systématiquement fonctionnelle la recherche des secteurs employeurs par métier.

### Utilisation dans VS Code

Ouvre les fichiers `.puml` avec l’extension PlantUML en **aperçu local**, depuis la racine du dossier consolidé. **Ne copie pas une seconde version** de ces fichiers ailleurs dans le projet.

### Provenance

`01_sources/openapi/docs_json_interface.json` (Swagger fournisseur conservé) et `01_sources/contrat_interface_2026-10-19.md` (contrat fourni), ainsi que les JSON contrôlés R16-R19 et R23-R24. La documentation de l'entrepôt **n'a pas été utilisée pour ajouter une seule entité ou route** dans ces fichiers.

Les exemples de séquences sont illustratifs : le fait que les paramètres existent dans le contrat ne garantit pas des résultats pour toutes leurs combinaisons.
