# MaCarrière — US-ORCH-023

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-023 — Se former en travaillant

**Scénario :** O27 · **Personas de test :** PER-FOR-004, PER-FOR-006, PER-FOR-007, PER-FOR-009 · **Expérience+ :** D14, D42 ; carte 098  
**Source utilisateur :** FR-07.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Les données de session ne suffisent pas à prouver une formation prise en charge par l’employeur.

#### Exemple à reproduire
> « Comment apprendre sans quitter mon emploi ? »

#### Comportement attendu
Montrer compétences/certifications/formations disponibles ; orienter vers les informations sur plan de développement et AFEST, sans garantie de financement.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir certifications ». **Service(s) :** Plan de compétences / AFEST.  
**URL source :** [Plan de compétences](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences) · [AFEST](https://travail-emploi.gouv.fr/rapport-lexperimentation-relative-aux-actions-de-formation-en-situation-de-travail-afest).

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
