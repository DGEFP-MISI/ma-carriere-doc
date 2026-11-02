"""Contrôle statique hors ligne de la carte UML strictement API ROME V3.
Ne remplace PAS le moteur de rendu PlantUML ni des appels live à l'API.
"""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '05_uml' / '00_modele_global'
MAP = BASE / '02_CARTE_21_GET_API.puml'
OPENAPI = ROOT / '01_sources' / 'openapi' / 'docs_json_interface.json'
MATRIX = ROOT / '04_relations' / 'matrice_statuts_apres_tests.csv'

def require(ok, message):
    if not ok:
        raise SystemExit('ECHEC : ' + message)

for p in (MAP, OPENAPI, MATRIX):
    require(p.is_file(), f'fichier introuvable: {p.relative_to(ROOT)}')
api = json.loads(OPENAPI.read_text(encoding='utf-8-sig'))
expected = {path for path, ops in api['paths'].items() if 'get' in ops}
other_methods = [(path, method.upper()) for path, ops in api['paths'].items()
                 for method in ('post', 'put', 'patch', 'delete') if method in ops]
require(len(expected) == 21 and not other_methods,
        f'Swagger non conforme au perimetre 21 GET: {len(expected)} GET, autres={other_methods}')
content = MAP.read_text(encoding='utf-8')
found = re.findall(r'^\s*component\s+"GET\s+(/[^"\n]+)"\s+as\s+[A-Za-z_]\w*', content, flags=re.MULTILINE)
print('GET Swagger :', len(expected))
print('GET representes dans la carte UML :', len(found))
if set(found) != expected or len(found) != len(expected):
    print('Manquants :', sorted(expected-set(found)))
    print('Inattendus :', sorted(set(found)-expected))
    print('Doublons :', sorted({x for x in found if found.count(x)>1}))
    raise SystemExit(1)
with MATRIX.open('r', encoding='utf-8-sig', newline='') as f:
    relationships = list(csv.DictReader(f, delimiter=';'))
require(len(relationships)==24 and len({r['id'] for r in relationships})==24,
        f'Matrice attendue de 24 relations uniques, observee: {len(relationships)}')
puml=sorted(BASE.glob('*.puml'))
require(len(puml)==3, f'3 diagrammes de reference attendus, observes: {len(puml)}')
for p in puml:
    t=p.read_text(encoding='utf-8-sig')
    require(t.lstrip().startswith('@startuml') and t.count('@enduml')==1,
            f'Bornes PlantUML incorrectes: {p.name}')
    require('octopilot.public.' not in t.lower() and 'octopilot.data_rco.' not in t.lower(),
            f'Table interne non autorisee dans le modele strict: {p.name}')
print('Relations dans la matrice :',len(relationships))
print('Diagrammes UML de reference :',len(puml))
print('OK : carte UML strictement 21 GET et ROME V3, inventaire coherent.')
print('Limite : controle textuel, sans execution de PlantUML ni interrogation de l API.')
