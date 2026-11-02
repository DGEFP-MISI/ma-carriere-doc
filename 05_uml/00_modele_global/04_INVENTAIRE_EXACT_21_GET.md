# Inventaire strict des 21 GET de l'API

Source : `/docs.json` transmis. Aucun autre endpoint ni aucune source directe.

| Domaine | Endpoint | Paramètres effectivement décrits |
|---|---|---|
| Métiers et compétences | `GET /domaines` | `grand_domaine` |
| Métiers et compétences | `GET /metiers` | `grand_domaine, domaine, competence, contexte, sans_contexte, mode_competence, q, fields, page` |
| Métiers et compétences | `GET /metiers/{rome}` | `**rome**, fields` |
| Métiers et compétences | `GET /metiers/{rome}/competences` | `**rome**, categorie, coeur_metier, depuis, fields, page` |
| Métiers et compétences | `GET /competences` | `q, categorie, rome, domaine, enjeu, macro_competence, code, fields, page` |
| Certifications et formation | `GET /certifications` | `q, rome, repertoire, formacode, acces, validation_partielle, fields, page` |
| Certifications et formation | `GET /certifications/{certifinfo}` | `**certifinfo**, fields` |
| Certifications et formation | `GET /certifications/blocs` | `q, certifinfo, fiche, rome, fields, page` |
| Certifications et formation | `GET /formacodes` | `q, rome, domaine, code, fields, page` |
| Territoires et sessions | `GET /territoires` | `q, zonage, region, departement, clpe, code, fields, page` |
| Territoires et sessions | `GET /sessions_a_venir` | `**zonage**, **territoire**, **certifinfo**, onisep, page, fields` |
| Territoires et sessions | `GET /sessions_en_cours` | `**zonage**, **territoire**, **certifinfo**, onisep, page, fields` |
| Indicateurs et études | `GET /mesures` | `fields` |
| Indicateurs et études | `GET /indicateurs` | `rome, zonage, territoire, fields, onisep` |
| Indicateurs et études | `GET /secteurs` | `zonage, territoire, naf, rome, fields` |
| Indicateurs et études | `GET /salaires` | `rome, zonage, region, fields` |
| Indicateurs et études | `GET /salaires/secteurs` | `rome, region, fields` |
| Indicateurs et études | `GET /recrutements` | `rome, zonage, region, departement, tri, fields` |
| Indicateurs et études | `GET /mobilites` | `rome, sens, region, age, fields` |
| Indicateurs et études | `GET /prospective/metiers` | `region, tri, fields` |
| Indicateurs et études | `GET /prospective/regions` | `rome, tri, fields` |

**Gras : paramètre marqué obligatoire dans OpenAPI.** Certaines obligations métier décrites dans le contrat peuvent diverger des `required` Swagger : signaler les différences, ne pas les corriger sans preuve.

## Données et statut des tests

- R16 : territoire -> indicateurs, validé sur F1610 et Montpellier, maille réelle par mesure.
- R17 : `/secteurs` territorial fonctionne ; filtrage `rome=F1610` à clarifier avec RCO.
- R18/R19 : filtres territoire et certifinfo testés ; absence d’identifiant de session/certifinfo dans réponses observées.
- R23 : filtres par compétences simples et multiples testés, `toutes` vs `au_moins_une` validés sur deux codes.
- R24 : contextes `contexte` / `sans_contexte` testés sur F16, résultats disjoints.

Les autres endpoints figurent dans le contrat, mais **la présente cartographie n’atteste pas une campagne de tests exhaustive**.
