# Journal de consolidation — 1er novembre 2026

**Entrée :** `API_DGEFP_RCO_VSCode_V2_complet(1).zip` (160 fichiers initiaux).
**Sortie :** dossier autonome `API_DGEFP_RCO_REFERENCE_V3`, strictement 21 GET / métier ROME V3.

## Corrections appliquées

1. **Script UML corrigé** : nouveau chemin vers `02_CARTE_21_GET_API.puml`, extraction des libellés `component "GET /..."`, comparaison automatique aux routes GET du Swagger fournisseur et contrôle des 24 relations.
2. **R16** : les deux fichiers JSON ont été renommés d'après leur **contenu réel**, sans toucher aux réponses ; rapport harmonisé avec les nouveaux noms.
3. **R23** : ajout du JSON `/competences?code=103659&page=1`, preuve du libellé `Poser des panneaux solaires` et des liens avec les codes ROME V3 `F1610` / `I1604`. Rapport actualisé : aucune erreur technique inférée de ce lien.
4. **R24** : conservation des deux erreurs HTTP 422 d'origine sous `erreurs_422_initiales/`; réussite des filtres `contexte` et `sans_contexte` vérifiée séparément.
5. **Documentation** : nouvelle page d'entrée unique et notices UML, rectification des anciens chemins, distinction nette échantillons historiques / preuves R17, clarification de 18 comparaisons de codes statiques.
6. **Déduplication** : suppression des copies de rapports répétées dans les sous-dossiers de JSON. Une seule version de chaque compte rendu reste à la racine de `06_controles/` ; ancien brouillon R17 placé en archive.
7. **UML historiques** : 11 anciens diagrammes/aperçus déplacés vers `05_uml/_archives_non_reference/` ; trois diagrammes stricts conservés comme seule référence.
8. **Périmètre** : ancien dossier sur le schéma SQL physique retiré et mode d'installation complémentaire obsolète supprimé. **Aucune source ni réponse JSON historique du catalogue initial n'a été modifiée.**
9. **Tests** : script global, script de vérification des preuves directes, lanceur Windows `LANCER_CONTROLES.cmd` ajoutés ; tâches VS Code mises à jour.

## Points qui demeurent ouverts (ils ne sont pas "corrigés" par le nettoyage)

- **R17** : résultats `/secteurs?rome=F1610` vides malgré des secteurs sans filtre métier ; sollicitation RCO à poursuivre si nécessaire.
- **R18/R19** : filtrage cohérent, mais absence d'identifiant et de code Certif Info renvoyés par les sessions.
- **Schéma fournisseur** : 10 réponses 200 non documentées ; le Swagger enrichi n'est pas officiel.
- **Rendu PlantUML** : contrôle des bornes et des routes fait en local ; le rendu graphique n'a pas été exécuté sauf mention contraire dans le rapport final.

Le dossier consolidé est **indépendant** des compléments et des précédentes archives. Après ouverture et vérification du ZIP, l'ancien dossier peut être supprimé par l'utilisatrice.
