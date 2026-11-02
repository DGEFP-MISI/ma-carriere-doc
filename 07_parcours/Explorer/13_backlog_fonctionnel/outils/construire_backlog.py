"""Produit les US et leurs SVG depuis la conception existante et les scénarios rédigés.

Ce script ne touche ni à l'application ni aux références API. Les corrections de
la table de parcours et ses liens sont limitées au périmètre documentaire autorisé.
"""
import csv
import hashlib
import html
import json
import os
import re
import textwrap
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
EXPLORER = HERE.parent
ROOT = EXPLORER.parents[1]
DATA = HERE / 'donnees'
SVG = HERE / 'svg'
SVG.mkdir(exist_ok=True)

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def rel(path, parent=HERE):
    return os.path.relpath(path, parent).replace('\\', '/')

def link(path, label=None, parent=HERE):
    target=rel(path,parent)
    return f'[{label or path.name}](<{target}>)' if ' ' in target else f'[{label or path.name}]({target})'

def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')

def code(value):
    return '`' + str(value).replace('`', "'") + '`'

def uid(number):
    return f'US-FON-{number:03}'

def story_link(number):
    return link(HERE / f'{uid(number)}.md', uid(number))

def e_links(text):
    return re.sub(r'\bE(\d{2})\b', lambda m: story_link(int(m[1])) + f' (E{m[1]})', text)

