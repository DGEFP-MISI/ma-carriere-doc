# MaCarrière × Expérience+ — Catalogue d’orchestration et passerelles

**Version de travail — 11 novembre 2026**  
**Finalité :** accueillir la question de l’usager, apporter l’information disponible dans MaCarrière, puis proposer au bon moment un service extérieur pertinent. **Ni diagnostic, ni score individuel, ni prescription, ni décision d’éligibilité.**

## 1. Sources et traçabilité

- **Expérience+ :** `Architecture Expérience+-modifs-DGEFP_reluMB.docx` (55 pages), fiches D01–D52 et cartes Particuliers/Employeurs. Source de travail éditoriale, **pas** source juridique validée.
- **Personas :** PER-FOR-001 à PER-FOR-010 (fiches HTML fournies), situations utilisées pour tester la pertinence des passerelles, non conditions de ciblage automatique.
- **Forums :** corpus « Forum Intelligence », 40 discussions / 89 observations réparties en 9 familles ; dossier historique de liens `MaCarriere_Corpus_URL_Historique_Consolide.xlsx` et synthèses `ANALYSE_DESCRIPTIVE.md`, `ANALYSE_AFFINITY_ET_PRIORITES.md`. Les **89 observations sont des questions reformulées, pas 89 citations exactes**. Les URL archivées et certains fragments cités doivent être revérifiés à la source avant publication.
- **Entretiens :** 17 entretiens, 229 notes, 96 citations extraites des transcriptions. Les signaux des forums et les entretiens sont conservés distinctement.

### 9 familles du corpus forums

| Code | Famille | Observations / 89 | Discussions distinctes / 40 |
|---|---|---:|---:|
| FR-01 | Améliorer ou préserver sa rémunération | 18 | 16 |
| FR-02 | Explorer et sécuriser un projet professionnel | 19 | 15 |
| FR-03 | Améliorer conditions et qualité de vie | 12 | 12 |
| FR-04 | Changer de secteur / rester dans le secteur | 10 | 8 |
| FR-05 | Valoriser ses acquis / découvrir des métiers transversaux | 9 | 8 |
| FR-06 | Changer de territoire / se rapprocher de ses proches | 8 | 7 |
| FR-07 | Se former, certifier ou éviter une formation | 6 | 6 |
| FR-08 | Évoluer ou changer de métier | 4 | 4 |
| FR-09 | Anticiper l’avenir du métier et du marché | 3 | 3 |

**Attention :** les discussions peuvent alimenter plusieurs familles. Ne pas additionner les comptes de discussions.

### Personas de référence

| Persona | Situation essentielle |
|---|---|
| PER-FOR-001 | Reconversion prudente, métier cible non défini |
| PER-FOR-002 | Promotion vers l’encadrement, arbitrage salaire/charge |
| PER-FOR-003 | Bien-être, horaires de jour, changement de territoire |
| PER-FOR-004 | Métier cible identifié, trajectoire et formation incertaines |
| PER-FOR-005 | Mieux gagner sa vie sans changer de métier |
| PER-FOR-006 | Mutations de métier, notamment liées à l’IA |
| PER-FOR-007 | Changer de secteur en préservant les acquis |
| PER-FOR-008 | Évoluer avec contraintes familiales et de territoire |
| PER-FOR-009 | Valoriser son expérience, évoluer/transmettre |
| PER-FOR-010 | Usure professionnelle, compromis revenu/conditions |

## 2. Règles d'orchestration

1. **Déclenchement par question / intention** : jamais par attribution d'un persona réel à l'utilisateur.
2. **Réponse MaCarrière d'abord si pertinente** : données métiers/compétences/certifications/formation/territoires/indicateurs **dans les seules limites des GET validés**.
3. **Passerelle proportionnée** : montrer une destination précise lorsque la question appelle une démarche externe, sans pousser automatiquement un dispositif.
4. **Pas de diagnostic ni d'éligibilité automatique** : le service externe reste compétent pour les droits, les décisions, la santé ou les calculs personnels.
5. **Ressources sourcées** : titre, rôle de la destination, URL officielle contrôlée, date de vérification, limites, conditions à vérifier. Une URL citée par Expérience+ n'est pas réputée vérifiée en novembre 2026.
6. **Aucune promesse d'accès** : immersion, POE, alternance, maintien de salaire et autres possibilités doivent être présentés sous conditions.
7. **Multivoies** : proposer éventuellement « explorer les métiers » et « voir l'acteur compétent », plutôt qu'un tunnel unique.
8. **Ne pas confondre** langage d'un utilisateur, reformulation analytique d'un forum et citation certifiée.

## 3. Catalogue des intentions d'orchestration

**Liens intégrés dans chaque ligne :** les URL sont extraites du cahier Expérience+ ou de ses destinations institutionnelles ; elles ne sont pas toutes vérifiées en direct à la date de ce document. Une URL peut changer et une condition réglementaire doit être vérifiée avant affichage en production.

Les formulations suivantes sont des **questions scénarisées pour tester le moteur**, construites à partir des thèmes documentés ; **elles ne sont pas présentées comme des verbatims exacts**.

