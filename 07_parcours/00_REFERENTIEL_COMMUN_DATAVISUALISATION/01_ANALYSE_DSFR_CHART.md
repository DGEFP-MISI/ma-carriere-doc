# Analyse vérifiée — DSFR Chart pour MaCarrière

## Sources publiques consultées (2 novembre 2026)
- Dépôt officiel : https://github.com/GouvernementFR/dsfr-chart
- README : https://github.com/GouvernementFR/dsfr-chart/blob/main/README.md
- Démonstration : https://gouvernementfr.github.io/dsfr-chart/ (site rendu dynamiquement : les écrans interactifs n'ont pas été testés automatiquement).
- Licence et version exacte : contrôle obligatoire à l'installation dans le dépôt, ne pas présumer la version CDN. Dépôt observé non archivé, branche principale `main`.

## Composants réellement documentés
| Composant documenté | Balise | Usage MaCarrière | Décision |
|---|---|---|---|
| Barres | `bar-chart` | Territoires, secteurs, mobilités, taux | Prioritaire |
| Courbes | `line-chart` | Seulement séries temporelles authentiques | Pas de courbe 2019→2030 inventée |
| Barres + ligne | `bar-line-chart` | Unités distinctes et séries comparables dans le temps | À encadrer, non nécessaire au MVP |
| Circulaire / anneau | `pie-chart` | Parts exhaustives avec même dénominateur | Sous conditions |
| Carte de France et monde | `map-chart` | Régions et départements | Prioritaire après contrôle codes |
| Carte régionale | `map-chart-reg` | Départements d’une région | À tester |
| Nuage de points | `scatter-chart` | Deux mesures de même population/grain ; sinon rejet | Exploration avancée conditionnée |
| Radar | `radar-chart` | Séries homogènes avec axes comparables | Écarté pour salaires vs recrutement |
| Jauge | `gauge-chart` | Mesure avec cible métier explicite et justifiée | Pas de cible arbitraire |
| Boîte de données | `data-box` | Valeur + source + date + graphique/tableau + export | Enveloppe commune prioritaire |

## Pré-requis techniques confirmés
- Bibliothèque de web components implémentés sous Vue; package npm `@gouvfr/dsfr-chart`.
- Projet utilisant DSFR. Charger `dsfr.min.css`, `icons-system.min.css` et `dsfr.module.min.js` puis scripts et CSS DSFR Chart.
- Usage avec bundler : `import '@gouvfr/dsfr-chart'; import '@gouvfr/dsfr-chart/css'` ; imports ciblés possibles mais mise en garde officielle pour plus de deux composants (charges répétées de moteurs).
- Valeurs des axes passées sous forme de chaînes sérialisées contenant listes JSON, pas des objets JavaScript bruts dans des attributs HTML.
- Palette, ratio, infobulles, axes, barres horizontales/empilées, surbrillance et vues sombre/claire documentés.
- DataBox peut exposer titre, description, source, date, vue tableau, plein écran, menu, export CSV et capture selon activation.

## Limites fondamentales
- **Cartes :** `level=reg` demande des codes DSFR Chart comme `IDF`, `ARA`, `GES`, alors que l'API peut retourner `11`, `84`, `44`. Adaptateur explicite et testé obligatoire; géographies outre-mer et Corse à contrôler. `level=dep` accepte codes de départements (dont 2A/2B); CLPE non supporté nativement par `map-chart`.
- **Tableau :** la DataBox documente une alternative tabulaire; ce n'est pas un composant de tableau analytique universel. Prévoir HTML/DSFR pour tableaux longs, filtres, tris et clavier.
- **Courbes :** 2030 est un horizon de projection, pas une série chronologique intermédiaire.
- **Radar :** n'assembler jamais des indicateurs d'unités/populations différentes.
- **Jauge :** nécessite un objectif légitime; ne pas inventer de seuil de succès.
- **Interaction :** le clic sur région, navigation clavier, remontée des événements, export et modal doivent être audités dans la version installée; ne pas supposer qu'une carte est navigable par défaut.
- **RGAA — approche de réutilisation :** privilégier les dispositifs d’accessibilité et les alternatives déjà documentés dans DSFR Chart. Ne pas réauditer la bibliothèque depuis zéro ; vérifier la restitution et les interactions une fois intégrées dans MaCarrière (titre, tableau, filtres, clavier, responsive). La conformité de l’application complète reste distincte de celle du composant.

## Matrice de décision graphique
1. Une valeur → chiffre clé avec unité/étiquette, pas graphique.
2. Deux à trente catégories comparables → barres horizontales, tri contrôlé, tableau.
3. Valeurs géographiques cohérentes → carte + liste ordonnée / tableau; pas de cartographie lorsqu'une maille repliée rend les territoires non comparables.
4. Composition d'un total prouvé → barres empilées/anneau si nombre de catégories raisonnable.
5. Dates répétées observées au même grain → courbe; jamais inventer les années intermédiaires.
6. Statistiques incompatibles ou incomparables → deux panneaux autonomes avec métadonnées, sans échelle commune.

## Pistes à vérifier par Codex
Confirmer l'API des événements, compatibilité framework, bundles et tailles, version et sécurité des dépendances, paramètres DataBox exacts, focus modalités, chargement différé, SSR, thèmes et comportement au redimensionnement. Ne pas engager de développement avant audit.
