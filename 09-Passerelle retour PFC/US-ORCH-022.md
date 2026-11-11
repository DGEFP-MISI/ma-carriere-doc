# MaCarrière — US-ORCH-022

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-022 — Aidance et vie professionnelle

**Scénario :** O26 · **Personas de test :** PER-FOR-008, PER-FOR-003 · **Expérience+ :** Cartes 056–058  
**Source utilisateur :** FR-03, FR-06 (pas de preuve aidance spécifique).

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Une responsabilité d’aidance ne peut être déduite d’un persona.

#### Exemple à reproduire
> « Je m’occupe d’un proche, quelles ressources existent pour concilier mon emploi ? »

#### Comportement attendu
Si explicitement exprimée, proposer les ressources proches aidants et l’exploration des métiers/horaires ; ne pas interroger la situation médicale du proche.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer conditions de travail ». **Service(s) :** Service-Public / France Aidants.  
**URL source :** [Service-Public](https://www.service-public.fr/particuliers/vosdroits/F16920) · [France Aidants](https://www.aidants.fr/).

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
