# MaCarrière — US-ORCH-011

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-011 — Métier transformé par l’IA

**Scénario :** O13 · **Personas de test :** PER-FOR-006, PER-FOR-007 · **Expérience+ :** D09, D14, D42  
**Source utilisateur :** F044/R19 ; FR-09.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Risque de prédiction non sourcée sur la disparition de métiers.

#### Exemple à reproduire
> « Mon métier évolue avec l’IA, que faire ? »

#### Comportement attendu
Présenter les compétences et évolutions métier effectivement disponibles ; proposer l’évolution des compétences ou CEP ; ne pas prédire le remplacement de l’emploi sans source.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir compétences et métiers ». **Service(s) :** CEP / plan de développement.  
**URL source :** [CEP](https://mon-cep.org/) · [plan de développement](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

---

**Traçabilité :** les questions scénarisées ne sont pas nécessairement des citations littérales des forums. Les liens et conditions des services tiers sont à vérifier avant mise en production.
