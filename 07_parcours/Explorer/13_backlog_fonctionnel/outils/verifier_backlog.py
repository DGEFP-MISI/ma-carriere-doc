"""Vérifie les fichiers livrés, sans les régénérer ni modifier l'application."""
import csv
import hashlib
import io
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
EXPLORER=HERE.parent
ROOT=EXPLORER.parents[1]

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def records(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream,delimiter=';'))

def check(condition,message):
    if not condition: raise AssertionError(message)

rows=records(EXPLORER/'03_TABLE_CONCEPTION.csv')
check([r['Parcours_ID'] for r in rows]==[f'E{n:02}' for n in range(1,32)],'31 IDs de conception')
archive=EXPLORER/'99_archives/2026-11-02_backlog_fonctionnel'
with zipfile.ZipFile(archive/'ETAT_AVANT.zip') as snapshot:
    old=list(csv.DictReader(io.StringIO(snapshot.read('07_parcours/Explorer/03_TABLE_CONCEPTION.csv').decode('utf-8-sig')),delimiter=';'))
check(set(old[0])<=set(rows[0]),'Colonnes de pilotage conservées')
for before,after in zip(old,rows):
    check(before['Parcours_ID']==after['Parcours_ID'],'Identité de ligne')
    check(json.loads(before['Appels_GET_detail'])==json.loads(after['Appels_GET_detail']),'Appels et champs existants conservés')
    check(before['Lot_technique']==after['Lot_technique'],'Lot conservé')

api=read(ROOT/'01_sources/openapi/docs_json_interface.json')
official={path:operation['get'] for path,operation in api['paths'].items() if 'get' in operation}
get_matrix=records(HERE/'MATRICE_GET.csv')
check({r['Endpoint'] for r in get_matrix}==set(official),'21 GET couverts sans ajout')
for r in get_matrix:
    check(json.loads(r['Parametres_officiels'])==official[r['Endpoint']].get('parameters',[]),'Paramètres officiels fidèles')
    check(bool(r['US']),'Au moins une US pour chaque GET')
for row in rows:
    for call in json.loads(row['Appels_GET_detail']):
        parameters={p['name']:p for p in official[call['endpoint']].get('parameters',[])}
        check(set(call['parametres'])<=set(parameters),'Aucun paramètre inventé')
        required={name for name,p in parameters.items() if p.get('required')}
        check(required<=set(call['parametres']),'Paramètres requis présents')

catalogue=read(ROOT/'02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json')['items']
measures=records(HERE/'MATRICE_MESURES.csv')
check(len(measures)==29 and {m['Mesure'] for m in measures}=={m['code'] for m in catalogue},'29 mesures couvertes')
by_code={m['Mesure']:m for m in measures}
for m in catalogue:
    record=by_code[m['code']]
    check(record['Grain']==m['grain'] and record['Millesime_observe']==str(m['millesime']),'Grain et millésime natifs')
    check(all('.'+field in record['Chemins_JSON'].split(',')[i] for i,field in enumerate(m['champs'])),'Tous les champs de mesure conservés')
    check(all(record[key] for key in ['Unites_populations','Presentation','Regles','Tests_dependances','Preuve']),'Mesure définie et testable')
    owner=(HERE/(record['US_proprietaire']+'.md')).read_text(encoding='utf-8')
    check(f'#### `{m["code"]}`' in owner,'Fiche technique dans l’US propriétaire')
check(len(records(HERE/'MATRICE_VISUALISATIONS.csv'))==25,'25 visualisations')
check({r['ID'] for r in records(HERE/'MATRICE_VISUALISATIONS.csv')}=={f'V{n:02}' for n in range(1,26)},'V01–V25')

coverage=records(HERE/'MATRICE_COUVERTURE_US.csv')
criteria=records(HERE/'MATRICE_CRITERES_ACCEPTATION.csv')
check(len(coverage)==35,'35 US dans le suivi')
check(len({r['Critere_ID'] for r in criteria})==len(criteria),'Critères uniques')
counts=Counter(r['US_ID'] for r in criteria)
broken=[]
for row in coverage:
    file=HERE/row['Fichier_US'];body=file.read_text(encoding='utf-8')
    check('\ufffd' not in body,'Aucun caractère de remplacement Unicode')
    check(re.findall(r'^## (\d+)\.',body,re.M)==[str(n) for n in range(1,11)],'10 sections exactes')
    section=body.split('## 4. Scénario nominal')[1].split('## 5.')[0]
    check(len(re.findall(r'^\| \d+ \|',section,re.M))>=5,'Scénario nominal détaillé')
    ids=re.findall(r'\*\*(US-FON-\d{3}-CA-\d+)\*\*',body)
    check(len(ids)==counts[row['US_ID']] and len(ids)>=6,'Critères synchronisés Markdown / CSV')
    for criterion in (c for c in criteria if c['US_ID']==row['US_ID']):
        check(all(criterion[key] in body for key in ['Etant_donne','Quand','Alors']),'Texte des critères fidèle')
    document=ET.parse(HERE/row['Schema_SVG']).getroot()
    check(document.tag=='{http://www.w3.org/2000/svg}svg','SVG valide')
    check(document.get('role')=='img' and document.get('aria-labelledby')=='titre description','Nom accessible du SVG')
    check(len(document.findall('.//{http://www.w3.org/2000/svg}text'))>=10,'Schéma contenant le parcours')
    if row['Conception_ID']:
        conception=next(r for r in rows if r['Parcours_ID']==row['Conception_ID'])
        for call in json.loads(conception['Appels_GET_detail']):
            fields=call['champs']+[f for fs in call.get('mesures',{}).values() for f in fs]
            check(all('`'+field+'`' in body for field in fields),'Champs de conception présents dans l’US')
for file in [EXPLORER/'04_BACKLOG_USER_STORIES.md',EXPLORER/'README.md',EXPLORER/'BACKLOG_EXPLORER_RESTANT.md',ROOT/'07_parcours/00_MODELE_COMMUN_USER_STORIES/MODELE_US_FONCTIONNELLE.md']+list(HERE.glob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        target=target.strip('<>')
        if target.startswith(('http','mailto:','#')):continue
        if not (file.parent/target.split('#')[0]).exists(): broken.append((str(file),target))
check(not broken,'Liens internes : '+str(broken))
protected=[p for p in read(archive/'INVENTAIRE_AVANT.json') if p.get('protege')]
for p in protected:
    check(hashlib.sha256((ROOT/p['path']).read_bytes()).hexdigest()==p['sha256'],'Référence intacte : '+p['path'])

result={'resultat':'OK','us':35,'fonctionnalites':31,'mesures':29,'visualisations':25,'GET':21,'criteres':len(criteria),'references_intactes':len(protected),'liens_rompus':0,'application_ou_HTTP_testes':False}
(HERE/'VERIFICATION_INDEPENDANTE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
