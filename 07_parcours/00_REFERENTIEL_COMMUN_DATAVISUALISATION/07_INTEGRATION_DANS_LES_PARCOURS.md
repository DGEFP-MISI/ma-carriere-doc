# Modifications recommandées — sans altérer les livrables existants

## Explorer V2
- **Recherche :** aucune visualisation avant choix d'objet référentiel; maintenir le fonctionnement initial.
- **Fiche métier, rubrique rémunération :** remplacer carte chiffre isolée par MaDataBox médiane + Q1/Q3 + source / grain; classement territorial barres et carte conditionnée.
- **Recrutements :** carte régionale / départementale uniquement si `maille_reelle` homogène et code géographique adapté; tableau obligatoire.
- **Métier, prospective :** distinguer créations nettes, départs fin carrière, postes à pourvoir en 2030; FAP87 et millésime explicités. Inclus dans la cible, pas supprimé.
- **Métier, mobilités :** origines et destinations séparées, barres avec populations et âge, FAP225.
- **Métier, secteurs :** barres secteur NAF38 en grain FAP225 ; ne pas valider relation précise `/secteurs?rome` tant que R17 ne l'est pas.
- **Fiche certification :** onglets/populations de mesures d'insertion, taux de réussite et salaire InserSup en panneaux indépendants.
- **Fiche domaine :** liste de métiers prioritaire; statistiques uniquement depuis endpoints dûment reliés.
- **Comparateur :** même tableau et mêmes panneaux que fiche métier, pas radar mélangeant unités.
- **Mes pistes :** indicateurs récupérés selon contexte courant, pas de copies de graphiques stockées.

## Faire évoluer ma situation V3
- **Mieux gagner ma vie :** DataBox salaire par territoire, salaires sectoriels FAP225, sans promesse d'amélioration personnelle.
- **Changer de métier :** listes compétences et éventuellement panneaux salaire/BMO séparés; pas de score de compatibilité.
- **Autre secteur :** barres NAF38 FAP225 et exploration domaine ROME; blocage R17 traçable.
- **Conditions de travail :** contexte souhaité/à éviter en filtres et étiquettes; aucun camembert artificiel.
- **Valoriser expérience :** tableau métiers OGR et certifications, chiffres insertion par population; VAE affichée comme voie documentée.
- **Multi-intentions :** une principale; autres panneaux repliables par intention, partage des mêmes composants sans fusion des données.

## Autres parcours
Chaque nouveau parcours déclare ses indicateurs dans la matrice CSV; n'implémente jamais de graphique avant contrôle du grain, source, unité, millésime, code territoire et preuve.

## Gestion du changement
Les changements ci-dessus sont des **propositions** à inscrire au backlog et au registre de décisions. Les dossiers Explorer et Faire évoluer déjà écrits restent inchangés.

## Arbitrage transversal DSFR Chart / RGAA (V1.1)
Les parcours réutilisent les composants officiels et leur accessibilité native. Codex vérifie l’intégration aux filtres, titres, alternatives et états applicatifs, **sans audit générique ni réimplémentation de DSFR Chart**. Tout besoin graphique non couvert est documenté et soumis à arbitrage.
