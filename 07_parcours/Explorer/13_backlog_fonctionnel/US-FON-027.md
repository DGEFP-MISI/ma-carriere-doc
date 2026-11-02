# US-FON-027 — Conserver et reprendre jusqu'à trois pistes de métiers

**Rattachement :** E27 · alias historique US-E27. **Lot :** L9.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-005](US-FON-005.md) (E05).

**État constaté au 2 novembre 2026 :** Fonction locale et préparation de reprise déjà présentes dans la maquette, avec plafond de trois validé. Le code actuel remplace la sélection, les deux métiers de comparaison et le territoire après validation du format HTML ou JSON ; son explication avant reprise est un critère UX à vérifier. La session et le format portable se testent dans le navigateur ; cela ne démontre aucun stockage serveur ou transfert réel entre parcours. Les modalités de production D08/D10 restent ouvertes sans retirer export/import de la cible.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de conserver et reprendre jusqu'à trois pistes de métiers, pour garder temporairement les métiers qui m'intéressent, les retrouver pendant mon exploration et préparer une reprise sans compte ni sauvegarde distante inventée. Je veux conserver temporairement des métiers pour poursuivre mon exploration.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite conserver et reprendre jusqu'à trois pistes de métiers, afin de garder temporairement les métiers qui m'intéressent, les retrouver pendant mon exploration et préparer une reprise sans compte ni sauvegarde distante inventée.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Le navigateur peut conserver l’état dans la session ; le refus de stockage doit laisser l’exploration et l’export utilisables.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Depuis un résultat, une fiche ou une relation métier, choisit garder cette piste. | Ajoute le métier ROME V3 effectivement sélectionné à l'état local s'il n'y est pas déjà, actualise le compteur et annonce l'ajout sans déplacer le focus. |
| 2 | Ajoute d'autres pistes puis ouvre Mes pistes. | Présente jusqu'à trois métiers distincts avec leurs noms, les actions ouvrir, retirer et choisir deux métiers à comparer ; explique la conservation temporaire. |
| 3 | Retire une piste depuis sa fiche ou Mes pistes. | Met à jour partout le même état local, le compteur et l'état des boutons ; garde les autres pistes et annonce le retrait. |
| 4 | Navigue, recharge l'onglet puis revient à Mes pistes. | Restaure la sélection de la session d'onglet lorsque le stockage de session est disponible, sans appel d'écriture API ; explique la limite de conservation. |
| 5 | Choisit exporter sa sélection pour la reprendre. | Produit le format portable prévu pour les identifiants et données locales nécessaires, avec une version de format client explicite, sans le présenter comme une réponse API ou un dossier de projet créé. |
| 6 | Importe une sélection sauvegardée. | Explique que la reprise remplace la sélection locale, valide le format, les types, les identifiants métier, les deux métiers de comparaison, le territoire, l'unicité et la limite de trois avant toute modification ; reprend ensuite le contexte validé. |
| 7 | Choisit deux pistes à comparer ou souhaite poursuivre son projet. | Ouvre le comparateur avec ces deux métiers ; garde la sélection portable pour les futurs parcours sans créer de faux lien ni simuler un transfert vers un produit encore absent. |

## 5. Scénarios alternatifs

- Quatrième métier : expliquer la limite de trois et proposer un retrait explicite ; aucune piste existante n'est remplacée silencieusement.
- Métier déjà retenu : conserver une seule occurrence et proposer l'action de retrait avec un état cohérent sur tous les écrans.
- Stockage de session indisponible : conserver l'état en mémoire pour la page courante, expliquer la limite et laisser la reprise portable si elle est disponible.
- Import illisible, format inconnu, identifiants invalides, doublons ou plus de trois pistes : décrire l'erreur sans écraser la sélection présente ni lancer des appels issus d'identifiants invalides.
- Les autres parcours ne sont pas disponibles : garder la préparation de reprise sans lien mort, faux bouton de projet créé ou confirmation de transfert non réalisé.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Trois pistes au maximum et unicité par ROME V3 ; seuls les métiers explicitement choisis sont retenus, sans présélection, ajout implicite ou classement de préférence calculé.
- La sélection est un état local client ; aucun GET d'écriture, compte utilisateur ou sauvegarde distante n'est inventé dans les 21 GET. Un ajout ne requiert pas de relire une fiche déjà connue.
- La préparation actuelle utilise une session d'onglet et le format client type=macarriere-selection, version=1, referentiel=ROME_V3, metiers[], comparaison[] et territoire ; les fichiers HTML de reprise intègrent ces données JSON, distinctes du contrat fournisseur. Durée, politique de stockage et raccordement en production restent documentés sans rouvrir le plafond validé.
- L'export/import porte un format de sélection client contrôlé, distinct des données fournisseurs ; il ne prouve ni fraîcheur des fiches, ni partage interapplications, ni création d'un projet dans un parcours absent.
- Le retrait est répercuté dans fiches, listes et Mes pistes ; le comparateur ne garde pas une identité silencieusement incohérente si une sélection change, et les décisions explicites de comparaison sont préservées ou redemandées.

**Règles héritées conservées :** Sélection de codes, pas mesure/statistique ; aucune sauvegarde serveur dans les21GET.

**Traitements :** État local des `rome_code` ; réemploi `/metiers/{rome}` ; Sélection de codes, pas mesure/statistique ; aucune sauvegarde serveur dans les21GET.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Sélection de codes, pas mesure/statistique ; aucune sauvegarde serveur dans les21GET.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3 ; grain ROME V3 ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

