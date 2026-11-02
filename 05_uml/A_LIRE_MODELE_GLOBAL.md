# Le modèle global à utiliser

Ouvrir `05_uml/00_modele_global/01_MODELE_LOGIQUE_API_V3.puml` en premier, puis `02_CARTE_21_GET_API.puml` et `03_EXEMPLES_CHAINAGES_GET.puml` dans **le même répertoire**.

Les blocs représentent **exclusivement les réponses et champs de l'API DGEFP–RCO** (21 GET). Aucune table, clé étrangère ou requête SQL n'est utilisable via cette API.

Les métiers sont en **ROME V3 uniquement**. Les compétences/contextes codés OGR proviennent de fiches ROME 4.0 dont l'information est ramenée au métier V3 parent ; aucun code métier V4 n'est restitué.

R17 reste partiel ; R18/R19 ne permettent pas de rattacher chaque session indépendamment depuis leur JSON ; R16, R23 et R24 sont valides **sur exemples**.

La documentation détaillée est dans `00_modele_global/00_LIRE_EN_PREMIER.md` et l'inventaire exact dans `04_INVENTAIRE_EXACT_21_GET.md`.
