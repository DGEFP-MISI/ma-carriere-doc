# Explorer — améliorations UX et recette navigateur

2 novembre 2026. Le véritable [Explorer](12_maquette_html/index.html) a été modifié sur place. Aucun nouveau produit, aucune nouvelle page d’accueil et aucun algorithme de recommandation n’ont été créés. Les 31 fonctionnalités E01–E31, les écrans existants et DSFR Chart sont conservés.

## Résultat de la recette

| Contrôle | Avant | Après | Portée |
|---|---|---|---|
| Contrôles existants, ordinateur | 179 réussis / 0 échec | 179 réussis / 0 échec | Navigation, données, tableaux, graphiques réellement rendus, interactions ; largeur 1410 px |
| Contrôles existants, mobile | 179 réussis / 0 échec | 179 réussis / 0 échec | Même socle à 320 px |
| Nouvelle matrice, 1280 px | 61 assertions réussies / 8 échouées | 69 réussies / 0 échec | Les dix missions et les contrôles transversaux, avec le même pilote final |
| Nouvelle matrice, 375 px | 59 assertions réussies / 8 échouées | 67 réussies / 0 échec | Même matrice sur petit écran |
| Erreurs JavaScript, matrice finale | Aucune observée | Aucune observée | Exceptions remontées par le navigateur |
| Contrôles API du dossier | Référence existante | 6 exécutés avec succès | Hors ligne, pas une campagne HTTP |
| Intégrité | État sauvegardé avant modification | 155 références protégées intactes ; 31 IDs conservés | Contrat, OpenAPI, JSON, UML et référentiel commun de visualisation |

**Trois points restent NON TESTÉS dans chacun des deux formats : rechargement natif Ctrl+R/F5 après navigation par fragments, vrai zoom navigateur 200/400 %, audit RGAA complet/lecteurs d’écran.** La session est reprise après de nouveaux chargements complets effectivement vérifiés ; ce contrôle est distinct du rechargement natif que le pilote n’a pas confirmé.

Rapports : [matrice avant](12_maquette_html/controles/resultats/TESTS_UX_CDP_AVANT.json), [matrice après](12_maquette_html/controles/resultats/TESTS_UX_CDP_APRES.json), [contrôles ordinateur](12_maquette_html/controles/resultats/CONTROLE_DESKTOP.json), [contrôles mobile](12_maquette_html/controles/resultats/CONTROLE_MOBILE.json). Les assertions comptent des vérifications techniques ; elles ne constituent pas un score UX.

## État de référence et documents lus

L’entrée active est `12_maquette_html/index.html`, construite par `sources/construire.py`. Les recherches et fiches sont rendues par `interface_citoyenne.js`, `experience_exploration.js` et le fournisseur local `donnees_exploration.js`. Les exports de travail ne sont pas fusionnés avec cette entrée.

Avant modification, les parcours déjà opérationnels ont été identifiés : recherche Métier/Diplôme/Domaine, fiches identifiées et sous-pages métier, exploration par savoir-faire/contextes, comparaison de deux métiers, mobilités, territoire, Mes pistes, export/reprise de sélection, liens profonds et états de recherche. La [sauvegarde initiale](99_archives/2026-11-02_ameliorations_ux/ETAT_AVANT.zip) et son [inventaire](99_archives/2026-11-02_ameliorations_ux/INVENTAIRE_AVANT.json) ont été réalisés avant les changements ; la recette existante réussissait déjà ses 179 contrôles par format.

Références retrouvées et lues dans Downloads : `MaCarriere_Explorer_Conception_UX_V2.md`, `MaCarriere_Charte_Editoriale_Langage_Positif_V1.md`, `MaCarriere_Prompt_Codex_Langage_Clair_Explorer.md`. La rédaction citoyenne locale, les documents Explorer et les preuves R23/R24 ont également été consultés. Le rapport `MaCarriere_Rapport_Tests_UX_10_Personas_Explorer_20261102.md` et `Markdown collé(2).md` n’ont pas été retrouvés dans le workspace ou parmi les fichiers de Downloads ; aucune règle ni résultat n’en est supposé.

