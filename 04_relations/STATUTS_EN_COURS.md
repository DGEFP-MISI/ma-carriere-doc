# État de validation des 24 relations

La **source de vérité est** `matrice_statuts_apres_tests.csv`. Le fichier `matrice_liens_controles.csv` conserve la matrice d'origine.

- `R01–R15`, `R20–R22` : correspondances de codes / paramètres **statiques** dans les échantillons historiques, non validées individuellement par une requête directement tracée pendant R16–R24.
- `R16` : territoire vers indicateurs **validé sur l'exemple F1610 / Montpellier**, 14 mesures et maille réelle propre à chaque mesure.
- `R17` : géographie et secteurs sans filtre ROME fonctionnent (35 secteurs), mais `rome=F1610` renvoie des listes vides aux deux mailles vérifiées : **point ouvert côté RCO**.
- `R18`, `R19` : résultats de sessions filtrées cohérents, mais aucune preuve ligne à ligne du rattachement Certif Info (codes absents des réponses).
- `R23` : compétence OGR vers métiers ROME V3, y compris recherche multicompétences `toutes` / `au_moins_une`, confirmée sur exemples. Code `103659` confirmé par `GET /competences`.
- `R24` : `contexte` et `sans_contexte` confirmés pour le contexte `300782` dans le domaine `F16`.

Il ne faut ni convertir « R17 ouvert » en « validé », ni convertir 18 comparaisons statiques en 18 validations HTTP.
