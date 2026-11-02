# UML strictement API DGEFP–RCO — ROME V3

**Un seul modèle de référence, trois diagrammes** dans `00_modele_global/` :

1. `01_MODELE_LOGIQUE_API_V3.puml` — entités **JSON** exposées par les GET ; aucune table SQL.
2. `02_CARTE_21_GET_API.puml` — inventaire complet des routes `GET` et liaisons par paramètres.
3. `03_EXEMPLES_CHAINAGES_GET.puml` — requêtes illustrées dans les réponses testées.

`sequences_api/` rassemble d'autres vues d'appel utiles ; `_archives_non_reference/` conserve les anciens modèles **uniquement à titre historique**. Ne pas reprendre leurs structures comme champs contractuels sans revalidation.

L'extension PlantUML dans VS Code peut afficher les fichiers `.puml`. Privilégier un rendu **local** pour ne pas communiquer des schémas internes à un serveur externe. Le vérificateur Python assure la présence et la cohérence textuelle des UML, mais **ne remplace pas le rendu PlantUML**.