def clean_legacy(text):
    replacements = {
        'code ROME V3 visible': 'nom métier visible ; identifiant ROME V3 interne',
        'Résultat avec type, RNCP/RS et code': 'Résultat avec intitulé, type et niveau reçus ; identifiants techniques internes',
        'Le libellé public Secteur indique clairement domaine professionnel': 'Le libellé public est Domaine professionnel, distinct du secteur économique',
        'plafond fixé en D08 (trois proposé)': 'plafond de trois fixé par le brief UX ; modalités de stockage de production à préciser',
        'trois proposé': 'trois au maximum, validé par le brief UX',
        'tranche ouverte >50000 EUR annuels si médiane null': 'tranche ouverte reçue (ex. « 50 000 euros et plus ») si médiane null',
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    return text

with (EXPLORER / '03_TABLE_CONCEPTION.csv').open(encoding='utf-8-sig', newline='') as stream:
    reader = csv.DictReader(stream, delimiter=';')
    original_columns = reader.fieldnames
    rows = list(reader)
for row in rows:
    for key in original_columns:
        if key != 'Appels_GET_detail':
            row[key] = clean_legacy(row[key])
    if row['Parcours_ID'] == 'E03':
        row['Question_usager'] = 'Quel domaine professionnel ?'
    if row['Parcours_ID'] == 'E04':
        row['Question_usager'] = 'Quels métiers de ce domaine professionnel ?'
    if row['Parcours_ID'] == 'E28':
        row['Dependances'] = 'E05;E06;E08;E09;E10;E11;E12;E17;E20;E23;E24;E25;E26;E31 ; E27 entrée facultative, comparaison directe possible'
by_e = {row['Parcours_ID']: row for row in rows}
parents = read(DATA / 'PARENTS_01_16.json') + read(DATA / 'PARENTS_17_31.json')
transversals = read(DATA / 'TRANSVERSALES.json')
specs = sorted(parents + transversals, key=lambda item: item['number'])
assert [s['number'] for s in specs] == list(range(1,36))
measure_specs = {m['code']:m for m in read(DATA / 'MESURES.json')}
catalogue_path = ROOT / '02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json'
catalogue = read(catalogue_path)['items']
assert set(measure_specs) == {m['code'] for m in catalogue}
api = read(ROOT / '01_sources/openapi/docs_json_interface.json')
allowed = {path for path,item in api['paths'].items() if 'get' in item}
assert len(allowed) == 21
calls_by_e = {e:json.loads(row['Appels_GET_detail']) for e,row in by_e.items()}

VIS = {
 'V01':['E09','E11','E12'], 'V02':['E08','E11','E25'], 'V03':['E25'],
 'V04':['E09','E10'], 'V05':['E08','E10'], 'V06':['E09','E10','E11','E12'],
 'V07':['E23'], 'V08':['E23'], 'V09':['E08','E24'], 'V10':['E24'],
 'V11':['E25','E08','E26'], 'V12':['E17'], 'V13':['E17','E12'], 'V14':['E17'],
 'V15':['E17','E20'], 'V16':['E18'], 'V17':['E03','E04'], 'V18':['E06','E07','E28'],
 'V19':['E04','E15','E16'], 'V20':['E28'], 'V21':['E09','E24'],
 'V22':['E10','E11','E12','E28'], 'V23':['E17'], 'V24':['E09'], 'V25':['E12','E31'],
}
vis_file = ROOT / '07_parcours/00_REFERENTIEL_COMMUN_DATAVISUALISATION/03_MATRICE_API_GRAPHIQUES.csv'
vis_rows = list(csv.DictReader(vis_file.open(encoding='utf-8-sig'), delimiter=';'))

# Typage : schémas officiels quand disponibles, valeurs réellement observées sinon.
# Une observation null ne démontre pas le type d'une valeur publiée.
native_sources = defaultdict(list)
def sources(endpoint, paths):
    native_sources[endpoint].extend(p for p in paths if p.exists())

base = ROOT / '02_reponses_observees'
controls = ROOT / '06_controles/resultats'
sources('/metiers/{rome}', [base/'metiers/response_metiers-rome.json'])
sources('/metiers/{rome}/competences', [base/'metiers/response_metiers{rome}competences.json'])
sources('/metiers', list((controls/'R23 test').glob('*metiers*.json')) + list((controls/'R24').glob('*.json')))
sources('/competences', list((controls/'R23 test').glob('*competences*.json')))
sources('/indicateurs', list((controls/'R16 test').glob('GET_indicateurs*.json')))
sources('/mesures', [catalogue_path])
sources('/mobilites', list((base/'indicateurs/mobilites').glob('*.json')))
sources('/salaires', list((base/'indicateurs/salaires').glob('*.json')))
sources('/salaires/secteurs', [base/'indicateurs/response_salairessecteurs.json'])
sources('/recrutements', list((base/'indicateurs/Recrutementregions').glob('*Recrutement*.json')))
sources('/prospective/regions', list((base/'indicateurs/prospectiveregions').glob('*.json')))
sources('/prospective/metiers', list((base/'indicateurs/ProspectiveMetier').glob('*.json')))
sources('/secteurs', list((base/'indicateurs/Secteurs').glob('*.json')))
sources('/certifications', [base/'certifications/response_certifications.json'])
sources('/certifications/{certifinfo}', [base/'certifications/response_certifications-certifinfo.json'])
sources('/certifications/blocs', [base/'certifications/response_certificationsblocs.json'])
sources('/formacodes', [base/'certifications/response_formacode.json'])
sources('/sessions_a_venir', [base/'sessions/response_sessions_a_venir.json'])
sources('/sessions_en_cours', [base/'sessions/response_sessions_en_cours.json'])
sources('/territoires', list((base/'territoires').glob('*.json')) + list((controls/'R16 test').glob('GET_territoires*.json')))

observed = defaultdict(lambda: defaultdict(set))
def kind(value):
    if value is None: return 'null'
    if isinstance(value,bool): return 'booléen'
    if isinstance(value,int): return 'entier'
    if isinstance(value,float): return 'nombre'
    if isinstance(value,str): return 'chaîne'
    if isinstance(value,list): return 'tableau'
    return 'objet'

def visit(endpoint, value, path='$'):
    observed[endpoint][path].add(kind(value))
    if isinstance(value,dict):
        for key,child in value.items(): visit(endpoint,child,path+'.'+key)
    if isinstance(value,list):
        for child in value: visit(endpoint,child,path+'[]')
for endpoint,paths in native_sources.items():
    for path in paths: visit(endpoint,read(path))

def deref(schema):
    while '$ref' in schema:
        value = api
        for key in schema['$ref'].removeprefix('#/').split('/'): value=value[key]
        schema=value
    return schema

def field_type(endpoint, path):
    schema = api['paths'][endpoint]['get'].get('responses',{}).get('200',{}).get('content',{}).get('application/json',{}).get('schema')
    found = None
    if schema:
        try:
            for token in path.removeprefix('$.').split('.'):
                schema=deref(schema)['properties'][token.removesuffix('[]')]
                if token.endswith('[]'): schema=deref(schema)['items']
            schema=deref(schema)
            found=schema.get('type')
            if found and schema.get('nullable'): found += ' ou null'
        except (KeyError,TypeError):
            pass
    values=observed[endpoint].get(path,set())
    if found: return found, 'Type OpenAPI officiel' + (' ; chemin observé' if values else ' ; valeur à tester')
    if values: return ' / '.join(sorted(values)), 'Types observés seulement ; null seul ne prouve pas le type publié'
    return 'À confirmer sur réponse', 'Chemin du contrat/conception ; non démontré par le schéma officiel ou les JSON chargés'

def table(headers, data):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|'] + ['| '+' | '.join(cell(v) for v in row)+' |' for row in data])+'\n'

def param_rows(endpoint, values):
    parameters={p['name']:p for p in api['paths'][endpoint]['get'].get('parameters',[])}
    result=[]
    for key,usage in values.items():
        assert key in parameters, (endpoint,key)
        p=parameters[key];s=p.get('schema',{});details=s.get('type','type non indiqué')
        if s.get('enum'): details+=' ; valeurs '+', '.join(map(str,s['enum']))
        if 'default' in s: details+=' ; défaut API '+json.dumps(s['default'],ensure_ascii=False)
        for constraint in ['minLength','maxLength','minimum','maximum']:
            if constraint in s: details+=f' ; {constraint}={s[constraint]}'
        result.append([code(key),p.get('in','query'),'Requis Swagger' if p.get('required') else 'Facultatif Swagger',code(details),usage])
    return result

PRE = {
 3:'L’arbre /domaines est une source contractuelle distincte de la liste locale issue des métiers.',
 6:'La pagination et la catégorie de la liste de compétences sont connues ; une page isolée n’est pas exhaustive.',
 8:'Le métier et le lieu sont identifiés. Chaque mesure peut avoir son propre repli, grain et millésime.',
 13:'Aucun métier cible ni niveau personnel n’est exigé pour choisir une compétence.',
 15:'Les contextes sélectionnés proviennent de la catégorie contexte_travail.',
 17:'La certification est reconnue par certifinfo_code ; l’intention de consultation est distincte de cette identité.',
 21:'Une certification et un zonage région/département/CLPE sont choisis. Depuis une commune, le parent est reçu et choisi explicitement.',
 22:'Une certification et un zonage région/département/CLPE sont choisis. Aucun code communal n’est réétiqueté sous une autre maille.',
 27:'Le navigateur peut conserver l’état dans la session ; le refus de stockage doit laisser l’exploration et l’export utilisables.',
 28:'Deux métiers reconnus peuvent être choisis directement ; les avoir gardés dans Mes pistes est facultatif.',
 30:'Le thème, la certification et la session restent des objets distincts ; les liens utilisent les identifiants reçus.',
}

LOCAL_TESTS = {
 1:'Missions 002/007, recherche clavier et états de recherche dans TESTS_UX_EXPLORER.',
 2:'Recette existante : choix de certification, deux intentions et fiches identifiées.',
 3:'Mission 007 sur la liste locale de domaines ; ce n’est pas une capture de /domaines.',
 4:'Mission 007 et contrôle de la liste locale du domaine F16.',
 5:'Missions 002/003/005 ; quatre questions et actions de fiche.',
 6:'Missions 003/009 ; page 1 observée, pas validation d’exhaustivité.',
 7:'Mission 004 : cible et historique avant/arrière.',
 8:'Mission 006 et contrôles DSFR Chart ; sous-rubriques partiellement restituées.',
 9:'Mission 008 : sélection et absence de transposition de Montpellier.',
 10:'Mission 006 et contrôles de cartes/barres sur les réponses disponibles.',
 11:'Mission 005 et contrôles de montants, cartes et alternative tabulaire.',
 12:'Contrôles DataBox, tableaux, unités et familles ; métadonnées et cas limites encore partiels.',
 13:'Mission 001 et guide au clavier ; deux choix natifs et compteur synchronisé.',
 14:'Cas R23, trois résultats au moins une et un résultat toutes sur le jeu ciblé.',
 15:'Contrôles de présence des filtres et sélection locale ; catalogue HTTP non couvert.',
 16:'Cas documentaires R24 ; combinaison générale non capturée signalée comme indisponible.',
 17:'Recette certification et indicateurs locaux ; plusieurs cohortes ont des valeurs null.',
 18:'Accordéons de blocs natifs ; recherche textuelle et pagination HTTP non démontrées.',
 19:'Navigation depuis certification vers métiers connus dans la recette existante.',
 20:'Liste locale et liens ; filtres d’accès/validation partielle HTTP à compléter.',
 21:'Vue locale sessions à venir ; Q11 ne vaut pas filtre HTTP validé.',
 22:'Bascule sessions en cours testée ; rattachement/garantie Q11 restent ouverts.',
 23:'Mission 010 : sens, âge, famille, période, source et focus.',
 24:'Mission 006 et contrôles des projections, négatifs et carte régionale.',
 25:'Graphiques et tableaux de salaires sectoriels présents ; variantes régionales non complètes.',
 26:'Deux lectures locales distinctes ; anomalie R17 non résolue.',
 27:'État gardé, quatrième refusée, retrait, export/reprise et nouveaux chargements complets ; Ctrl+R/F5 natif NON TESTÉ.',
 28:'Missions 002/009 ; choix/inversion/retours testés, deuxième série statistique absente.',
 29:'Tags du métier et page thématique ; filtrage général de catalogue à compléter.',
 30:'Thèmes disponibles localement ; chaîne filtrée complète à capturer.',
 31:'Vingt-neuf notices locales ; cela ne démontre pas la disponibilité d’une mesure pour tout métier.',
}

def bullets(values):
    return '\n'.join('- '+str(value) for value in values)+'\n'

def all_fields(call):
    return list(dict.fromkeys(call['champs'] + [p for fields in call.get('mesures',{}).values() for p in fields]))

def write_csv(path, columns, records):
    with path.open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=columns,delimiter=';')
        writer.writeheader(); writer.writerows(records)

