# Contrôle R18 — Certifications + territoire → Sessions à venir

**Date du contrôle :** 1er novembre 2026  
**Source :** réponse JSON exportée de l'interface Swagger, fournie par l'utilisatrice  
**Endpoint :** `GET /sessions_a_venir`  
**Paramètres indiqués pour le test :** `certifinfo=112561`, `zonage=region`, `territoire=76`, `onisep=exclure`, `page=1`  
**Statut :** **partiellement validé** — réponses opérationnelles et cohérence territoriale observées ; rattachement individuel à la certification non vérifiable dans la réponse seule.

## 1. Résultats contrôlés

| Contrôle | Valeur observée | Appréciation |
|---|---|---|
| Nombre d'éléments dans `items` | 10 | Conforme à `total=10` |
| Pagination | `page=1`, `page_size=100`, `last_page=1` | Pas de page supplémentaire signalée |
| Localisation | 10 lignes à **Tarbes**, `code_insee=65440` | Cohérent avec la région Occitanie demandée (`76`) |
| Organisme formateur | `CENTRE DE TARBES` | Identique pour les 10 lignes |
| SIRET du formateur | `82422814200132` | Identique pour les 10 lignes |
| Date de début la plus proche | `2026-11-23` | Postérieure à la date du contrôle |
| Dernière date de début | `2027-09-06` | Date maximum dans l'échantillon |
| Dates de fin | De `2027-01-26` à `2028-05-18` | Dates retournées par l'API |
| `tag_onisep` | `false` sur 10/10 | Cohérent avec `onisep=exclure` |
| `formation_apprentissage` | `true` sur 3/10 | Signalement descriptif, sans déduction métier |
| `formation_contrat_pro` | `true` sur 3/10 | Les trois lignes sont aussi marquées apprentissage ; sémantique à confirmer si utile |
| `nb_sessions` | `1` dans chaque ligne | Somme des valeurs : 10 |
| Doublons JSON strictement identiques | 0 | Ne prouve pas l'unicité métier des sessions |

## 2. Relation réellement démontrée

L'appel filtré par les paramètres ci-dessus renvoie une liste de dix résultats, situés dans la région demandée et portant tous `tag_onisep=false`.

**Limite :** la réponse ne restitue ni `certifinfo`, ni `rncp`, ni identifiant stable de session. Le fait qu'une liste soit retournée pour `certifinfo=112561` est une preuve de fonctionnement de l'appel filtré, mais **ne permet pas de vérifier indépendamment que chaque session est effectivement rattachée à la certification 112561**. Il ne faut pas assimiler le SIRET formateur à un identifiant de session.

## 3. Contrôles complémentaires recommandés

1. Vérifier le lien de `112561` à la certification dans `/certifications` ou `/certifications/{certifinfo}` si nécessaire.
2. Demander à RCO comment tracer pour chaque ligne de `/sessions_a_venir` l'identifiant Certif Info et/ou un identifiant unique de session lorsque ces champs ne sont pas exposés.
3. Tester R19 à paramètres identiques sur `/sessions_en_cours`, sans présumer du nombre de résultats.

## 4. Conclusion

**R18 : partiellement validée sur réponse réelle.** Cohérence du territoire, pagination, dates et exclusion Onisep contrôlées. La preuve de jointure certification → session reste indirecte tant que l'identifiant de certification n'est pas restitué dans les éléments ou vérifié via une autre source.
