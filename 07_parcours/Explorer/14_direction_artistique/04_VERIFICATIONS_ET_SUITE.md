# Vérifications et suite du chantier visuel

Résultats du 2 novembre 2026. La première intégration est appliquée au HTML existant. Les 31 fonctions restent dans la cible ; les statuts de réalisation et dépendances API ne sont pas changés par la direction artistique.

## Résultats exécutés

| Vérification | Résultat | Preuve |
|---|---|---|
| Construction des composants officiels et partagés | Réussie ; DSFR 1.15.4, DSFR Chart 2.1.1, ressources locales embarquées | `commun_datavisualisation/dist/ASSEMBLAGE.json` |
| Tests des adaptateurs statistiques | 20 réussis, aucun échec | Commande Node `--test --test-isolation=none .../tests/adaptateurs.test.mjs` exécutée ; adaptateurs inchangés |
| Assemblage HTML autonome | Réussi, mêmes 29 notices et mêmes données | `12_maquette_html/controles/resultats/ASSEMBLAGE.json` |
| Contrôles existants ordinateur | 179 réussis, aucun échec, largeur 1410 px | [Rapport ordinateur](../12_maquette_html/controles/resultats/CONTROLE_DESKTOP.json) |
| Contrôles existants mobile | 179 réussis, aucun échec, reflow 320 px | [Rapport mobile](../12_maquette_html/controles/resultats/CONTROLE_MOBILE.json) |
| Dix missions UX sur 1280 et 375 px | 69 et 67 vérifications réussies, aucun échec ; limites NON TESTÉES conservées | [Recette UX](../12_maquette_html/controles/resultats/TESTS_UX_CDP_APRES.json) |
| Recette de la présentation et des SVG | 82 vérifications réussies, aucun échec ni erreur JavaScript ; captures à 1440/375/320 px | [Recette direction artistique](preuves/RECETTE_DIRECTION.json) |
| Intégrité du contrat et des preuves | 155 fichiers de référence intacts ; 35 US, table et backlog inchangés | [Rapport d’intégrité](preuves/INTEGRITE.json) |
| Données et fonctions métier | Payload embarqué strictement identique ; handlers, adaptateurs et code des graphiques existants identiques | Même rapport ; comparaison avec l’archive avant modification |

Le rapport de présentation contient l’empreinte SHA-256 du fichier réellement testé. Les contrôles de présentation ont été relancés après les dernières corrections de couleurs et d’espacement.

## Ce qui a été contrôlé précisément

- Les quatre portes conservent leur ordre, leurs noms et leurs routes. Elles n’imbriquent aucun autre contrôle interactif et sont atteintes par la touche Tab avec un focus visible.
- Les deux familles de recrutement restent séparées, sans somme ; la médiane salariale garde sa famille, ses huit métiers, le temps complet, l’Hérault et 2023. La maille et le repli sont visibles en langage courant.
- Les aperçus ne transposent pas les chiffres à un autre lieu. Le comparateur conserve les deux identités et la colonne statistique non renseignée n’emprunte pas les chiffres de l’autre métier.
- Les icônes officielles sont réellement chargées ; aucun score, jauge ou badge prospectif n’est ajouté. Les nouveaux repères gardent zéro, null, absence et secret distincts.
- Onze vues sont contrôlées sans débordement global à 1440, 375 et 320 px. Les graphiques restent à la demande et conservent les quartiles natifs et leur alternative tabulaire.
- Le thème sombre est exercé via `data-fr-theme`. L’échantillon de contrastes des textes de repère, du lien actif et de l’icône vérifié dans ce thème dépasse 4,5:1 ; cela ne constitue pas un audit exhaustif de tous les états. Les anciennes couleurs fixes du lien actif ont été corrigées.
- Le mouvement réduit est respecté. Aucune ressource métier distante n’est appelée dans cette application locale.
- Les trois SVG ont été rendus dans Edge et leurs captures relues. Les espacements de la variante mobile ont été corrigés après cette relecture. Le SVG de comparaison reprend les quatre rubriques actuelles ; il n’invente pas une nouvelle navigation.

## Captures à consulter

- [Fiche intégrée — ordinateur](preuves/FICHE_DESKTOP.png).
- [Fiche intégrée — mobile 375 px](preuves/FICHE_MOBILE_375.png) et [320 px](preuves/FICHE_MOBILE_320.png).
- [Recherche — ordinateur](preuves/RECHERCHE_DESKTOP.png).
- [Comparateur intégré](preuves/COMPARATEUR_DESKTOP.png).
- [Salaires et tableau/graphique officiels](preuves/SALAIRES_DESKTOP.png).
- [Thème sombre — ordinateur](preuves/FICHE_SOMBRE_DESKTOP.png).

Les captures suffixées `_MAQUETTE.png` sont les rendus des supports SVG. Les autres captures proviennent directement de l’application modifiée ; ces deux types de preuve restent distingués.

## Limites et dépendances conservées

Les vérifications sont locales, sur les réponses enregistrées. Elles ne démontrent pas le fonctionnement HTTP des 21 GET, les variantes manquantes ou une correction fournisseur. Q01, Q06, Q07, Q11 et Q14 restent suivies ; Q05 reste conditionnelle. L’anomalie R17, les précautions BMO et la traçabilité des sessions ne sont pas corrigées par le visuel.

Le rechargement natif Ctrl+R/F5 après navigation par fragments, le vrai zoom navigateur 200/400 %, les lecteurs d’écran et la conformité RGAA complète restent NON TESTÉS. La reprise après un nouveau chargement complet et le reflow 320 px sont des contrôles distincts, déjà tracés. Aucun test avec des salariés réels ni résultat de recherche utilisateur n’est revendiqué.

La production HTTP, les autres parcours et leurs URL ne sont pas présents ici. La sélection portable existante reste disponible ; aucune destination ou transmission vers un service absent n’est simulée. Le téléchargement CSV des statistiques reste à réaliser selon US-FON-012, distinct de l’export des pistes.

Les choix graphiques restent révisables à partir d’essais de compréhension, sans rouvrir le périmètre fonctionnel. Aucun nouveau label métier, classement ou seuil métier ne peut être déduit de cette direction artistique.

## Réexécuter

Après le build partagé et l’assemblage HTML, exécuter les lanceurs existants de contrôles et de missions UX, puis `outils/lancer_recette.ps1`. Edge est lancé en mode invisible. `outils/verifier_integrite.py` contrôle les sources et données ; le vérificateur du backlog reste également applicable.

L’état initial est conservé dans `../99_archives/2026-11-02_direction_artistique/ETAT_AVANT.zip`. Le brief et l’HTML d’intention fournis dans Téléchargements n’ont pas été modifiés.
