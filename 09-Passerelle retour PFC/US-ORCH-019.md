# MaCarrière — US-ORCH-019

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-019 — Discrimination liée à l’âge

**Scénario :** O22 · **Personas de test :** PER-FOR-009, PER-FOR-010 · **Expérience+ :** D08, D47, D52  
**Source utilisateur :** Absence de question forum dédiée confirmée.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
L’IA ne doit ni conclure à une discrimination établie ni minimiser le signal.

#### Exemple à reproduire
> « On me refuse un poste à cause de mon âge, où m’adresser ? »

#### Comportement attendu
Présenter les droits et la compétence du Défenseur des droits ; fournir le lien et laisser l’utilisateur décider.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Information métiers, si demandée ». **Service(s) :** Défenseur des droits.  
**URL source :** [Défenseur des droits](https://www.defenseurdesdroits.fr/).

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
