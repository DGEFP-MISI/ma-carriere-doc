# Composants et première intégration

L’évolution est intégrée au fichier existant [index.html](../12_maquette_html/index.html). Aucun nouvel Explorer, nouveau routeur, framework ou projet n’a été créé. Le socle présent est une application locale autonome ; l’application de production connectée n’est pas dans ce dossier. Aucun branchement HTTP n’est revendiqué.

## Catalogue réutilisable

| Composition | Fichier | Usage et contrat de présentation | États / alternative |
|---|---|---|---|
| `MaInfographie.icon` | `../../commun_datavisualisation/src/infographie.js` | Liste fermée d’icônes officielles DSFR ; décoratives, accompagnées de texte | Aucun fait ou statut porté par la seule icône |
| `MaInfographie.question` | Même fichier | Porte d’entrée : question, description, aperçu, même route de destination | Ancre native, focus visible, aucun contrôle interactif imbriqué |
| `MaInfographie.repere` | Même fichier | Affiche une valeur native et son unité, sans calcul ; réemploie les états de `MaDataviz.valeur` | Zéro, absence, null, secret, type invalide distingués en texte |
| `MaInfographie.provenance` | Même fichier | Lieu effectif, période, population et source fournis par le parcours | N’invente aucune métadonnée manquante |
| `MaInfographie.decorate` | Même fichier | Icône de résultat et remplacement des anciennes flèches décoratives | N’altère ni le texte d’action, ni les handlers, ni les identifiants |
| Socle visuel et thèmes | `../../commun_datavisualisation/src/infographie.css` | Tokens DSFR, compositions, responsive, contraste, mouvement réduit | États DSFR conservés ; contenu intégral à 320 px |
| `apercuQuestion` / `cartesQuestions` | `../12_maquette_html/sources/infographie_explorer.js` | Adaptation de présentation propre à Explorer, à partir des réponses déjà reçues | Une sélection de lieu non couverte n’affiche aucun repère de Montpellier |
| `disposerInfographie` | Même fichier | Rapproche les DataBox existantes de leur question dans les vues salaires/recrutements | Modèles, valeurs, tableaux, groupes et chargement à la demande inchangés |

Ces compositions sont propres à MaCarrière et compatibles avec le DSFR ; elles ne sont pas présentées comme de nouveaux composants officiels DSFR Chart. Les types de graphiques restent ceux déjà installés : DataBox, BarChart, LineChart, MapChart et TableChart. Aucun graphique statistique personnalisé n’a été créé.

## Séparation des responsabilités

1. Données : JSON natifs inchangés dans le dossier API, embarqués par le constructeur existant.
2. Adaptation statistique : `src/adaptateurs.mjs` inchangé ; états, familles, mailles et séries restent ses contrats.
3. Règles et état de parcours : recherche, choix, stockage, comparaison, sessions et navigation existants conservés.
4. Présentation : composants communs `MaInfographie`, styles et pont `infographie_explorer.js`. Les conditions montrées en aperçu sont une sélection éditoriale de trois libellés réellement présents, pas un classement d’importance ou une mesure de pénibilité.

## Écrans intégrés progressivement

**Fiche métier.** Les quatre questions conservent leur ordre et leurs routes. Elles montrent respectivement des conditions natives, les deux familles de projets de recrutement, la médiane et sa population, et un métier proche effectivement référencé. Le salaire ne devient pas un salaire individuel. Le lieu demandé reste distinct du bassin ou département observé. Les descriptions détaillées sont conservées ; les liens existants vers mobilités, prospective, formations et secteurs sont visibles sous les questions.

**Recherche et résultats.** Même formulaire, mêmes modes et même sélection explicite avant ouverture. Base neutre, titres et cartes plus lisibles, icônes officielles. Aucun texte de recherche n’est transformé en identifiant.

**Salaires et recrutements.** Les visualisations officielles sont rapprochées des métriques et tableaux correspondants. Aucune ouverture automatique de graphique n’est imposée. Les tableaux, sources, limites et séries restent disponibles avec leurs valeurs natives.

**Comparateur.** Même paire A/B, mêmes sélecteurs, inversion, rubriques et retours. Identités et colonnes utilisent le socle visuel commun. La colonne statistique du second métier reste non renseignée lorsqu’aucune réponse ne l’alimente.

**Autres écrans.** Certification, domaine, guide, sessions, Mes pistes, mobilités, prospective, secteurs et sources conservent leur contenu et leurs interactions ; ils bénéficient du même socle de typographie, tableaux, états et thèmes. Leur couverture HTTP reste celle du backlog, pas celle d’un chantier de présentation.

## Fichiers modifiés et construction

- Nouveaux composants partagés : `src/infographie.js`, `src/infographie.css`.
- `commun_datavisualisation/scripts/build.mjs` : embarque les compositions et cinq icônes DSFR supplémentaires ; distributions officielles conservées.
- `12_maquette_html/sources/infographie_explorer.js` : pont de présentation.
- `sources/experience_exploration.js` : seul le rendu de la vue d’ensemble est enrichi ; les autres fonctions sont inchangées.
- `sources/interface_citoyenne.js` : un appel au placement/décor après le rendu ; handlers et règles conservés.
- `sources/modele.html` : classe de présentation et déclaration de compatibilité des thèmes.
- `sources/construire.py` : assemble les nouveaux fichiers ; `index.html` et documents de contrôle sont reconstruits.
- Les README et ce dossier documentent le chantier. Les US, la table de conception, le contrat, Swagger, UML et JSON de référence ne sont pas modifiés.

Reconstruire avec le build Node partagé, puis `sources/construire.py`, selon les commandes du README existant. Le résultat reste autonome et ouvrable sans serveur. Les captures sont des preuves, pas une application parallèle.

## Ce qui reste à valider ou réaliser

La direction proposée n’ajoute pas de label « Métier qui recrute » ou « Métier d’avenir » : aucune règle produit et contractuelle ne l’autorise. Ajouter un tel repère exigerait une règle explicitement décidée et démontrée, pas une simple couleur.

La compréhension auprès de salariés réels de profils variés, les lecteurs d’écran, l’audit RGAA complet et le zoom navigateur natif restent à recetter. Les questions RCO, la couverture des variantes de données et l’application de production HTTP restent suivies dans le backlog existant. L’export CSV des statistiques reste une tâche E12 ; les actions désactivées ne sont pas présentées comme livrées.
