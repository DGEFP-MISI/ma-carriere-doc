# MaCarrière — US-ORCH-025

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-025 — Confiance dans les perspectives emploi

**Scénario :** O29 · **Personas de test :** PER-FOR-006, PER-FOR-007, PER-FOR-001 · **Expérience+ :** D09 ; carte 040  
**Source utilisateur :** F044/R19 ; FR-09.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Les indicateurs et les offres n’ont pas nécessairement le même périmètre ni la même date.

#### Exemple à reproduire
> « Est-ce que ce métier recrute vraiment ? »

#### Comportement attendu
Afficher recrutements envisagés, difficultés et offres avec sources/dates distinctes ; proposer France Travail pour continuer.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir indicateurs locaux ». **Service(s) :** Offres France Travail.  
**URL source :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche).

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
