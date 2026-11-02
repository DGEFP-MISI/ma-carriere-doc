# Visualisations partagées MaCarrière

Bibliothèque de présentation réutilisée par Explorer, sans créer une seconde application. Aucune donnée métier extérieure, aucun endpoint supplémentaire. Les futurs parcours pourront fournir leurs propres réponses natives aux mêmes adaptateurs et compositions.

Les paquets officiels **@gouvfr/dsfr-chart 2.1.1** et **@gouvfr/dsfr 1.15.4** sont installés par npm. Les archives officielles locales sont référencées dans `package.json`, verrouillées dans `package-lock.json` et vérifiées contre les empreintes du registre. Cette installation hors ligne évite de dépendre de la prise en charge du proxy Windows par npm. La provenance et les licences sont dans `vendor/`.

## Organisation

- `src/adaptateurs.mjs` : valeurs typées, états statistiques, séries, familles, continuité mensuelle et codes des cartes. Aucun accès réseau, aucune conversion annuel/mensuel, aucun agrégat métier.
- `src/composants.js` : compositions natives DataBox, BarChart, LineChart, MapChart et TableChart. Aucune bibliothèque de dessin concurrente.
- `src/styles.css` : intégration responsive et alternatives tabulaires.
- `src/infographie.js` et `src/infographie.css` : compositions de présentation MaCarrière, sans règle statistique ni état de parcours ; questions, repères sourcés, icônes officielles et thèmes. [Catalogue d’usage et intégration Explorer](../Explorer/14_direction_artistique/03_COMPOSANTS_ET_INTEGRATION.md).
- `scripts/build.mjs` : assemble les distributions officielles et embarque les ressources CSS pour conserver l’ouverture autonome du HTML. Les scripts officiels ne sont pas réécrits ; la distribution moderne DSFR est isolée dans une fonction pour éviter les collisions de variables globales. Les polyfills de la distribution destinée aux anciens navigateurs ne sont pas chargés.
- `tests/adaptateurs.test.mjs` : cas réels issus des JSON et cas limites unitaires.
- `dist/` : fichiers reconstruisibles, manifeste et résultat des tests.
- `outils/` : Node local ; aucun changement des installations ou du PATH système.

## Reconstruire et tester

Depuis la racine du dossier API, dans PowerShell :

```powershell
$dvRoot = Join-Path (Get-Location) '07_parcours/commun_datavisualisation'
$dvNode = Join-Path $dvRoot 'outils/node-v24.22.2-win-x64/node.exe'
& $dvNode "$dvRoot/scripts/build.mjs"
& $dvNode --test --test-isolation=none "$dvRoot/tests/adaptateurs.test.mjs"
& "$env:LOCALAPPDATA/Programs/Python/Python313/python.exe" -B 07_parcours/Explorer/12_maquette_html/sources/construire.py
& ./07_parcours/Explorer/12_maquette_html/controles/scripts/lancer_controles.ps1
```

Un Node compatible déjà installé peut remplacer le Node local. Après suppression volontaire des dépendances, réinstaller les archives verrouillées avec le CLI npm du Node local :

```powershell
$dvNpm = Join-Path $dvRoot 'outils/node-v24.22.2-win-x64/node_modules/npm/bin/npm-cli.js'
& $dvNode $dvNpm ci --offline --ignore-scripts --no-audit --no-fund --prefix $dvRoot
```

`outils/installer.ps1` conserve la procédure de téléchargement vérifié pour l’environnement ministériel. Il n’est pas nécessaire de la relancer pour reconstruire ou consulter Explorer. Aucun identifiant ni secret n’est enregistré.

## Utilisation dans un parcours

```js
MaDataviz.begin();
const rows = MaDataviz.serie(reponse.items, 'territoire_libelle', 'salaire_net_mensuel_median');
// Filtrer préalablement une seule famille et un seul contexte statistique.
conteneur.innerHTML = MaDataviz.html({
  title: 'Les salaires selon la région', rows, unit: '€ nets par mois',
  source: reponse.source_libelle, date: reponse.millesime,
  description: 'Préciser le groupe, le temps de travail et le territoire réellement couverts.'
});
MaDataviz.mount(conteneur);
```

`kind` accepte `bar` (défaut), `line`, `map`, `key`. Une carte reçoit `map`, `level` et le repère `national` réellement publié. Une courbe exige des mois consécutifs et des nombres présents. Les listes incomplètes restent des barres séparées ; elles ne deviennent pas des répartitions totalisant artificiellement 100 %.

Les graphiques sont montés à l’ouverture de leur accordéon natif ; les tableaux lisibles sont disponibles indépendamment. DataBox fournit la bascule graphique/tableau et les mentions de source et de période. Le tableau autonome demeure disponible lorsque le graphique est fermé ou aucune valeur ne peut être dessinée. Les légendes longues disposent d’un graphique défilant sur petit écran et d’un tableau avec leurs libellés complets.

Les options natives de téléchargement, capture et plein écran restent désactivées dans cette intégration. La version installée ne protège pas toutes les cellules CSV contenant des virgules ou retours à la ligne ; un export statistique fidèle nécessite une adaptation dédiée, distincte de l’export existant de Mes pistes. Aucune conformité RGAA globale n’est déduite de la seule utilisation des composants.

Voir [le compte rendu d’intégration](../Explorer/11_INTEGRATION_DSFR_CHART.md).
