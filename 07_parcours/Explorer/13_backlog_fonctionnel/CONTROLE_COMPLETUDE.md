# Contrôle du backlog fonctionnel

Contrôle documentaire exécuté le 2 novembre 2026 par `outils/construire_backlog.py`. Aucune requête HTTP ni exécution de l’application dans ce contrôle.

| Contrôle | Résultat |
|---|---|
| Fonctionnalités / rattachements E01–E31 | 31 conservées, alias US-E01–US-E31 maintenus |
| US fonctionnelles | 35, dont 4 transversales ; 10 rubriques et au moins 5 étapes nominales chacune |
| Critères | 324 critères identifiés ; au moins 4 spécifiques par US, formulés Étant donné / Quand / Alors ; critères supplémentaires par mesure |
| Schémas SVG | 35 XML valides, title/desc et alternative textuelle du scénario |
| Mesures / visualisations | 29 notices natives et 25 identifiants V01–V25 reliés aux US |
| Endpoints / paramètres | 21 GET officiels couverts ; noms des paramètres de chaque appel contrôlés contre le Swagger |
| Chemins JSON | 1736 occurrences tracées, type officiel / observé / à confirmer distingués |
| Liens internes générés | Aucun lien de fichier rompu |
| Table de conception | 31 lignes, colonnes de pilotage d’origine conservées, 5 colonnes de liaison ajoutées |
| Intégrité des références | 155 fichiers protégés comparés par SHA-256 : aucun modifié |


## Limites du contrôle

La présence d’un chemin dans la conception n’établit pas qu’il est retourné pour chaque réponse. Les tableaux de types marquent explicitement les chemins non observés et les types non précisés. Les dix endpoints sans schéma officiel nécessitent un test fournisseur/documentaire ciblé ; aucun schéma dérivé n’a été élevé au rang de contrat officiel.

Ce contrôle vérifie les documents et leur traçabilité. Il ne valide ni des valeurs métier nouvelles, ni un fonctionnement HTTP, ni le rendu responsive de l’application, ni une conformité RGAA. Les recettes antérieures sont référencées avec leurs limites ; aucune compilation de l’application n’est nécessaire pour cette modification documentaire.

Une tentative de capture du SVG de comparaison dans Edge a échoué au démarrage du navigateur avec « Accès refusé » (canal Mojo/crashpad du bac à sable). Le rendu visuel navigateur des SVG n’est donc pas déclaré vérifié. Les 35 SVG ont été contrôlés comme XML, avec titre, description et scénario textuel équivalent ; ils restent directement ouvrables dans un navigateur.

## Réexécution

Depuis la racine, exécuter le script Python `07_parcours/Explorer/13_backlog_fonctionnel/outils/construire_backlog.py`. Il reconstruit les documents depuis la table et les données de rédaction ; conserver toute modification éditoriale dans ces sources avant de le relancer.

Exécuter ensuite `07_parcours/Explorer/13_backlog_fonctionnel/outils/verifier_backlog.py`. Cette seconde lecture contrôle les fichiers livrés, leur contenu réel, les critères Markdown/CSV, les champs conservés par rapport à l’archive et les paramètres requis officiels. Son dernier résultat est enregistré dans [VERIFICATION_INDEPENDANTE.json](VERIFICATION_INDEPENDANTE.json).

Les empreintes avant travail et les précédents fichiers sont dans `../99_archives/2026-11-02_backlog_fonctionnel/`. Le rapport structuré correspondant est [CONTROLE_COMPLETUDE.json](CONTROLE_COMPLETUDE.json).