La charte fournie porte encore le statut de proposition : elle guide les changements sûrs, sans prétendre à une validation métier définitive. Les anciennes propositions de priorisation n’annulent pas la décision de conserver E01–E31. Le brief actuel autorise les améliorations de navigation et la règle explicite de remise à zéro du champ au changement de mode.

## Changements appliqués

| Avant | Après | Emplacement | Vérification |
|---|---|---|---|
| Changement de mode gardant une saisie parfois ambiguë et le libellé de l’ancienne recherche | Saisie, résultats et erreur remis à zéro ; mode annoncé ; consigne visible ; action nommée selon l’objet ; focus rendu au champ. Territoire, comparaison et pistes conservés | `persistentSearch`, gestion du mode, `pageTitle` | Mission 007 et clavier |
| Ajout confirmé essentiellement par un message temporaire ; bouton « Garder » inchangé | État durable « Piste gardée », retrait depuis la fiche/résultats, lien vers Mes pistes ; mise à jour locale avec maintien du focus | `pisteControl`, `updatePisteControls`, `addPiste` | Mission 005, limite/retrait et session |
| Retours aux fiches disponibles dans certains onglets seulement | Identités A/B, sélecteurs A/B, inversion et liens vers les deux fiches dans tous les onglets ; retour vers la fiche consultée | `experienceComparator`, gestion `compareOrigin` | Missions 002/009 et historique |
| Deux savoir-faire précochés ; libellés codés à la main ; chips périmées après une modification | Aucun choix par défaut ; libellés natifs ; compteur et chips synchronisés ; choix/retrait explicites ; erreur associée en l’absence de critères | `experienceGuide`, `updateGuideSelection`, `submitGuide` | Mission 001, clavier et cibles mesurées |
| Cas couvert reconnu uniquement par le nombre de compétences | Reconnaissance du jeu exact de critères ; une compétence exploite ses `rome_codes[]` observés ; deux compétences exploitent les réponses multicritères observées | `guideMatches`, payload `competencesRecherche` | Recette existante R23 et mission 001 ; preuve de fidélité |
| Une combinaison non couverte pouvait ressembler à une absence de métier | Message distinct « Cette combinaison n’est pas renseignée ici », choix conservés, possibilité de les modifier | `experienceGuideResults` | Contrôle de la combinaison non disponible |
| Filtres de mobilité fonctionnels mais contexte à relire dans plusieurs endroits | Intitulé « Mobilités observées », population, groupe, âge, période, sens et provenance conservés à proximité des filtres ; exploration des métiers proches séparée des flux | `mobilites` | Mission 010, changements des trois filtres et focus |
| Catégorie « Tension extrême » pouvant nécessiter une explication | Phrase explicative uniquement lorsque la catégorie est effectivement reçue ; valeur source et contexte conservés | `recrutements` | Catégorie et valeurs originales toujours contrôlées |
| Cartes et actions peu différenciées ; boutons de retrait des chips de 32 × 40,4 px | Hiérarchie typographique, espacements et ombres discrets ; survol/focus/sélection/désactivation distincts ; boutons de chips de 44 × 44 px | `ameliorations_ux.css` | Captures, reflow, clavier, tailles réelles |
| Sans JavaScript : instruction générale mais contenu principal vide | Aperçu lisible issu de la description métier native, source et limites ; navigation interactive non promise | Gabarit et constructeur | DOM, dimensions et captures avec JavaScript désactivé |

La saisie reste conservée lorsqu’on navigue entre fiches dans le même mode. Au changement d’objet recherché, l’effacement est annoncé avant la nouvelle recherche. Aucun ancien résultat n’est présenté comme résultat du nouveau mode.

## Les dix missions exécutées

Les identifiants 001–010 reprennent les missions du brief. **Il s’agit de tests navigateur sur le jeu couvreur/étancheur disponible, pas d’entretiens avec dix personnes réelles.**

