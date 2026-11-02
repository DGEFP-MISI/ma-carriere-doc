# US-FON-002 — Rechercher un diplôme ou un titre

**Rattachement :** E02 · alias historique US-E02. **Lot :** L2.

**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.

**Dépendances et passerelles :** aucune.

**État constaté au 2 novembre 2026 :** Recherche et fiches locales testées sur les titres disponibles ; cas RS/inactifs et recherche HTTP à compléter.

[Retour au backlog](../04_BACKLOG_USER_STORIES.md) · [Modèle commun](../../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md)

## 1. Objectif fonctionnel

Permettre à la personne de rechercher un diplôme ou un titre, pour choisir la certification qui correspond à mon point de départ. Je veux retrouver une certification et identifier son type.

## 2. User Story

En tant que personne qui explore ses possibilités professionnelles, je souhaite rechercher un diplôme ou un titre, afin de choisir la certification qui correspond à mon point de départ.

## 3. Préconditions

- Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.
- Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.
- Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.

## 4. Scénario nominal

| Étape | Action utilisateur | Comportement attendu du système |
|---|---|---|
| 1 | Choisit Diplôme ou titre | Annonce le mode et la remise à zéro de la saisie précédente. |
| 2 | Saisit au moins deux caractères et recherche | Demande /certifications avec q et page. |
| 3 | Compare les résultats | Distingue noms, types et niveaux reçus sans équivalence inférée. |
| 4 | Sélectionne une certification | Ouvre le détail avec certifinfo_code, et non fiche_code. |
| 5 | Choisit Je possède ce titre ou Je souhaite l’obtenir | Garde l’objet sélectionné et organise la lecture selon cette intention. |

## 5. Scénarios alternatifs

- Titre ancien ou inactif introuvable : ne pas promettre archive ni équivalence.
- Certification RS : conserver son type et ne pas inventer de blocs RNCP.
- Erreur : garder le contexte et une nouvelle action de recherche.

**États et erreurs complémentaires à couvrir :** Chargement/erreur partielle, 400/401/404/422/429/503/5xx/réseau ; annuler réponse périmée ; null, 0, secret_stat, clé absente et liste vide distincts ; reprise bornée, aucune donnée de remplacement. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.

## 6. Règles de gestion

- Intitulé, type et niveau reçus guident le citoyen ; les codes de jointure restent internes.
- Certif Info, fiche RNCP/RS et métier sont des identifiants différents.
- Absence d’un diplôme dans une réponse ne signifie pas inexistence.

**Règles héritées conservées :** Certification active RNCP/RS ; type et niveau ne sont pas un score ; pas d'archive exposée.

**Traitements :** `/certifications?q=...&page=...` → `certifinfo_code` ; Certification active RNCP/RS ; type et niveau ne sont pas un score ; pas d'archive exposée.

**Règles statistiques :** Afficher source, période/millésime, définition/unité, grain et géographie effective ; aucun score/delta/agrégat inventé, aucune inférence personnelle ; secret_stat non calculable. Certification active RNCP/RS ; type et niveau ne sont pas un score ; pas d'archive exposée.

**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.

Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.

## 7. Données et API

**Source et portée de conception :** Certif Info ; grain certification ; période dates variables. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.

### Appel 1 — GET `/certifications`

**Déclenchement :** À la sélection ou ouverture de la section. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.

| Paramètre exact | Emplacement | Obligation du contrat | Type / domaine Swagger | Usage pour cette US |
|---|---|---|---|---|
| `q` | query | Facultatif Swagger | `string ; défaut API null ; minLength=2 ; maxLength=100` | 2–100 caractères |
| `page` | query | Facultatif Swagger | `integer ; défaut API 1 ; minimum=0` | >=1 |

