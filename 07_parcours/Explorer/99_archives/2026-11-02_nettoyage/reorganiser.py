"""Journal exécutable du rangement du 2 novembre 2026, limité à Explorer."""
import csv
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path

EXPLORER = Path(__file__).resolve().parents[2]
ROOT = EXPLORER.parents[1]
ARCHIVE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def safe(path):
    path = path.resolve()
    if not path.is_relative_to(EXPLORER):
        raise ValueError(f"Cible hors Explorer : {path}")
    return path

def write(path, text):
    path = safe(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def move(old, new):
    source, target = safe(EXPLORER / old), safe(EXPLORER / new)
    if not source.exists():
        raise FileNotFoundError(source)
    if target.exists():
        raise FileExistsError(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(target))
    moves.append({"avant": old, "apres": new})

if (ARCHIVE / "INVENTAIRE_AVANT.json").exists():
    raise SystemExit("Le rangement a déjà été lancé. Consulter son journal avant toute reprise.")
before = [{"path": str(p.relative_to(ROOT)).replace("\\", "/"), "sha256": sha(p)}
          for p in sorted(ROOT.rglob("*")) if p.is_file() and p != Path(__file__).resolve()]
write(ARCHIVE / "INVENTAIRE_AVANT.json", json.dumps(before, ensure_ascii=False, indent=2))
with zipfile.ZipFile(ARCHIVE / "LIVRABLES_L0_AVANT_MISE_A_JOUR.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(EXPLORER.glob("[0-9][0-9]_*.md")):
        archive.write(path, path.name)
    archive.write(EXPLORER / "03_TABLE_CONCEPTION.csv", "03_TABLE_CONCEPTION.csv")

moves = []
base = "12_maquette_html/"
archive12 = base + "archives/2026-11-02_avant_rangement/"
for filename in ["LIRE_MOI.md", "AFFICHAGE_GRAND_PUBLIC.md", "libelles_publics.js"]:
    move(base + filename, archive12 + filename)
shutil.copy2(EXPLORER / base / "modele.html", EXPLORER / archive12 / "modele_avec_script_initial.html")
for filename in ["construire.py", "interface_citoyenne.js", "modele.html"]:
    move(base + filename, base + "sources/" + filename)
for filename in ["verifier_navigateur.js", "extraire_controle.py"]:
    move(base + filename, base + "controles/scripts/" + filename)
for filename in ["CONTROLE_DESKTOP.json", "CONTROLE_MOBILE.json", "ASSEMBLAGE.json"]:
    move(base + filename, base + "controles/resultats/" + filename)
for filename in ["controle-desktop.dom.html", "controle-mobile.dom.html"]:
    move(base + filename, base + "controles/traces/" + filename)
move(base + "controle-mobile.html", base + "controles/controle-mobile.html")
for filename in ["apercu-desktop.png", "apercu-mobile.png"]:
    move(base + filename, base + "apercus/" + filename)
move(base + "PREUVES_LIBELLES.json", base + "preuves/PREUVES_LIBELLES.json")
move(base + "REDACTION_CITOYENNE.md", base + "documentation/REDACTION_CITOYENNE.md")

# Conserver les rendus initiaux et leurs liens relatifs dans un même ensemble.
old_ux = "11_ux_ui/archives/conception_initiale/"
for filename in ["mobile", "apercus_controle", "ARCHITECTURE_EXPERIENCE.svg", "ETATS_ET_ERREURS.svg", "PLANCHE_VISUALISATIONS.svg", "controle_apercus.ps1"]:
    move("11_ux_ui/" + filename, old_ux + filename)
for filename in ["CONCEPTION_UX_UI.md", "LIVRAISON_ET_RECETTE.md"]:
    path = EXPLORER / "11_ux_ui" / filename
    text = path.read_text(encoding="utf-8-sig")
    note = "\n**Statut au 2 novembre 2026 :** conception initiale conservée pour les preuves et la structure. Pour la présentation actuelle, consulter [le HTML citoyen](../12_maquette_html/index.html) et [sa règle éditoriale](../12_maquette_html/documentation/REDACTION_CITOYENNE.md). Les visuels initiaux et les constats Figma de ce document ne prouvent pas l'état actuel de l'interface HTML.\n"
    first, rest = text.split("\n", 1)
    text = first + "\n" + note + rest
    for target in ["mobile/", "ARCHITECTURE_EXPERIENCE.svg", "ETATS_ET_ERREURS.svg", "PLANCHE_VISUALISATIONS.svg"]:
        text = text.replace("](" + target, "](archives/conception_initiale/" + target)
    write(path, text)

# Le gabarit actif contient seulement l'enveloppe ; plus de JavaScript initial mort.
template = EXPLORER / base / "sources/modele.html"
text = template.read_text(encoding="utf-8-sig")
text, count = re.subn(r"<script>\s*'use strict';.*?</script>", "<script>\n__EXPLORER_INTERFACE__\n</script>", text, count=1, flags=re.S)
if count != 1:
    raise ValueError("Script initial du gabarit non trouvé")
text = text.replace("</style>", 'h1[tabindex="-1"]:focus{outline:none}.catalog-card{min-width:0;overflow-wrap:anywhere}.catalog-card code{word-break:break-word}</style>')
write(template, text)

# Sortir du constructeur les corrections éditoriales, désormais dans le vrai source.
builder = EXPLORER / base / "sources/construire.py"
text = builder.read_text(encoding="utf-8-sig")
start = text.index("for before, after in ")
end = text.index("html = re.sub(", start)
transforms = text[start:end]
citizen_path = EXPLORER / base / "sources/interface_citoyenne.js"
scope = {"citizen_js": citizen_path.read_text(encoding="utf-8-sig")}
exec(transforms, {}, scope)
write(citizen_path, scope["citizen_js"])
text = text[:start] + text[end:]
text = text.replace("HERE = Path(__file__).resolve().parent\nROOT = HERE.parents[2]", "SOURCE = Path(__file__).resolve().parent\nHERE = SOURCE.parent\nROOT = HERE.parents[2]\nCONTROLES = HERE / 'controles'\nRESULTATS = CONTROLES / 'resultats'\nPREUVES = HERE / 'preuves'\nfor directory in (CONTROLES, RESULTATS, PREUVES):\n    directory.mkdir(parents=True, exist_ok=True)")
text = text.replace('(HERE / "modele.html")', '(SOURCE / "modele.html")').replace('(HERE / "interface_citoyenne.js")', '(SOURCE / "interface_citoyenne.js")')
text = text.replace("import re\n", "")
old = 'html = re.sub(r"<script>\\s*\'use strict\';.*?</script>", lambda _: "<script>\\n" + citizen_js + "\\n</script>", html, count=1, flags=re.S)'
if old not in text:
    raise ValueError("Injection historique non trouvée")
text = text.replace(old, 'assert html.count("__EXPLORER_INTERFACE__") == 1\nhtml = html.replace("__EXPLORER_INTERFACE__", citizen_js)')
text = text.replace('(HERE / "verifier_navigateur.js")', '(CONTROLES / "scripts/verifier_navigateur.js")')
text = "\n".join(line for line in text.split("\n") if not line.startswith('html = html.replace("</style>"'))
text = text.replace('(HERE / "controle-mobile.html")', '(CONTROLES / "controle-mobile.html")')
text = text.replace('(HERE / "ASSEMBLAGE.json")', '(RESULTATS / "ASSEMBLAGE.json")')
text = text.replace('(HERE / "PREUVES_LIBELLES.json")', '(PREUVES / "PREUVES_LIBELLES.json")')
write(builder, text)

extract = EXPLORER / base / "controles/scripts/extraire_controle.py"
text = extract.read_text(encoding="utf-8-sig").replace('here = Path(__file__).resolve().parent', 'here = Path(__file__).resolve().parents[1]')
text = text.replace('(here / f"controle-{kind}.dom.html")', '(here / "traces" / f"controle-{kind}.dom.html")')
text = text.replace('(here / f"CONTROLE_{kind.upper()}.json")', '(here / "resultats" / f"CONTROLE_{kind.upper()}.json")')
write(extract, text)
write(ARCHIVE / "DEPLACEMENTS.json", json.dumps(moves, ensure_ascii=False, indent=2))
print(json.dumps({"deplacements": len(moves), "fichiers_avant": len(before), "suppression": 0}, ensure_ascii=False))
