# Des noms à l'écran, des codes dans les traitements

Correction du2 novembre2026 à la demande produit : présenter les libellés disponibles et expliquer les données sans imposer les noms des référentiels au grand public. Les31 fonctionnalités sont maintenues.

## Ce que fournit réellement l'API

| Objet | Champs observés dans les réponses | Exemple de nom affichable |
|---|---|---|
| Métier | rome_code / rome_libelle | Pose et restauration de couvertures |
| Domaine professionnel | domaine_code / domaine_libelle | Second œuvre |
| Compétence | competence_code / competence_libelle | Poser des panneaux solaires |
| Conditions de travail | contexte_travail_codes[] / contexte_travail_libelles[] | En grande hauteur |
| Groupe de métiers pour les salaires | fap_225_code / fap_225_libelle | Couvreurs ; Ouvriers non qualifiés du gros œuvre du bâtiment |
| Groupe de métiers pour les recrutements | fap_228_code / fap_228_libelle | Couvreurs |
| Groupe de métiers pour la prospective | fap_87_code / fap_87_libelle | Ouvriers qualifiés du gros œuvre du bâtiment |
| Secteur économique | secteur_naf38_code / secteur_naf38_libelle | Construction |
| Thème de formation | formacode_code / formacode_libelle | Couverture |
| Territoire d'un indicateur | territoire_code / territoire_libelle | Hérault |

Ces couples sont observés dans les JSON du dossier. PREUVES_LIBELLES.json conserve le chemin de preuve et les champs de chaque nom utilisé. Cela ne garantit pas qu'un champ sera renseigné dans toutes les réponses futures. Les sources normatives restent le contrat et le Swagger ; cette vérification n'est pas un nouveau test HTTP.

## Règle d'interface

- Le nom fourni est le libellé principal. Les codes servent aux paramètres et aux relations, sans devenir des intitulés pour l'utilisateur.
- Les tableaux de résultats n'affichent plus de colonne réservée aux identifiants. Les en-têtes du comparateur portent les noms des deux métiers.
- Les groupes de statistiques conservent leur nom, le nombre de métiers si disponible, la population, le lieu et la période. Retirer un sigle ne permet pas de transformer une donnée familiale en donnée du seul métier.
- « Groupe de métiers », « secteur d'activité », « thème de formation » et « territoire disponible » sont des explications de présentation. Elles ne créent aucun nouveau champ métier ni nouvelle relation API.
- Les références techniques sont facultatives et séparées dans Sources ; elles restent disponibles dans les données embarquées et les preuves.
- Aucun libellé manquant n'est deviné. Dans la future intégration, consulter le GET de référence prévu si son identifiant le permet ; sinon afficher « Nom non renseigné » dans son contexte, sans fabriquer de correspondance.

## Modifications locales

construire.py collecte les couples code/nom réellement observés et les embarque dans la maquette. Les champs métier de famille et de nomenclature sont prioritaires sur les simples codes de situations observées. libelles_publics.js adapte uniquement les textes de présentation ; les valeurs de filtres, routes, identifiants et montants ne sont pas réécrits. Les sommes, périodes, populations et valeurs sources sont conservées.

L'écran des thèmes de formation présente désormais « Couverture », reçu dans le JSON /formacodes, plutôt qu'une liste de numéros dont les noms n'étaient pas affichés. La sélection de certifications présentée reste un exemple : aucune requête filtrée n'est déclarée validée.

La recette comporte79 vérifications par format : les58 contrôles de navigation/reflow existants et21 contrôles de vocabulaire, un par vue. Elle ne remplace ni un test utilisateur de compréhension ni une recette RGAA. Les documents de référence et les JSON sources sont inchangés.