L’ajout, le retrait, l’export et la reprise de pistes sont locaux. Aucun GET de sauvegarde et aucun endpoint d’écriture n’existent dans le contrat. Le détail ci-dessous sert uniquement à retrouver une fiche si elle n’est plus en cache.

### Appel 1 — GET `/metiers/{rome}`

**Déclenchement :** Aucun appel à l'ajout/retrait ; détail seulement si cache absent au réaffichage. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `rome` | path | Requis Swagger | `string` | chemin code ROME V3 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.grand_domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.grand_domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.appellations` | array | Type OpenAPI officiel ; chemin observé |
| `$.definitions` | array | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_numerique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_transition_demographique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_emploi_reglemente` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.tag_emploi_cadre` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.metiers_proches_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.metiers_proches_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.savoir_etre_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.contexte_travail_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.contexte_travail_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.fap228_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.formacode_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.formacode_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/metiers/response_metiers-rome.json](../../../02_reponses_observees/metiers/response_metiers-rome.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/metiers/response_metiers-rome.json](../../../02_reponses_observees/metiers/response_metiers-rome.json).

**Contrôle local déjà rapporté :** État gardé, quatrième refusée, retrait, export/reprise et nouveaux chargements complets ; Ctrl+R/F5 natif NON TESTÉ. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E27 : Unicité, plafond, navigation/rechargement selon D08 ; aucun GET requis à chaque ajout.

**Points RCO associés :** Aucun blocage RCO ; aucune sauvegarde serveur parmi les 21 GET ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-027-CA-01** — **Étant donné** aucune piste n'est enregistrée, **Quand** la personne garde le métier ouvert, **Alors** ce métier apparaît une seule fois dans Mes pistes avec compteur et bouton actualisés, sans ajout d'un exemple imposé.

**US-FON-027-CA-02** — **Étant donné** trois métiers distincts sont retenus, **Quand** un quatrième est demandé, **Alors** la limite est expliquée et aucun des trois n'est remplacé avant un retrait explicite.

**US-FON-027-CA-03** — **Étant donné** un métier est déjà retenu et visible dans plusieurs vues, **Quand** il est retiré depuis l'une d'elles, **Alors** son état est retiré partout, le compteur est actualisé et les autres pistes sont conservées.

**US-FON-027-CA-04** — **Étant donné** la session d'onglet accepte le stockage et contient des pistes, **Quand** la personne navigue puis recharge l'onglet, **Alors** la sélection est reprise pour cette session sans sauvegarde API prétendue.

**US-FON-027-CA-05** — **Étant donné** la personne exporte sa sélection, **Quand** le format portable est produit, **Alors** il contient une sélection client identifiable et aucun message n'affirme qu'un projet distant ou un transfert vers un autre parcours a été créé.

**US-FON-027-CA-06** — **Étant donné** une sélection exportée conforme comporte jusqu'à trois ROME V3 distincts et un contexte de comparaison et de lieu valide, **Quand** elle est importée, **Alors** le format est validé avant mutation puis remplace la sélection locale selon la règle annoncée, reprend les deux métiers de comparaison et le territoire, sans dépasser trois pistes.

**US-FON-027-CA-07** — **Étant donné** un import est invalide ou dépasse le plafond, **Quand** la validation échoue, **Alors** les pistes présentes restent intactes et une erreur utile est annoncée sans code interprété arbitrairement.

**US-FON-027-CA-08** — **Étant donné** les deux autres parcours ne sont pas encore fournis, **Quand** la personne souhaite préparer la suite, **Alors** la sélection reste consultable et portable sans lien mort ni confirmation d'un raccordement inexistant.

**US-FON-027-CA-09** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-027-CA-10** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Ajout/retrait; pas de collecte serveur; plafond de trois fixé par le brief UX ; modalités de stockage de production à préciser ; Ajouter/retirer, conserver jusqu'à trois pistes proposé, comparer deux ; durée affichée selon décision de stockage ; Unicité, plafond, navigation/rechargement selon D08 ; aucun GET requis à chaque ajout ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E27` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : boutons garder/retirer avec nom du métier, compteur, liste de trois cartes maximum, sélection de deux métiers, actions de reprise et messages de limite ; états vide, partiel, plein, doublon, import invalide et stockage indisponible.
- Annoncer ajout, retrait et erreur sans déplacer le focus ; les boutons gardent une cible tactile suffisante, état perceptible autrement que par couleur et nom accessible stable ; le rechargement ou import ne déclenche pas une navigation surprise.
- Export/import et message de durée sont compréhensibles sans jargon technique ; l'interface explique le remplacement par la sélection reprise avant de modifier une sélection existante et n'invente pas d'écran de futur parcours.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Mes pistes temporaires ; Ajouter/retirer, conserver jusqu'à trois pistes proposé, comparer deux ; durée affichée selon décision de stockage ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Session d’onglet et format portable de reprise préparés ; raccordement aux autres parcours reporté à leur disponibilité selon instruction utilisateur, sans supprimer la fonction ; D08/D10 production restent ouverts.

**SEO / validation conservés :** Proposition à valider D10 : Ne pas indexer liste personnelle. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-027 — scénario, interactions et alternatives](svg/US-FON-027.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-027.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
