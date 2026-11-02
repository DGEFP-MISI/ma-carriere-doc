# Méthode d'audit d'une relation API

Pour chaque lien envisagé, consigner :

1. Endpoint source exact, paramètres et page réellement demandés.
2. Champ source retourné, valeur **observée**, nullabilité et éventuel tableau.
3. Endpoint cible, chemin ou paramètre qui accepte ce code (référence OpenAPI ou contrat).
4. Réponse cible obtenue avec ce code, identifiant retourné et éventuelle pagination.
5. Statut : `Contrat`, `Observé`, `Test de liaison confirmé`, `À confirmer`.
6. Granularité et limites : ROME / FAP 225 / FAP 228 / FAP 87, repli, mesures indisponibles.
7. Conserver les **requêtes effectivement jouées** si disponibles (sans jeton / données secrètes).

**Hors périmètre :** relations physiques SQL et jointures internes. Ces éléments ne sont pas accessibles par les 21 GET et ne sont ni testés ni représentés dans le modèle exploitable.