def owned_measures(number):
    return [m for m in catalogue if measure_specs[m['code']]['owner']==f'E{number:02}']

def detailed_measures(number):
    # La mesure emploi_secteurs est pilotée par E26, et fait aussi partie des
    # quatorze mesures contractuelles de la fiche territoriale E08.
    return [m for m in catalogue if m['ressource']=='/indicateurs'] if number==8 else owned_measures(number)

def svg_text(text, x, y, width=64, size=18, color='#161616', weight='normal'):
    lines=textwrap.wrap(str(text),width=width,break_long_words=False,break_on_hyphens=False) or ['']
    return ''.join(f'<text x="{x}" y="{y+i*(size+8)}" font-size="{size}" fill="{color}" font-weight="{weight}">{html.escape(line)}</text>' for i,line in enumerate(lines)),len(lines)*(size+8)

def make_svg(spec):
    number=spec['number']; key=uid(number); parts=[]
    text,height=svg_text(f'{key} — {spec["title"]}',36,42,width=88,size=24,weight='bold');parts.append(text)
    text,height=svg_text('Schéma fonctionnel cible • noms compréhensibles • aucune valeur métier simulée',36,85,width=100,size=17,color='#454545');parts.append(text)
    parts.append('<rect x="24" y="112" width="1152" height="42" fill="#000091" rx="4"/>')
    parts.append('<text x="42" y="140" font-size="18" fill="white" font-weight="bold">Étape et action de la personne</text><text x="540" y="140" font-size="18" fill="white" font-weight="bold">Réponse attendue de l’interface</text>')
    y=168
    for i,(action,response) in enumerate(spec['steps'],1):
        a,ha=svg_text(f'{i}. {action}',44,y+30,width=45,size=18)
        b,hb=svg_text(response,540,y+30,width=58,size=18)
        block=max(ha,hb)+34
        parts.append(f'<rect x="24" y="{y}" width="1152" height="{block}" rx="6" fill="'+('#f5f5fe' if i%2 else '#f6f6f6')+'"/>')
        parts += [a,b]
        y+=block+15
    parts.append(f'<rect x="24" y="{y}" width="1152" height="48" rx="4" fill="#e8edff"/>')
    parts.append(f'<text x="42" y="{y+31}" font-size="20" font-weight="bold" fill="#000091">Issues alternatives : expliquer, conserver les choix utiles, proposer une reprise</text>');y+=74
    for alternative in spec['alternatives']:
        text,h=svg_text('• '+alternative,42,y,width=106,size=17);parts.append(text);y+=h+10
    y+=12
    endpoints=list(dict.fromkeys(c['endpoint'] for c in calls_by_e.get(f'E{number:02}',[])))
    footer='Données : '+(' ; '.join('GET '+e for e in endpoints) if endpoints else 'réutilisation des GET des US métier ; aucun endpoint ajouté')
    text,h=svg_text(footer,42,y,width=110,size=16,color='#454545');parts.append(text);y+=h+14
    text,h=svg_text('Le scénario, les règles, les champs et les critères détaillés du fichier Markdown font foi. Ce schéma ne prouve ni le développement ni un test HTTP.',42,y,width=110,size=16,color='#454545');parts.append(text);y+=h+30
    document=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {y}" width="1200" height="{y}" role="img" aria-labelledby="titre description"><title id="titre">{html.escape(key+" — "+spec["title"])}</title><desc id="description">Parcours nominal en {len(spec["steps"])} étapes, actions de la personne et réponses attendues du système, puis issues alternatives. Alternative textuelle intégrale dans la section 4 de la User Story.</desc><rect width="1200" height="{y}" fill="white"/><g font-family="Arial, sans-serif">'+''.join(parts)+'</g></svg>'
    (SVG/f'{key}.svg').write_text(document,encoding='utf-8')

def measure_block(m):
    spec=measure_specs[m['code']]
    prefix='$.items[].valeurs[]' if m['ressource']=='/indicateurs' else ('$' if m['ressource']=='/certifications' else '$.items[]')
    if m['ressource']=='/certifications':
        route='GET /certifications/{certifinfo} : champs à la racine ; GET /certifications : mêmes champs sous $.items[]'
    else: route='GET '+m['ressource']
    fields=', '.join(code(prefix+'.'+field) for field in m['champs'])
    return '\n'.join([
        f'#### {code(m["code"])} — {m["libelle"]}', '',
        f'**Source API :** {route}. '+('Filtrer `items[].mesure` par ce code ; ne pas supposer une forme commune de `valeurs[]`.' if m['ressource']=='/indicateurs' else 'Conserver les familles/populations réellement publiées.'), '',
        f'**Grain :** {code(m["grain"])}. **Mailles du catalogue :** '+', '.join(m['mailles'])+'. **Millésime observé :** '+str(m['millesime'])+'.', '',
        f'**Producteur :** {m["source"]}. **Unité et population :** {spec["unit"]}', '',
        f'**Définition source :** {m["definition"]}', '',
        f'**Champs nécessaires :** {fields}.', '',
        f'**Présentation attendue :** {spec["visual"]}', '',bullets(spec['rules']),
        '**Dépendance / tests :** '+spec['notes'], '',
        '**Preuve :** '+link(catalogue_path,'notice native /mesures')+' ; les paramètres exacts figurent dans les appels ci-dessus. La présence au catalogue ne prouve pas une valeur disponible pour tout métier ou lieu.', '',
    ])

