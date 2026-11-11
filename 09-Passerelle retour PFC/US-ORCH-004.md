# MaCarrière — US-ORCH-004

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-004 — Financer et sécuriser une reconversion

**Scénario :** O04 · **Personas de test :** PER-FOR-004, PER-FOR-008, PER-FOR-010 · **Expérience+ :** D11, D12  
**Source utilisateur :** F047/SRC023 ; F037/SRC006.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
L’API de formation ne permet pas de calculer les droits au financement ni le maintien de rémunération.

#### Exemple à reproduire
> « Comment me former sans perdre mes revenus ? »

#### Comportement attendu
Présenter les formations/certifications disponibles ; expliquer que plusieurs financements peuvent exister selon situation ; proposer les sources officielles adaptées sans promettre d’éligibilité.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir les voies d’accès ». **Service(s) :** Transitions Pro / Mon Compte Formation.  
**URL source :** [Transitions Pro](https://www.transitionspro.fr/) · [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-prive/html/#/).

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
