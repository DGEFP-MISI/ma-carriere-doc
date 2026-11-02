"""Audit hors-ligne : inventaire des opérations du dernier docs.json et comparaison de version."""
import json, csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CURRENT=ROOT/'01_sources/openapi/docs_json_interface.json'
PREVIOUS=ROOT/'01_sources/openapi/swagger_precedent.json'
OUT=ROOT/'06_controles/resultats'; OUT.mkdir(parents=True,exist_ok=True)
new=json.loads(CURRENT.read_text(encoding='utf-8'))
old=json.loads(PREVIOUS.read_text(encoding='utf-8'))
def methods(data):
 return {(p,verb): op for p,entries in data['paths'].items() for verb,op in entries.items() if verb in ('get','post','put','patch','delete')}
a,b=methods(new),methods(old)
with (OUT/'comparaison_openapi.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['methode','endpoint','dans_docs_interface','dans_swagger_precedent','parametres_ajoutes','parametres_retires','schema_200_present'])
 for path,verb in sorted(a.keys()|b.keys()):
  n=a.get((path,verb),{});o=b.get((path,verb),{})
  x={p['name'] for p in n.get('parameters',[])}; y={p['name'] for p in o.get('parameters',[])}
  sch=n.get('responses',{}).get('200',{}).get('content',{}).get('application/json',{}).get('schema')
  w.writerow([verb.upper(),path,'oui' if n else 'non','oui' if o else 'non',','.join(sorted(x-y)),','.join(sorted(y-x)),'oui' if sch else 'non'])
print('Endpoints dans docs interface :', len(a))
print('Endpoints dans Swagger précédent :', len(b))
print('Rendu dans :',OUT/'comparaison_openapi.csv')
