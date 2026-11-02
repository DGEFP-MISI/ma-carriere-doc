# Vérifications locales : API DGEFP–RCO / ROME V3

**Un seul dossier à ouvrir**, `API_DGEFP_RCO_REFERENCE_V3`. Exécuter le contrôle global `python scripts/verifier_dossier.py` depuis sa racine.

- `resultats/comparaison_openapi.csv` : version courante / ancien Swagger.
- `resultats/comparaison_echantillons.csv` : seulement noms de champs vs contrats publiés (pas validation des types).
- `resultats/comparaison_schemas_complementaires.csv` : version analytique non officielle ; vérification limitée aux 57 JSON initialement inventoriés.
- `resultats/controle_relations_api.csv` : 24 relations, tests **statiques** de cohérence ; 18 identifiants communs observés, pas 18 tests HTTP.
- `VALIDATION_R16...R24...md` : sept rapports de preuves **directes** (dont deux R23). Leurs JSON sont sous `resultats/Rxx`.
- `CONTROLE_R24_ERREUR_422_A_RETESTER.md` : incident initial et correction `fields`; les deux réponses 422 sont sous `resultats/R24/erreurs_422_initiales/`.

**Statuts** : R16 validé sur cas ; R17 **partiel et ouvert** ; R18/R19 filtrage cohérent, rattachement individuel non prouvé ; R23/R24 validés sur exemples.

**Les sources et rapports historiques ne sont pas des données supplémentaires accessibles via l'API.**
