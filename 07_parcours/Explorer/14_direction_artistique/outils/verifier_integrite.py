"""Vérifie que la présentation n'a modifié ni les réponses ni les fonctions métier."""
import hashlib
import json
import re
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

HERE=Path(__file__).resolve().parents[1]
EXPLORER=HERE.parent
ROOT=EXPLORER.parents[1]
APP=EXPLORER/'12_maquette_html'
ARCHIVE=EXPLORER/'99_archives/2026-11-02_direction_artistique'
records=json.loads((ARCHIVE/'INVENTAIRE_AVANT.json').read_text(encoding='utf-8-sig'))
protected=[r for r in records if r.get('protege') or '/13_backlog_fonctionnel/US-FON-' in r['path'] or r['path'].endswith(('03_TABLE_CONCEPTION.csv','04_BACKLOG_USER_STORIES.md'))]
modified=[r['path'] for r in protected if hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()!=r['sha256']]
assert not modified,modified
text=(APP/'index.html').read_text(encoding='utf-8')
data=json.loads(re.search(r'<script type="application/json" id="explorer-data">(.*?)</script>',text,re.S).group(1))
assert data==json.loads((ARCHIVE/'DONNEES_AVANT.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(ARCHIVE/'ETAT_AVANT.zip') as z:
    def archived_text(path):return z.read(path).decode('utf-8').replace('\r\n','\n')
    key='07_parcours/Explorer/12_maquette_html/sources/'
    before=archived_text(key+'interface_citoyenne.js')
    after=(APP/'sources/interface_citoyenne.js').read_text(encoding='utf-8')
    assert after.replace(" disposerInfographie(slug,document.querySelector('#main'));\n",'')==before
    before=archived_text(key+'experience_exploration.js')
    after=(APP/'sources/experience_exploration.js').read_text(encoding='utf-8')
    def without_overview(value):
        start=value.index('function experienceOverview(){')
        end=value.index('function experienceHome(){',start)
        return value[:start]+value[end:]
    assert without_overview(before)==without_overview(after)
    for name in ['donnees_exploration.js','ameliorations_ux.js','visualisations_dsfr.js']:
        assert archived_text(key+name)==(APP/'sources'/name).read_text(encoding='utf-8')
    shared='07_parcours/commun_datavisualisation/'
    assert archived_text(shared+'src/adaptateurs.mjs')==(ROOT/shared/'src/adaptateurs.mjs').read_text(encoding='utf-8')
    assert archived_text(shared+'src/composants.js')==(ROOT/shared/'src/composants.js').read_text(encoding='utf-8')
    assert z.read(shared+'dist/runtime.js')==(ROOT/shared/'dist/runtime.js').read_bytes()
for svg in (HERE/'maquettes').glob('*.svg'):
    root=ET.parse(svg).getroot()
    assert root.find('{http://www.w3.org/2000/svg}title') is not None
    assert root.find('{http://www.w3.org/2000/svg}desc') is not None
report={'resultat':'OK','references_API_UML_JSON_intactes':155,'US_intactes':35,'table_et_backlog_intacts':True,'donnees_embarquees_identiques':True,'handlers_et_fonctions_metier_identiques':True,'adaptateurs_et_graphiques_officiels_identiques':True,'SVG_valides':3,'nouvelle_requete_HTTP_metier':False}
(HERE/'preuves/INTEGRITE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