field_records=[]
criteria_records=[]
def render_story(spec):
    n=spec['number']; key=uid(n); e=f'E{n:02}' if n<=31 else None
    row=by_e.get(e); calls=calls_by_e.get(e,[]); measures=detailed_measures(n)
    lot=row['Lot_technique'] if row else spec['lot']
    related=row['Dependances'] if row else '; '.join(spec['related'])
    pieces=[f'# {key} — {spec["title"]}', '',
        f'**Rattachement :** {e+" · alias historique US-"+e if e else "exigence transversale des 31 fonctionnalités"}. **Lot :** {lot}.', '',
        '**Périmètre :** inclus. Les dépendances et les tests à réaliser organisent la réalisation, sans retirer la fonctionnalité.', '',
        '**Dépendances et passerelles :** '+e_links(related)+'.', '',
        '**État constaté au 2 novembre 2026 :** '+spec['state'], '',
        link(EXPLORER/'04_BACKLOG_USER_STORIES.md','Retour au backlog',parent=HERE)+' · '+link(ROOT/'07_parcours/00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md','Modèle commun'), '',
        '## 1. Objectif fonctionnel','',
        ('Permettre à la personne de '+spec['title'][0].lower()+spec['title'][1:]+', pour '+spec['benefit']+'. '+row['Besoin_utilisateur']) if row else spec['objective'], '',
        '## 2. User Story','',
        (f'En tant que personne qui explore ses possibilités professionnelles, je souhaite {spec["title"][0].lower()+spec["title"][1:]}, '+("afin d’" if spec['benefit'][0].lower() in 'aeiouéèêàîôù' else 'afin de ')+spec['benefit']+'.') if row else spec['story'], '',
        '## 3. Préconditions','',
    ]
    pre=['Les noms et identifiants sélectionnables proviennent des réponses autorisées ; aucun métier, lieu ou résultat n’est choisi implicitement.', 'Les appels disposent de leurs paramètres exacts et le contexte de navigation est identifié. Les GET sont protégés par l’intégration prévue au contrat ; aucun secret d’accès n’est embarqué dans le HTML public.']
    if row:
        if n in PRE: pre.append(PRE[n])
        pre.append('Les fonctionnalités liées restent accessibles selon les dépendances ci-dessus ; un volet indisponible ne bloque pas toute la fiche.')
    else: pre=spec['preconditions']
    pieces += [bullets(pre),'## 4. Scénario nominal','',table(['Étape','Action utilisateur','Comportement attendu du système'],[[i,*step] for i,step in enumerate(spec['steps'],1)]),'## 5. Scénarios alternatifs','',bullets(spec['alternatives'])]
    if row:
        pieces += ['**États et erreurs complémentaires à couvrir :** '+row['Etats_vides_erreurs'].rstrip('. ')+'. Les statuts ci-dessus sont des cas de recette, leur retour effectif dépend de l’endpoint ; ne pas inventer un corps d’erreur serveur.', '']
    pieces += ['## 6. Règles de gestion','',bullets(spec['rules'])]
    if row:
        pieces += ['**Règles héritées conservées :** '+row['Regle_metier'], '', '**Traitements :** '+row['Traitements'], '', '**Règles statistiques :** '+row['Regles_statistiques'], '']
    pieces += [
        '**Règles communes :** noms et explications en langage courant ; ROME V3 uniquement ; aucune source métier extérieure aux 21 GET ; aucune moyenne, conversion annuelle/mensuelle, interpolation ou correspondance construite. Les codes restent internes aux requêtes, routes et tests.', '',
        'Une valeur nulle, absente, `secret_stat`, zéro et une liste vide conservent leur sens distinct. Afficher le lieu réellement mesuré et expliquer le repli par indicateur ; ne pas attribuer un résultat de famille à un seul métier ou un résultat national à une session.', '',
        '## 7. Données et API','',
    ]
    if row:
        pieces += [f'**Source et portée de conception :** {row["Source"]} ; grain {row["Granularite"]} ; période {row["Millesime"]}. Les métadonnées de chaque réponse/mesure priment toute valeur observée dans un exemple.', '']
        if n==27: pieces += ['L’ajout, le retrait, l’export et la reprise de pistes sont locaux. Aucun GET de sauvegarde et aucun endpoint d’écriture n’existent dans le contrat. Le détail ci-dessous sert uniquement à retrouver une fiche si elle n’est plus en cache.', '']
        for i,call in enumerate(calls,1):
            endpoint=call['endpoint']; assert endpoint in allowed
            pieces += [f'### Appel {i} — GET {code(endpoint)}', '', '**Déclenchement :** '+call['declenchement']+'. Ordre/chaînage : suivre les étapes du scénario, les identifiants reçus et les dépendances liées ; charger les détails à leur ouverture et réutiliser le cache à paramètres strictement identiques.', '']
            pieces += [table(['Paramètre exact','Emplacement','Obligation du contrat','Type / domaine Swagger','Usage pour cette US'],param_rows(endpoint,call['parametres'])) if call['parametres'] else 'Aucun paramètre pour cet appel.\n']
            typed=[]
            for path in all_fields(call):
                typ,evidence=field_type(endpoint,path)
                typed.append([code(path),typ,evidence])
                field_records.append({'US':key,'Conception_ID':e,'Endpoint_GET':endpoint,'Chemin_JSON':path,'Type':typ,'Niveau_preuve':evidence})
            pieces += [table(['Chemin JSON exact','Type connu','Niveau de preuve du chemin/type'],typed)]
            refs=list(dict.fromkeys(native_sources[endpoint]))
            pieces += ['**Réponses natives utilisées pour vérifier les chemins :** '+('; '.join(link(p,rel(p,ROOT)) for p in refs) if refs else 'aucun JSON natif enregistré pour cet endpoint dans les jeux chargés ; contrat à compléter par un test GET ciblé')+'.', '']
        pieces += ['### Preuves et contrôles restant à produire','',
            '**Documenté :** '+link(ROOT/'01_sources/contrat_interface_2026-10-19.md','contrat')+' ; '+link(ROOT/'01_sources/openapi/docs_json_interface.json','OpenAPI officiel')+'. Dix réponses sur les 21 GET n’ont pas de schéma officiel de réponse ; un type observé ne devient pas un schéma fournisseur.', '',
            '**Références conservées de la conception :** '+ '; '.join(link(ROOT/p.strip(),p.strip()) for p in row['Preuve_reference'].split(';') if p.strip())+'.', '',
            '**Contrôle local déjà rapporté :** '+LOCAL_TESTS[n]+' '+link(EXPLORER/'TESTS_UX_EXPLORER.md','Recette UX existante')+'. Ces résultats sur JSON locaux ne valident pas les appels HTTP.', '',
            '**Tests à réaliser :** '+row['Tests_a_realiser']+'.', '',
            '**Points RCO associés :** '+row['Clarifications_RCO']+' Lire le tri déjà établi dans '+link(EXPLORER/'06_DECISIONS_ET_POINTS_A_VALIDER.md','Q01–Q14')+' avant toute nouvelle demande ; ne pas redemander une réponse démontrée par le contrat.', '',
        ]
    else:
        pieces += [spec['api_note'],'', '**Preuves et références :** '+ '; '.join(link(ROOT/p,p) for p in spec['proofs'])+'.','', '**Tests restant nécessaires :**','',bullets(spec['tests'])]
    if measures:
        pieces += [f'### Couverture détaillée des {len(measures)} mesures rattachées à cette US','', 'Chaque mesure est un sous-scénario de cette US. Ses champs, sa population et ses critères sont conservés même si aucune valeur n’est publiée dans le jeu local.', '']
        if n==8: pieces += ['Les quatorze mesures de `/indicateurs` sont détaillées ici. Le pilotage du sous-scénario `emploi_secteurs` appartient à '+story_link(26)+' : il reste obligatoire dans cette fiche territoriale et est partagé entre les deux US, sans créer une trentième mesure.', '']
        for measure in measures: pieces.append(measure_block(measure))
    if n==24: pieces += ['**Complément obligatoire :** tous les champs de la mesure `metiers_2030`, ses définitions et ses critères sont explicités dans '+story_link(8)+'. Cette US ajoute les classements et comparaisons régionaux détaillés, sans réduire les cinq composantes aux seules créations nettes.', '']
    if n==28: pieces += ['**Réutilisation des mesures :** reprendre l’ensemble des sous-scénarios pertinents de '+', '.join(story_link(i) for i in [8,17,23,24,25,26])+', avec deux réponses identifiées et des populations comparables. Une valeur absente pour B reste absente ; le tableau commun ne lui attribue jamais la valeur de A.', '']
    pieces += ['## 8. Critères d’acceptation','']
    criteria=list(spec['acceptance'])
    for m in measures: criteria.extend(measure_specs[m['code']]['acceptance'])
    criteria += [
        ['un intitulé public et son identifiant technique disponibles','le contenu est présenté','les noms sont compréhensibles, les sources restent accessibles et aucun code de référentiel n’est imposé à la personne'],
        ['une réponse absente, protégée ou en erreur pour un seul volet','les autres réponses sont disponibles','les volets disponibles restent consultables et l’état manquant est expliqué sans valeur de substitution'],
    ]
    for i,(given,when,then) in enumerate(criteria,1):
        pieces += [f'**{key}-CA-{i:02}** — **Étant donné** {given}, **Quand** {when}, **Alors** {then}.', '']
        criteria_records.append({'Critere_ID':f'{key}-CA-{i:02}','US_ID':key,'Conception_ID':e or '',
            'Etant_donne':given,'Quand':when,'Alors':then,
            'Statut':'Spécifié ; non exécuté dans ce chantier documentaire',
            'Recette_liee':'T-'+e if e else 'Transversal aux recettes T-E01 à T-E31',
            'Preuves':'Voir section 7 et état constaté de l’US ; tests antérieurs à périmètre limité'})
    if row: pieces += ['**Trace de conception conservée :** '+row['Critere_acceptation'], '', '**Recette de rattachement :** `T-'+e+'` ; les critères ci-dessus constituent les cas vérifiables à décliner dans cette recette et la matrice de traçabilité.', '']
    pieces += ['## 9. Composants UX/UI','',bullets(spec['ux']),
        '**États à rendre accessibles :** initial, saisie/choix, attente annoncée, résultat, résultat partiel, vide, valeur non renseignée/protégée, erreur et reprise. Afficher des messages près des commandes concernées ; conserver les sélections utiles et ignorer les réponses périmées.', '',
        '**Accessibilité :** libellés permanents, structure des titres, liens explicites, focus visible et logique, navigation intégrale au clavier ; annoncer les changements utiles sans lire chaque frappe. Aucune information portée par la seule couleur, le survol ou une carte. Tableau de données équivalent pour chaque graphique ; source, période, unité, population et lieu effectif accessibles au même endroit.', '',
        '**Responsive et sobriété :** progression par questions, détails à la demande, réemploi des GET identiques ; repli sans perte de contenu, lecture à 320 px et zoom navigateur 200/400 % à recetter. JavaScript indisponible : afficher le contenu de repli et les limites réelles. Une recette locale ne constitue pas une conformité RGAA complète.', '',
        '**Bibliothèques :** DSFR installé pour les contrôles et tableaux ; DSFR Chart officiel (`@gouvfr/dsfr-chart` 2.1.1 dans l’intégration actuelle) et DataBox quand une représentation convient. Pas de graphique personnalisé pour remplacer un composant adapté. GenUI n’est pas une dépendance de réalisation décidée ; aucun service ni endpoint supplémentaire n’est supposé.', '',
    ]
    if row: pieces += ['**Composants et interaction hérités :** '+row['Composant_UI'], '', '**SEO / validation conservés :** '+row['SEO']+'. Ce statut est une proposition de déploiement, pas une décision produit acquise.', '']
    pieces += ['## 10. Maquette fonctionnelle','',f'![{key} — scénario, interactions et alternatives](svg/{key}.svg)', '',f'[Ouvrir le schéma SVG accessible](svg/{key}.svg). Le texte intégral du scénario en section 4 et des alternatives en section 5 fournit son alternative. Il s’agit de la cible fonctionnelle, sans données de démonstration inventées ni déclaration de disponibilité HTTP.', '']
    (HERE/f'{key}.md').write_text('\n'.join(pieces),encoding='utf-8')
    make_svg(spec)

