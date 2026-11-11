# MaCarrière — US-ORCH-009

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-009 — Usure et maintien en emploi

**Scénario :** O10, O23 · **Personas de test :** PER-FOR-010, PER-FOR-009 · **Expérience+ :** D03, D05, D30–D32  
**Source utilisateur :** F023/SRC012 ; F066/SRC011.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Un signal d’usure n’autorise ni diagnostic médical ni recommandation d’aptitude.

#### Exemple à reproduire
> « J’adore mon métier mais il m’épuise physiquement. »

#### Comportement attendu
Proposer des pistes de mobilité si demandées ; présenter les ressources maintien en emploi et santé au travail, sans question médicale intrusive ni score.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer métiers proches ». **Service(s) :** Maintien en emploi / santé au travail.  
**URL source :** [Maintien en emploi](https://travail-emploi.gouv.fr/le-maintien-en-emploi) · [santé au travail](https://travail-emploi.gouv.fr/sante-au-travail).

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
