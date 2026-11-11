# MaCarrière — US-ORCH-026

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-026 — Cumul emploi-retraite

**Scénario :** O30 · **Personas de test :** PER-FOR-009 · **Expérience+ :** D21  
**Source utilisateur :** Hors besoins majoritaires du corpus.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Le service ne doit pas simuler des conditions individuelles de cumul.

#### Exemple à reproduire
> « Puis-je reprendre un travail après ma retraite ? »

#### Comportement attendu
Expliquer la possibilité de principe, rediriger vers les pages officielles de droits et afficher métiers/offres si cela est demandé.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer offres ». **Service(s) :** Info Retraite.  
**URL source :** [Info Retraite](https://parcours.info-retraite.fr/cumul-emploi-retraite).

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