for spec in specs: render_story(spec)

coverage=[]
for spec in specs:
    n=spec['number'];e=f'E{n:02}' if n<=31 else ''; row=by_e.get(e)
    coverage.append({
        'US_ID':uid(n),'Conception_ID':e,'Alias_historique':'US-'+e if e else '',
        'Titre':spec['title'],'Fichier_US':f'{uid(n)}.md','Schema_SVG':f'svg/{uid(n)}.svg',
        'Lot_technique':row['Lot_technique'] if row else spec['lot'],
        'Dependances':row['Dependances'] if row else ','.join(spec['related']),
        'GET':','.join(dict.fromkeys(c['endpoint'] for c in calls_by_e.get(e,[]))),
        'Mesures_proprietaires':','.join(m['code'] for m in owned_measures(n)),
        'Mesures_detaillees':','.join(m['code'] for m in detailed_measures(n)),
        'Visualisations':','.join(v for v,es in VIS.items() if e in es),
        'Nb_etapes_nominal':len(spec['steps']),
        'Statut_constate':spec['state'],
        'Tests_restants':row['Tests_a_realiser'] if row else ' ; '.join(spec['tests']),
        'Clarifications':row['Clarifications_RCO'] if row else 'Voir D08/D10 et les US métier liées',
    })
write_csv(HERE/'MATRICE_COUVERTURE_US.csv',list(coverage[0]),coverage)
write_csv(HERE/'MATRICE_CHAMPS_JSON.csv',list(field_records[0]),field_records)
write_csv(HERE/'MATRICE_CRITERES_ACCEPTATION.csv',list(criteria_records[0]),criteria_records)

