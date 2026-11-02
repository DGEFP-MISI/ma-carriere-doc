"""Vérifie l'évolution documentaire et le maintien des invariants API."""
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
EXPLORER=HERE.parents[1]
ROOT=EXPLORER.parents[1]
before=json.loads((HERE/'INVENTAIRE_AVANT.json').read_text(encoding='utf-8'))
outside=[r for r in before if not r['path'].startswith('07_parcours/Explorer/')]
changed=[r['path'] for r in outside if not (ROOT/r['path']).is_file() or hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()!=r['sha256']]
with zipfile.ZipFile(HERE/'ETAT_AVANT.zip') as archive:
    old=list(csv.DictReader(io.StringIO(archive.read('03_TABLE_CONCEPTION.csv').decode('utf-8-sig')),delimiter=';'))
with (EXPLORER/'03_TABLE_CONCEPTION.csv').open(encoding='utf-8-sig',newline='') as stream:
    reader=csv.DictReader(stream,delimiter=';');fields=reader.fieldnames;rows=list(reader)
api_changes=[r['Parcours_ID'] for r,prior in zip(rows,old) if any(r[k]!=prior[k] for k in fields if k not in {'Composant_UI','Critere_acceptation'})]
ids_ok=len(rows)==31 and {r['Parcours_ID'] for r in rows}=={f'E{i:02}' for i in range(1,32)}
links,missing=0,[]
for path in EXPLORER.rglob('*.md'):
    if any(part in {'archives','99_archives'} for part in path.relative_to(EXPLORER).parts):continue
    for href in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8-sig')):
        target=href.strip('<>').split('#',1)[0]
        if not target or re.match(r'(https?://|mailto:|app:|plugin:)',target):continue
        links+=1
        if not (path.parent/unquote(target)).exists():missing.append({'doc':str(path.relative_to(EXPLORER)),'lien':target})
reports={k:json.loads((EXPLORER/f'12_maquette_html/controles/resultats/CONTROLE_{k}.json').read_text(encoding='utf-8-sig')) for k in ['DESKTOP','MOBILE']}
result={'date':'2026-11-02','references_hors_explorer':len(outside),'references_modifiees':changed,'ids_31_conserves':ids_ok,'colonnes_table':len(fields),'modifications_API_dans_table':api_changes,'liens_verifies':links,'liens_casses':missing,'tests_locaux':{k:{'reussis':v.get('passed'),'echoues':v.get('failed')} for k,v in reports.items()},'nouveaux_tests_HTTP':False,'autres_parcours_reellement_relies':False,'persistance_prototype':'session d’onglet et fichier de reprise, pas de compte serveur'}
(HERE/'VERIFICATION_EVOLUTION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(1 if changed or not ids_ok or api_changes or missing or any(v.get('failed') for v in reports.values()) else 0)
