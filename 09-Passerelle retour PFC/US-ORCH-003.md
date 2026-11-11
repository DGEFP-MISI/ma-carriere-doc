# MaCarrière — US-ORCH-003

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-003 — Métier cible et formation

**Scénario :** O03 · **Personas de test :** PER-FOR-004, PER-FOR-001, PER-FOR-008 · **Expérience+ :** D11, D12, D14  
**Source utilisateur :** F046/SRC021 ; FR-07.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
L’utilisateur a un métier cible et cherche une voie d’accès, non un questionnaire d’orientation.

#### Exemple à reproduire
> « Je sais quel métier je veux faire, mais quelle formation choisir ? »

#### Comportement attendu
Afficher certifications associées et formations/sessions disponibles ; distinguer diplôme, certification et session ; renvoyer vers Mon Compte Formation ou CEP si question de démarche.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Consulter certifications et formations ». **Service(s) :** Mon Compte Formation.  
**URL source :** [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-prive/html/#/).

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
