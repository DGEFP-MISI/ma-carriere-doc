from pathlib import Path
import json, csv
ROOT=Path(__file__).resolve().parents[1]
OPENAPI=ROOT/'03_catalogue/docs_json_ENRICHI_NON_OFFICIEL.json'
SRC=ROOT/'02_reponses_observees'
OUT=ROOT/'06_controles/resultats/comparaison_schemas_complementaires.csv'
a=json.loads(OPENAPI.read_text(encoding='utf-8'))
with (SRC/'inventaire_echantillons.csv').open(encoding='utf-8-sig',newline='') as f: entries=list(csv.DictReader(f,delimiter=';'))
res=[]
def check_node(obj,schema,path='$'):
 errors=[]
 if not isinstance(schema,dict):return errors
 if isinstance(obj,dict):
  props=schema.get('properties',{})
  for k,v in obj.items():
   if k not in props:errors.append(path+'.'+k)
   else:errors+=check_node(v,props[k],path+'.'+k)
 elif isinstance(obj,list):
  item=schema.get('items',{})
  for i,v in enumerate(obj):errors+=check_node(v,item,path+'[]')
 return errors
for entry in entries:
 ep=entry['endpoint_associe'];f=entry['fichier_relatif']
 s=a['paths'][ep]['get']['responses']['200'].get('content',{}).get('application/json',{}).get('schema',{})
 obj=json.loads((SRC/f).read_text(encoding='utf-8'))
 missing=sorted(set(check_node(obj,s)))
 res.append((f,ep,'OK_CHAMPS_OBSERVES_DECRITS' if not missing else 'CHAMPS_A_EXAMINER',' | '.join(missing)))
OUT.parent.mkdir(exist_ok=True,parents=True)
with OUT.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['fichier','endpoint','etat','champs_observes_non_decrits']);w.writerows(res)
print('Endpoints documentes (200 schema) :', sum(bool(v['get'].get('responses',{}).get('200',{}).get('content',{}).get('application/json',{}).get('schema',{})) for v in a['paths'].values()), '/',len(a['paths']))
print('Fichiers analyses :',len(res))
print('Echantillons avec champs non decrits :',sum(x[2]!='OK_CHAMPS_OBSERVES_DECRITS' for x in res))
print('Rapport :',OUT)
print('ATTENTION : verifier les champs ne valide pas les types, les endpoints en direct ou les relations SQL.')