measure_records=[]
for m in catalogue:
    s=measure_specs[m['code']];owner=s['owner']; route=m['ressource']
    endpoint='/certifications/{certifinfo}' if route=='/certifications' else route
    prefix='$.items[].valeurs[]' if route=='/indicateurs' else ('$' if route=='/certifications' else '$.items[]')
    measure_records.append({
        'Mesure':m['code'],'Libelle':m['libelle'],'US_proprietaire':uid(int(owner[1:])),
        'Conception_ID':owner,'Endpoint_GET':endpoint,
        'Parametres':next((json.dumps(c['parametres'],ensure_ascii=False) for c in calls_by_e[owner] if c['endpoint']==endpoint),'Voir appels de l’US propriétaire'),
        'Chemins_JSON':','.join(prefix+'.'+f for f in m['champs']),
        'Grain':m['grain'],'Mailles':','.join(m['mailles']),'Millesime_observe':m['millesime'],
        'Producteur':m['source'],'Unites_populations':s['unit'],'Presentation':s['visual'],
        'Regles': ' ; '.join(s['rules']),'Reutilisation':'E12,E31,E28 selon comparabilité ; E24 pour metiers_2030',
        'Tests_dependances':s['notes'],'Preuve':rel(catalogue_path,ROOT),
        'Niveau_preuve':'Notice catalogue observée ; valeur et disponibilité HTTP à tester par cas',
    })
write_csv(HERE/'MATRICE_MESURES.csv',list(measure_records[0]),measure_records)

visual_records=[]
for row in vis_rows:
    visual_records.append({
        'ID':row['ID'],'Question_usager':row['Question_usager'],
        'US':','.join(uid(int(e[1:])) for e in VIS[row['ID']]),
        'Conception_ID':','.join(VIS[row['ID']]),
        'Composant_cible':row['Visualisation_recommandee'],
        'Regles':row['Regles_limites'],
        'Ajustement_backlog':
            'V11 distingue tx_salaries_secteur 2023 (E25) de tx_actifs_secteur/nb_actifs_emploi 2021 (E08/E26) ; aucune substitution.' if row['ID']=='V11' else
            'Les chemins et métadonnées de l’US priment les champs candidats. Pas de maille_reelle inventée sur /salaires ; pas de camembert forcé ni graphe de quartiles trompeur.',
        'Source':rel(vis_file,ROOT),
    })
write_csv(HERE/'MATRICE_VISUALISATIONS.csv',list(visual_records[0]),visual_records)

endpoint_records=[]
for endpoint in sorted(allowed):
    operation=api['paths'][endpoint]['get']
    owners=[e for e,calls in calls_by_e.items() if any(c['endpoint']==endpoint for c in calls)]
    endpoint_records.append({
        'Methode':'GET','Endpoint':endpoint,
        'US':','.join(uid(int(e[1:])) for e in owners),'Conception_ID':','.join(owners),
        'Parametres_officiels':json.dumps(operation.get('parameters',[]),ensure_ascii=False),
        'Schema_reponse_officiel':'présent' if operation.get('responses',{}).get('200',{}).get('content',{}).get('application/json',{}).get('schema') else 'absent ; documentation et JSON à distinguer',
        'Preuve':'01_sources/openapi/docs_json_interface.json',
    })
assert all(r['US'] for r in endpoint_records)
write_csv(HERE/'MATRICE_GET.csv',list(endpoint_records[0]),endpoint_records)

# Les 31 lignes et colonnes de pilotage sont conservées, enrichies de liens stables.
added=['US_fonctionnelle_ID','US_fonctionnelle_fichier','Maquette_SVG','Statut_actuel_local','Couverture_backlog']
for row in rows:
    number=int(row['Parcours_ID'][1:]);spec=specs[number-1]
    row.update({
        'US_fonctionnelle_ID':uid(number),
        'US_fonctionnelle_fichier':f'13_backlog_fonctionnel/{uid(number)}.md',
        'Maquette_SVG':f'13_backlog_fonctionnel/svg/{uid(number)}.svg',
        'Statut_actuel_local':spec['state'],
        'Couverture_backlog':'Scénario nominal ; alternatives ; règles ; champs/types/preuves ; critères ; UX ; SVG ; transversal US-FON-032 à 035',
    })
write_csv(EXPLORER/'03_TABLE_CONCEPTION.csv',list(dict.fromkeys(original_columns+added)),rows)

