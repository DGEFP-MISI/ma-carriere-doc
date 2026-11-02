"""Vérifie l'intégrité des références, les 31 IDs et les dépendances de la livraison."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
EXPLORER = ROOT / '07_parcours/Explorer'
snapshot = json.loads((EXPLORER / '99_archives/2026-11-02_dsfr_chart/INVENTAIRE_AVANT.json').read_text(encoding='utf-8-sig'))
protected = []
changed = []
for item in snapshot:
    rel = item['path']
    path = ROOT / rel
    intact = path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']
    if rel.startswith(('01_sources/', '02_reponses_observees/', '03_', '04_', '05_', '06_controles/', '07_parcours/00_REFERENTIEL_COMMUN_DATAVISUALISATION/')):
        protected.append({'path': rel, 'intact': intact})
    if not intact:
        changed.append(rel)
rows = list(csv.DictReader((EXPLORER / '03_TABLE_CONCEPTION.csv').open(encoding='utf-8-sig'), delimiter=';'))
ids = [row['Parcours_ID'] for row in rows]
report = {
    'date': '2026-11-02',
    'references_protegees': len(protected),
    'references_modifiees': [r['path'] for r in protected if not r['intact']],
    'fichiers_preexistants_modifies': changed,
    'conception_ids': ids,
    'conception_31_ids': len(ids) == 31 and set(ids) == {f'E{i:02}' for i in range(1, 32)},
    'controle_http_realise': False,
}
destination = EXPLORER / '12_maquette_html/controles/resultats/INTEGRITE_DSFR_CHART.json'
destination.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
assert not report['references_modifiees'], report['references_modifiees']
assert report['conception_31_ids'], ids
print(f"{len(protected)} références intactes ; E01–E31 conservés ; aucun test HTTP déclaré.")
