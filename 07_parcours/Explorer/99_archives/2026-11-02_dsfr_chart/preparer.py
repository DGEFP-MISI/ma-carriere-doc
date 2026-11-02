"""Sauvegarde l'état et compare la référence PROPRE sans la modifier."""
import hashlib,json,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
EXPLORER=HERE.parents[1]
ROOT=EXPLORER.parents[1]
if (HERE/'ETAT_AVANT.zip').exists():raise SystemExit('État déjà sauvegardé.')
files=[p for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(HERE)]
inventory=[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
(HERE/'INVENTAIRE_AVANT.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
with zipfile.ZipFile(HERE/'ETAT_AVANT.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for p in files:
        if p.is_relative_to(EXPLORER) and not any(x in {'archives','99_archives','traces','apercus'} for x in p.relative_to(EXPLORER).parts):archive.write(p,p.relative_to(EXPLORER))
reference=ROOT.parent/'API_DGEFP_RCO_REFERENCE_V3_PROPRE.zip'
comparison=[]
with zipfile.ZipFile(reference) as archive:
    for item in archive.infolist():
        if item.is_dir():continue
        parts=Path(item.filename).parts
        start=next((i for i,p in enumerate(parts) if p.startswith(('01_sources','02_reponses_observees','03_catalogue','04_relations','05_uml','06_controles'))),None)
        if start is None:continue
        relative=Path(*parts[start:]);target=ROOT/relative
        comparison.append({'path':str(relative).replace('\\','/'),'present':target.is_file(),'identique':target.is_file() and hashlib.sha256(target.read_bytes()).digest()==hashlib.sha256(archive.read(item)).digest()})
(HERE/'COMPARAISON_REFERENCE_PROPRE.json').write_text(json.dumps({'archive':reference.name,'sha256':hashlib.sha256(reference.read_bytes()).hexdigest(),'fichiers':comparison},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'references_comparees':len(comparison),'ecarts':[x for x in comparison if not x['identique']]},ensure_ascii=False))