index=[
    '# Backlog fonctionnel — Explorer', '',
    'Les **31 fonctionnalités E01 à E31 sont conservées**. Ce fichier est le point d’entrée du backlog fonctionnel : une US détaillée et un schéma SVG par fonctionnalité, complétés par quatre US transversales nécessaires à leur recette. Les 35 US appliquent les dix rubriques du modèle demandé.', '',
    '**Référentiel au 2 novembre 2026.** Les scénarios décrivent la cible de réalisation. Les états constatés distinguent ce qui est documenté, observé dans un JSON, contrôlé localement et encore à tester. Aucune US n’est déclarée livrée ou validée en HTTP sur la seule base de ce backlog.', '',
    '[Modèle commun MaCarrière](../00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md) · [Table de conception et pilotage](03_TABLE_CONCEPTION.csv) · [Plan de réalisation](09_PLAN_DE_REALISATION.md) · [Décisions à arbitrer](10_DECISIONS_A_ARBITRER.md)', '',
    '## Utiliser le backlog', '',
    'Chaque lien ouvre l’US complète : objectif, User Story, préconditions, scénario nominal en tableau, alternatives, règles, API et preuves, critères Étant donné / Quand / Alors, composants accessibles et schéma SVG. Les anciens identifiants `US-E01` à `US-E31` restent des alias ; les IDs E et T-E sont conservés.', '',
    'Pour alimenter un outil de développement, importer la matrice des US, puis reprendre le Markdown complet comme description et ses critères `US-FON-NNN-CA-NN` comme cas de recette. Les lots sont des dépendances de réalisation, sans retrait ni report de périmètre. Les sous-scénarios de mesures restent dans leur US propriétaire et peuvent être découpés en tâches techniques sans les perdre.', '',
    'Les US transversales 032–035 s’appliquent à chaque US métier. Une fiche ne peut pas être déclarée terminée si ses données sont correctes mais que la navigation, le langage, les états d’erreur ou les alternatives accessibles ne le sont pas.', '',
    '## Les 31 fonctionnalités décidées','',
]
index.append(table(['ID conception / alias','US fonctionnelle','Lot','Mesures / visualisations'],[
    [f'<a id="us-e{n:02}"></a>E{n:02} · US-E{n:02}',
     f'[US-FON-{n:03} — {specs[n-1]["title"]}](13_backlog_fonctionnel/US-FON-{n:03}.md)',
     by_e[f'E{n:02}']['Lot_technique'],
     f'{len(owned_measures(n))} mesures propriétaires ; '+', '.join(v for v,es in VIS.items() if f'E{n:02}' in es)] for n in range(1,32)]))
index += ['## Exigences transversales','',table(['US','Objet','Application'],[
    [f'[{uid(s["number"])}](13_backlog_fonctionnel/{uid(s["number"])}.md)',s['title'],', '.join(s['related'])] for s in transversals]),
    '## Contrôler qu’aucun besoin ne disparaît','',
    '- [Matrice de couverture des 35 US](13_backlog_fonctionnel/MATRICE_COUVERTURE_US.csv) : rattachements, lots, dépendances, tests et clarifications.',
    '- [Matrice des 29 mesures](13_backlog_fonctionnel/MATRICE_MESURES.csv) : champs, grain, mailles, millésime, unité, population, composant, règles et preuve pour chacune.',
    '- [Matrice des 25 visualisations V01–V25](13_backlog_fonctionnel/MATRICE_VISUALISATIONS.csv) : chacune est reliée à ses US, y compris les deux populations sectorielles distinctes.',
    '- [Matrice des 21 GET](13_backlog_fonctionnel/MATRICE_GET.csv) : couverture et paramètres officiels, sans endpoint ajouté.',
    '- [Matrice des champs JSON et types](13_backlog_fonctionnel/MATRICE_CHAMPS_JSON.csv) : schéma officiel, observation et champs restant à confirmer distingués.',
    '- [Matrice des critères d’acceptation](13_backlog_fonctionnel/MATRICE_CRITERES_ACCEPTATION.csv) : IDs stables et colonnes Étant donné / Quand / Alors, prêtes pour le suivi de recette.',
    '- [Résultat du contrôle documentaire et d’intégrité](13_backlog_fonctionnel/CONTROLE_COMPLETUDE.md).', '',
    'E08 détaille les 14 mesures territoriales, dont `emploi_secteurs` partagé avec E26 qui en conserve le pilotage. E17 détaille les 11 mesures de certification ; E23 les deux sens des mobilités ; E25 les salaires sectoriels ; E26 les secteurs employeurs et la dynamique économique. E24 approfondit la prospective et ses cinq composantes ; E28 réutilise les indicateurs pour deux métiers avec un contrôle de comparabilité. E12 inclut l’export fidèle des données, qui reste à réaliser lorsque l’action DataBox est désactivée.', '',
    '## Preuves, tests et dépendances','',
    '**Documenté** signifie présent au contrat/Swagger ; **observé** signifie présent dans un JSON identifié ; **testé localement** concerne le comportement du prototype sur ce jeu ; **validé HTTP** nécessite une requête réelle avec paramètres, statut et réponse conservés. La rédaction des US ne crée aucune preuve HTTP nouvelle.', '',
    'Les priorités de réalisation sont celles des lots L1 à L10. Les disponibilités partielles ou anomalies fournisseur restent attachées aux fonctionnalités incluses. Q01, Q06, Q07, Q11 et Q14 restent les principaux points fournisseur ; Q05 dépend d’une reproduction avec les champs pluriels corrects. Consulter le tri Q01–Q14 de [06](06_DECISIONS_ET_POINTS_A_VALIDER.md) : les autres points commencent par un GET autonome et ne déclenchent pas une demande RCO inutile.', '',
    'La recette complète reste à réaliser sur HTTP réel, pagination, autres métiers/lieux/cohortes, protection statistique et réponses invalides. Le rechargement natif Ctrl+R/F5, le zoom navigateur 200/400 %, les lecteurs d’écran et la conformité RGAA ne sont pas déclarés validés. Les autres parcours MaCarrière ne sont pas simulés : les pistes sont portables, leur raccordement sera branché lorsque les destinations seront fournies.', '',
    'Le [suivi des travaux restant dans le prototype](BACKLOG_EXPLORER_RESTANT.md) est un tableau d’exécution partiel, complémentaire à ce backlog fonctionnel exhaustif.', '',
    '## Maintenance et conservation','',
    'Les 31 lignes et les colonnes de pilotage de la table sont conservées, avec liens US/SVG et état local courant. La version précédente de ce fichier et de la table est conservée dans [l’archive avant enrichissement](99_archives/2026-11-02_backlog_fonctionnel/ETAT_AVANT.zip). Contrat, Swagger, JSON natifs, UML et référentiel commun de datavisualisation restent intacts.', '',
    'Les données de rédaction dans `13_backlog_fonctionnel/donnees/` et le script `outils/construire_backlog.py` permettent de reconstruire les descriptions et matrices. Pour une évolution, mettre à jour ces sources et la table avant régénération, puis contrôler les différences ; ne pas régénérer après une édition manuelle d’US sans la reporter dans les données de rédaction.', '',
]
(EXPLORER/'04_BACKLOG_USER_STORIES.md').write_text('\n'.join(index),encoding='utf-8')

