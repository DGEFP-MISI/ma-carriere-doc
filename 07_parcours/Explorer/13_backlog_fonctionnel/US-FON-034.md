# US-FON-034 — Comprendre les données et leurs sources sans connaître les référentiels

**Rattachement :** exigence transversale des 31 fonctionnalités. **Lot :** Transversal L2 à L9 ; validation Métier/Data et recette L10.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-001](US-FON-001.md) (E01); [US-FON-002](US-FON-002.md) (E02); [US-FON-003](US-FON-003.md) (E03); [US-FON-004](US-FON-004.md) (E04); [US-FON-005](US-FON-005.md) (E05); [US-FON-006](US-FON-006.md) (E06); [US-FON-007](US-FON-007.md) (E07); [US-FON-008](US-FON-008.md) (E08); [US-FON-009](US-FON-009.md) (E09); [US-FON-010](US-FON-010.md) (E10); [US-FON-011](US-FON-011.md) (E11); [US-FON-012](US-FON-012.md) (E12); [US-FON-013](US-FON-013.md) (E13); [US-FON-014](US-FON-014.md) (E14); [US-FON-015](US-FON-015.md) (E15); [US-FON-016](US-FON-016.md) (E16); [US-FON-017](US-FON-017.md) (E17); [US-FON-018](US-FON-018.md) (E18); [US-FON-019](US-FON-019.md) (E19); [US-FON-020](US-FON-020.md) (E20); [US-FON-021](US-FON-021.md) (E21); [US-FON-022](US-FON-022.md) (E22); [US-FON-023](US-FON-023.md) (E23); [US-FON-024](US-FON-024.md) (E24); [US-FON-025](US-FON-025.md) (E25); [US-FON-026](US-FON-026.md) (E26); [US-FON-027](US-FON-027.md) (E27); [US-FON-028](US-FON-028.md) (E28); [US-FON-029](US-FON-029.md) (E29); [US-FON-030](US-FON-030.md) (E30); [US-FON-031](US-FON-031.md) (E31).

**État constaté au 2 novembre 2026 :** Instruction citoyenne actée ; libellés, sources, valeurs et absence de vocabulaire interne contrôlés localement. Métadonnées documentées et JSON observés, avec notices disponibles pour 29 mesures. Validation de compréhension et formulations métier finales à mener ; aucun score de lisibilité ni résultat d’étude réelle inventé. HTTP réel à tester séparément.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Présenter les informations de façon utile aux salariés de tous profils : ce qui est mesuré, pour qui, où et quand. Conserver la précision statistique et les sources sans imposer les codes, le vocabulaire interne ou une lecture experte de la donnée.

## 2. User Story

En tant que personne qui veut décider de son avenir professionnel sans être spécialiste des données, je souhaite comprendre les noms, les chiffres et leurs limites, afin de réfléchir à mes possibilités avec des repères fiables.

## 3. Préconditions

- Les noms des métiers, domaines, certifications, compétences, contextes, lieux et secteurs sont issus des libellés natifs associés aux identifiants.
- Les notices des 29 mesures, les sources et les définitions contractuelles sont disponibles pour les restitutions concernées.
- Chaque réponse statistique conserve son grain, sa population, sa période, son unité et sa géographie effective ; une absence de valeur reste distincte d’une absence de documentation.
- Les textes d’explication s’appuient sur les définitions disponibles ; la validation Métier/Data des formulations définitives reste à mener.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Ouvre une fiche métier depuis une recherche par nom. | Affiche le nom du métier et les questions de première lecture : activités, opportunités, salaires et autres pistes ; garde les rubriques détaillées accessibles ensuite. |
| 2 | Consulte un salaire. | Présente la médiane et une explication de son sens, l’unité nette mensuelle ou annuelle, la population à temps complet, le groupe de métiers concerné, le lieu effectif, l’année et la source. |
| 3 | Consulte les recrutements et les perspectives à 2030. | Distingue projets de recrutement, offres publiées et estimations à horizon 2030 ; conserve les valeurs reçues et explique qu’il ne s’agit pas d’emplois garantis à la personne. |
| 4 | Ouvre un détail ou la rubrique Sources. | Présente les définitions, organismes, périodes, populations, périmètres et limites utiles avec des mots compréhensibles, sans noms de champs techniques ni mentions de version du projet. |
| 5 | Rencontre une donnée absente, confidentielle ou portant sur une zone plus large. | Explique la situation avec le bon message et propose de poursuivre en modifiant ses choix ou en consultant une autre rubrique ; ne présente pas l’absence d’information comme une absence d’emploi. |
| 6 | Compare deux métiers puis garde une piste. | Laisse lire les repères séparément, signale les groupes et populations différents et conserve l’action de choix à la personne, sans note globale ni recommandation de réussite individuelle. |