| ID | Mission et assertion principale | 1280 px | 375 px |
|---|---|---|---|
| 001 | Entrée sans métier cible, choix explicite de savoir-faire, compteur et résultats | Réussi | Réussi |
| 002 | Recherche couvreur, comparaison avec l’étanchéité, sélection/inversion et retour sans perte des deux choix | Réussi | Réussi |
| 003 | Description/conditions identifiables, limites et données conservées | Réussi | Réussi |
| 004 | Métier proche, fiche liée, retour arrière puis navigation avant | Réussi | Réussi |
| 005 | Salaire : unité, population territoriale, année et source ; piste gardée puis retrouvée | Réussi | Réussi |
| 006 | Recrutements actuels distingués des projections 2019–2030 | Réussi | Réussi |
| 007 | Métier → Domaine : remise à zéro annoncée, focus utile, nouvelle recherche et sélection du domaine | Réussi | Réussi |
| 008 | Modification du territoire, choix visible, absence de transposition des chiffres et retour au périmètre renseigné | Réussi | Réussi |
| 009 | Deux métiers, savoir-faire communs sans maîtrise individuelle inventée, absence explicite | Réussi | Réussi |
| 010 | Mobilités : avant/après, âge et famille réellement appliqués ; population, période, source et focus conservés | Réussi | Réussi |

## Contrôles transversaux et limites

