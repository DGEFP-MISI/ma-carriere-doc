# Maquette HTML Explorer V2

**Version de présentation destinée aux citoyens :** les mentions internes ont été retirées des écrans et les chiffres sont expliqués au voisinage des valeurs. Les sources, dates, lieux et limites utiles restent visibles. La rédaction actuelle est portée par interface_citoyenne.js ; voir [la règle éditoriale](REDACTION_CITOYENNE.md). Les notes précédentes ci-dessous décrivent aussi des états antérieurs ; les fichiers de contrôle actualisés font foi pour la version présente.

**Affichage grand public mis à jour :** noms à la place des codes et référentiels, précisions statistiques conservées. Voir [la règle et les preuves](AFFICHAGE_GRAND_PUBLIC.md). Les rapports de contrôle actualisés comportent79 vérifications réussies par format, dont21 contrôles de vocabulaire.

Ouvrir **[index.html](index.html)** dans Edge, Firefox ou Chrome par double-clic. Aucune installation, aucun serveur, aucune connexion à l'API. Le fichier est autonome : CSS, interactions et extraits JSON sont embarqués. Il peut être copié seul pour une revue.

Entrées utiles : [F1610](index.html#essentiel), [recherche](index.html#recherche), [compétences/contextes](index.html#guide), [certification](index.html#certification), [comparateur F1610/F1613](index.html#comparateur), [Mes pistes](index.html#pistes), [sources](index.html#sources).

La maquette reprend les21 vues de conception, dont les neuf sections métier. Les31 fonctionnalités restent la cible ; tous leurs traitements ne constituent pas une application opérationnelle dans cette démonstration. Les29 mesures et leurs définitions restent consultables dans Sources.

## Interactions disponibles

- Navigation entre vues, sommaire mobile, accordéons, alternatives tabulaires aux barres.
- Recherche locale parmi les métiers des JSON embarqués, et ouverture de leurs descriptions disponibles.
- Ajout/retrait de pistes, sans doublon ; mémoire de consultation uniquement, effacée au rechargement. Trois pistes est une convention de démonstration.
- Sélection des deux compétences R23 ; modes au moins une / toutes avec les réponses effectivement observées. Une combinaison non couverte affiche un message explicite, sans réponse inventée.
- Contextes avec trois choix exclusifs : indifférent / rechercher / éviter ; les choix sont conservés pendant la navigation.
- Deux intentions de certification ; listes observées de sessions à venir et en cours ; blocs RNCP dépliables avec les textes reçus.
- Quatre lectures du comparateur illustré F1610/F1613. Les données manquantes du second métier sont indiquées, sans copie des chiffres du premier.
- Dialogue de territoire : seul le jeu Montpellier est disponible. Le lieu mesuré reste précisé pour chaque indicateur.

La recherche Certification/Domaine ouvre les fiches d'exemple et le précise ; elle ne représente pas une requête serveur filtrée. Les changements de région/âge, les autres familles et certains panneaux détaillés restent des accès de démonstration explicites. Le comparateur illustre les deux métiers nommés à l'écran ; il n'exécute pas la comparaison de toute paire sélectionnée. Aucun taux, rapprochement ou score n'est calculé pour compléter une absence.

## Visuel et accessibilité

Mise en page inspirée des principes DSFR, palette sobre, police Marianne si installée et Arial en repli local ; aucune dépendance distante. Il ne s'agit pas d'un import de la distribution officielle DSFR, ni d'une certification RGAA. Les assets officiels de marque et le logo d'attribution RCO restent à intégrer à la future application ; aucune image officielle n'est reconstituée ici.

Lien d'évitement, titres, labels, commandes natives, focus visible, annonces de statut, tableaux avec en-têtes, figures avec lecture tabulaire et réduction du mouvement sont prévus. Les longues colonnes deviennent des fiches libellées sur mobile.

## Vérifications du 2 novembre 2026

Contrôles réellement exécutés dans Edge headless sur fichiers locaux : **58/58 sur ordinateur**, viewport1410×1005, et **58/58 à320×844**, dans un document srcdoc de largeur imposée. Les21 vues sont rendues, sans débordement horizontal détecté. Contrôles d'ajout/retrait de pistes, recherche locale, modes R23, absence de réponse inventée sur combinaison non couverte, intentions/session/onglets, dialogue,29mesures et absence d'erreur JavaScript. Aucune ressource HTTP chargée par le document.

Un débordement des longs codes techniques de Sources à320px a été corrigé avant la dernière passe. Rapports : [CONTROLE_DESKTOP.json](CONTROLE_DESKTOP.json) et [CONTROLE_MOBILE.json](CONTROLE_MOBILE.json). Aperçus : [ordinateur](apercu-desktop.png) et [mobile320](apercu-mobile.png). Ce dernier présente le document320px à gauche d'une capture plus large de contrôle.

Ces résultats ne sont pas des tests HTTP de l'API, des tests utilisateurs, ni une recette complète au lecteur d'écran. Ils ne clôturent pas les questions RCO existantes. Les données conservent la date et les limites de leurs preuves ; la maquette ne promet ni disponibilité de formation ni actualisation en temps réel.

## Sources et maintenance

Sources :11_ux_ui/ECRANS_STRUCTURE.json, MATRICE_VISUALISATIONS.csv, catalogue observé /mesures, JSON F1610/compétences, campagnes R23/R24, certification/blocs et sessions. Les chemins exacts de construction sont dans construire.py. Aucune source contractuelle ou JSON de référence n'est modifiée.

Le source visuel est modele.html. Après modification, lancer construire.py pour régénérer index.html et le document de contrôle mobile. Ce script utilise seulement la bibliothèque standard Python. verifier_navigateur.js s'exécute uniquement avec le paramètre verification=1 ; l'extraction des rapports Edge est faite par extraire_controle.py. ASSEMBLAGE.json conserve l'empreinte du HTML produit.