| ID | Question-type / intention | Personas concernés pour test | Preuve forums / sources | Réponse interne MaCarrière | Passerelle à proposer | Références Expérience+ | Décision à arbitrer |
|---|---|---|---|---|---|---|---|
| O01 | Je veux changer, mais je ne sais pas quoi faire | PER-FOR-001, PER-FOR-004, PER-FOR-008 | FR-02; F068/SRC022 | Explorer métiers et compétences par langage naturel | CEP; bilan de compétences si demandé<br>**Liens :** [CEP](https://mon-cep.org/) · [Bilan de compétences](https://travail-emploi.gouv.fr/le-bilan-de-competences) | D09,D10 | À quel moment proposer le CEP ? |
| O02 | Je veux un autre métier sans repartir de zéro | PER-FOR-001, PER-FOR-007, PER-FOR-009 | FR-05,FR-04; F039/R11 | Compétences et métiers proches; mobilité | CEP; France VAE si certification visée<br>**Liens :** [CEP](https://mon-cep.org/) · [France VAE](https://vae.gouv.fr/) | D09,D13,D24 | Ne pas assimiler proximité à accès garanti |
| O03 | Je connais mon métier cible mais pas la formation | PER-FOR-004, PER-FOR-001, PER-FOR-008 | FR-07; F046/SRC021 | Fiche métier → certifications → sessions si disponibles | Mon Compte Formation; CEP<br>**Liens :** [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-prive/html/#/) · [CEP](https://mon-cep.org/) | D10,D11,D12,D14 | Accès direct formation ou guidance ? |
| O04 | Comment financer un changement de métier ? | PER-FOR-004, PER-FOR-008, PER-FOR-010 | FR-07,FR-01; F047/SRC023 | Certifications/formations liées au métier, sans chiffrer un droit | Mon Compte Formation; Transitions Pro; CEP<br>**Liens :** [Transitions Pro](https://www.transitionspro.fr/) · [Projet de transition professionnelle](https://travail-emploi.gouv.fr/le-projet-de-transition-professionnelle) · [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-prive/html/#/) | D11,D12,D14 | Vérifier statut salarié et financement avant renvoi |
| O05 | Puis-je faire reconnaître mon expérience sans reprendre les études ? | PER-FOR-007, PER-FOR-009, PER-FOR-001 | FR-05; F039/R11 | Compétences/activités déclarées → certifications possibles | France VAE<br>**Liens :** [France VAE](https://vae.gouv.fr/) | D13,D43 | Distinguer association métier/certification et recevabilité VAE |
| O06 | Je veux évoluer dans mon entreprise | PER-FOR-002, PER-FOR-005, PER-FOR-009 | FR-08,FR-01; F041/R04 | Fiches métiers proches, compétences et comparaison de conditions | Entretien de parcours professionnel; plan de compétences<br>**Liens :** [Entretien professionnel](https://travail-emploi.gouv.fr/lentretien-professionnel) · [Plan de développement des compétences](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences) | D04,D14,D41,D42 | Positionner le renvoi employeur sans prescrire |
| O07 | Une promotion vaut-elle la charge supplémentaire ? | PER-FOR-002, PER-FOR-005 | FR-01; F040/A02 | Comparer données métier/salaire avec période et limites, responsabilités | CEP ou entretien professionnel si besoin<br>**Liens :** [Entretien professionnel](https://travail-emploi.gouv.fr/lentretien-professionnel) · [CEP](https://mon-cep.org/) | D04,D09,D41 | Ne pas simuler salaire individuel |
| O08 | Je veux être mieux payé sans changer de métier | PER-FOR-005, PER-FOR-002 | FR-01; F021/A06 | Salaire par secteur/territoire si données fiables; offres | France Travail offres; APEC selon public<br>**Liens :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche) · [APEC](https://www.apec.fr/candidat.html) | D09,D24 | Informer sur limites des sources salaires |
| O09 | Je veux garder mon salaire mais réduire le stress | PER-FOR-005, PER-FOR-003, PER-FOR-010 | FR-03,FR-01; F040/A02; F042/A07 | Explorer secteurs/postes/métiers proches et conditions | CEP; santé au travail si lien avec poste/santé<br>**Liens :** [CEP](https://mon-cep.org/) · [Maintien en emploi](https://travail-emploi.gouv.fr/le-maintien-en-emploi) | D03,D05,D09,D32 | Ne pas attribuer un état de santé |
| O10 | Mon travail m’épuise physiquement | PER-FOR-010, PER-FOR-009, PER-FOR-003 | FR-03; F023/SRC012; F066/SRC011 | Métiers proches et descriptions de contraintes du quotidien | Santé au travail; maintien en emploi<br>**Liens :** [Maintien en emploi](https://travail-emploi.gouv.fr/le-maintien-en-emploi) · [Santé au travail](https://travail-emploi.gouv.fr/sante-au-travail) | D03,D05,D30,D31,D32 | Ne pas demander de diagnostic médical |
| O11 | Je travaille de nuit : quels métiers proches avec d’autres horaires ? | PER-FOR-003, PER-FOR-008, PER-FOR-010 | FR-03,FR-06 | Comparer activités, horaires disponibles et emplois locaux | Santé au travail ou CEP selon formulation<br>**Liens :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche) · [CEP](https://mon-cep.org/) | D03,D05,D32,D36 | Préciser que les horaires varient selon l’employeur |
| O12 | Je veux changer de secteur mais garder mes compétences | PER-FOR-007, PER-FOR-006, PER-FOR-009 | FR-04,FR-05; F038/R10; F039/R11 | Mobilités métiers/compétences et marché | CEP; VAE ou formation selon besoin<br>**Liens :** [CEP](https://mon-cep.org/) · [France VAE](https://vae.gouv.fr/) | D09,D13,D24 | Distinction métier/secteur et preuve de transférabilité |
| O13 | Mon métier se transforme à cause de l’IA | PER-FOR-006, PER-FOR-007 | FR-09; F044/R19 | Compétences associées, métiers proches et perspectives disponibles | CEP; formation/plan compétences<br>**Liens :** [Plan de développement des compétences](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences) · [CEP](https://mon-cep.org/) | D09,D14,D42 | Aucune prédiction non sourcée sur disparition métier |
| O14 | Je veux travailler plus près de chez moi | PER-FOR-003, PER-FOR-008 | FR-06; F041/R04; F064/R17 | Offres/indicateurs territoriaux, comparaison métiers | France Travail; structures régionales<br>**Liens :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche) | D09,D24 | Ne pas garantir la proximité d’offres |
| O15 | Je souhaite changer mais mes contraintes familiales bloquent | PER-FOR-008, PER-FOR-003, PER-FOR-001 | FR-06,FR-03; F047/SRC023 | Explorer métiers/horaires/territoires/formations | CEP; ressources aidants si aidance exprimée<br>**Liens :** [CEP](https://mon-cep.org/) · [Congé proche aidant](https://www.service-public.fr/particuliers/vosdroits/F16920) · [France Aidants](https://www.aidants.fr/) | D09,D18; cartes 056-058 | Proposer aidance uniquement si exprimée |
| O16 | Puis-je essayer ce métier avant de m’engager ? | PER-FOR-001, PER-FOR-004, PER-FOR-007, PER-FOR-009 | FR-02,FR-07 | Quotidien et possibilités du métier | Immersion possible pour certains salariés en reconversion, notamment avec accompagnement CEP ; préciser les modalités selon le temps de travail<br>**Liens :** [Immersion des actifs — règles et cas](https://aide.immersion-facile.beta.gouv.fr/fr/article/est-il-possible-de-realiser-une-immersion-lorsque-lon-est-en-activite-1yb59te/) · [Trouver un CEP](https://mon-cep.org/) · [Immersion facilitée](https://immersion-facile.beta.gouv.fr/) | D15,D28; carte 037 | Ne pas présumer l’éligibilité ; distinguer temps de travail, congés, accord employeur et rémunération |
| O17 | Peut-on être recruté pour ses habiletés sans le diplôme ? | PER-FOR-001, PER-FOR-004, PER-FOR-007 | FR-05,FR-07 | Accès métier; exigences de certification | France Travail MRS; POE selon offres<br>**Liens :** [MRS France Travail](https://www.francetravail.fr/employeur/vos-recrutements/selectionnez-des-candidats/la-methode-de-recrutement-par-si.html) · [Préparation opérationnelle à l’emploi](https://travail-emploi.gouv.fr/la-preparation-operationnelle-lemploi-poe) | D24,D26,D27 | Ne pas promettre MRS/POE sur le métier |
| O18 | Comment trouver des entreprises au-delà des offres ? | PER-FOR-001, PER-FOR-007, PER-FOR-009 | FR-02; F045/SRC027 | Offres FT et territoire | La Bonne Boîte / FT, si service actif<br>**Liens :** [La Bonne Boîte](https://labonneboite.francetravail.fr/) · [Offres France Travail](https://candidat.francetravail.fr/offres/recherche) | D24,D25; carte 039 | Vérifier service et lien de destination |
| O19 | J’ai de l’expérience et je veux transmettre | PER-FOR-009, PER-FOR-002, PER-FOR-010 | FR-05 | Explorer métiers de formation/encadrement proches | CEP; ressources tutorat/AFEST<br>**Liens :** [Tutorat](https://travail-emploi.gouv.fr/le-tutorat) · [CEP](https://mon-cep.org/) | D41,D42,D46; carte 098 | Ne pas présumer compétence pédagogique |
| O20 | Je veux créer mon activité ou devenir indépendant | PER-FOR-009, PER-FOR-007, PER-FOR-005 | FR-08,FR-05 | Métiers/activités proches et compétences | Bpifrance Création; CEP<br>**Liens :** [Bpifrance Création](https://bpifrance-creation.fr/) | D16 | Pas de conseil financier ou juridique personnalisé |
| O21 | Je cherche un emploi et ne sais pas quelle démarche faire | PER-FOR-001, PER-FOR-004, PER-FOR-009 | FR-02; F045/SRC027 | Métiers qui recrutent, offres et territoires | France Travail; APEC ou Cap emploi selon situation<br>**Liens :** [France Travail](https://www.francetravail.fr/candidat/50-ans-et-plus.html) · [APEC](https://www.apec.fr/candidat/accompagnement.html) · [Cap emploi](https://www.capemploi.info/qui-sommes-nous/vous-etes-une-personne-en-situation-de-handicap-decouvrez-les-missions-des-cap-emploi.html) | D09; cartes 027,031-034,040 | Éviter de présenter ces services comme interchangeables |
| O22 | Je crains une discrimination liée à mon âge | PER-FOR-009, PER-FOR-010 | FR-02 (signal contextuel, pas preuve dédiée) | Informations métiers et compétences si utiles | Défenseur des droits<br>**Liens :** [Défenseur des droits](https://www.defenseurdesdroits.fr/) · [Discriminations au travail](https://travail-emploi.gouv.fr/la-protection-contre-les-discriminations) | D08,D47,D52 | Ne pas qualifier juridiquement un cas individuel |
| O23 | Je dois adapter mon poste plutôt que changer | PER-FOR-010, PER-FOR-003 | FR-03; F023/SRC012 | Explorer les possibilités métier si demandé | Santé au travail; maintien emploi; Agefiph selon contexte<br>**Liens :** [Maintien en emploi](https://travail-emploi.gouv.fr/le-maintien-en-emploi) · [Agefiph](https://www.agefiph.fr/centre-aide/maintenir-dans-lemploi) · [Santé au travail](https://travail-emploi.gouv.fr/sante-au-travail) | D03,D05,D07,D31-D35 | Pas de conclusion médicale/aptitude |
| O24 | Je reprends après un arrêt long et j’hésite à changer | PER-FOR-010, PER-FOR-009 | Signal non directement documenté dans les 89 questions accessibles | Informations métiers proches si souhaitées | Santé au travail / Assurance maladie<br>**Liens :** [Reprise et emploi Assurance maladie](https://www.ameli.fr/entreprise/vos-salaries/retour-emploi) · [Visite de préreprise](https://www.ameli.fr/entreprise/vos-salaries/retour-emploi/visite-pre-reprise) | D31,D33,D34,D50 | Confirmer besoin usager et voie d’accès |
| O25 | Je veux réduire mon activité avant la retraite | PER-FOR-009, PER-FOR-010 | Signal à confirmer dans forums | Activités, conditions et métiers compatibles | Info Retraite; Assurance retraite<br>**Liens :** [Info Retraite](https://www.info-retraite.fr/) · [Retraite progressive](https://www.service-public.fr/particuliers/vosdroits/F12842) | D17-D21 | Pas de calcul retraite ni éligibilité |
| O26 | Je suis aidant et j’ai besoin de concilier travail et obligations | PER-FOR-008, PER-FOR-003 | FR-03,FR-06 (non spécifique aidance) | Explorer emploi local et conditions du quotidien | Service-Public congé proche aidant; ressources aidants<br>**Liens :** [Congé proche aidant](https://www.service-public.fr/particuliers/vosdroits/F16920) · [France Aidants](https://www.aidants.fr/) | cartes 056-058 | Ne pas inférer aidance à partir du persona |
| O27 | Je veux me former en travaillant | PER-FOR-004, PER-FOR-006, PER-FOR-007, PER-FOR-009 | FR-07 | Compétences à acquérir, certifications et sessions | Plan de compétences; AFEST; CEP<br>**Liens :** [Plan de développement des compétences](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences) · [AFEST](https://travail-emploi.gouv.fr/rapport-lexperimentation-relative-aux-actions-de-formation-en-situation-de-travail-afest) | D14,D42; carte 098 | Ne pas promettre AFEST ou prise en charge |
| O28 | Je veux comparer une formation longue et une alternative courte | PER-FOR-001, PER-FOR-004, PER-FOR-008 | FR-07; F043/A05; F047/SRC023 | Comparer certifications, blocs et sessions disponibles | CEP; France VAE; financement officiel<br>**Liens :** [France VAE](https://vae.gouv.fr/) · [CEP](https://mon-cep.org/) · [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-prive/html/#/) | D10-D14 | Durées, coûts et insertion uniquement si données disponibles |
| O29 | Je veux changer mais je crains le marché actuel | PER-FOR-006, PER-FOR-007, PER-FOR-001 | FR-09; F044/R19 | Indicateurs datés, recrutements, offres et limites | France Travail, APEC, CEP<br>**Liens :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche) · [APEC](https://www.apec.fr/candidat.html) | D09; carte 040 | Pas de prévisions non documentées |
| O30 | Je suis retraité et souhaite reprendre une activité | PER-FOR-009 | Non établi comme besoin prioritaire du corpus actifs | Offres et fiches métiers si pertinentes | Info Retraite / Assurance retraite<br>**Liens :** [Info Retraite](https://www.info-retraite.fr/) · [Cumul emploi-retraite](https://parcours.info-retraite.fr/cumul-emploi-retraite) | D21 | Hors cœur MVP, mais orienter sans blocage |

## 4. Correspondance exhaustive D01–D52 (pas de diagnostic MaCarrière)

**Code d’usage :** `I` = information courte ; `R` = renvoi externe ; `Q` = reconnaître le type de question ; `C` = contexte uniquement ; `X` = ne pas reproduire l'outil. Tous les liens doivent être revérifiés.

| Réf. | Ressource Expérience+ | Usage MaCarrière | Personas à tester | Orchestrations |
|---|---|---|---|---|
| D01 | Autodiagnostic court maintien en emploi | Q/C/X | PER-FOR-003, PER-FOR-010 | O09–O11,O23 |
| D02 | Autodiagnostic long parcours et capacités | Q/C/X | PER-FOR-001, PER-FOR-003, PER-FOR-008, PER-FOR-010 | O01,O09,O15 |
| D03 | Visites médicales au travail | I/R | PER-FOR-003, PER-FOR-010 | O09–O11,O23 |
| D04 | Entretien de parcours professionnel | I/R | PER-FOR-002, PER-FOR-005, PER-FOR-009 | O06,O07 |
| D05 | Maintien en emploi et adaptation du poste | I/R | PER-FOR-003, PER-FOR-010 | O10,O23 |
| D06 | Compte professionnel de prévention | I/R | PER-FOR-010 | O10,O25 |
| D07 | RQTH | I/R | PER-FOR-010 | O23 |
| D08 | Discrimination liée à l’âge | I/R | PER-FOR-009, PER-FOR-010 | O22 |
| D09 | CEP | I/R | PER-FOR-001, PER-FOR-004, PER-FOR-006, PER-FOR-007, PER-FOR-008 | O01–O04,O12 |
| D10 | Bilan de compétences | I/R | PER-FOR-001, PER-FOR-004 | O01,O28 |
| D11 | CPF | I/R | PER-FOR-001, PER-FOR-004, PER-FOR-008 | O03,O04,O28 |
| D12 | Période de reconversion professionnelle | I/R | PER-FOR-004, PER-FOR-007, PER-FOR-008 | O04,O12 |
| D13 | VAE | I/R | PER-FOR-001, PER-FOR-007, PER-FOR-009 | O02,O05,O28 |
| D14 | Plan de développement des compétences | I/R | PER-FOR-002, PER-FOR-006, PER-FOR-009 | O06,O13,O27 |
| D15 | Atout Senior | I/R | PER-FOR-009 | O16 |
| D16 | Création ou reprise d’entreprise | I/R | PER-FOR-005, PER-FOR-007, PER-FOR-009 | O20 |
| D17 | Retraite progressive | I/R | PER-FOR-009, PER-FOR-010 | O25 |
| D18 | Temps partiel aménagé | I/R | PER-FOR-008, PER-FOR-009, PER-FOR-010 | O15,O25 |
| D19 | Améliorer pension/retraite | I/R | PER-FOR-009, PER-FOR-010 | O25 |
| D20 | Carrière longue | I/R | PER-FOR-009, PER-FOR-010 | O25 |
| D21 | Cumul emploi-retraite | I/R | PER-FOR-009 | O30 |
| D22 | Autodiagnostic employeur | C/X | PER-FOR-002, PER-FOR-010 | O09,O23 |
| D23 | Simulation coût non-prévention | C/X | PER-FOR-010 | O10 |
| D24 | Clarifier besoin de compétences | C | PER-FOR-001, PER-FOR-007, PER-FOR-009 | O02,O17,O18 |
| D25 | Offre sans biais âge | C/R | PER-FOR-009 | O18,O22 |
| D26 | MRS | I/R | PER-FOR-001, PER-FOR-004, PER-FOR-007 | O17 |
| D27 | POE | I/R | PER-FOR-004, PER-FOR-007 | O17 |
| D28 | Immersion professionnelle | I/R | PER-FOR-001, PER-FOR-004, PER-FOR-007 | O16 |
| D29 | Organiser l’intégration | C | PER-FOR-004, PER-FOR-009 | O21 |
| D30 | Repérer situation fragile | Q/C | PER-FOR-010 | O10 |
| D31 | Mobiliser santé au travail | I/R | PER-FOR-010 | O10,O23,O24 |
| D32 | Adapter poste/organisation | I/R | PER-FOR-003, PER-FOR-010 | O09–O11,O23 |
| D33 | Reprise après arrêt long | I/R | PER-FOR-010 | O24 |
| D34 | Essai encadré | I/R | PER-FOR-010 | O23,O24 |
| D35 | Aides Agefiph maintien | I/R | PER-FOR-010 | O23 |
| D36 | Agir sur organisation du travail | Q/C | PER-FOR-003, PER-FOR-010 | O09–O11 |
| D37 | DUERP risque de désinsertion | C | PER-FOR-010 | O23 |
| D38 | FIPU | C/R | PER-FOR-010 | O23 |
| D39 | C2P côté employeur | C | PER-FOR-010 | O10 |
| D40 | Ressources prévention | I/R | PER-FOR-010 | O23 |
| D41 | Entretiens professionnels | I/R | PER-FOR-002, PER-FOR-005, PER-FOR-009 | O06,O07,O19 |
| D42 | Plan de développement | I/R | PER-FOR-002, PER-FOR-006, PER-FOR-009 | O06,O13,O27 |
| D43 | VAE en entreprise | I/R | PER-FOR-007, PER-FOR-009 | O05 |
| D44 | Période reconversion employeur | C/R | PER-FOR-004, PER-FOR-007 | O04,O12 |
| D45 | Période reconversion (autre fiche du document) | C/R | PER-FOR-004, PER-FOR-007, PER-FOR-010 | O04,O12 |
| D46 | Tutorat/transmission/mentorat | I/R | PER-FOR-002, PER-FOR-009 | O19 |
| D47 | Prévenir discrimination âge | I/R | PER-FOR-009 | O22 |
| D48 | Accord/plan travailleurs expérimentés | C | PER-FOR-009, PER-FOR-010 | O06,O23 |
| D49 | Indicateurs travailleurs expérimentés | C | PER-FOR-009, PER-FOR-010 | O22 |
| D50 | Prévenir inaptitude/documenter | I/R | PER-FOR-010 | O23,O24 |
| D51 | Associer représentants du personnel | I/R | PER-FOR-010 | O23 |
| D52 | Anticiper signalements discrimination | I/R | PER-FOR-009, PER-FOR-010 | O22 |

## 5. Cartes sans fiche D ou ajoutées : ne pas perdre les passerelles

| Cartes Expérience+ | Opportunité MaCarrière | Personas | Décision / statut |
|---|---|---|---|
| Carte « Projet de transition professionnelle » | Passerelle financement de reconversion avec continuité de revenu sous conditions | 001,004,008,010 | Vérifier fiche officielle Transitions Pro, période et conditions |
| 027–030 — France Travail, indemnisation, simulation allocation, portabilité santé | Identifier le bon interlocuteur pour conséquences du changement d’emploi | 001,004,008 | Éviter tout calcul de droit dans MaCarrière |
| 031–034 — CEP, Senior 360, APEC, Cap emploi | Aiguillage selon la question et le service compétent | 001,004,007,009,010 | Vérifier périmètres/services actifs |
| 035–038 — valoriser parcours, Agil’Cadres, immersion, programmes APEC | Aide à l'action après exploration | 001,007,009 | Immersion prioritaire à investiguer |
| 039 — La Bonne Boîte | Recherche d’entreprises au-delà des offres | 001,005,007 | Vérifier disponibilité du service |
| 040–041 — offres France Travail et recrutement par simulation | Offres + voie d’accès alternative | 001,004,007 | Passerelles distinctes de l’API métier |
| 042–047 — contrats, aides et droits pendant recherche | Réponse courte, puis destination officielle | 004,009 | Vérifier âge/statut et actualité |
| 048–055 — CESU, Aidants Connect, épargne, santé et ALD | Orientation seulement si la question sort de l’information métier | 008,010 | Hors cible à ne pas montrer par défaut |
| 056–058 — proche aidant, don de jours, ressources aidants | Reconnaître contraintes d’aidance exprimées | 008,003 | Respect des données sensibles |
| Employeurs 059–108 | Exploiter méthodes, acteurs et voies possibles sans ouvrir un parcours employeur | 002,009,010 | Ne pas importer diagnostics/scores employeurs |
| Carte AFEST ajoutée dans partie employeurs | Connaître et rediriger vers la formation en situation de travail | 004,006,007,009 | Vérifier source et disponibilité |

## 6. Exemples de traçabilité forums (titres de fils et IDs, non citations littérales)

| Référence historique | Signal identifié | Orchestration / personas |
|---|---|---|
| F023 / SRC012 | « J'adore mon métier, mais il m'éclate physiquement » — fragment archivé à revérifier | O10, O23 / PER-FOR-010 |
| F066 / SRC011 | Épuisement dans les soins et conditions dégradées — fragment archivé à revérifier | O10 / PER-FOR-010 |
| F040 / A02-01, A02-02 | Augmentation de 10 % face à télétravail/équipe | O07,O09 / PER-FOR-002,005 |
| F041 / R04-01 à 03 | Contre-offre, promotion externe et rapprochement territorial | O07,O14 / PER-FOR-002,003,008 |
| F043 / A05-01, A05-02 | Longues études pour rémunération perçue identique | O28 / PER-FOR-004,008 |
| F044 / R19-01 à 03 | Développeur inquiet des mutations et de l’IA | O13,O29 / PER-FOR-006 |
| F039 / R11-01 à 04 | Expérience tourisme et management, exploration métiers transversaux | O02,O12 / PER-FOR-007,009 |
| F038 / R10-01 à 04 | Graphisme, rémunération et secteur perçu en déclin | O12,O13 / PER-FOR-006,007 |
| F045 / SRC027 | Critères basiques localisation/métier/salaire mal respectés par les offres | O14,O21 / PER-FOR-003,008 |
| F046 / SRC021 | Choix formation initiale / alternance | O03,O27 / PER-FOR-004 |
| F047 / SRC023 | Études de trois ans et contrainte financière | O04,O28 / PER-FOR-004,008 |
| F068 / SRC022 | Changement sans savoir par où commencer, besoin de débouchés rapides | O01,O21 / PER-FOR-001 |

## 7. Décisions à prendre en atelier

1. La carte d’orchestration doit-elle apparaître **dans les réponses conversationnelles**, **dans les fiches Explorer**, ou les deux ?
2. Un service externe s’affiche-t-il sur simple détection d’intention ou après une confirmation légère de l’usager ?
3. Quand plusieurs services sont plausibles, faut-il afficher **une destination principale et une alternative** plutôt qu’un catalogue ?
4. Qui maintient la table des destinations et vérifie **URL, statut, conditions, date** ?
5. Quelle preuve minimale pour chaque scénario : 1 référence Expérience+ + forum ou entretien + service officiel actif ?
6. Distinguer **lien direct de démarche**, **lien d’explication**, et **orientation vers un professionnel**.
7. Définir la stratégie de repli si l’API MaCarrière ne permet pas de fournir la donnée attendue : ne jamais inventer, et orienter vers le service compétent.
8. Tester chaque scénario avec les personas concernés **sans considérer les personas comme une règle de profilage**.

## 8. Backlog recommandé

- **ORCH-01** — Table des intentions, déclencheurs et règles de non-déclenchement (O01–O30).
- **ORCH-02** — Répertoire des destinations officielles avec validation métier et date de contrôle.
- **ORCH-03** — Gabarit DSFR : « Pour aller plus loin » / destination + rôle du service + limite de MaCarrière.
- **ORCH-04** — Traçabilité forums et entretiens : question reformulée, URL/ID, statut de vérification, persona de test.
- **ORCH-05** — Tests de non-surorientation : pas de CTA financement sur une simple question salariale, pas de CTA santé si seul le métier est mentionné.
- **ORCH-06** — Tests multi-intentions et priorisation : usure + revenu, salaire + territoire, expérience + formation, mutation + sécurité.
- **ORCH-07** — Revue du contrat de 21 GET : champ réellement disponible, donnée partielle, repli vers service externe.

## 9. Statut du présent document

**Présélection fonctionnelle, non validation.** Les correspondances persona–intention sont des **cas de test proposés**, non des observations directement attribuées à chaque persona. Les thèmes et identifiants forums viennent des corpus historiques récupérés, mais les 89 lignes détaillées de la base d'origine ne sont pas toutes présentes comme fichier exploitable dans cette session : la jointure individuelle exhaustive « 89 observations → O01–O30 » reste à effectuer lorsque la base d'origine est disponible. Les URL officielles d’Expérience+ sont des **candidates à vérifier** avant publication ; ce document ne valide ni droit, ni éligibilité, ni possibilité technique non documentée.


## 7. User Stories de recette — orchestration et passerelles

**Convention :** formulations de test dérivées du corpus, jamais verbatims certifiés sauf indication expresse ; les liens ci-dessous sont documentaires et restent à contrôler en production. Chaque US concerne le comportement visible de MaCarrière et non une décision automatique de droit ou de santé. Les personas sont des cas de test, **pas des profils à inférer sur les utilisateurs**.

### US-ORCH-001 — Question sans métier cible

**Scénario :** O01 · **Personas de test :** PER-FOR-001, PER-FOR-004, PER-FOR-008 · **Expérience+ :** D09, D10  
**Source utilisateur :** F068 / SRC022 ; FR-02.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Le besoin ne correspond pas encore à un métier ROME et un renvoi automatique vers une formation serait prématuré.

#### Exemple à reproduire
> « Je veux changer mais je ne sais pas quoi faire. »

#### Comportement attendu
Identifier l’intention de clarification ; ouvrir l’exploration par activités ou compétences en langage courant ; proposer le CEP comme accompagnement facultatif.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer des métiers ». **Service(s) :** CEP.  
**URL source :** [CEP](https://mon-cep.org/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-002 — Transférer ses compétences

**Scénario :** O02, O12 · **Personas de test :** PER-FOR-001, PER-FOR-007, PER-FOR-009 · **Expérience+ :** D09, D13, D24  
**Source utilisateur :** F039/R11 ; FR-04, FR-05.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Le secteur change mais certaines compétences peuvent rester utiles ; la proximité métier n’établit pas une possibilité d’embauche.

#### Exemple à reproduire
> « Je veux changer de secteur sans repartir de zéro. »

#### Comportement attendu
Restituer les métiers et compétences identifiés par l’API ; indiquer ce qui est connu et inconnu ; proposer un CEP et la VAE uniquement si la certification est pertinente.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir métiers et compétences proches ». **Service(s) :** CEP / France VAE.  
**URL source :** [CEP](https://mon-cep.org/) · [France VAE](https://vae.gouv.fr/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-005 — Expérience sans diplôme

**Scénario :** O05 · **Personas de test :** PER-FOR-007, PER-FOR-009, PER-FOR-001 · **Expérience+ :** D13, D43  
**Source utilisateur :** F039/R11 ; FR-05.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Le diplôme ne doit pas être considéré comme seule porte d’entrée et une correspondance RNCP ne vaut pas recevabilité VAE.

#### Exemple à reproduire
> « J’ai l’expérience mais pas le diplôme. »

#### Comportement attendu
Montrer les certifications liées au métier ; présenter France VAE comme possibilité à examiner ; ne pas affirmer que l’usager obtiendra la certification.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir certifications liées ». **Service(s) :** France VAE.  
**URL source :** [France VAE](https://vae.gouv.fr/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-006 — Évoluer dans la même entreprise

**Scénario :** O06 · **Personas de test :** PER-FOR-002, PER-FOR-005, PER-FOR-009 · **Expérience+ :** D04, D14, D41, D42  
**Source utilisateur :** F041/R04 ; FR-08.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
La recherche classique de métiers ne montre pas les leviers de mobilité interne.

#### Exemple à reproduire
> « Puis-je évoluer dans mon entreprise sans démissionner ? »

#### Comportement attendu
Explorer les compétences et métiers adjacents puis proposer une ressource sur l’entretien professionnel et le plan de développement des compétences.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Comparer les métiers proches ». **Service(s) :** Entretien professionnel.  
**URL source :** [Entretien professionnel](https://travail-emploi.gouv.fr/lentretien-professionnel).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-007 — Promotion salaire / responsabilités

**Scénario :** O07 · **Personas de test :** PER-FOR-002, PER-FOR-005 · **Expérience+ :** D04, D09, D41  
**Source utilisateur :** F040/A02 ; FR-01.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Les arbitrages portent sur plusieurs critères ; nos données ne décrivent pas la prime ou la responsabilité effective d’un poste individuel.

#### Exemple à reproduire
> « Est-ce que la hausse de salaire vaut la charge de manager ? »

#### Comportement attendu
Comparer les informations vérifiées et datées sur les métiers ; signaler les limites ; proposer un CEP ou un échange professionnel si une aide à la décision est demandée.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Comparer salaires et quotidien ». **Service(s) :** CEP.  
**URL source :** [CEP](https://mon-cep.org/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-008 — Mieux gagner sa vie sans changer de métier

**Scénario :** O08 · **Personas de test :** PER-FOR-005, PER-FOR-002 · **Expérience+ :** D09, D24  
**Source utilisateur :** F021/A06 ; FR-01.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Un salaire de référence ne garantit pas la rémunération d’une offre ni d’une région.

#### Exemple à reproduire
> « Je veux gagner davantage sans changer de métier. »

#### Comportement attendu
Utiliser les indicateurs salariaux et sectoriels disponibles avec source, période et limites ; proposer les offres France Travail comme exploration du marché.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Comparer secteurs ou territoires ». **Service(s) :** Offres France Travail.  
**URL source :** [Offres France Travail](https://candidat.francetravail.fr/offres/recherche).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-010 — Horaires et travail de nuit

**Scénario :** O11 · **Personas de test :** PER-FOR-003, PER-FOR-008, PER-FOR-010 · **Expérience+ :** D05, D32, D36  
**Source utilisateur :** FR-03 ; FR-06.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
L’horaire d’un poste varie entre employeurs ; des descriptions métiers génériques ne prouvent pas des horaires de jour garantis.

#### Exemple à reproduire
> « Je veux arrêter de travailler de nuit. »

#### Comportement attendu
Explorer métiers/territoires/conditions dans la limite des données ; afficher incertitude sur horaires et proposer des offres/CEP en contexte.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer les métiers ». **Service(s) :** France Travail / CEP.  
**URL source :** [France Travail](https://candidat.francetravail.fr/offres/recherche) · [CEP](https://mon-cep.org/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-011 — Métier transformé par l’IA

**Scénario :** O13 · **Personas de test :** PER-FOR-006, PER-FOR-007 · **Expérience+ :** D09, D14, D42  
**Source utilisateur :** F044/R19 ; FR-09.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Risque de prédiction non sourcée sur la disparition de métiers.

#### Exemple à reproduire
> « Mon métier évolue avec l’IA, que faire ? »

#### Comportement attendu
Présenter les compétences et évolutions métier effectivement disponibles ; proposer l’évolution des compétences ou CEP ; ne pas prédire le remplacement de l’emploi sans source.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir compétences et métiers ». **Service(s) :** CEP / plan de développement.  
**URL source :** [CEP](https://mon-cep.org/) · [plan de développement](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-014 — Recrutement sur habiletés / POE

**Scénario :** O17 · **Personas de test :** PER-FOR-001, PER-FOR-004, PER-FOR-007 · **Expérience+ :** D24, D26, D27  
**Source utilisateur :** FR-05 ; FR-07.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Un métier peut être accessible par plusieurs voies, mais certains titres sont légalement requis.

#### Exemple à reproduire
> « Peut-on être recruté sans le diplôme demandé ? »

#### Comportement attendu
Montrer l’accès métier/certifications ; expliquer MRS et POE quand adaptées ; préciser que le dispositif dépend des recrutements et critères du service.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir voies d’accès ». **Service(s) :** France Travail MRS / POE.  
**URL source :** [France Travail MRS](https://www.francetravail.fr/employeur/vos-recrutements/selectionnez-des-candidats/la-methode-de-recrutement-par-si.html) · [POE](https://travail-emploi.gouv.fr/la-preparation-operationnelle-lemploi-poe).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-016 — Transmettre et tutorer

**Scénario :** O19 · **Personas de test :** PER-FOR-009, PER-FOR-002, PER-FOR-010 · **Expérience+ :** D41, D42, D46  
**Source utilisateur :** FR-05 (signal contextuel).

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Le tutorat n’est pas une qualification automatiquement acquise.

#### Exemple à reproduire
> « Je veux transmettre ce que je sais plutôt que tout recommencer. »

#### Comportement attendu
Explorer métiers et compétences liés à la transmission ; présenter les ressources tutorat et CEP, sans prétendre à un poste disponible.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer métiers associés ». **Service(s) :** Tutorat / CEP.  
**URL source :** [Tutorat](https://travail-emploi.gouv.fr/le-tutorat) · [CEP](https://mon-cep.org/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-017 — Créer ou reprendre son activité

**Scénario :** O20 · **Personas de test :** PER-FOR-009, PER-FOR-007, PER-FOR-005 · **Expérience+ :** D16  
**Source utilisateur :** FR-05 ; FR-08.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Créer son activité n’est pas une reconversion nécessitant systématiquement une formation.

#### Exemple à reproduire
> « Je souhaite devenir indépendant. »

#### Comportement attendu
Proposer exploration des activités et compétences ; orienter vers les ressources de création sans conseil juridique/financier individualisé.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer activités/métiers ». **Service(s) :** Bpifrance Création.  
**URL source :** [Bpifrance Création](https://bpifrance-creation.fr/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-018 — Accompagnement vers l’emploi

**Scénario :** O21 · **Personas de test :** PER-FOR-001, PER-FOR-004, PER-FOR-009 · **Expérience+ :** D09 ; cartes 027, 031–034  
**Source utilisateur :** F045/SRC027 ; FR-02.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
La réponse dépend du type d’accompagnement et du statut ; les services ne sont pas interchangeables.

#### Exemple à reproduire
> « Je cherche un emploi et je ne sais pas vers qui aller. »

#### Comportement attendu
Montrer offres et métiers pertinents, puis proposer France Travail ou APEC/Cap emploi seulement si la demande correspond à leurs missions.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir offres et métiers ». **Service(s) :** France Travail / APEC / Cap emploi.  
**URL source :** [France Travail](https://candidat.francetravail.fr/offres/recherche) · [APEC](https://www.apec.fr/candidat/accompagnement.html) · [Cap emploi](https://www.capemploi.info/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-020 — Reprendre une activité après arrêt

**Scénario :** O24 · **Personas de test :** PER-FOR-010, PER-FOR-009 · **Expérience+ :** D31, D33, D34, D50  
**Source utilisateur :** Pas de preuve forum spécifique retrouvée.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
La situation nécessite un interlocuteur spécialisé plutôt qu’une recommandation de métier.

#### Exemple à reproduire
> « Je reprends après un arrêt, vers qui me tourner ? »

#### Comportement attendu
Orienter vers informations officielles de santé au travail et de préreprise sans demander de données de santé ni évaluer l’aptitude.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer métiers uniquement si demandé ». **Service(s) :** Assurance maladie / santé au travail.  
**URL source :** [Assurance maladie](https://www.ameli.fr/entreprise/vos-salaries/retour-emploi) · [santé au travail](https://travail-emploi.gouv.fr/sante-au-travail).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-021 — Retraite progressive et temps partiel

**Scénario :** O25 · **Personas de test :** PER-FOR-009, PER-FOR-010 · **Expérience+ :** D17–D20  
**Source utilisateur :** Non confirmé comme priorité du corpus forums.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
MaCarrière ne calcule aucun droit individuel à pension.

#### Exemple à reproduire
> « Est-il possible de travailler moins avant la retraite ? »

#### Comportement attendu
Présenter sommairement les possibilités, renvoyer aux simulateurs officiels ; ne pas collecter la carrière détaillée.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Explorer activités éventuelles ». **Service(s) :** Info Retraite.  
**URL source :** [Info Retraite](https://www.info-retraite.fr/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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

### US-ORCH-023 — Se former en travaillant

**Scénario :** O27 · **Personas de test :** PER-FOR-004, PER-FOR-006, PER-FOR-007, PER-FOR-009 · **Expérience+ :** D14, D42 ; carte 098  
**Source utilisateur :** FR-07.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
Les données de session ne suffisent pas à prouver une formation prise en charge par l’employeur.

#### Exemple à reproduire
> « Comment apprendre sans quitter mon emploi ? »

#### Comportement attendu
Montrer compétences/certifications/formations disponibles ; orienter vers les informations sur plan de développement et AFEST, sans garantie de financement.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Voir certifications ». **Service(s) :** Plan de compétences / AFEST.  
**URL source :** [Plan de compétences](https://travail-emploi.gouv.fr/le-plan-de-developpement-des-competences) · [AFEST](https://travail-emploi.gouv.fr/rapport-lexperimentation-relative-aux-actions-de-formation-en-situation-de-travail-afest).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

### US-ORCH-024 — Comparer formation longue et alternative

**Scénario :** O28 · **Personas de test :** PER-FOR-001, PER-FOR-004, PER-FOR-008 · **Expérience+ :** D10–D14  
**Source utilisateur :** F043/A05 ; F047/SRC023.

#### User Story
**ETQ** usager ou usagère qui exprime une question sur son parcours, **je veux** obtenir l’information pertinente et accéder au bon service, **afin de** savoir où poursuivre ma démarche sans être soumis à un diagnostic.

#### Constat
La durée et le coût peuvent ne pas être disponibles ou comparables.

#### Exemple à reproduire
> « Trois ans de formation, est-ce nécessaire ? »

#### Comportement attendu
Afficher uniquement certifications, blocs, sessions et durées quand disponibles et vérifiés ; proposer VAE/CEP ; ne pas inventer équivalence ou coût.

#### Passerelle(s) et lien(s)
**CTA MaCarrière :** « Comparer voies d’accès ». **Service(s) :** France VAE / CEP.  
**URL source :** [France VAE](https://vae.gouv.fr/) · [CEP](https://mon-cep.org/).

#### Critères d'acceptation
- **Étant donné** la question de l’exemple, **quand** MaCarrière répond, **alors** la réponse traite l’intention et ne se limite pas à une suggestion générique de formation.
- **Étant donné** que des données métiers ou certifications pertinentes sont disponibles, **alors** elles sont présentées avec leur source et leurs limites, sans créer de chiffres ou de conditions d’accès.
- **Étant donné** que la démarche relève d’un service tiers, **alors** un lien explicite vers ce service est proposé, avec une explication de son rôle.
- **Étant donné** que la question ne justifie pas une passerelle spécifique, **alors** MaCarrière ne multiplie pas les liens non pertinents.
- **Dans tous les cas**, aucun score, diagnostic, prescription ou décision d’éligibilité n’est produit.

#### À joindre à la recette
Capture de la question et de la réponse ; référence du GET métier/certification le cas échéant ; capture du CTA ; contrôle du lien et de la destination ; décision sur l’opportunité de présenter cette passerelle dans le MVP.

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


## 8. Préconisations de recette transversales

- **US-ORCH-T01 — Pas de passerelle systématique :** sur une question factuelle directement couverte par la fiche métier, ne pas afficher automatiquement CEP, CPF et VAE.
- **US-ORCH-T02 — Source et lien :** chaque renvoi affiche un libellé compréhensible et un lien explicite ; les pages de destination doivent être vérifiées avant mise en production.
- **US-ORCH-T03 — Pas d’inférence persona :** ne pas déclencher une ressource « senior », handicap ou aidant du seul fait d’un métier, d’un âge présumé ou d’une catégorie statistique.
- **US-ORCH-T04 — Pas de diagnostic :** toute question sur une difficulté physique ou psychologique déclenche au besoin une orientation vers un acteur compétent, jamais un bilan de santé, score ou conclusion d’aptitude.
- **US-ORCH-T05 — Aucune promesse :** les réponses sur CPF, financement, salaire maintenu, VAE, MRS, POE ou immersion restent conditionnelles et renvoient aux services compétents.
- **US-ORCH-T06 — Données API :** aucune réponse chiffrée ne doit être inventée ; une réponse hors couverture des GET doit indiquer les limites et, si possible, proposer une passerelle.
- **US-ORCH-T07 — Accessibilité :** lien et CTA discernables au clavier, intitulés explicites, pas de panneau latéral seul pour porter une sortie essentielle.
- **US-ORCH-T08 — Continuité :** permettre de revenir à la fiche métier ou au projet en cours après une proposition de lien externe ; ne pas imposer un tunnel.

## 9. Statut des URLs et des sources

Les adresses ci-dessus ont été reprises du cahier Expérience+ (55 pages) et de destinations institutionnelles qu’il mentionne. Elles sont des **liens documentaires**, non une garantie de disponibilité ou de conformité juridique au 11/11/2026. Contrôle final requis : redirections, page active, périmètre du dispositif, public concerné, conditions, date de mise à jour, choix du libellé du CTA et validation métier.

**Traçabilité forum :** les références Fxxx/Rxx/SRCxxx désignent les fiches du corpus consolidé. Une question scénarisée n’est pas un verbatim littéral. Les 26 US détaillées et les 8 US transversales sont des propositions de spécifications, pas des décisions MVP déjà prises.
