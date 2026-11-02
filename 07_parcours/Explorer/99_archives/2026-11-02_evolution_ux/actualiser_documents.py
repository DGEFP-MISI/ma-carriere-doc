"""Synchronise les recommandations UX, sans modifier les appels API ni les IDs."""
import csv
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
EXPLORER=HERE.parents[1]
marker='## Évolution UX ciblée — 2 novembre 2026'
note='''
## Évolution UX ciblée — 2 novembre 2026

La maquette existante est conservée comme socle de restitution des données. Son point d'entrée est désormais la recherche, qui reste disponible dans les fiches avec ses trois modes et sa saisie. La première lecture du métier suit quatre questions : activités, opportunités, salaires et autres pistes ; les contenus détaillés, dont mobilités et prospective2030, restent accessibles ensuite. Les filtres savoir-faire/contextes sont simultanés, sans étapes numérotées. Le comparateur porte sur les deux métiers effectivement choisis ; le lieu est sélectionné parmi les territoires observés, sans transposer les chiffres d'un autre lieu.

Mes pistes utilise une session d'onglet et un format de reprise portable dans la maquette. Il s'agit d'une préparation opérationnelle, pas d'un arbitrage définitif de stockage de production. L'utilisatrice a demandé d'avancer sans les deux autres parcours, à raccorder plus tard : aucune liaison vers un produit absent n'est simulée. D08/D10 restent ouverts sur les modalités de production. Aucune des31 fonctionnalités n'est retirée et aucun nouveau GET n'est ajouté.

Voir [l'évolution appliquée et ses limites](12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md) et [les contrôles actuels](12_maquette_html/README.md). Les nombres de contrôles cités dans les sections historiques correspondent à leurs étapes respectives. La recherche reste alimentée par les JSON observés ; ces contrôles locaux ne prouvent pas une recherche HTTP réelle, un partage interapplications, ni une conformité RGAA.
'''
for p in EXPLORER.glob('[0-9][0-9]_*.md'):
    text=p.read_text(encoding='utf-8-sig')
    if marker in text:raise SystemExit('Déjà actualisé : '+p.name)
    first,rest=text.split('\n',1)
    text=first+'\n'+note+'\n'+rest
    text=text.replace('mémoire de consultation uniquement, effacée au rechargement','session d’onglet dans la maquette ; stockage final à arbitrer')
    text=text.replace('Choisir mémoire ou stockage de session','Confirmer le stockage de session proposé pour le prototype et choisir la stratégie de production')
    if p.name.startswith('05_'):
        text=text.replace('B -->|Secteur ROME|','B -->|Domaine professionnel|')
        anchor='    D --> K["Sélection d\'un code Certif Info"]'
        text=text.replace(anchor,'    J --> J1["Quatre questions : activités, opportunités, salaires, autres pistes"]\n    J1 --> J2["Détails accessibles : mobilités, prospective2030, formations, conditions"]\n    J --> A\n'+anchor)
    if p.name.startswith('07_'):
        text+='\nPour poursuivre, lire aussi les sources du HTML et EVOLUTION_STRUCTURE_UX.md. Conserver la séparation des vues et des adaptateurs ; remplacer la source locale par les réponses HTTP réelles lors de l’intégration autorisée. Ne pas présenter le catalogue local de domaines comme un JSON /domaines capturé. Ne pas déclarer les autres parcours reliés avant leur intégration réelle.\n'
    p.write_text(text,encoding='utf-8')

path=EXPLORER/'03_TABLE_CONCEPTION.csv'
with path.open(encoding='utf-8-sig',newline='') as stream:
    reader=csv.DictReader(stream,delimiter=';');fields=reader.fieldnames;rows=list(reader)
changes={
 'E01':'Entrée par recherche persistante, mode et saisie conservés ; ouverture après sélection explicite d’un métier.',
 'E02':'Résultats pilotés par la liste de certifications ; la fiche correspond à l’identifiant sélectionné, sans ouvrir un exemple imposé.',
 'E03':'Mode Domaine dans la barre persistante ; adaptateur arborescent selon contrat, réponse réelle à collecter ; liste locale issue des domaines observés sans faux effectif.',
 'E04':'Ouvrir le domaine effectivement choisi et les métiers de ce domaine ; conserver recherche et lieu au retour.',
 'E05':'Première lecture par quatre questions ; mobilités, prospective2030, formations et conditions détaillées restent accessibles.',
 'E09':'Choix territorial identifié dans un sélecteur filtrable ; garder le lieu demandé et annoncer le lieu mesuré ; ne pas copier les chiffres de Montpellier.',
 'E13':'Filtres de savoir-faire accessibles simultanément, sans numérotation d’étapes.',
 'E14':'Mode au moins une/toutes conservé avec les autres filtres ; annuler les réponses de recherche périmées.',
 'E15':'Conditions accessibles simultanément aux savoir-faire ; trois choix exclusifs par contexte.',
 'E16':'Conserver le domaine et les choix avec/sans contexte ; aucune réponse d’une autre combinaison utilisée comme résultat.',
 'E17':'Ouvrir la certification sélectionnée ; séparer champs réellement reçus, absence de détail et données d’une autre certification.',
 'E27':'Session d’onglet et format portable de reprise préparés ; raccordement aux autres parcours reporté à leur disponibilité selon instruction utilisateur, sans supprimer la fonction ; D08/D10 production restent ouverts.',
 'E28':'Choix libre de deux métiers depuis résultats, fiches ou pistes ; inversion ; comparaison limitée aux données des métiers choisis ; tous les détails restent accessibles.'}
for row in rows:
    if row['Parcours_ID'] in changes:
        row['Composant_UI']+=' ; Évolution UX ciblée : '+changes[row['Parcours_ID']]
        row['Critere_acceptation']+=' ; Vérifier les scénarios de navigation correspondants dans la recette UX, sans déduire un test HTTP d’un contrôle du prototype.'
assert len(rows)==31
with path.open('w',encoding='utf-8-sig',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter=';',lineterminator='\r\n');writer.writeheader();writer.writerows(rows)

p=EXPLORER/'11_ux_ui/CONCEPTION_UX_UI.md'
text=p.read_text(encoding='utf-8-sig');first,rest=text.split('\n',1)
text=first+'\n\n**Évolution courante :** la navigation de première lecture utilise désormais quatre questions et une recherche persistante ; les neuf vues détaillées décrites historiquement restent accessibles. Voir [la structure mise à jour](../12_maquette_html/documentation/EVOLUTION_STRUCTURE_UX.md). Les premiers visuels Figma/SVG ne sont pas annoncés mis à jour à distance.\n'+rest
p.write_text(text,encoding='utf-8')
print('Livrables et 31 lignes synchronisés, signatures API conservées.')
