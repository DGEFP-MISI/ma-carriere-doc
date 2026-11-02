J'ai analysé ton fichier `index(1).html` et je l'ai comparé à notre document MaCarrière — Explorer UX V2.

Mon avis : c'est une très bonne base de démonstration, nettement plus aboutie que nos premiers wireframes. Elle montre déjà comment transformer les données de l'API DGEFP–RCO en informations compréhensibles pour le salarié.

En revanche, je ne la validerais pas encore comme maquette fonctionnelle définitive. Elle est très riche sur les données, mais nous avons encore quelques écarts importants avec notre philosophie d'exploration.

## 1. Mon évaluation

Exploitation des données API

5/5

Lisibilité des indicateurs

4/5

Aide à la décision

4/5

Recherche et découverte

2/5

Continuité entre parcours

2/5

Base accessibilité et responsive

3/5

Appréciation de conception fondée sur le HTML et son JavaScript, sans audit RGAA ni recette navigateur complète.

## 2. Ce que je conserverais absolument

L'explication des chiffres. Le prototype distingue bien les projets de recrutement, les offres, les tensions et les salaires. Il signale aussi quand un salaire concerne une famille de huit métiers plutôt que le seul métier de couvreur.

La fiche métier approfondie. Elle permet d'examiner les compétences, les conditions, les territoires, les mobilités et les perspectives 2030. Les informations présentes sont beaucoup plus exploitables qu'une fiche descriptive classique.

Le langage grand public. Beaucoup de titres sont formulés comme de vraies questions : « Combien peut-on gagner ? », « Les employeurs cherchent-ils à recruter ? », etc.

L'utilisation des vrais extraits JSON. Le HTML embarque un jeu de données conséquent et des vérifications automatiques, au lieu de reposer uniquement sur des valeurs inventées.

## 3. Les écarts avec notre UX V2

| Priorité | Ce que je constate dans le HTML                                                                                               | Ce que je recommande                                                                                    |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| P0       | L'ouverture par défaut mène à la fiche métier `essentiel`, pas à Explorer                                                     | Ouvrir la recherche comme point d'entrée                                                                |
| P0       | La barre de recherche n'est pas persistante sur les fiches                                                                    | Garder le mode, la recherche et la possibilité de changer d'objet en haut de page                       |
| P0       | La recherche fonctionne sur le jeu local embarqué, avec une certification et un domaine essentiellement prévus pour l'exemple | Préparer des composants pilotés par les résultats réels de `/metiers`, `/certifications` et `/domaines` |
| P1       | La fiche métier comporte neuf rubriques principales dans la navigation latérale                                               | Les regrouper sous nos quatre grandes questions décisionnelles, avec les détails accessibles ensuite    |
| P1       | Le comparateur est principalement construit autour du couple F1610 / F1613                                                    | Permettre de choisir librement les deux métiers parmi les pistes ou les résultats                       |
| P1       | La localisation est fixée à Montpellier dans le dialogue                                                                      | Prévoir un vrai choix territorial et afficher la maille réelle de chaque indicateur                     |
| P1       | La sélection de pistes est conservée uniquement dans l'état JavaScript de la page                                             | La rendre partageable avec les deux autres parcours, selon la stratégie de conservation retenue         |
| P2       | La recherche guidée par compétences est présentée en trois sections numérotées                                                | Supprimer cette apparence de parcours à étapes et garder les filtres accessibles simultanément          |

### Le point le plus important : la fiche métier est encore trop dominante

Dans le code, la navigation latérale comprend les recrutements, salaires, territoires, mobilités, prospective, secteurs, formations, etc.

C'est très intéressant pour un utilisateur qui veut approfondir, mais cela peut devenir intimidant pour une personne qui découvre MaCarrière.

Je conserverais toutes ces rubriques, mais derrière une première lecture beaucoup plus simple :

FICHE MÉTIER — PREMIÈRE LECTURE

## Pose et restauration de couvertures

ROME V3 · F1610

Second œuvre

Transition écologique

Que fait-on dans ce métier ?

Activités, compétences, conditions

Où sont les opportunités ?

Recrutements, tensions, territoires

Combien gagne-t-on ?

Salaire, quartiles, secteurs

Quelles autres pistes ?

Métiers proches, compétences communes

Pour aller plus loin

Mobilités observées

Perspectives 2030

Certifications

Conditions détaillées

ComparerAjouter à mes pistesPréparer mon projet

Cette organisation réutilise tes contenus actuels ; elle change uniquement leur hiérarchie.

## 4. Trois observations techniques importantes

Premièrement, le HTML est un prototype autonome, pas encore un client API. Il embarque environ 576 Ko de JSON et réalise ses recherches sur ces données locales. C'est tout à fait adapté à la démonstration, mais cela signifie que les recherches libres, les autres métiers et les nouveaux territoires ne sont pas encore couverts comme dans le produit cible.

Deuxièmement, le travail sur les états de données est sérieux. Tu as déjà des distinctions entre zéro et donnée absente, une prise en compte des périmètres statistiques, ainsi qu'un script de vérification déclenchable avec `?verification=1`. C'est une bonne base pour bâtir la recette, même si la présence de tests dans le fichier ne démontre pas à elle seule qu'ils passent tous.

Troisièmement, l'accessibilité est amorcée, mais pas validée. Il y a un lien d'évitement, des styles de focus, des éléments structurés et une adaptation mobile. Il faudra notamment vérifier la gestion du focus au changement de vue, les onglets, les annonces de mise à jour et la navigation clavier. Et nous avons aujourd'hui du CSS inspiré du DSFR, plutôt qu'une intégration complète de ses composants.

## 5. Mon arbitrage pour l'équipe

Je ne recommencerais surtout pas cette maquette. Je la conserverais comme socle de référence pour la restitution des données, en demandant une évolution ciblée de la structure UX.

Je distinguerais trois chantiers :

1. Revoir le point d'entrée et la navigation : recherche persistante, trois modes, ouverture d'une fiche après sélection d'une référence.
2. Réorganiser la fiche métier autour de quatre questions, sans perdre les rubriques approfondies déjà développées.
3. Rendre les composants réellement transversaux : comparateur libre, Mes pistes partagé et passerelle vers Préparer mon projet.

Le reste — notamment la richesse des données et leurs précautions d'interprétation — est une base à préserver.

Mon verdict : très bonne maquette de démonstration des capacités de l'API, mais encore trop proche d'un observatoire détaillé pour représenter notre expérience Explorer définitive.

Avec ces ajustements, elle pourra devenir une base UX cohérente avec nos trois cartes MaCarrière, sans sacrifier tout le travail décisionnel réalisé.