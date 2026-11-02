"""Vérifie les références et invariants du rangement, sans test HTTP."""
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

EXPLORER = Path(__file__).resolve().parents[2]
ROOT = EXPLORER.parents[1]
HERE = Path(__file__).resolve().parent
before = json.loads((HERE / "INVENTAIRE_AVANT.json").read_text(encoding="utf-8"))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
outside = [r for r in before if not r["path"].startswith("07_parcours/Explorer/")]
changed = [r["path"] for r in outside if not (ROOT / r["path"]).is_file() or sha(ROOT / r["path"]) != r["sha256"]]
movements = json.loads((HERE / "DEPLACEMENTS.json").read_text(encoding="utf-8"))
missing_before = []
for record in before:
    if not record["path"].startswith("07_parcours/Explorer/"):
        continue
    relative = record["path"][len("07_parcours/Explorer/"):]
    destination = relative
    for movement in sorted(movements, key=lambda m:len(m["avant"]), reverse=True):
        if relative == movement["avant"] or relative.startswith(movement["avant"]+"/"):
            destination = movement["apres"] + relative[len(movement["avant"]):]
            break
    if not (EXPLORER / destination).is_file():
        missing_before.append(record["path"])
with zipfile.ZipFile(HERE / "LIVRABLES_L0_AVANT_MISE_A_JOUR.zip") as archive:
    original = list(csv.DictReader(io.StringIO(archive.read("03_TABLE_CONCEPTION.csv").decode("utf-8-sig")), delimiter=";"))
with (EXPLORER / "03_TABLE_CONCEPTION.csv").open(encoding="utf-8-sig", newline="") as stream:
    reader = csv.DictReader(stream, delimiter=";")
    fields = reader.fieldnames
    current = list(reader)
allowed = {"Composant_UI", "Critere_acceptation"}
csv_errors = [r["Parcours_ID"] for r, old in zip(current, original) if any(r[k] != old[k] for k in fields if k not in allowed)]
ids_ok = len(current) == 31 and {r["Parcours_ID"] for r in current} == {f"E{i:02}" for i in range(1,32)}
link_errors, checked = [], 0
for path in EXPLORER.rglob("*.md"):
    if "archives" in path.relative_to(EXPLORER).parts or "99_archives" in path.relative_to(EXPLORER).parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8-sig")):
        target = target.strip("<>").split("#",1)[0]
        if not target or re.match(r"(?:https?://|mailto:|app:|plugin:)", target):
            continue
        checked += 1
        if not (path.parent / unquote(target)).exists():
            link_errors.append({"document":str(path.relative_to(EXPLORER)),"lien":target})
before_index = next(r for r in before if r["path"].endswith("12_maquette_html/index.html"))
same_html = sha(EXPLORER / "12_maquette_html/index.html") == before_index["sha256"]
counts = {}
for kind in ("DESKTOP", "MOBILE"):
    counts[kind] = json.loads((EXPLORER / f"12_maquette_html/controles/resultats/CONTROLE_{kind}.json").read_text(encoding="utf-8-sig"))
rows = list(csv.DictReader((EXPLORER / "11_ux_ui/MATRICE_VISUALISATIONS.csv").open(encoding="utf-8-sig"), delimiter=";"))
result = {"date":"2026-11-02","sources_hors_explorer_verifiees":len(outside),"sources_hors_explorer_modifiees":changed,"ids_31_conserves":ids_ok,"colonnes_table":len(fields),"modifications_API_dans_table":csv_errors,"liens_documents_actifs_verifies":checked,"liens_casses":link_errors,"html_identique_avant_apres":same_html,"mesures_catalogue":len(rows),"controles_html":{k:{"reussis":v.get("passed"),"echoues":v.get("failed")} for k,v in counts.items()},"nouveaux_tests_HTTP":False}
result["fichiers_preexistants_introuvables_apres_rangement"] = missing_before
(HERE / "VERIFICATION_RANGEMENT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(1 if changed or missing_before or not ids_ok or csv_errors or link_errors or not same_html or len(rows)!=29 or any(v.get("failed") for v in counts.values()) else 0)
