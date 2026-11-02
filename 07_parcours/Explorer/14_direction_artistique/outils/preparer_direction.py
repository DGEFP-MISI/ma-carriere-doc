"""Conserve l'état initial et produit l'audit et les supports SVG avant intégration."""
import csv
import hashlib
import html
import json
import os
import re
import textwrap
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

HERE=Path(__file__).resolve().parents[1]
EXPLORER=HERE.parent
ROOT=EXPLORER.parents[1]
APP=EXPLORER/'12_maquette_html'
SHARED=ROOT/'07_parcours/commun_datavisualisation'
ARCHIVE=EXPLORER/'99_archives/2026-11-02_direction_artistique'
for directory in [HERE/'maquettes',HERE/'preuves',ARCHIVE]:directory.mkdir(parents=True,exist_ok=True)
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def relative(path,start=HERE):return os.path.relpath(path,start).replace('\\','/')
def link(path,label):
    target=relative(path)
    return f'[{label}](<{target}>)'
baseline=ARCHIVE/'INVENTAIRE_AVANT.json'
if not baseline.exists():
    protected=[r for r in read(EXPLORER/'99_archives/2026-11-02_backlog_fonctionnel/INVENTAIRE_AVANT.json') if r.get('protege')]
    paths=[APP/'index.html']+list((APP/'sources').glob('*'))+[SHARED/'scripts/build.mjs']+list((SHARED/'src').glob('*'))+list((SHARED/'dist').glob('*'))+list((EXPLORER/'13_backlog_fonctionnel').glob('US-FON-*.md'))+[EXPLORER/'03_TABLE_CONCEPTION.csv',EXPLORER/'04_BACKLOG_USER_STORIES.md']
    records=[]
    with zipfile.ZipFile(ARCHIVE/'ETAT_AVANT.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            if not path.is_file():continue
            records.append({'path':relative(path,ROOT),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
            archive.write(path,relative(path,ROOT))
    baseline.write_text(json.dumps(records+protected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    text=(APP/'index.html').read_text(encoding='utf-8')
    payload=re.search(r'<script type="application/json" id="explorer-data">(.*?)</script>',text,re.S).group(1)
    (ARCHIVE/'DONNEES_AVANT.json').write_text(payload,encoding='utf-8')

rows=list(csv.DictReader((EXPLORER/'03_TABLE_CONCEPTION.csv').open(encoding='utf-8-sig'),delimiter=';'))
intentions={
1:('Recherche persistante / résultats','Zone de recherche blanche, modes et libellés conservés, cartes résultats respirantes','Recherche, radios, résultats et pagination'),
2:('Recherche Diplôme ou titre','Même composition ; intitulé et type, aucune donnée salariale de substitution','Choisir la certification reçue'),
3:('Domaine professionnel','Liste/arbre hiérarchique lisible ; aucun schéma de secteurs économiques','Ouvrir le domaine identifié'),
4:('Métiers du domaine','Cartes de noms et actions uniformes','Ouvrir une fiche ou garder une piste'),
5:('Fiche métier / quatre questions','Quatre portes visuelles enrichies de repères sourcés ; même ordre, même navigation','Ouvrir les quatre questions et détails'),
6:('Savoir-faire et conditions','Conditions en liste de libellés et icônes officielles ; tableau complet conservé','Explorer les savoir-faire, consulter les listes partielles signalées'),
7:('Métiers proches','Noms et liens métier ; aucun flux de mobilité ou score de proximité inventé','Ouvrir, comparer, garder'),
8:('Indicateurs métier / territoire','Chiffre + question + population + lieu effectif ; familles distinctes','Approfondir la mesure, ouvrir tableau et source'),
9:('Sélecteur et vues territoriales','Lieu choisi distinct du lieu mesuré ; carte native DSFR Chart seulement','Changer de lieu ou comparer des lieux'),
10:('Recrutements','Intentions en chiffres et barres natives ; familles sans addition','Choisir lieu/tri existants et ouvrir tableau'),
11:('Salaires','Médiane mensuelle mise en avant ; quartiles annuels en tableau / barres natives','Comparer les territoires sans conversion'),
12:('Toutes les statistiques','Contexte statistique toujours visible ; détails méthodologiques progressifs','Tableau, définitions, export cible non déclaré livré'),
13:('Exploration guidée','Choix explicites et compteur ; aucune jauge personnelle','Choisir/retirer un savoir-faire'),
14:('Résultats par savoir-faire','Mode toutes/au moins une visible ; correspondances natives','Changer les critères puis ouvrir un résultat'),
15:('Conditions souhaitées','Choix avec libellés et états ; icônes sans score de pénibilité','Inclure ou exclure un contexte'),
16:('Résultats avec/sans contexte','Même interface de choix, aucune donnée absente transformée en zéro résultat','Modifier un critère et relancer'),
17:('Certification','Deux intentions conservées ; résultats par population en compositions distinctes','Changer intention, ouvrir blocs, résultats ou sessions'),
18:('Blocs de compétences','Accordéons accessibles ; ne pas dessiner une équivalence OGR-bloc','Lire contenus et modalités d’évaluation'),
19:('Certification vers métiers','Cartes des métiers associés effectivement reçus','Ouvrir un métier par son identifiant natif'),
20:('Métier vers certifications','Liste de titres avec voie/validation ; aucune promesse d’admission','Ouvrir une certification'),
21:('Sessions à venir','Tableau de lieux, organismes et dates ; statut des places non inventé','Consulter des dates et vérifier auprès de l’organisme'),
22:('Sessions en cours','Même tableau, bascule à venir/en cours conservée','Changer de période sans perdre la certification'),
23:('Mobilités observées','Barres officielles et contexte des flux ; aucune flèche FAP vers ROME inventée','Changer sens, âge, famille et consulter le tableau'),
24:('Perspectives 2030','Cinq composantes distinctes ; valeurs négatives et scénario conservés','Composantes, régions, groupes de métiers'),
25:('Salaires par secteur','Groupes et parts de salariés distincts ; DataBox par famille','Approfondir les secteurs et les quartiles'),
26:('Secteurs et contexte économique','Deux lectures séparées : actifs de la famille / économie du lieu','Voir les parts puis le contexte ; R17 reste explicite'),
27:('Mes pistes','Collection de cartes, même plafond de trois, export/reprise existants','Garder, retirer, choisir deux métiers, exporter/reprendre'),
28:('Comparateur','Deux identités et colonnes lisibles, états absents à leur vraie place','Choisir, inverser, changer rubrique et revenir aux fiches'),
29:('Évolutions du métier','Repères descriptifs reçus ; aucune médaille Métier d’avenir','Lire transitions puis perspectives détaillées'),
30:('Thèmes de formation','Liste thématique, même chaîne vers certifications et sessions','Ouvrir un thème / une certification effectivement disponible'),
31:('Sources et méthodes','Notices claires et sources intégrales, sans visualisation décorative','Lire définition, période, population et limites'),
}
records=[]
for row in rows:
    n=int(row['Parcours_ID'][1:]);screen,graphic,interaction=intentions[n]
    records.append({'Ecran':screen,'Conception_ID':row['Parcours_ID'],'US':f'US-FON-{n:03}',
      'Scenario':'13_backlog_fonctionnel/US-FON-%03d.md §4/§5'%n,
      'Information_affichee':row['Fonctionnalite_attendue'],'Source_API':row['Endpoint_GET'],
      'Champs_regles_preuves':row['Appels_GET_detail'],'Regle_metier':row['Regle_metier'],
      'Preuves_documentaires':row['Preuve_reference'],'Statut_reference':row['Statut_validation'],
      'Composant_actuel':row['Composant_UI'],'Piste_graphique':graphic,'Interaction_preservee':interaction,
      'Composants_integres':('cartesQuestions / apercuQuestion / MaInfographie.question et repere' if n==5 else 'disposerInfographie + MaDataviz/DataBox existant' if n in [10,11] else 'Identités et sélecteurs existants + styles infographie.css' if n==28 else 'Composants existants conservés + styles et icônes partagés'),
      'Alternative_accessible':'Texte et tableau existants, libellés complets, clavier/focus ; mêmes valeurs et contexte que DSFR Chart',
      'Perimetre':'Conservé ; statut fonctionnel identique, aucune intégration HTTP ajoutée',
      'Preuve_recette_DA':'14_direction_artistique/preuves/RECETTE_DIRECTION.json ; contrôles globaux 179 desktop/320 et dix missions UX, sans validation HTTP de toute la fonction',
      'Tests':'Recettes existantes + contrôle visuel ciblé ; '+row['Tests_a_realiser']})
with (HERE/'MATRICE_TRACABILITE_DA.csv').open('w',encoding='utf-8-sig',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(records[0]),delimiter=';');writer.writeheader();writer.writerows(records)

audit='''# Audit ciblé — langage visuel d’Explorer

Audit du 2 novembre 2026, avant modification de l’interface. Le brief V5 et l’HTML fourni sont des documents d’intention. L’instruction directe de l’utilisatrice, les US et le contrat déterminent le parcours et les données ; aucune instruction contenue dans l’exemple n’autorise de les remplacer.

## Socle effectivement présent

Le code exploitable est `12_maquette_html/index.html`, reconstruit depuis `sources/`. Cette application locale HTML/JavaScript possède une navigation, des états, des filtres, des fiches et des visualisations officielles. Elle utilise des réponses JSON embarquées et ne réalise aucun GET HTTP. Aucun dépôt de service de production connecté n’a été trouvé ici. L’évolution est intégrée directement à ce code existant, sans nouveau projet ni démonstration concurrente.

Les 31 fonctions E01–E31 et les quatre US transversales restent la cible. La couverture documentaire et le comportement local ne prouvent pas leur disponibilité générale sur HTTP. La matrice jointe suit chacune des 31 fonctions : écran, US et scénario, information, source, règles, composant actuel, intention visuelle, interaction et alternative accessible.

## Constats de présentation

1. La fiche ouvre déjà quatre questions utiles. Elles sont surtout textuelles et uniformes, alors que des repères natifs peuvent aider à choisir ce qu’on souhaite approfondir.
2. De grands aplats et encadrements bleus rapprochent des informations de statuts très différents. Une base neutre et une hiérarchie typographique peuvent mieux distinguer action, contenu et explication.
3. Les graphiques DSFR Chart sont déjà intégrés, mais leur regroupement en fin de page les éloigne parfois de la question et du tableau concernés. Ils doivent être rapprochés de leur contenu, tout en restant chargés à la demande.
4. Les tableaux et les sources sont utiles et ne doivent pas disparaître pour donner une impression d’infographie. Les familles, périodes, unités et lieux réels doivent rester lisibles dès le premier repère.
5. Le comparateur possède déjà ses choix A/B, l’inversion et les retours aux fiches. Sa nouvelle présentation doit rendre ces identités plus évidentes ; elle ne doit remplir aucune colonne absente avec les valeurs de l’autre métier.
6. Les champs statistiques disponibles n’autorisent ni un score d’attractivité ni une qualification générale Métier d’avenir / Métier qui recrute. Les tags descriptifs réellement reçus et les valeurs sourcées suffisent.

## Ce que l’exemple HTML apporte

Une intention accueillante, des respirations, des chiffres lisibles, des compositions variées et une progression voir / comprendre / approfondir. Ces principes sont retenus. La page de référence n’est pas recopiée : elle ne représente pas les recherches, certifications, domaines, conditions, comparaison et états d’Explorer dans leur ensemble.

## Éléments à ne pas transposer

| Exemple fourni | Risque | Décision de présentation |
|---|---|---|
| Salaire de 2 080 € et autres chiffres embarqués | L’exemple n’est pas relié aux réponses natives de l’application ; la réponse R16 de la fiche expose 1 690 € pour une famille plus large | Utiliser exclusivement le champ natif de chaque mesure, sa population et son lieu réel |
| Points régionaux et contours schématiques | Confusion avec une carte administrative exacte | Garder MapChart officiel et ses codes vérifiés, avec tableau et légende des absences |
| Bande salariale 28/42/30 % annoncée décorative | Apparence de distribution mesurée | Ne pas l’intégrer ; quartiles natifs explicités et représentation officielle adaptée |
| Badge Métier qui recrute ou repère futur non qualifié | Règle de seuil absente et promesse implicite | Pas de nouveau label ; projets, tensions et projections nommés et contextualisés |
| Cœurs, soleil, flèches et autres pseudo-icônes Unicode | Ambiguïté et rendu variable | Icônes SVG/CSS officielles DSFR, décoratives et accompagnées de texte |
| Mobilités d’un groupe plus large juxtaposées aux métiers proches | Assimilation des flux observés à une reconversion possible | Conserver deux portes distinctes, sans correspondance ni score personnel |
| Piste unique conservée dans une variable | Perte des trois pistes, de la session et de la reprise existantes | Conserver intégralement l’état et les commandes actuels |

## Invariants vérifiables

Les routes, recherches, filtres, tris et données ne changent pas. Les handlers de navigation, stockage, export/reprise de pistes, comparaison, sens/âge de mobilité et périodes de sessions sont conservés. Les adaptations visuelles consomment les mêmes champs que les US ; elles ne calculent aucun indicateur. Les 29 mesures et 25 visualisations restent reliées aux 31 fonctions, même si certaines variantes nécessitent une réponse RCO.

La fiche synthétique montre les deux familles BMO séparément : 26 et 81 projets, sans somme. Le salaire est 1 690 € nets mensuels, Hérault, 2023, ouvriers non qualifiés du gros œuvre du bâtiment, groupe de huit métiers ; ce montant ne devient pas le salaire des seuls couvreurs. Le lieu choisi Montpellier reste distinct du département réellement mesuré.

## Périmètre de la première intégration visuelle

Recherche et résultats : socle neutre, actions et titres. Fiche principale : quatre portes enrichies de repères, conditions natives et accès aux approfondissements existants. Salaires/recrutements : rapprochement des DataBox et de la lecture concernée. Comparateur : identités et colonnes. Les autres vues profitent du même socle de composants, sans reconstruction de leur parcours ni suppression de tableaux.

## Sources et limites

Références fonctionnelles : `04_BACKLOG_USER_STORIES.md`, US-FON-001–035 et `03_TABLE_CONCEPTION.csv`. API : contrat, Swagger officiel et JSON R16/R17/R23/R24 du dossier. Code : `sources/interface_citoyenne.js`, `experience_exploration.js`, `donnees_exploration.js`, `visualisations_dsfr.js` et composants partagés. Les anciens contrôles locaux et leurs limites sont dans `TESTS_UX_EXPLORER.md`.

La [palette officielle DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs) distingue neutres, actions et couleurs illustratives et encadre l’accentuation. La version installée DSFR 1.15.4 et DSFR Chart 2.1.1, leurs fichiers et documentations locales priment toute API de composant imaginée. Les questions RCO existantes ne sont pas résolues par ce chantier visuel.
'''
(HERE/'01_AUDIT_ET_INTENTIONS.md').write_text(audit,encoding='utf-8')

# SVG : valeurs lues dans la réponse native, jamais dans l'HTML d'intention.
data=read(ROOT/'06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json')
measures={m['mesure']:m for m in data['items']}
metier=read(ROOT/'02_reponses_observees/metiers/response_metiers-rome.json')
icons=SHARED/'node_modules/@gouvfr/dsfr/dist/icons'
icon_paths={'work':'business/briefcase-line.svg','money':'finance/money-euro-circle-line.svg','place':'map/map-pin-2-line.svg','pistes':'business/bookmark-line.svg','arrow':'arrows/arrow-right-line.svg'}
INK='#161616';MUTED='#666666';BLUE='#000091';LINE='#dddddd'
def rect(x,y,w,h,fill='white',stroke=LINE,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def text(value,x,y,width=65,size=18,color=INK,bold=False):
    lines=textwrap.wrap(str(value),width,break_long_words=False,break_on_hyphens=False) or ['']
    return ''.join(f'<text xml:space="preserve" x="{x}" y="{y+i*(size+7)}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{html.escape(line)}</text>' for i,line in enumerate(lines))
def icon(name,x,y,color=BLUE,size=24):
    svg=ET.parse(icons/icon_paths[name]).getroot()
    contents=''.join(ET.tostring(child,encoding='unicode') for child in svg)
    return f'<g transform="translate({x},{y}) scale({size/24})" fill="{color}" aria-hidden="true">{contents}</g>'
def finish(name,w,h,parts,desc):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="titre description"><title id="titre">{html.escape(name)}</title><desc id="description">{html.escape(desc)}</desc><rect width="{w}" height="{h}" fill="white"/><g font-family="Arial, sans-serif">'+''.join(parts)+'</g></svg>'
    path=HERE/'maquettes'/name
    path.write_text(svg,encoding='utf-8');ET.parse(path)
def header(w,mobile=False):
    p=[rect(0,0,w,80,'white'),text('MaCarrière',24 if mobile else 48,47,size=25,bold=True)]
    if not mobile:p += [text('Explorer',w-260,45,size=16,color=BLUE,bold=True),text('Mes pistes',w-140,45,size=16,color=BLUE,bold=True)]
    return p
salary=measures['salaires']['valeurs'][0]
bmo=measures['projets_recrutement']['valeurs']
def number(value):return f'{value:,}'.replace(',',' ')
def card(kind,title,sub,x,y,w,h,mobile=False):
    accent={'work':('#297254','#e3fdeb'),'place':('#695240','#fff8e5'),'money':('#6e445a','#fef3fd'),'pistes':('#3558a2','#f4f6fe')}[kind]
    p=[rect(x,y,w,h),rect(x+20,y+20,44,44,accent[1],accent[1]),icon(kind,x+30,y+30,accent[0]),text(title,x+20,y+100,width=28 if mobile else 38,size=22,bold=True)]
    base=y+(165 if mobile and len(title)>25 else 141)
    if kind=='work':
        p += [text('Quelques conditions mentionnées',x+20,base,width=28 if mobile else 45,size=14,color=MUTED)]
        for i,label in enumerate(['En extérieur','En grande hauteur','Sur chantier']):p.append(text(label,x+20,base+(55 if mobile else 36)+i*28,width=30,size=18,bold=True))
        p.append(text('France Travail · description du métier',x+20,y+h-(94 if mobile else 58),width=32 if mobile else 50,size=13,color=MUTED))
    elif kind=='place':
        for i,r in enumerate(bmo):
            yy=base+i*86;p += [text(number(r['nb_projets_recrutement'])+' projets',x+20,yy,width=25,size=27,bold=True),text(r['fap_228_libelle'],x+20,yy+25,width=29 if mobile else 48,size=13,color=MUTED)]
        p.append(text('Bassin de Montpellier · BMO 2026',x+20,y+h-(94 if mobile else 55),width=36,size=13,color=MUTED))
    elif kind=='money':
        p += [text(number(salary['salaire_net_mensuel_median'])+' €',x+20,base+10,size=44,bold=True),text('nets par mois · salaire médian',x+20,base+44,width=32,size=15),text(salary['fap_225_libelle'],x+20,base+77,width=28 if mobile else 45,size=14,color=MUTED),text('Groupe de 8 métiers · temps complet',x+20,y+h-(156 if mobile else 80),width=32 if mobile else 45,size=13,color=MUTED),text('Hérault · 2023 · INSEE, traitements RCO',x+20,y+h-(104 if mobile else 55),width=31 if mobile else 48,size=13,color=MUTED)]
    else:
        p += [text('Des métiers signalés comme proches',x+20,base,width=30 if mobile else 45,size=16),text("Travaux d’étanchéité et d’isolation",x+20,base+(55 if mobile else 45),width=24 if mobile else 40,size=21,bold=True),text('Comparer les activités et les conditions',x+20,y+h-(152 if mobile else 80),width=30 if mobile else 47,size=14,color=MUTED),text('France Travail · métiers proches',x+20,y+h-(96 if mobile else 55),width=38,size=13,color=MUTED)]
    p += [text(sub,x+20,y+h-(40 if mobile else 22),width=31 if mobile else 50,size=13,color=BLUE,bold=True),icon('arrow',x+w-42,y+h-48 if mobile else y+h-40)]
    return p

# La composition conserve la recherche, le lieu, les quatre questions et leurs routes.
for mobile in [False,True]:
    w=375 if mobile else 1440;p=header(w,mobile)
    if mobile:
        p += [rect(16,99,343,52,'#f6f6f6'),text('Modifier ma recherche',32,132,width=30,size=16,color=BLUE,bold=True),text('Les quatre questions sur ce métier',20,199,width=32,size=16,color=BLUE),text(metier['rome_libelle'],20,263,width=18,size=30,bold=True),text('Comprenez le travail et les possibilités',20,362,width=32,size=17),rect(20,410,212,44,BLUE,BLUE),text('Garder cette piste',36,438,size=16,color='white',bold=True),text('Comparer avec un autre métier',20,489,width=32,size=16,color=BLUE),text('Montpellier · votre lieu choisi',20,541,width=32,size=15)]
        y=584;cw=335;x=20;ch=460
    else:
        p += [rect(48,108,1344,94,'#f6f6f6'),text('Métier        Diplôme ou titre        Domaine professionnel',68,137,size=15,color=BLUE),text('Un métier ou un nom de poste',68,175,size=15,bold=True),text('Rechercher',1050,175,size=16,color=BLUE,bold=True),text('Montpellier · changer de lieu',1180,175,width=25,size=13,color=BLUE),text('Vos questions',48,270,size=15,bold=True)]
        for i,l in enumerate(['Que fait-on dans ce métier ?','Où sont les opportunités ?','Combien gagne-t-on ?','Quelles autres pistes ?','Pour aller plus loin']):p.append(text(l,48,315+i*58,width=24,size=15,color=BLUE))
        p += [text('Pose et restauration de couvertures',320,286,width=42,size=42,bold=True),text('Comprenez le travail et regardez les possibilités qui comptent pour vous.',320,346,width=85,size=18,color=MUTED),rect(320,382,192,46,BLUE,BLUE),text('Garder cette piste',338,411,size=16,color='white',bold=True),text('Comparer avec un autre métier',538,411,size=16,color=BLUE),text('Montpellier · votre lieu choisi      Choisir un lieu',320,467,size=15)]
        y=510;cw=510;x=320;ch=350
    for i,(kind,title,cta) in enumerate([('work','Que fait-on dans ce métier ?','Les activités et les savoir-faire'),('place','Où sont les opportunités ?','Comprendre les besoins des employeurs'),('money','Combien gagne-t-on ?','Lire les salaires et les secteurs'),('pistes','Quelles autres pistes ?','Découvrir les métiers proches')]):
        xx=x if mobile else x+(i%2)*(cw+24);yy=y+i*(ch+20) if mobile else y+(i//2)*(ch+24)
        p += card(kind,title,cta,xx,yy,cw,ch,mobile)
    end=y+4*(ch+20) if mobile else y+2*(ch+24)
    p += [text('Pour aller plus loin',x,end+35,size=24,bold=True)]
    for i,label in enumerate(['Les parcours professionnels observés','Les changements possibles à 2030','Les certifications et formations','Les secteurs qui emploient']):p += [text(label,x,end+80+i*(56 if mobile else 37),width=34 if mobile else 70,size=16,color=BLUE)]
    end+=330 if mobile else 260
    annotations_height=260 if mobile else 180
    p += [rect(0,end,w,annotations_height,'#f6f6f6'),text('Annotations de conception — hors écran citoyen',20,end+30,width=35 if mobile else 90,size=15,bold=True),text('Même navigation : US005/008/009/027/028. Les valeurs viennent de R16, pas du fichier HTML d’intention. Groupes et lieux restent distincts. Toutes les rubriques restent accessibles.',20,end+(86 if mobile else 58),width=36 if mobile else 145,size=14,color=MUTED)]
    finish('01_FICHE_METIER_MOBILE.svg' if mobile else '01_FICHE_METIER_DESKTOP.svg',w,end+annotations_height,p,'Fiche métier existante, quatre questions enrichies de repères natifs, sources et accès aux approfondissements. Les actions et routes sont inchangées.')

p=header(1280)+[text('Deux métiers, pour y voir plus clair',48,151,width=60,size=36,bold=True),text('Choisissez les métiers. Regardez ce qui compte pour vous, sans score global.',48,194,width=100,size=18,color=MUTED)]
for x,name,letter in [(48,metier['rome_libelle'],'A'),(664,"Travaux d’étanchéité et d’isolation",'B')]:
    p += [rect(x,234,568,180,'#f6f6f6'),text('Métier '+letter,x+20,268,size=15,color=BLUE,bold=True),text(name,x+20,305,width=32,size=24,bold=True),text('Choisir un métier',x+20,385,size=15,color=BLUE)]
p += [text('Inverser les métiers',48,455,size=16,color=BLUE),text('Le travail     Savoir-faire et conditions     Emploi et salaires     Les formations',48,519,width=105,size=17,color=BLUE,bold=True),text('Les mêmes repères, leurs limites en plus',48,590,size=27,bold=True)]
for x in [48,664]:p.append(rect(x,624,568,300))
p += [text(number(salary['salaire_net_mensuel_median'])+' € nets / mois',72,678,size=34,bold=True),text(salary['fap_225_libelle'],72,721,width=45,size=17),text('Groupe de 8 métiers · Hérault · 2023',72,787,width=46,size=15,color=MUTED),text('INSEE · temps complet · médiane',72,822,width=46,size=15,color=MUTED),text('Information non disponible',688,678,width=32,size=27,bold=True),text('Les chiffres du métier A ne sont pas utilisés pour remplir cette colonne.',688,727,width=44,size=18,color=MUTED),text('Revoir la fiche du métier A',72,887,size=16,color=BLUE),text('Revoir la fiche du métier B',688,887,size=16,color=BLUE),text('Les tableaux, sources et détails restent disponibles dans chaque rubrique.',48,979,width=110,size=18),rect(0,1040,1280,160,'#f6f6f6'),text('Annotations — US028 / US012 / US032–035',48,1080,size=18,bold=True),text('Identités A/B, inversion, retours, mêmes données et mêmes filtres. Aucune comparaison salariale complète n’est revendiquée en l’absence de réponse pour B.',48,1120,width=126,size=16,color=MUTED)]
finish('02_COMPARATEUR_DESKTOP.svg',1280,1200,p,'Comparateur existant à deux métiers ; identité des colonnes, mêmes contrôles, donnée absente explicitée sans emprunter les chiffres de l’autre métier.')

grammar='''# Grammaire visuelle — infographie interactive

Cette direction est appliquée à Explorer existant. « Voir, comprendre, approfondir » est une règle de présentation, pas une nouvelle séquence obligatoire du parcours. Les écrans, routes, choix et scénarios restent ceux des US.

## Composition

Fond neutre, grande typographie pour le message utile, quatre portes d’entrée conservées, rythme entre texte, repère et tableau. Les actions restent Bleu France. Pas de grand décor bleu, personnage, médaille d’attractivité, radar, jauge personnelle ou pourcentage décoratif.

Les aperçus sont de vraies données : deux lignes BMO, sans somme ; médiane mensuelle de la famille et du département réellement couverts ; conditions et métiers proches reçus. Les détails gardent leurs tableaux et sources. L’absence reste visible, y compris sur une seule colonne de comparaison. Une carte est le MapChart officiel, jamais une géographie dessinée pour la composition.

## Tokens et accentuation

Utiliser les tokens DSFR de décision : `--background-default-grey`, `--background-alt-grey`, `--text-default-grey`, `--text-mention-grey`, `--border-default-grey`, `--text-action-high-blue-france`, `--background-action-high-blue-france`. Les couples illustratifs émeraude, moutarde et glycine sont limités à des repères de contenu dans les compositions, sans changer les couleurs des boutons, du focus ni des états système. Cartes et tuiles gardent leurs fonds blancs/gris. La couleur n’exprime aucune valeur statistique sans légende.

Les variables conservent leurs correspondances de thème. Tester le thème sombre par le mécanisme `data-fr-theme` existant du DSFR ; ne pas ajouter un choix de thème au parcours dans ce chantier. Les SVG de conception illustrent le thème clair et ne constituent pas une recette du thème sombre.

## Typographie et densité

Marianne installée avec le DSFR, repli Arial/sans-serif. Échelle fluide pour les titres, 16 px pour le texte courant, 14 px minimum pour les contextes de données de l’infographie. Les noms longs sont conservés et retournent à la ligne. Espacements multiples de 4/8 px, pas de tailles fixes qui tronquent les valeurs ou le contenu.

## Icônes et interactions

Uniquement les icônes officielles du paquet DSFR installé : mallette, repère géographique, euro, marque-page et flèche. Elles accompagnent un texte et sont `aria-hidden`. Aucun cœur, emoji ni symbole approximatif ne remplace une commande. Les ancres et boutons existants gardent leur rôle, nom et cible ; pas de lien imbriqué dans une carte-lien.

Clavier, focus visible, états pressés/sélectionnés, erreurs associées et annonces existantes sont conservés. Cibles de 44 px pour les nouvelles compositions. Aucun mouvement nécessaire : respecter `prefers-reduced-motion`. Sur mobile, empiler les quatre portes sans masquer leurs contextes ; les graphiques lourds restent à la demande.

## Visualisations

DSFR Chart 2.1.1 reste le moteur : DataBox, BarChart, LineChart, MapChart et TableChart réellement présents. Chiffre isolé → texte ou repère natif. Répartition incomplète → barres, jamais un camembert à 100 %. Quartiles → tableau explicite et représentation native adaptée, pas un minimum/maximum. Série mensuelle → courbe uniquement avec mois et valeurs présents. Projections → composantes distinctes avec négatifs, sans série annuelle fabriquée. Toute visualisation possède les mêmes valeurs dans un tableau accessible, avec unité, population, source, période et lieu réel.

## Maquettes commentées

- [Fiche métier — ordinateur](maquettes/01_FICHE_METIER_DESKTOP.svg).
- [Fiche métier — mobile](maquettes/01_FICHE_METIER_MOBILE.svg).
- [Comparateur — ordinateur](maquettes/02_COMPARATEUR_DESKTOP.svg).

Les annotations hors écran relient ces supports aux US. Le contrat et les scénarios priment toute simplification graphique de ces SVG. Les maquettes ne démontrent pas un test HTTP ou une conformité RGAA.

Sources techniques : [palette et accentuation DSFR](https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs), fichiers officiels installés dans `commun_datavisualisation/node_modules/@gouvfr/`, catalogue DSFR Chart local et intégration actuelle documentée dans `11_INTEGRATION_DSFR_CHART.md`.
'''
(HERE/'02_GRAMMAIRE_VISUELLE.md').write_text(grammar,encoding='utf-8')
print(json.dumps({'audit':len(records),'svg':3,'archive':str(ARCHIVE)},ensure_ascii=True))