inventory=read(EXPLORER/'99_archives/2026-11-02_backlog_fonctionnel/INVENTAIRE_AVANT.json')
protected=[item for item in inventory if item.get('protege')]
modified=[item['path'] for item in protected if hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()!=item['sha256']]
assert not modified,modified
assert len(rows)==31
assert [row['Parcours_ID'] for row in rows]==[f'E{n:02}' for n in range(1,32)]
assert set(VIS)=={row['ID'] for row in vis_rows}
assert len(measure_records)==29 and len(visual_records)==25
for spec in specs:
    n=spec['number'];key=uid(n);body=(HERE/f'{key}.md').read_text(encoding='utf-8')
    assert re.findall(r'^## (\d+)\.',body,re.M)==[str(i) for i in range(1,11)],key
    assert len(spec['steps'])>=5 and len(spec['acceptance'])>=4,key
    document=ET.parse(SVG/f'{key}.svg').getroot()
    assert document.find('{http://www.w3.org/2000/svg}title') is not None,key
    assert document.find('{http://www.w3.org/2000/svg}desc') is not None,key

broken=[]
for file in [EXPLORER/'04_BACKLOG_USER_STORIES.md']+list(HERE.glob('US-FON-*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        if target.startswith(('http','mailto:','#')):continue
        path=target.strip('<>').split('#')[0]
        resolved=(file.parent/path).resolve()
        if resolved==HERE/'CONTROLE_COMPLETUDE.md':continue  # produit après les assertions
        if not resolved.exists():broken.append((rel(file,ROOT),target))
assert not broken,broken

checks={
    'date':'2026-11-02','us':35,'fonctionnalites_conservees':31,'us_transversales':4,
    'rubriques_par_us':10,'schemas_svg_accessibles':35,'mesures':29,'visualisations':25,
    'endpoints_get':21,'champs_traces':len(field_records),'criteres_acceptation':len(criteria_records),'liens_internes_rompus':len(broken),
    'references_protegees_verifiees':len(protected),'references_modifiees':modified,
    'requete_HTTP_executee':False,'application_modifiee':False,
}
(HERE/'CONTROLE_COMPLETUDE.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=[
    '# Contrôle du backlog fonctionnel','',
    'Contrôle documentaire exécuté le 2 novembre 2026 par `outils/construire_backlog.py`. Aucune requête HTTP ni exécution de l’application dans ce contrôle.', '',
    table(['Contrôle','Résultat'],[
        ['Fonctionnalités / rattachements E01–E31','31 conservées, alias US-E01–US-E31 maintenus'],
        ['US fonctionnelles','35, dont 4 transversales ; 10 rubriques et au moins 5 étapes nominales chacune'],
        ['Critères',str(len(criteria_records))+' critères identifiés ; au moins 4 spécifiques par US, formulés Étant donné / Quand / Alors ; critères supplémentaires par mesure'],
        ['Schémas SVG','35 XML valides, title/desc et alternative textuelle du scénario'],
        ['Mesures / visualisations','29 notices natives et 25 identifiants V01–V25 reliés aux US'],
        ['Endpoints / paramètres','21 GET officiels couverts ; noms des paramètres de chaque appel contrôlés contre le Swagger'],
        ['Chemins JSON',str(len(field_records))+' occurrences tracées, type officiel / observé / à confirmer distingués'],
        ['Liens internes générés','Aucun lien de fichier rompu'],
        ['Table de conception','31 lignes, colonnes de pilotage d’origine conservées, 5 colonnes de liaison ajoutées'],
        ['Intégrité des références',str(len(protected))+' fichiers protégés comparés par SHA-256 : aucun modifié'],
    ]),'',
    '## Limites du contrôle','',
    'La présence d’un chemin dans la conception n’établit pas qu’il est retourné pour chaque réponse. Les tableaux de types marquent explicitement les chemins non observés et les types non précisés. Les dix endpoints sans schéma officiel nécessitent un test fournisseur/documentaire ciblé ; aucun schéma dérivé n’a été élevé au rang de contrat officiel.', '',
    'Ce contrôle vérifie les documents et leur traçabilité. Il ne valide ni des valeurs métier nouvelles, ni un fonctionnement HTTP, ni le rendu responsive de l’application, ni une conformité RGAA. Les recettes antérieures sont référencées avec leurs limites ; aucune compilation de l’application n’est nécessaire pour cette modification documentaire.', '',
    'Une tentative de capture du SVG de comparaison dans Edge a échoué au démarrage du navigateur avec « Accès refusé » (canal Mojo/crashpad du bac à sable). Le rendu visuel navigateur des SVG n’est donc pas déclaré vérifié. Les 35 SVG ont été contrôlés comme XML, avec titre, description et scénario textuel équivalent ; ils restent directement ouvrables dans un navigateur.', '',
    '## Réexécution','',
    'Depuis la racine, exécuter le script Python `07_parcours/Explorer/13_backlog_fonctionnel/outils/construire_backlog.py`. Il reconstruit les documents depuis la table et les données de rédaction ; conserver toute modification éditoriale dans ces sources avant de le relancer.', '',
    'Exécuter ensuite `07_parcours/Explorer/13_backlog_fonctionnel/outils/verifier_backlog.py`. Cette seconde lecture contrôle les fichiers livrés, leur contenu réel, les critères Markdown/CSV, les champs conservés par rapport à l’archive et les paramètres requis officiels. Son dernier résultat est enregistré dans [VERIFICATION_INDEPENDANTE.json](VERIFICATION_INDEPENDANTE.json).', '',
    'Les empreintes avant travail et les précédents fichiers sont dans `../99_archives/2026-11-02_backlog_fonctionnel/`. Le rapport structuré correspondant est [CONTROLE_COMPLETUDE.json](CONTROLE_COMPLETUDE.json).', '',
]
(HERE/'CONTROLE_COMPLETUDE.md').write_text('\n'.join(report),encoding='utf-8')
assert (HERE/'CONTROLE_COMPLETUDE.md').exists()
print(json.dumps(checks,ensure_ascii=True))