| Chemin JSON exact | Type connu | Niveau de preuve du chemin/type |
|---|---|---|
| `$.items[].certifinfo_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].certifinfo_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].repertoire_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].fiche_code` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].type_certification_libelle` | string ou null | Type OpenAPI officiel ; chemin observé |
| `$.items[].niveau_certification_code` | string ou null | Type OpenAPI officiel ; chemin observé |

**Réponses natives utilisées pour vérifier les chemins :** [02_reponses_observees/certifications/response_certifications.json](../../../02_reponses_observees/certifications/response_certifications.json).

### Preuves et contrôles restant à produire

**Documenté :** [contrat](../../../01_sources/contrat_interface_2026-10-19.md) ; [OpenAPI officiel](../../../01_sources/openapi/docs_json_interface.json). Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.

**Références conservées de la conception :** [02_reponses_observees/certifications/response_certifications.json](../../../02_reponses_observees/certifications/response_certifications.json).

**Contrôle local déjà rapporté :** Recette existante : choix de certification, deux intentions et fiches identifiées. [Recette UX existante](../TESTS_UX_EXPLORER.md). Ces résultats sur JSON locaux ne valident pas les appels HTTP.

**Tests à réaliser :** T-E02 : Recherches représentatives dont titre/RS et plusieurs résultats ; distinguer non trouvé et erreur.

**Points RCO associés :** Q02/Q09 : limites de recherche et certifications actives ; tri contractuel/tests/demande fournisseur dans 06 section Q01–Q14. Lire le tri déjà établi dans [Q01–Q14](../06_DECISIONS_ET_POINTS_A_VALIDER.md) avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.

## 8. Critères d’acceptation

**US-FON-002-CA-01** — **Étant donné** des titres voisins, **Quand** je lis les résultats, **Alors** chaque carte garde son type et son identité.

**US-FON-002-CA-02** — **Étant donné** un titre sélectionné, **Quand** j’ouvre la fiche, **Alors** le chemin utilise son certifinfo_code reçu.

**US-FON-002-CA-03** — **Étant donné** un diplôme ancien introuvable, **Quand** la recherche aboutit, **Alors** aucune archive ou équivalence non exposée n’est proposée.

**US-FON-002-CA-04** — **Étant donné** un changement de mode, **Quand** je choisis Diplôme ou titre, **Alors** l’ancien résultat disparaît et le champ reçoit le focus.

**US-FON-002-CA-05** — **Étant donné** un intitulé public et son identifiant technique disponibles, **Quand** le contenu est présenté, **Alors** les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne.

**US-FON-002-CA-06** — **Étant donné** une réponse absente, protégée ou en erreur pour un seul volet, **Quand** les autres réponses sont disponibles, **Alors** les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution.

**Trace de conception conservée :** Un certificat sélectionné ouvre /certifications/{certifinfo} ; Résultat avec intitulé, type et niveau reçus ; identifiants techniques internes ; conserver l'intention de consultation en ouvrant la fiche ; Recherches représentatives dont titre/RS et plusieurs résultats ; distinguer non trouvé et erreur ; états d'erreur de la ligne vérifiés, aucune preuve HTTP déduite de fixtures. ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire. ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.

**Recette de rattachement :** `T-E02` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.

## 9. Composants UX/UI

- DSFR : recherche persistante, cartes nom/type/niveau, lien de fiche et choix d’intention.
- Aucun graphique de classement des diplômes ni score d’adéquation.

**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.

**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.

**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.

**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.

**Composants et interaction hérités :** Recherche de certifications ; Résultat avec intitulé, type et niveau reçus ; identifiants techniques internes ; conserver l'intention de consultation en ouvrant la fiche ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles. ; Évolution UX ciblée : Résultats pilotés par la liste de certifications ; la fiche correspond à l’identifiant sélectionné, sans ouvrir un exemple imposé.

**SEO / validation conservés :** Proposition à valider D10 : Titre canonique certification. Ce statut est une proposition de déploiement, pas une décision produit acquise.

## 10. Maquette fonctionnelle

![US-FON-002 — scénario, interactions et alternatives](svg/US-FON-002.svg)

[Ouvrir le schéma SVG accessible](svg/US-FON-002.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.
