# Contrôle R23 — Compétences → Métiers

**Date du contrôle :** 1er novembre 2026  
**Statut :** relation métier-compétence validée sur l'exemple OGR `125416` ; modalités multi-compétences restant à tester.  
**Méthode :** comparaison de deux réponses JSON réellement exportées depuis l'interface Swagger. Aucun appel direct ni requête SQL effectués par l'assistant.

## 1. Appels testés

```http
GET /competences?code=125416&page=1
GET /metiers?competence=125416&mode_competence=toutes&page=1
```

**Fichiers preuves :**

- `R23 GET competencescode=125416&page=1.json`
- `R23 GET metierscompetence=125416&mode_competence=toutes&page=1.json`

Les URL utilisées ont été communiquées comme consignes de test ; les fichiers JSON ne contiennent pas eux-mêmes l'URL effective ou le statut HTTP.

## 2. Réponse de `/competences`

| Attribut | Valeur observée |
|---|---|
| `competence_code` | `125416` |
| `competence_libelle` | Réaliser un raccordement d'étanchéité |
| `categorie_competence_code` | `savoir_faire` |
| `categorie_competence_libelle` | Savoir-faire |
| `domaine_competence_code` | `3` |
| `enjeu_competence_code` | `3D` |
| `macro_competence_code` | `300220` |
| `macro_competence_libelle` | Raccorder, gérer un réseau technique |
| `nb_metiers` | 2 |
| `rome_codes` | `F1610`, `F1705` |
| `rome_coeur_metier_codes` | `F1610` |
| `total` | 1 compétence |

La source de la réponse indique « France Travail - ROME 4.0 (compétences et contextes de travail, codes OGR) rattaché au ROME V3 ».

## 3. Réponse de `/metiers`

`total = 2` ; `items` comporte exactement 2 métiers ; `page = 1`, `page_size = 100`, `last_page = 1`.

| `rome_code` | `rome_libelle` | Domaine métier | Dans `rome_coeur_metier_codes` de `/competences` |
|---|---|---|---|
| `F1610` | Pose et restauration de couvertures | `F16` — Second œuvre | Oui |
| `F1705` | Pose de canalisations | `F17` — Travaux et gros œuvre | Non |

**Vérifications croisées :**

- Les codes des deux métiers de `/metiers` correspondent exactement à `rome_codes` de `/competences`.
- `nb_metiers = 2` concorde avec `total = 2` de `/metiers`.
- Les libellés ROME sont cohérents entre les deux réponses.
- La compétence est indiquée « cœur de métier » pour `F1610` seulement. Cela ne signifie pas que `F1705` n'est pas associé à la compétence : il est bien présent dans `rome_codes` et dans `/metiers`.

## 4. Limites du test

- Avec **un seul** code dans le paramètre `competence`, `mode_competence=toutes` ne permet pas de vérifier sa différence avec `au_moins_une`.
- La réponse de `/metiers` ne retourne pas la liste détaillée des compétences qui ont servi au filtrage en mode `toutes` ; la concordance est vérifiée ici par recoupement avec `/competences`.
- Le sens du classement des résultats ne peut pas être testé avec cet échantillon.
- Aucune relation physique SQL n'a été vérifiée.

## 5. Conclusion

**R23 — Validée sur le cas OGR `125416` → ROME V3 `F1610` et `F1705`.** La distinction « compétence portée par un métier » / « compétence cœur de métier » est bien observable.

Pour tester spécifiquement les règles de mode de recherche multicode, utiliser un jeu de plusieurs compétences et comparer `mode_competence=toutes` et `mode_competence=au_moins_une` ; le contrat donne en exemple les codes `103659,125416,300021`. Cette vérification reste distincte de R23.

## 6. Prochaine étape proposée — R24 Contextes de travail → Métiers

Un contexte de travail effectivement présent dans le résultat métier `F1610` est `300782` (« En grande hauteur »). Tester séparément :

```http
GET /metiers?domaine=F16&contexte=300782&fields=rome_code,rome_libelle,contexte_travail_codes&page=1
GET /metiers?domaine=F16&sans_contexte=300782&fields=rome_code,rome_libelle,contexte_travail_codes&page=1
```

Attendu d'après le contrat : `F1610` peut apparaître dans la première réponse ; il devrait être exclu de la seconde, si les deux appels portent sur les mêmes données. Vérifier les résultats réels avant de conclure.
