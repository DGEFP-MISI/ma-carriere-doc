"""Exécute la batterie locale et sort avec erreur si un des contrôles échoue.
Aucune requête réseau. N'utilise que Python standard.
"""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=['verifier_contrat.py','verifier_echantillons.py','verifier_schemas_complementaires.py',
         'verifier_relations_api.py','verifier_uml_global.py','verifier_preuves_directes.py']
errors=[]
for script in SCRIPTS:
    print(f'\n===== {script} =====',flush=True)
    res=subprocess.run([sys.executable,str(ROOT/'scripts'/script)],cwd=ROOT,check=False)
    if res.returncode:
        errors.append((script,res.returncode))
print('\n===== SYNTHESE =====')
if errors:
    print('ECHEC de',len(errors),'contrôle(s) :', errors)
    sys.exit(1)
print('OK :',len(SCRIPTS),'contrôles exécutés avec succès.')
print('Hors ligne ; les conclusions ne prouvent ni les types sur tous les cas ni les appels HTTP live.')
