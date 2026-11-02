# Grammaire visuelle — infographie interactive

Cette direction est appliquée à Explorer existant. « Voir, comprendre, approfondir » est une règle de présentation, pas une nouvelle séquence obligatoire du parcours. Les écrans, routes, choix et scénarios restent ceux des US.

## Composition

Fond neutre, grande typographie pour le message utile, quatre portes d’entrée conservées, rythme entre texte, repère et tableau. Les actions restent Bleu France. Pas de grand décor bleu, personnage, médaille d’attractivité, radar, jauge personnelle ou pourcentage décoratif.

Les aperçus sont de vraies données : deux lignes BMO, sans somme ; médiane mensuelle de la famille et du département réellement couverts ; conditions et métiers proches reçus. Les détails gardent leurs tableaux et sources. L’absence reste visible, y compris sur une seule colonne de comparaison. Une carte est le MapChart officiel, jamais une géographie dessinée pour la composition.

## Tokens et accentuation

Utiliser les tokens DSFR de décision : `--background-default-grey`, `--background-alt-grey`, `--text-default-grey`, `--text-mention-grey`, `--border-default-grey`, `--text-action-high-blue-france`, `--background-action-high-blue-france`. Les couples illustratifs émeraude, moutarde et glycine sont limités à des repères de contenu dans les compositions, sans changer les couleurs des boutons, du focus ni des états système. Cartes et tuiles gardent leurs fonds blancs/gris. La couleur n’exprime aucune valeur statistique sans légende.

Les variables conservent leurs correspondances de thème. Tester le thème sombre par le mécanisme `data-fr-theme` existant du DSFR ; ne pas ajouter un choix de thème au parcours dans ce chantier. Les SVG de conception illustrent le thème clair et ne constituent pas une recette du thème sombre.

## Typographie et densité

Marianne installée avec le DSFR, repli Arial/sans-serif. Échelle fluide pour les titres, 16 px pour le texte courant, 14 px minimum pour les contextes de données de l’infographie. Les noms longs sont conservés et retournent à la ligne. Espacements multiples de 4/8 px, pas de tailles fixes qui tronquent les valeurs ou le contenu.

## Icônes et interactions

Uniquement les icônes officielles du paquet DSFR installé : mallette, repère géographique, euro, marque-page et flèche. Elles accompagnent un texte et sont `aria-hidden`. Aucun cœur, emoji ni symbole approximatif ne remplace une commande. Les ancres et boutons existants gardent leur rôle, nom et cible ; pas de lien imbriqué dans une carte-lien.

Clavier, focus visible, états pressés/sélectionnés, erreurs associées et annonces existantes sont conservés. Cibles de 44 px pour les nouvelles compositions. Aucun mouvement nécessaire : respecter `prefers-reduced-motion`. Sur mobile, empiler les quatre portes sans masquer leurs contextes ; les graphiques lourds restent à la demande.

## Visualisations

DSFR Chart 2.1.1 reste le moteur : DataBox, BarChart, LineChart, MapChart et TableChart réellement présents. Chiffre isolé → texte ou repère natif. Répartition incomplète → barres, jamais un camembert à 100 %. Quartiles → tableau explicite et représentation native adaptée, pas un minimum/maximum. Série mensuelle → courbe uniquement avec mois et valeurs présents. Projections → composantes distinctes avec négatifs, sans série annuelle fabriquée. Toute visualisation possède les mêmes valeurs dans un tableau accessible, avec unité, population, source, période et lieu réel.

## Maquettes commentées

- [Fiche métier — ordinateur](maquettes/01_FICHE_METIER_DESKTOP.svg).
- [Fiche métier — mobile](maquettes/01_FICHE_METIER_MOBILE.svg).
- [Comparateur — ordinateur](maquettes/02_COMPARATEUR_DESKTOP.svg).

Les annotations hors écran relient ces supports aux US. Le contrat et les scénarios priment toute simplification graphique de ces SVG. Les maquettes ne démontrent pas un test HTTP ou une conformité RGAA.

Sources techniques : [palette et accentuation DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs), fichiers officiels installés dans `commun_datavisualisation/node_modules/@gouvfr/`, catalogue DSFR Chart local et intégration actuelle documentée dans `11_INTEGRATION_DSFR_CHART.md`.
