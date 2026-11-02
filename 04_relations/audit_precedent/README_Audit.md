# Audit croisé API DGEFP–RCO — 1 novembre 2026

## Périmètre
Comparaison du fichier `swagger (2).json` version `0.1.0` aux réponses JSON reçues dans ce projet (dont `Indicateurs(1).zip`, les réponses certifications, fiche métier, compétences, sessions, territoires). Ce rapport audite **les opérations exposées** et **les exemples disponibles** ; il ne permet pas d'exclure des routes absentes de l'OpenAPI.

## Constats vérifiés
- **21 routes GET** sont déclarées.
- **11/21** routes déclarent un schéma de réponse HTTP 200 ; les **10 autres non** : `/indicateurs`, `/mesures`, `/domaines`, `/mobilites`, `/prospective/metiers`, `/prospective/regions`, `/recrutements`, `/salaires`, `/salaires/secteurs`, `/secteurs`.
- **4 occurrences de champs hors schéma** dans les réponses observées : `rome_code` et `rome_libelle` en racine dans `/metiers/{rome}/competences`, `items[].tag_onisep` dans chacun des 2 endpoints de sessions.
- **18/21** routes disposent ici d'au moins un JSON observé ; il n'y a pas de JSON de sortie exploitable ici pour `/metiers`, `/competences`, `/domaines`. Cela **ne signifie pas** que les requêtes n'ont jamais été testées ailleurs.
- CertifInfo `112561` -> RNCP `RNCP36101` -> 4 blocs RNCP à codes partagés. Le ROME `F1610` apparaît dans la fiche métier, les certifications et plusieurs réponses d'indicateurs.
- `/metiers/{rome}/competences` : `total=144`, `last_page=2`, mais 100 items dans la réponse fournie, donc **page 1 uniquement**.
- `/territoires?zonage=commune` : `total=34920`, 100 items fournis, `last_page=350` ; `/territoires?zonage=clpe` : `total=361`, page 1/4.
- `/indicateurs` France F1610 retourne 14 mesures, dont trois avec `valeurs=[]` dans l'échantillon ; les 14 codes sont présents dans `/mesures` (29 définitions).
- Les 4 réponses `/secteurs` observées ont `items=[]` et `total=0`, mais `ensemble` renseigné ; impossible de confirmer à partir de ces seules réponses l'accès aux secteurs employeurs du métier.
- Au moins une certification retournée par `/certifications` présente `etat_certifinfo_libelle="Archivées"` alors que l'endpoint annonce les certifications actives ; l'interprétation du statut doit être clarifiée.

## Ce qu'on ne peut pas vérifier depuis HTTP
Les tables physiques, vues SQL, contraintes PK/FK, cardinalités exactes, jointures internes, règles de filtre et routes non documentées nécessitent les routes réellement enregistrées, le code des contrôleurs/services, et des schémas SQL (ou migrations et définition des vues).

## Demandes minimales au développeur
1. Exporter **l'intégralité des routes actives**, et comparer avec les 21 routes OpenAPI (`php bin/console debug:router` si Symfony).
2. Produire le schéma SQL des tables/vues utilisées, avec PK/FK et les requêtes/jointures des 21 endpoints ; préciser si certaines associations sont calculées sans contrainte SQL.
3. Ajouter les dix schémas de réponses HTTP 200 manquants et les quatre champs non déclarés.
4. Fournir pour chaque route un **exemple de requête réel** (paramètres) et un **exemple de réponse**, avec les conditions de null, tableaux vides, secret_stat, pagination, repli et granularités ROME/FAP.
5. Clarifier les points de l'onglet `04_Points_a_valider_dev.csv` (notamment `/secteurs`, sessions et certificats archivés).

## Matrice des appels
`03_Matrice_relations_appels_API.csv` indique le champ source, le paramètre destination, un exemple, et surtout le **niveau de vérification**. Ne pas confondre correspondance d'identifiants observés et preuve qu'une requête avec le filtre ciblé a été exécutée.

## Sécurité
Ne pas fournir de jeton d'authentification ni de secret. L'audit utilise des données d'exemple ; respecter les conditions de diffusion liées aux données RCO.
