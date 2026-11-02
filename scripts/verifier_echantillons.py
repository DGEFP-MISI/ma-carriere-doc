"""Audit hors ligne non destructif. Compare les clés JSON observées aux propriétés OpenAPI déclarées."""
import json, csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SWAG=json.loads((ROOT/'01_sources/openapi/docs_json_interface.json').read_text(encoding='utf8'))
SOURCE=ROOT/'02_reponses_observees';OUT=ROOT/'06_controles/resultats';OUT.mkdir(parents=True,exist_ok=True)
with (SOURCE/'inventaire_echantillons.csv').open(encoding='utf-8-sig',newline='') as f:
 entries=list(csv.DictReader(f,delimiter=';'))
rows=[]
for ent in entries:
 p=SOURCE/ent['fichier_relatif'];ep=ent['endpoint_associe']
 try: obj=json.loads(p.read_text(encoding='utf8'))
 except Exception as e: rows.append([ent['fichier_relatif'],ep,'json_invalide','','',str(e)]);continue
 op=SWAG.get('paths',{}).get(ep,{}).get('get',{})
 schema=op.get('responses',{}).get('200',{}).get('content',{}).get('application/json',{}).get('schema',{})
 if not schema:
  rows.append([ent['fichier_relatif'],ep,'schema_200_non_documente','','','Ne permet pas de conclure à une absence de champ']);continue
 props=schema.get('properties',{})
 observed=set(obj.keys()) if isinstance(obj,dict) else set()
 extra=sorted(observed-set(props))
 items= obj.get('items') if isinstance(obj,dict) else None
 item_schema=props.get('items',{}).get('items',{})
 item_props=set(item_schema.get('properties',{}))
 observed_item=set().union(*(set(item) for item in items if isinstance(item,dict))) if isinstance(items,list) else set()
 missing_item=sorted(observed_item-item_props) if item_props else []
 rows.append([ent['fichier_relatif'],ep,'comparaison_champs_observes',','.join(extra),','.join(missing_item),
   'Des clés absentes peuvent résulter de fields, pagination ou variantes des paramètres'])
with (OUT/'comparaison_echantillons.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['fichier','endpoint','etat','cles_racine_non_declarees','cles_items_non_declarees','limite']);w.writerows(rows)
print('Échantillons analysés :', len(rows));print('Sans schéma 200 :',sum(x[2]=='schema_200_non_documente' for x in rows))
print('Rapport :', OUT/'comparaison_echantillons.csv')
