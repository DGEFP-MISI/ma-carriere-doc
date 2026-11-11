# MaCarrière — US-ORCH-013

**Statut :** proposition de recette à arbitrer · **Public prioritaire :** actifs occupés · **Rôle :** information et orchestration, sans diagnostic ni décision d’éligibilité.

### US-ORCH-013 — Permettre à un actif occupé de découvrir l’immersion professionnelle

**Scénario :** O16 · **Personas de test :** PER-FOR-001, PER-FOR-004, PER-FOR-007, PER-FOR-009 ; complément PER-FOR-010 selon l’intention · **Expérience+ :** D15, D28 ; carte 037  
**Source utilisateur :** FR-02 / FR-07 (signaux qualitatifs contextuels ; l’existence d’un besoin de PMSMP spécifiquement formulé dans ces sources n’est pas établie).  
**Source réglementaire / démarche :** [Immersion facilitée — Est-il possible de réaliser une immersion lorsque l’on est en activité ?](https://aide.immersion-facile.beta.gouv.fr/fr/article/est-il-possible-de-realiser-une-immersion-lorsque-lon-est-en-activite-1yb59te/) (fiche datée du 27/09/2024, à revalider avant production).

#### User Story
**ETQ** actif occupé envisageant une évolution ou une reconversion, **je veux** comprendre si je peux découvrir un autre métier grâce à une immersion et vers qui m’orienter, **afin de** tester ma piste sans recevoir une réponse destinée uniquement aux demandeurs d’emploi.

#### Constat
MaCarrière vise prioritairement les **actifs occupés**. Le simple lien vers l’accueil d’Immersion facilitée ne répond pas aux questions concrètes d’un salarié : puis-je le faire alors que je travaille, faut-il prévenir mon employeur, qu’en est-il de ma rémunération ? Une orientation non contextualisée peut laisser croire à tort que l’immersion est réservée aux demandeurs d’emploi ou accessible de droit à tous les salariés.

#### Exemples à reproduire
- « Je suis en CDI et je voudrais tester un autre métier avant de démissionner. »
- « Je travaille déjà : est-ce que je peux faire une immersion pendant mes congés sans prévenir mon employeur ? »
- « Si je fais une immersion pendant mes horaires de travail, est-ce que je garde mon salaire ? »
- « Je ne suis pas inscrit à France Travail : qui peut m’aider à organiser cette immersion ? »

*Ces formulations sont des scénarios de recette construits pour MaCarrière, et non des verbatims littéraux issus des forums.*

#### Comportement attendu
1. Reconnaître l’intention « découvrir/tester un métier avant de se reconvertir » et le contexte **salarié en activité** lorsque celui-ci est explicite.
2. Présenter brièvement l’immersion professionnelle (PMSMP) comme une possibilité **soumise à conditions**, sans établir l’éligibilité.
3. Si l’actif n’est pas inscrit à France Travail, expliquer que la fiche Immersion facilitée l’invite à contacter un **conseiller en évolution professionnelle (CEP)** pour être accompagné et porter la demande de convention.
4. Expliquer, uniquement si cela répond à la question, les trois configurations décrites dans la fiche :
   - **En dehors des horaires habituels ou pendant les congés :** pas de signature de l’employeur actuel requise pour la convention selon la fiche ; couverture AT/MP par l’organisme prescripteur.
   - **Sur le temps de travail avec accord de l’employeur :** signature de l’employeur, contrat et rémunération maintenus ; couverture AT/MP assurée par l’employeur.
   - **Sur le temps de travail sans accord :** situation particulière à traiter avec le conseiller ; suspension du contrat envisageable et pas de rémunération par l’employeur pendant l’immersion selon cette configuration.
5. Proposer les deux passerelles principales : **Comprendre l’immersion quand on est en activité** et **Trouver mon conseiller CEP** ; en complément, permettre de rechercher une entreprise accueillante.
6. Rester dans le rôle MaCarrière : information, exploration et orientation, **pas de diagnostic ni de validation de convention**.

#### Passerelles et liens officiels
- **CTA principal :** [Comprendre les possibilités d’immersion quand on est salarié](https://aide.immersion-facile.beta.gouv.fr/fr/article/est-il-possible-de-realiser-une-immersion-lorsque-lon-est-en-activite-1yb59te/)
- **CTA d’accompagnement :** [Trouver mon conseiller en évolution professionnelle](https://mon-cep.org/)
- **CTA optionnel :** [Rechercher une entreprise accueillante — Immersion facilitée](https://immersion-facile.beta.gouv.fr/)

#### Critères d’acceptation
- [ ] L’utilisateur se présente comme salarié : la réponse est centrée sur les possibilités d’immersion **en activité** et non sur un parcours de demandeur d’emploi par défaut.
- [ ] L’IA ne dit ni « l’immersion est réservée aux demandeurs d’emploi » ni « tous les salariés y ont droit ».
- [ ] Si l’utilisateur demande si son employeur doit être informé, la réponse distingue correctement les trois configurations et n’affirme pas une confidentialité absolue.
- [ ] Si l’utilisateur demande s’il conserve sa rémunération, la réponse précise les conditions correspondant à la configuration évoquée ; aucune garantie générique de maintien de salaire.
- [ ] Si l’utilisateur est en activité et non inscrit à France Travail, l’orientation vers le CEP apparaît.
- [ ] Au moins un lien mène vers la **fiche explicative pour les actifs**, et non uniquement vers l’accueil d’Immersion facilitée.
- [ ] La réponse n’évalue pas l’éligibilité individuelle, ne simule pas une convention et ne prescrit pas de démissionner ou de prendre des congés.
- [ ] Les informations juridiques de la fiche (mise à jour 27/09/2024) sont revérifiées avant publication en production.

#### À joindre à la recette
Captures des quatre questions/réponses ; captures des CTA ; contrôle des trois URLs ; preuve que la règle de routage « actif occupé » est bien prise en compte ; date de vérification de la fiche officielle.

---

**Traçabilité :** les questions scénarisées ne sont pas nécessairement des citations littérales des forums. Les liens et conditions des services tiers sont à vérifier avant mise en production.
