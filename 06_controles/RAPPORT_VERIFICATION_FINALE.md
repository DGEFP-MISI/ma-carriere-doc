# Vérification finale du dossier de référence API DGEFP–RCO — 01/11/2026

## Objet et périmètre

Archive source : `API_DGEFP_RCO_VSCode_V2_complet(1).zip`. Nouvelle racine de travail : `API_DGEFP_RCO_REFERENCE_V3`.

Périmètre : **21 GET de l'API spécifique, exclusivement identifiants métiers ROME V3**, sans table ou accès SQL, ni autre API. Les compétences et contextes OGR issus de ROME 4.0 sont rattachés au ROME V3 parent, conformément au contrat.

## Contrôles effectivement exécutés dans la copie consolidée

| Vérification | Résultat local | Réserve |
|---|---|---|
| `verifier_contrat.py` | **OK**, 21 GET actuels et 21 précédents | Comparaison d'exports fournis, pas une interrogation du serveur |
| `verifier_echantillons.py` | **OK**, 57 JSON initiaux inspectés | 45 **fichiers** ne disposent pas de schéma officiel HTTP 200 sur leur route, pas 45 routes |
| `verifier_schemas_complementaires.py` | **OK**, 21/21 modèles analytiques disponibles ; 0 fichier avec champ inconnu | Schémas enrichis **non officiels**, contrôle des noms de clés seulement |
| `verifier_relations_api.py` | **OK**, 24 relations, 18 correspondances statiques, 6 non testables par cette méthode | Correspondance de codes ≠ appel HTTP effectif |
| `verifier_uml_global.py` | **OK**, 21 GET présents exactement une fois dans la carte ; 24 relations ; 3 UML de référence | Pas de rendu PlantUML exécuté ici |
| `verifier_preuves_directes.py` | **OK**, contrôles R16, R17, R18, R19, R23, R24 sur les JSON remis | Ces cas ne constituent pas des tests exhaustifs de l'API |

**Six scripts sur six terminés sans échec.** Vérification Python de la syntaxe des scripts : OK. **89 fichiers JSON** analysés syntaxiquement dans le dossier (catalogue, sources et preuves). Les **62 fichiers** du contrat et des réponses initiales (`01_sources` + `02_reponses_observees`) ont été comparés octet par octet avec l'archive extraite : **aucune modification**.

## Correctifs et consolidation

- Le contrôle UML défaillant a été corrigé : noms exacts du fichier et des composants `GET /...`, comparaison aux 21 routes Swagger.
- Les deux preuves R16 étaient inversées : renommées d'après le contenu réellement retourné, et rapport aligné.
- La réponse `GET /competences?code=103659&page=1` est ajoutée à R23 ; libellé et rattachements ROME V3 contrôlés.
- Les premiers retours 422 de R24 sont classés comme erreurs `fields`, séparément des réponses de filtres réussies.
- Les anciens UML et le brouillon R17 sont conservés comme archives **non références** ; les rapports répétés ont été dédupliqués.
- Les notices de lecture, tâches VS Code, chemin d'entrée unique, statut R17 et matrice de relations ont été harmonisés.
- Un lanceur Windows `LANCER_CONTROLES.cmd` et un manifeste SHA256 ont été ajoutés.

## Points réellement ouverts

1. **R17** : `/secteurs` sans filtre ROME renvoie 35 secteurs ; avec `rome=F1610` les deux réponses disponibles sont vides. Ce comportement doit être éclairci côté RCO, pas masqué par le nettoyage.
2. **R18 / R19** : filtres de session cohérents ; aucun identifiant de session ni code Certif Info dans les objets retournés pour vérifier indépendamment le rattachement ligne par ligne.
3. **Swagger officiel** : 10 routes sans schéma 200 déclaré. Le complément ne remplace pas le Swagger fournisseur.
4. Le contrôle de ce dossier est **local et hors connexion**. Les scripts PowerShell et la représentation graphique PlantUML n'ont pas été exécutés dans cet environnement Linux ; seul leur contenu statique est conservé.

## Décision

Le dossier est **prêt à être utilisé comme espace VS Code consolidé** pour l'analyse des 21 GET et les relations ROME V3. Il ne démontre pas que l'ensemble des filtres fonctionnent en production. Ne supprimer l'ancienne copie qu'après téléchargement, extraction et ouverture du nouveau dossier.