## 5. Scénarios alternatifs

- Le libellé nécessaire est absent : le système indique qu’il ne peut pas nommer cet élément et conserve la trace technique pour investigation ; il ne fabrique pas un nom ni ne remplace le titre citoyen par un code incompréhensible.
- Une statistique concerne une famille de plusieurs métiers : le nom du groupe et la portée de la statistique sont indiqués au voisinage du chiffre, sans l’attribuer au seul métier consulté.
- Une médiane numérique est absente mais une tranche annuelle ouverte est publiée : la tranche est expliquée en texte ; aucun montant mensuel précis n’est inventé.
- Les nombres et taux de recrutement semblent divergents : les valeurs originales sont conservées avec une explication prudente de leur statut ; le client ne les corrige pas par calcul.
- Une situation de mobilité désigne une famille ou une situation hors emploi sans identifiant de métier : le nom reçu est lisible, mais aucun lien vers une fiche métier n’est déduit.
- Une information sur l’insertion concerne une autre population ou un autre horizon : elle reste dans son groupe propre, sans comparaison directe trompeuse.

## 6. Règles de gestion

- Les codes restent dans les relations techniques ; les résultats et commandes affichent les noms natifs. Les noms officiels des organismes sources restent accessibles.
- Les mentions Explorer V2, maquette, campagnes de tests, schémas, paramètres et contraintes d’intégration ne font pas partie de l’écran citoyen. Les limites statistiques nécessaires à sa décision y restent.
- ROME V3 est le référentiel interne autorisé ; aucun code métier ROME 4.0 n’est restitué. Les groupes FAP sont expliqués comme groupes statistiques sans imposer leurs codes.
- La médiane n’est ni une moyenne ni un salaire garanti ; Q1 et Q3 ne sont pas un minimum et un maximum ; annuel et mensuel restent distincts sans conversion.
- Les projets BMO, les offres et les emplois occupés restent des objets différents. Aucune probabilité d’embauche, score de territoire, moyenne de médianes ou corrélation n’est ajoutée.
- Mobilités et compétences communes décrivent des observations et relations entre métiers ; elles ne prouvent ni les acquis personnels ni la réussite d’une reconversion.
- Les perspectives 2030 conservent leur horizon et leurs composantes publiées ; aucun récit de croissance annuelle ni garantie individuelle n’est généré.
- Les 29 mesures restent accessibles par leur usage et leur notice. La présence d’une notice ne fait pas croire qu’une valeur est publiée pour chaque métier ou territoire.
- La catégorie de tension reçue est conservée ; une explication conditionnelle accompagne la catégorie concernée, sans la transformer en score ou en promesse.
- La charte éditoriale disponible reste une proposition sur les formulations non explicitement décidées ; la validation de compréhension auprès de personnes réelles n’est pas déduite des tests navigateur.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

Aucun GET supplémentaire. Réutiliser les libellés et valeurs des réponses de chaque US ainsi que /mesures pour les définitions et métadonnées. Dans /indicateurs, la provenance inclut notamment items[].mesure, libelle, grain, maille_demandee, maille_reelle, territoire_libelle, repli, source_libelle et millesime. Lire les métadonnées propres aux autres routes sans leur inventer cette enveloppe. Les explications sont fondées sur le contrat et les notices ; elles n’ajoutent aucun calcul ni source de données.

