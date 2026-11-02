# US-FON-014 — Trouver les métiers liés à plusieurs compétences

**Rattachement :** E14 · alias historique US-E14. **Lot :** L3.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** [US-FON-013](US-FON-013.md) (E13).

**État constaté au 2 novembre 2026 :** Cas R23 et navigation locale testés ; autres combinaisons et pagination HTTP à tester.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de trouver les métiers liés à plusieurs compétences, pour examiner tout ou partie de mes critères. Je veux retrouver les métiers portant tout ou partie des compétences sélectionnées.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite trouver les métiers liés à plusieurs compétences, afin d’examiner tout ou partie de mes critères.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Vérifie ses compétences choisies | Conserve les codes reçus et les contraintes de nombre. |
| 2 | Choisit Toutes ou Au moins une | Explique le mode, sans score de maîtrise. |
| 3 | Lance | Demande /metiers avec competence et mode_competence explicites. |
| 4 | Parcourt les résultats | Montre noms et critères trouvés lorsqu’ils sont fournis ; suit les pages. |
| 5 | Ouvre une fiche ou modifie ses choix | Garde les critères et un retour vers le guide. |

## 5. Scénarios alternatifs

- Jeu local non capturé : indisponibilité, pas faux zéro.
- Vraie réponse vide : modifier les critères sans métier fictif.
- Compteurs absents dans toutes : ne pas les reconstruire ni déclarer abusivement une erreur.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- R23 donne 3 en au_moins_une et 1 en toutes pour ses deux codes seulement.
- Les champs de rapprochement sont conditionnels, notamment selon le mode.
- Reconnaître le jeu exact de codes, pas seulement leur nombre.
- Ne pas transformer des critères trouvés en pourcentage d’adéquation personnelle.

**Règles héritées conservées :** Classement API nb_macro_competences_trouvees puis nb_competences_trouvees ; match conditionnel selon mode, aucun taux personnel calculé.

**Traitements :** `/metiers?competence=...&mode_competence=toutes` ou `au_moins_une` ; Classement API nb_macro_competences_trouvees puis nb_competences_trouvees ; match conditionnel selon mode, aucun taux personnel calculé.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Classement API nb_macro_competences_trouvees puis nb_competences_trouvees ; match conditionnel selon mode, aucun taux personnel calculé.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** ROME V3/OGR ; grain ROME V3 ; période référentiel courant. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/metiers`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `competence` | query | Facultatif Swagger | `string ; défaut API null` | 1–10 codes OGR séparés virgules |
| `mode_competence` | query | Facultatif Swagger | `string ; valeurs toutes, au_moins_une ; défaut API null` | toutes ou au_moins_une |
| `domaine` | query | Facultatif Swagger | `string ; défaut API null` | facultatif |
| `q` | query | Facultatif Swagger | `string ; défaut API null ; minLength=2 ; maxLength=100` | facultatif |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].rome_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].rome_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].grand_domaine_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].grand_domaine_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].appellations` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].definitions` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_ecologique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_numerique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_transition_demographique` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_emploi_reglemente` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].tag_emploi_cadre` | boolean ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].metiers_proches_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].metiers_proches_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].savoir_etre_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].contexte_travail_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].contexte_travail_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].fap228_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_codes` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].formacode_libelles` | array | Type OpenAPI officiel ; chemin observé |
| `$.items[].source_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].nb_macro_competences_trouvees` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].nb_competences_trouvees` | entier | Types observés seulement ; null seul ne prouve pas le type publié |
| `$.items[].competences_trouvees_codes` | tableau | Types observés seulement ; null seul ne prouve pas le type publié |

**Réponses natives utilisées pour vérifier les chemins :** [06_controles/resultats/R23 test/R23 GET metierscompetence=125416&mode_competence=toutes&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416&mode_competence=toutes&page=1.json>); [06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json>); [06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json](<../../../06_controles/resultats/R23 test/R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json>); [06_controles/resultats/R24/R24 GET metiersdomaine=F16&contexte=300782&page=1.json](<../../../06_controles/resultats/R24/R24 GET metiersdomaine=F16&contexte=300782&page=1.json>); [06_controles/resultats/R24/R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json](<../../../06_controles/resultats/R24/R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json>).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [06_controles/VALIDATION_R23_recherche_multicompetences.md](../../../06_controles/VALIDATION_R23_recherche_multicompetences.md).

**Contrôle local déjà rapporté :** Cas R23, trois résultats au moins une et un résultat toutes sur le jeu ciblé. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E14 : Rejouer R23 puis autres codes, 1/10/11 entrées, pagination et champs de match conditionnels.

**Points RCO associés :** Q04 : classement et périmètre des correspondances ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-014-CA-01** — **Étant donné** les deux critères R23 en au_moins_une, **Quand** je lis leur réponse, **Alors** ses trois métiers, et eux seuls, sont proposés.

**US-FON-014-CA-02** — **Étant donné** le même jeu en toutes, **Quand** je lis la réponse, **Alors** son seul métier est proposé.

**US-FON-014-CA-03** — **Étant donné** les compteurs absents en toutes, **Quand** j’affiche les résultats, **Alors** aucun compteur fictif ni zéro par défaut n’est ajouté.

**US-FON-014-CA-04** — **Étant donné** un changement de critère ou mode, **Quand** je relance, **Alors** la réponse correspond aux nouveaux paramètres exacts.

**US-FON-014-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-014-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Test 125416+103659 toutes=1 au_moins_une=3 ; Choisir tous/au moins un ; montrer uniquement les correspondances renvoyées et le classement API par macro-compétences ; Rejouer R23 puis autres codes, 1/10/11 entrées, pagination et champs de match conditionnels ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E14` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : radios, critères actifs, cartes et pagination.
- Choix conservés après vide/erreur ; pas de classement de compatibilité.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Recherche multicompétences ; Choisir tous/au moins un ; montrer uniquement les correspondances renvoyées et le classement API par macro-compétences ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Mode au moins une/toutes conservé avec les autres filtres ; annuler les réponses de recherche périmées.

**SEO / validation conservés :** Proposition à valider D10 : Navigation métier. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-014 — scénario, interactions et alternatives](svg/US-FON-014.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-014.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
