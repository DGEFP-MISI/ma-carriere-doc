# Contrôle R19 — Certifications + territoires → Sessions en cours

**Date du contrôle :** 1er novembre 2026  
**Statut :** validation fonctionnelle observée ; rattachement individuel des résultats à la certification non vérifiable dans le JSON  
**Méthode :** réponse réelle exportée depuis l'interface Swagger, sans appel API depuis VS Code.

## 1. Appel testé

```http
GET /sessions_en_cours?certifinfo=112561&zonage=region&territoire=76&onisep=exclure&page=1
```

Source : `response_1793547268595.json` (JSON utilisateur). Certification de référence : code Certif Info `112561`. Territoire : région Occitanie (`76`).

## 2. Résultat observé

- HTTP : statut non inclus dans le fichier JSON fourni ; il n'est pas déduit.
- `total` = **8** ; `page_size` = **100** ; `page` = **1** ; `last_page` = **1**.
- `items` : **8 objets**, et `nb_sessions = 1` dans chacun de ces objets (somme = **8**).
- **5 SIRET distincts**, **4 communes** : Tarbes (4), Toulouse (2), Nîmes (1), Plaisance-du-Touch (1).
- `tag_onisep = false` dans les 8 résultats ; cohérent avec `onisep=exclure`.
- Tous les résultats ont `date_debut <= 2026-11-01 <= date_fin`.

### Tableau des lignes retournées

| Commune | Code INSEE | Organisme | SIRET | Début | Fin | Apprentissage | Contrat pro | Continue conventionnée | Onisep |
|---|---|---|---|---|---|---|---|---|---|
| Nîmes | 30189 | CENTRE DE FORMATION D APPRENTIS | 77566202600845 | 2026-09-01 | 2027-07-31 | Oui | Oui | Non | Non |
| Tarbes | 65440 | CENTRE DE TARBES | 82422814200132 | 2026-09-21 | 2027-05-27 | Non | Non | Non | Non |
| Tarbes | 65440 | CENTRE DE TARBES | 82422814200132 | 2026-09-21 | 2027-10-07 | Oui | Oui | Non | Non |
| Plaisance-du-Touch | 31424 | CRS PROMOTION PROFESSIONNELLE | 77694482900030 | 2026-08-31 | 2027-07-30 | Oui | Non | Non | Non |
| Tarbes | 65440 | DR AE OCCITANIE | 82436343600901 | 2026-06-08 | 2027-02-18 | Non | Non | Oui | Non |
| Toulouse | 31555 | INNOVISTA | 51871742600036 | 2026-01-05 | 2027-06-30 | Non | Non | Oui | Non |
| Tarbes | 65440 | DR AE OCCITANIE | 82436343600901 | 2026-09-21 | 2027-05-27 | Non | Non | Oui | Non |
| Toulouse | 31555 | INNOVISTA | 51871742600036 | 2025-11-13 | 2026-12-31 | Oui | Oui | Non | Non |

**Répartition des attributs (catégories non exclusives) :** `formation_apprentissage=true` dans 4 lignes, `formation_contrat_pro=true` dans 3, `formation_continue_conventionnee=true` dans 3, `formation_initiale=true` dans 0. `presentiel_distantiel` vaut 1 pour 2 lignes et 0 pour 6 lignes ; la signification exacte des valeurs doit être confirmée dans le contrat, sans interprétation forcée.

## 3. Comparaison avec R18

Le test R18 utilisait `GET /sessions_a_venir?certifinfo=112561&zonage=region&territoire=76&onisep=exclure&page=1` : **10 résultats**, tous à Tarbes, avec `date_debut` entre **2026-11-23** et **2027-09-06**.

Dans R19 : **8 résultats**, avec des dates de début entre **2025-11-13** et **2026-09-21**, toutes antérieures au 1er novembre 2026, et des dates de fin ultérieures.

**Observation :** cette paire de réponses est cohérente avec les noms « à venir » et « en cours » à la date du contrôle ; elle ne prouve pas la totalité des règles temporelles côté serveur.

## 4. Traçabilité et limites

**Observé :** acceptation apparente des paramètres utilisés, pagination cohérente, localisation dans la région demandée, respect apparent du filtre Onisep et temporalité des sessions cohérente.

**Non démontré par la réponse :** chaque `item` n'affiche ni `certifinfo`, ni ID de session. L'export JSON ne permet donc pas de prouver isolément que chaque ligne correspond à `112561`, ni de vérifier l'unicité métier de chaque session. La présence de valeurs cohérentes ne démontre pas le SQL sous-jacent.

**Question documentaire à conserver :** le contrat prévoit-il une identité de session et un identifiant Certif Info disponibles via `fields` ou faut-il une autre source pour vérifier le lien exact ?

## 5. Conclusion

**R19 — Réponse cohérente sur le jeu testé, avec traçabilité individuelle à confirmer.** Conserver le JSON de réponse comme preuve et poursuivre les contrôles des relations restantes sans modifier les contrats officiels.
