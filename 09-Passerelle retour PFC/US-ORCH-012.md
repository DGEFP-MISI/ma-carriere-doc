# MaCarrière — US-ORCH-012

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-012 — Proximité et contraintes familiales

**Scénario :** O14, O15 · **Personas de test :** PER-FOR-003, PER-FOR-008 · **Expérience+ :** D09, D18  
**Source utilisateur :** F064/R17 ; F041/R04 ; FR-06.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Un changement de territoire ne doit pas être inféré et les données locales peuvent manquer.

#### Exemple à reproduire
> « Je veux travailler près de chez moi. »

#### Comportement attendu
Mobiliser le territoire déclaré et les indicateurs/offres disponibles ; ne jamais déduire un lieu précis ; orienter vers les offres ciblées et accompagnement si besoin.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Consulter emploi territorial ». **Service(s) :** Offres France Travail.  
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
