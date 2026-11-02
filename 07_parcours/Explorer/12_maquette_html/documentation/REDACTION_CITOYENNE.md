# Rédaction destinée aux salariés et aux citoyens

Instruction produit du2 novembre2026 : ne conserver dans les écrans que ce qui aide la personne à comprendre, explorer et choisir. Les noms internes, versions, conventions de conception, tests et détails d'intégration n'ont pas leur place dans ce parcours. Les sources, dates, populations et limites nécessaires à la bonne lecture restent accessibles. Le périmètre fonctionnel E01–E31 est conservé.

## Ce qui change dans le HTML

- Retrait du bandeau technique, des mentions de version et de maquette, des références aux campagnes, aux schémas, au fournisseur, aux étapes futures de réalisation et aux champs d'intégration. Retrait des panneaux de références techniques dans Sources.
- Questions formulées du point de vue de la personne : « Combien peut-on gagner ? », « Les employeurs cherchent-ils à recruter ? », « Où regarder les possibilités d'emploi ? ».
- Définition du salaire médian au voisinage du montant ; temps complet, salaire net, mois/année, groupe de huit métiers, lieu et année maintenus.
- Distinction explicite entre projets de recrutement, publications d'offres et emplois garantis. Aucun classement personnel ajouté.
- Explication des parts, des populations suivies après formation, des parcours observés et des estimations2030. Pas de conversion en faux effectifs sur100, de score ou de calcul supplémentaire.
- Le signe d'une évolution et d'un écart est expliqué sans recomposer les valeurs. Les changements entre régions restent mentionnés dans la prospective.
- Les données indisponibles donnent un message compréhensible et une possibilité de poursuivre : changer ses choix ou consulter une fiche. L'absence d'information n'est pas présentée comme l'absence de métier ou d'emploi.
- Les parcours professionnels conservent les deux sens de lecture et proposent les tranches d'âge réellement présentes dans les JSON. Aucun filtre sans réponse correspondante n'est rempli par une autre réponse.
- Les sessions ont des dates en français ; les places disponibles ne sont pas promises. Les deux populations d'insertion présentées ne sont pas comparées comme si elles étaient équivalentes.
- Les29mesures restent décrites dans Sources avec une explication de leur usage et de leurs limites, sans noms de champs techniques.

## Contrôle des faits

Les valeurs de référence restent celles des JSON locaux. La page présente un repère mensuel de1690€ pour le groupe de huit métiers de l'Hérault en2023,26projets pour les Couvreurs du bassin de Montpellier en2026 et des perspectives2019–2030 par groupes séparés. Elle ne présente pas ces observations comme des chiffres du jour ou comme des résultats individualisés.

Les sources originales et leur nom complet restent dans les données embarquées. Dans les citations visibles, les termes d'accès technique sont retirés sans changer l'organisme source. Les [preuves de correspondance code/libellé](../preuves/PREUVES_LIBELLES.json) sont conservées et les sources de référence ne sont pas modifiées.

Une erreur de présentation a également été corrigée : la catégorie de compétence provient de categorie_competence_libelle, réellement présent dans le JSON, et non d'un nom de champ supposé.

## Organisation des fichiers

Les écrans et les textes actuels sont dans [interface_citoyenne.js](../sources/interface_citoyenne.js). Le [gabarit](../sources/modele.html) contient l'enveloppe et les styles ; l'ancien script a été retiré du gabarit actif et conservé en archive. Le [constructeur](../sources/construire.py) assemble le fichier autonome [index.html](../index.html) et le document de contrôle mobile. Les anciennes adaptations et notes sont dans [les archives](../archives/README.md) ; elles ne participent plus à l'assemblage.

Les contrôles navigateur portent sur les21vues, l'absence de vocabulaire interne même dans les détails repliés, les noms publics, le reflow, les interactions, la présence des sources et plusieurs invariants statistiques. Ils ne prouvent pas à eux seuls une compréhension universelle. Aucun test avec de vrais utilisateurs ni audit complet RGAA n'est revendiqué. Une validation de compréhension avec des personnes aux niveaux de lecture et de familiarité numérique variés reste nécessaire ; aucun score de lisibilité artificiel ne remplace ces échanges.
