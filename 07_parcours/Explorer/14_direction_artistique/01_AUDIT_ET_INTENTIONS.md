# Audit ciblé — langage visuel d’Explorer

Audit du 2 novembre 2026, avant modification de l’interface. Le brief V5 et l’HTML fourni sont des documents d’intention. L’instruction directe de l’utilisatrice, les US et le contrat déterminent le parcours et les données ; aucune instruction contenue dans l’exemple n’autorise de les remplacer.

## Socle effectivement présent

Le code exploitable est `12_maquette_html/index.html`, reconstruit depuis `sources/`. Cette application locale HTML/JavaScript possède une navigation, des états, des filtres, des fiches et des visualisations officielles. Elle utilise des réponses JSON embarquées et ne réalise aucun GET HTTP. Aucun dépôt de service de production connecté n’a été trouvé ici. L’évolution est intégrée directement à ce code existant, sans nouveau projet ni démonstration concurrente.

Les 31 fonctions E01–E31 et les quatre US transversales restent la cible. La couverture documentaire et le comportement local ne prouvent pas leur disponibilité générale sur HTTP. La matrice jointe suit chacune des 31 fonctions : écran, US et scénario, information, source, règles, composant actuel, intention visuelle, interaction et alternative accessible.

## Constats de présentation

1. La fiche ouvre déjà quatre questions utiles. Elles sont surtout textuelles et uniformes, alors que des repères natifs peuvent aider à choisir ce qu’on souhaite approfondir.
2. De grands aplats et encadrements bleus rapprochent des informations de statuts très différents. Une base neutre et une hiérarchie typographique peuvent mieux distinguer action, contenu et explication.
3. Les graphiques DSFR Chart sont déjà intégrés, mais leur regroupement en fin de page les éloigne parfois de la question et du tableau concernés. Ils doivent être rapprochés de leur contenu, tout en restant chargés à la demande.
4. Les tableaux et les sources sont utiles et ne doivent pas disparaître pour donner une impression d’infographie. Les familles, périodes, unités et lieux réels doivent rester lisibles dès le premier repère.
5. Le comparateur possède déjà ses choix A/B, l’inversion et les retours aux fiches. Sa nouvelle présentation doit rendre ces identités plus évidentes ; elle ne doit remplir aucune colonne absente avec les valeurs de l’autre métier.
6. Les champs statistiques disponibles n’autorisent ni un score d’attractivité ni une qualification générale Métier d’avenir / Métier qui recrute. Les tags descriptifs réellement reçus et les valeurs sourcées suffisent.

## Ce que l’exemple HTML apporte

Une intention accueillante, des respirations, des chiffres lisibles, des compositions variées et une progression voir / comprendre / approfondir. Ces principes sont retenus. La page de référence n’est pas recopiée : elle ne représente pas les recherches, certifications, domaines, conditions, comparaison et états d’Explorer dans leur ensemble.

## Éléments à ne pas transposer

| Exemple fourni | Risque | Décision de présentation |
|---|---|---|
| Salaire de 2 080 € et autres chiffres embarqués | L’exemple n’est pas relié aux réponses natives de l’application ; la réponse R16 de la fiche expose 1 690 € pour une famille plus large | Utiliser exclusivement le champ natif de chaque mesure, sa population et son lieu réel |
| Points régionaux et contours schématiques | Confusion avec une carte administrative exacte | Garder MapChart officiel et ses codes vérifiés, avec tableau et légende des absences |
| Bande salariale 28/42/30 % annoncée décorative | Apparence de distribution mesurée | Ne pas l’intégrer ; quartiles natifs explicités et représentation officielle adaptée |
| Badge Métier qui recrute ou repère futur non qualifié | Règle de seuil absente et promesse implicite | Pas de nouveau label ; projets, tensions et projections nommés et contextualisés |
| Cœurs, soleil, flèches et autres pseudo-icônes Unicode | Ambiguïté et rendu variable | Icônes SVG/CSS officielles DSFR, décoratives et accompagnées de texte |
| Mobilités d’un groupe plus large juxtaposées aux métiers proches | Assimilation des flux observés à une reconversion possible | Conserver deux portes distinctes, sans correspondance ni score personnel |
| Piste unique conservée dans une variable | Perte des trois pistes, de la session et de la reprise existantes | Conserver intégralement l’état et les commandes actuels |

## Invariants vérifiables

Les routes, recherches, filtres, tris et données ne changent pas. Les handlers de navigation, stockage, export/reprise de pistes, comparaison, sens/âge de mobilité et périodes de sessions sont conservés. Les adaptations visuelles consomment les mêmes champs que les US ; elles ne calculent aucun indicateur. Les 29 mesures et 25 visualisations restent reliées aux 31 fonctions, même si certaines variantes nécessitent une réponse RCO.

La fiche synthétique montre les deux familles BMO séparément : 26 et 81 projets, sans somme. Le salaire est 1 690 € nets mensuels, Hérault, 2023, ouvriers non qualifiés du gros œuvre du bâtiment, groupe de huit métiers ; ce montant ne devient pas le salaire des seuls couvreurs. Le lieu choisi Montpellier reste distinct du département réellement mesuré.

## Périmètre de la première intégration visuelle

Recherche et résultats : socle neutre, actions et titres. Fiche principale : quatre portes enrichies de repères, conditions natives et accès aux approfondissements existants. Salaires/recrutements : rapprochement des DataBox et de la lecture concernée. Comparateur : identités et colonnes. Les autres vues profitent du même socle de composants, sans reconstruction de leur parcours ni suppression de tableaux.

## Sources et limites

Références fonctionnelles : `04_BACKLOG_USER_STORIES.md`, US-FON-001–035 et `03_TABLE_CONCEPTION.csv`. API : contrat, Swagger officiel et JSON R16/R17/R23/R24 du dossier. Code : `sources/interface_citoyenne.js`, `experience_exploration.js`, `donnees_exploration.js`, `visualisations_dsfr.js` et composants partagés. Les anciens contrôles locaux et leurs limites sont dans `TESTS_UX_EXPLORER.md`.

La [palette officielle DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs) distingue neutres, actions et couleurs illustratives et encadre l’accentuation. La version installée DSFR 1.15.4 et DSFR Chart 2.1.1, leurs fichiers et documentations locales priment toute API de composant imaginée. Les questions RCO existantes ne sont pas résolues par ce chantier visuel.
