# Modèle commun de User Story fonctionnelle — MaCarrière

Ce modèle s’applique à Explorer, Faire évoluer ma situation et aux futurs parcours. Il décrit le besoin et le comportement attendu avant le découpage technique. Il ne crée ni fonctionnalité non décidée, ni source de données, ni recommandation automatisée.

Chaque US porte un identifiant stable. Dans un parcours, préciser aussi les anciens identifiants, les dépendances, le lot technique, le niveau de preuve et les liens vers la conception, les tests et la maquette. Les identifiants peuvent être qualifiés par le parcours pour éviter une collision entre deux backlogs.

```text
US-FON-NNN — Nom de la fonctionnalité
Parcours : …
Alias / conception : …
Périmètre : inclus / décision à instruire, sans confondre avec l’état de développement
Lot et dépendances : …
État : documenté / JSON observé / testé localement / HTTP validé sur cas tracé / à confirmer
```

## 1. Objectif fonctionnel

Décrire le résultat utile pour la personne, les limites de la fonction et son articulation avec le parcours. Éviter de remplacer l’objectif par le nom d’un composant ou d’une route API.

## 2. User Story

En tant que **[profil utilisateur]**, je souhaite **[action ou besoin]**, afin de **[bénéfice attendu]**.

## 3. Préconditions

Préciser l’objet éventuellement sélectionné, les données nécessaires, les autorisations réellement requises, les dépendances et les hypothèses. Distinguer le comportement du démonstrateur local de celui du service connecté. Ne pas rendre un compte ou un métier cible obligatoires sans décision produit.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Entre dans la fonction depuis un point identifié | Affiche le contexte et les actions adaptées |
| 2 | Saisit ou sélectionne une information | Conserve les choix et vérifie les critères documentés |
| 3 | Déclenche l’action | Exécute les appels utiles, annonce l’attente et protège les choix |
| 4 | Consulte le résultat | Affiche les données disponibles, leur sens et leurs limites |
| 5 | Poursuit son exploration | Ouvre l’objet choisi ou revient au contexte précédent sans perte injustifiée |

Remplacer ces étapes génériques par les gestes et résultats précis de la fonctionnalité. Ajouter des étapes quand un changement de filtre, une reprise ou un retour fait partie du chemin normal.

## 5. Scénarios alternatifs

Décrire les bifurcations utiles : plusieurs résultats, absence réelle, combinaison non renseignée, modification des choix, données partielles, pagination, valeur manquante, erreur et reprise. Pour chaque cas, donner le résultat visible et l’issue proposée.

Une réponse vide, l’absence d’un exemple local et l’échec d’un appel ne sont pas trois formulations d’un même état.

## 6. Règles de gestion

Préciser les règles métier, conditions d’affichage, contrôles et interprétations. Séparer décisions actées et propositions à arbitrer. Pour MaCarrière : noms compréhensibles, ROME V3 uniquement, sources conservées, aucune maîtrise personnelle ou employabilité déduite d’une référence métier.

Pour les statistiques, conserver unité, population, source, période, grain et territoire réellement mesuré. Distinguer `0`, `null`, champ absent, liste vide, liste incomplète et `secret_stat`. Ne pas recomposer de valeurs masquées ni calculer de score, delta, taux ou série non prévus.

## 7. Données et API

| Ordre / déclenchement | GET autorisé | Paramètres et origine | Champs / types | Traitement et restitution |
|---|---|---|---|---|
| … | Route exacte | Chemin/query, obligatoire/facultatif, valeurs admises | Chemins JSON réellement décrits, avec leur preuve | Sélection, formatage, pagination, réutilisation ; pas de calcul métier inventé |

Indiquer les sources documentaires, les réponses observées et les tests validés séparément. Un contrat local décrit une API ; il ne constitue pas lui-même une source de données distante accessible par le produit. Pour une opération purement locale, écrire « Aucun appel spécifique » et décrire les données réutilisées, sans inventer de POST ou de stockage serveur.

Ajouter les traitements des valeurs manquantes, les règles statistiques propres à l’indicateur et les dépendances fournisseur. Identifier explicitement toute demande non couverte, sans proposer une autre source métier.

## 8. Critères d’acceptation

Chaque critère a un identifiant stable et doit être vérifiable :

```gherkin
Étant donné [contexte observable et données identifiées]
Quand [action précise]
Alors [résultat observable et contrôlable]
```

Couvrir le nominal, les alternatives importantes et les limites d’interprétation. Préciser pour chaque campagne : réalisé ou à exécuter, périmètre local ou HTTP, preuve et résultat. Une spécification, un test statique et une interaction navigateur ne démontrent pas le même niveau de fonctionnement.

## 9. Composants UX/UI

Lister les composants réellement nécessaires : DSFR pour formulaires, navigation, cartes, tableaux, messages et dialogues ; DSFR Chart pour les visualisations pertinentes, préférentiellement avec DataBox et alternative tabulaire. Ne pas ajouter un graphique à une information mieux comprise en texte ou tableau.

Décrire états initial, saisi, sélectionné, attente, vide, partiel, erreur, réussite et désactivation lorsqu’ils s’appliquent. Préciser clavier, libellés et erreurs associés, focus après mise à jour, annonces, contraste, tailles tactiles, responsive et mouvement réduit. Une alternative accessible contient les mêmes valeurs et leur contexte.

**GenUI n’est pas un prérequis du backlog Explorer actuel.** Si un futur parcours l’emploie, documenter le moteur effectivement disponible et les composants autorisés ; aucune génération de faits métier ou de règles de recommandation n’est impliquée par ce modèle.

## 10. Maquette fonctionnelle

Lier un SVG autonome, avec titre et description accessibles, montrant l’entrée, les contrôles, la restitution, les alternatives et les poursuites. Le SVG est une spécification d’interactions, pas la preuve qu’une fonction est développée ou conforme RGAA.

Utiliser des libellés de champs et emplacements explicites, sans faux salaires, métiers, formations ou taux. Tout chiffre métier illustré doit être relié à une preuve ; les emplacements sans donnée restent nommés comme tels.

## Convention de traçabilité et fin de rédaction

Une US est rédigée quand ses dix sections, ses critères, ses appels autorisés, ses preuves, ses dépendances et son SVG sont présents et cohérents. Cela ne signifie pas qu’elle est réalisée ou validée en production.

Conserver les colonnes de pilotage métier, API, UI/UX, développement, SEO et validation dans la table commune du parcours. Relier chaque US à cette table et vérifier que toutes les fonctions, mesures et variantes prévues possèdent au moins un propriétaire fonctionnel. Les fonctions dépendant d’un test restent dans le périmètre.

Application initiale : [backlog Explorer](../Explorer/04_BACKLOG_USER_STORIES.md).
