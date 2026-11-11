# MaCarrière — US-ORCH-015

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-015 — Trouver des entreprises au-delà des offres

**Scénario :** O18 · **Personas de test :** PER-FOR-001, PER-FOR-007, PER-FOR-009 · **Expérience+ :** D24, D25 ; carte 039  
**Source utilisateur :** F045/SRC027 ; FR-02.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
L’absence d’offres ne signifie pas l’absence d’opportunités.

#### Exemple à reproduire
> « Où chercher des entreprises si je ne trouve pas d’offre ? »

#### Comportement attendu
Proposer les offres accessibles dans MaCarrière et une passerelle vers un service de recherche d’entreprises, si celui-ci est actif.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir les offres ». **Service(s) :** La Bonne Boîte.  
**URL source :** [La Bonne Boîte](https://labonneboite.francetravail.fr/).

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
