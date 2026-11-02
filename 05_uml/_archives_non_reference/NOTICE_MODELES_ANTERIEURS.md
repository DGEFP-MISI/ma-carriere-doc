# Modèle UML des données exposées — Étape 2

**Périmètre :** API DGEFP – indicateurs emploi-formation 0.1.0, 21 endpoints GET ; exclusivement Swagger fourni et réponses JSON remises, sans autres API.

## Comment utiliser les fichiers

- `API_RCO_UML_00_Associations.puml` : vue de relations par identifiant ou paramètre. **Les pointillés ne représentent PAS des clés étrangères physiques**.
- `API_RCO_UML_01_...` à `05_...` : structures de réponse et objets JSON imbriqués, classés par domaine. Un objet `items[]` est dessiné en composition `0..*` ; si `ensemble` est un objet observé, il est noté `0..1` **sans garantie contractuelle de présence**.
- `API_RCO_Matrice_Relations.csv` : vérification de chaque lien, champ et limite, importable dans Grist.
- `API_RCO_Mesures_Champs.csv` : 29 définitions de `/mesures` et listes exactes de champs déclarés par mesure (JSON observé).

## Niveau de preuve

**Bleu (Swagger)** : le schéma de réponse HTTP 200 documente les propriétés, sans attribut `required` dans les schémas examinés. La notation `0..*` prouve seulement que le champ est un tableau, elle ne garantit pas que le tableau sera toujours présent ni la cardinalité métier.

**Orange (JSON observé)** : forme présente dans les JSON fournis, **pas** déclarée par schéma 200 du Swagger. Cela concerne `/indicateurs`, `/mesures`, `/mobilites`, `/prospective/metiers`, `/prospective/regions`, `/recrutements`, `/salaires`, `/salaires/secteurs`, `/secteurs`.

**Gris (non documenté)** : `/domaines` n'a ni schéma 200 dans le Swagger, ni JSON rattachable dans les fichiers analysés dans cette étape ; seule sa description fonctionnelle est exploitable.

## Relations pouvant être justifiées

1. **Codes ROME V3** : liens entre métiers, certifications, compétences, Formacodes et filtres de recherche, avec liste `rome_codes[]` lorsqu'elle est déclarée. Aucun code ROME 4.0 n'est restitué.
2. **Certification – bloc** : `fiche_code`, `bloc_competences_codes[]`, `certifinfo_codes[]` ; attention RNCP / RS et valeurs nulles.
3. **Territoires** : `zonage` doit accompagner `territoire_code` pour éviter une confusion entre codes de régions/départements ; un CLPE expose `commune_codes[]` ; une commune expose notamment `clpe_code`, `departement_code`, `region_code`, `epci_code`, `zone_emploi_code`.
4. **Indicateurs – mesures** : dans les JSON fournis, `items[].mesure` correspond à `/mesures.items[].code`, et `items[].valeurs[]` est un tableau dont le schéma change selon la mesure. Les valeurs ont le `grain` et la `maille_reelle` de l'item, **pas nécessairement du métier ROME ou du territoire demandé**.
5. **Prospective / mobilités / salaires / recrutements** : les familles FAP87, FAP225 et FAP228 ne doivent pas être confondues ni associées comme une classification unique. Le paramètre `rome` sert de filtre, mais la granularité publiée peut rester FAP.
6. **Sessions** : `/sessions_a_venir` et `/sessions_en_cours` acceptent le filtre `certifinfo`, mais les objets retournés dans le Swagger ne portent ni ce code ni un identifiant de session. On ne doit pas déduire une clé unique à partir de `(siret_formateur, date_debut, code_insee)`.

## Limites de cardinalité

Aucune relation de base de données (`1-N`, `N-N`, clés SQL, contraintes de non-nullité) n'est prouvée par un Swagger décrivant une API de lecture. Les seules multiplicités renseignées dans les diagrammes détaillés correspondent aux **collections JSON** ou objets imbriqués des exemples. L'unicité revendiquée de `certifinfo_code` dans la fiche de certification est une convention du contrat, pas la preuve d'un index de base physique.

## Règles d'utilisation des données

- `null` = absence de valeur ; **jamais zéro**.
- `secret_stat` = statistique masquée ; ne pas la convertir en nombre.
- Sources, millésimes et grains sont fournis par les réponses /mesures ou les enveloppes de réponses lorsqu'ils existent.
- Pas d'indicateur calculé, de rapprochement métier ou de donnée externe ajouté.