- Recherche sans résultat, chargement et erreur : testés. La latence et la faute sont injectées uniquement dans le fournisseur local, puis retirées ; cela ne valide pas un service HTTP.
- `null` réellement présent dans la certification : conservé et non remplacé par zéro. Les contrôles existants vérifient également zéro, secret statistique, valeurs négatives et alternatives de DSFR Chart.
- Quatrième piste : refusée avec explication ; retrait opérationnel ; trois puis deux pistes reprises après nouveaux chargements complets. Le nouveau document est confirmé, sans assimiler ce contrôle au Ctrl+R/F5 non confirmé.
- Clavier : lien d’évitement, changement de mode par flèche, recherche avec Entrée, focus visible ; parcours du guide avec Tab, Espace et Entrée sans souris. Ce contrôle ne remplace pas un audit de tous les composants ni une recette lecteur d’écran.
- Aucune page de la série contrôlée ne déborde à 375/1280 px ; reflow du comparateur testé à 640/320 px. Grossissement visuel CDP appliqué à 200/400 %, distinct du zoom navigateur resté NON TESTÉ.
- Mouvement réduit : préférence émulée, contenu toujours visible, styles sans animation/transition ; aucune animation de défilement n’est requise pour lire les panneaux.
- Contrastes : six mesures de texte sur les composants touchés par format, ratio minimal **5,34:1** ; boutons du guide mesurés, dont retraits de chips à **44 × 44 px**. Cet échantillon ne couvre pas tous les états/composants. Le contrôle de contraste s’appuie sur le [critère 3.2 du RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) et son [glossaire](https://accessibilite.numerique.gouv.fr/methode/glossaire/).
- Sans JavaScript : aperçu réellement présent, visible et capturé. Les fonctions interactives restent annoncées comme nécessitant JavaScript.
- Liens `href="#"` : aucun détecté. Le format de sélection prépare la reprise des pistes ; aucune navigation vers un parcours absent n’est simulée.

Le pilote initial a été corrigé avant la comparaison finale : choix d’éléments visibles sur mobile, envoi complet d’Entrée, attente des chargements et séparation des tests avec/sans JavaScript. Les premiers résultats non fiables ne sont pas attribués à l’application ; ils sont conservés dans les diagnostics de l’archive. Les rapports finaux avant/après utilisent le même pilote.

## Fidélité des données et points métier/Data

[La preuve de fidélité](12_maquette_html/controles/resultats/FIDELITE_DONNEES_UX.json) compare les données embarquées avant/après : **21 champs principaux antérieurs, aucun modifié**. La seule clé ajoutée, `competencesRecherche`, contient exactement les deux réponses natives `/competences` de R23, sans en modifier le contenu. Les sources JSON, le contrat, les Swagger et les UML restent intacts ; [preuve d’intégrité](12_maquette_html/controles/resultats/INTEGRITE_DSFR_CHART.json).

Les associations unitaires viennent de `rome_codes[]` reçus ; les listes multicritères reprennent les réponses R23 existantes. Un lien observé avec un métier ne mesure ni la maîtrise ni l’employabilité. Aucun vrai zéro serveur en recherche par savoir-faire n’est présent dans ces preuves : ce cas n’est pas déclaré validé.

Les flux de mobilité sont au grain FAP225, nationaux, 2022–2023, avec les sens et âges des réponses présentes. Ils n’exposent pas de code métier de destination permettant de fabriquer un lien vers une fiche. Les métiers proches utilisent leur relation native et restent présentés séparément. Le paramètre API d’âge est `age` ; `tranche_age_libelle` est le libellé reçu. L’ancienne mention `tranche_age` dans le rapport d’intégration 11 a été corrigée.

La validation des formulations publiques reste à faire avec Métier/Data avant diffusion. Les données complémentaires, le branchement HTTP, les questions RCO existantes et les tests non couverts sont suivis dans le [petit backlog](BACKLOG_EXPLORER_RESTANT.md).

## Fichiers modifiés ou ajoutés

| Fichier | Rôle du changement |
|---|---|
| `12_maquette_html/sources/interface_citoyenne.js` | Actions des fiches, état des pistes, guide, mobilité, présentation conditionnelle, rendu/focus |
| `12_maquette_html/sources/experience_exploration.js` | Modes de recherche, titres, comparateur A/B, source de retour, session et messages associés aux champs |
| `12_maquette_html/sources/ameliorations_ux.js` | Compositions ciblées des pistes et savoir-faire ; résolution des critères documentés |
| `12_maquette_html/sources/ameliorations_ux.css` | Polissage visuel, états, cibles, responsive et mouvement réduit |
| `12_maquette_html/sources/modele.html` | Contenu principal accessible sans JavaScript, point de focus principal |
| `12_maquette_html/sources/construire.py` | Lecture des deux réponses natives supplémentaires, assemblage et aperçu sans JavaScript |
| `12_maquette_html/controles/scripts/tester_ux_cdp.mjs`, `lancer_tests_ux.ps1` | Matrice réelle de missions, clavier, historique, états, session, captures et limites explicites |
| `12_maquette_html/controles/scripts/verifier_navigateur.js`, `verifier_exploration.js` | Assertions adaptées au choix explicite et aux boutons gardés/retirés ; fonctionnalités contrôlées conservées |
| `12_maquette_html/index.html`, documents de contrôle, manifestes et rapports | Artefacts reconstruits à partir des sources actives |
| `12_maquette_html/apercus/`, `99_archives/2026-11-02_ameliorations_ux/` | Captures après, sauvegarde et captures avant |
| `README.md`, `12_maquette_html/README.md`, `11_INTEGRATION_DSFR_CHART.md` | Documentation du nouvel état et correction du nom du paramètre d’âge |

## Captures et reproduction

| Écran | Avant 1280 px | Après 1280 px | Avant 375 px | Après 375 px |
|---|---|---|---|---|
| Fiche métier | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-1280-essentiel.png) | [Après](12_maquette_html/apercus/ux-apres-1280-essentiel.png) | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-375-essentiel.png) | [Après](12_maquette_html/apercus/ux-apres-375-essentiel.png) |
| Savoir-faire | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-1280-guide.png) | [Après](12_maquette_html/apercus/ux-apres-1280-guide.png) | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-375-guide.png) | [Après](12_maquette_html/apercus/ux-apres-375-guide.png) |
| Comparateur | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-1280-comparateur.png) | [Après](12_maquette_html/apercus/ux-apres-1280-comparateur.png) | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-375-comparateur.png) | [Après](12_maquette_html/apercus/ux-apres-375-comparateur.png) |
| Mobilités | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-1280-mobilites.png) | [Après](12_maquette_html/apercus/ux-apres-1280-mobilites.png) | [Avant](99_archives/2026-11-02_ameliorations_ux/captures/ux-avant-375-mobilites.png) | [Après](12_maquette_html/apercus/ux-apres-375-mobilites.png) |

Depuis la racine du workspace :

```powershell
& ./07_parcours/Explorer/12_maquette_html/controles/scripts/lancer_controles.ps1
& ./07_parcours/Explorer/12_maquette_html/controles/scripts/lancer_tests_ux.ps1 -Phase apres
```

Le lanceur utilise Edge sans fenêtre et le Node déjà installé localement. Les clics et touches passent par CDP ; les sélecteurs sont pilotés par leur événement DOM de changement. Aucun accès réseau métier ni dépendance de test supplémentaire n’est ajouté. `-Phase avant` rejoue les nouveaux critères sur la sauvegarde initiale et retourne donc les écarts attendus.