**Preuves et références :** [AGENTS.md](../../../AGENTS.md); [07_parcours/Explorer/02_SPECIFICATIONS_API.md](../02_SPECIFICATIONS_API.md); [07_parcours/Explorer/12_maquette_html/documentation/REDACTION_CITOYENNE.md](../12_maquette_html/documentation/REDACTION_CITOYENNE.md); [07_parcours/Explorer/12_maquette_html/preuves/PREUVES_LIBELLES.json](../12_maquette_html/preuves/PREUVES_LIBELLES.json); [07_parcours/Explorer/TESTS_UX_EXPLORER.md](../TESTS_UX_EXPLORER.md); [07_parcours/Explorer/11_INTEGRATION_DSFR_CHART.md](../11_INTEGRATION_DSFR_CHART.md); [07_parcours/Explorer/11_ux_ui/MATRICE_VISUALISATIONS.csv](../11_ux_ui/MATRICE_VISUALISATIONS.csv).

**Tests restant nécessaires :**

- Faire relire les explications conditionnelles, notamment la tension extrême, par Métier/Data avant diffusion.
- Vérifier la compréhension avec des salariés de profils, niveaux de lecture et familiarités numériques variés ; aucun entretien réel n’est revendiqué à ce stade.
- Tester des libellés absents ou longs et des cas de tranche ouverte sans afficher de code comme seul nom public.
- Vérifier les 29 notices et les textes d’absence après branchement de nouvelles réponses, notamment cohortes, replis et secrets.
- Faire clore Q06/Q07 sur les règles de secret et les nombres/taux BMO sans réécrire les valeurs côté interface.

## 8. Critères d’acceptation

**US-FON-034-CA-01** — **Étant donné** un objet disposant d’un nom dans la réponse, **Quand** la personne le retrouve dans un résultat ou un filtre, **Alors** son nom est affiché et aucun code de référentiel n’est nécessaire pour le reconnaître ou le choisir.

**US-FON-034-CA-02** — **Étant donné** un salaire au grain familial, **Quand** la personne lit le montant, **Alors** elle trouve à proximité le sens de la médiane, l’unité, la population, le groupe, le lieu, l’année et la source.

**US-FON-034-CA-03** — **Étant donné** une valeur sous secret statistique, **Quand** la personne consulte l’indicateur, **Alors** le message explique la confidentialité et aucune valeur numérique de remplacement ou déduction par différence n’apparaît.

**US-FON-034-CA-04** — **Étant donné** une mesure disponible seulement sur une zone plus large, **Quand** la personne consulte les résultats de son lieu, **Alors** le lieu effectivement mesuré et le repli sont expliqués sans attribuer le chiffre à la zone demandée.

**US-FON-034-CA-05** — **Étant donné** des résultats après formation concernant apprentis et demandeurs d’emploi, **Quand** la personne consulte les deux repères, **Alors** les populations, bases et horizons propres restent lisibles et ne sont pas présentés comme équivalents.

**US-FON-034-CA-06** — **Étant donné** une notice connue mais une valeur absente pour la sélection, **Quand** la personne ouvre Sources puis revient à l’indicateur, **Alors** la définition reste accessible et l’absence de valeur ne devient ni zéro ni impossibilité d’exercer le métier.

**US-FON-034-CA-07** — **Étant donné** une fiche complète et ses panneaux repliés, **Quand** la personne parcourt les contenus citoyens, **Alors** les sources et limites utiles restent présentes tandis que versions du projet, noms de champs et détails de test ne sont pas affichés.

**US-FON-034-CA-08** — **Étant donné** deux métiers comparés ou une mobilité observée, **Quand** la personne lit les résultats, **Alors** aucun score personnel, taux de réussite individuel ou lien métier fondé uniquement sur un libellé de famille n’est ajouté.

**US-FON-034-CA-09** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-034-CA-10** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

## 9. Composants UX/UI

- Questions en langage courant, paragraphes courts, titres par besoin et présentation progressive sans suppression des rubriques.
- DataBox ou carte de chiffre clé lorsque le nombre suffit ; graphique officiel seulement si la comparaison apporte une information utile.
- Texte d’aide à proximité des notions statistiques ; détails et notices consultables sans survol obligatoire.
- Sources nommées, dates, unités, populations et territoire effectif visibles ou directement accessibles ; 29 notices sans noms de champs internes.
- États textuels distincts pour donnée inconnue, non publiée pour confidentialité, zéro observé, liste sans résultat et zone plus large.
- Listes, accordéons et tableaux pour compétences, voies d’accès et sessions ; aucune visualisation décorative ou personnalisation fictive.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

## 10. Maquette fonctionnelle

![US-FON-034 — scénario, interactions et alternatives](svg/US-FON-034.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-034.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
