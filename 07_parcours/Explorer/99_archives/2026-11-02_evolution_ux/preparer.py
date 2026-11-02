"""Conserve l'état avant l'évolution ciblée de la navigation UX."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPLORER = HERE.parents[1]
ROOT = EXPLORER.parents[1]
if (HERE / "ETAT_AVANT.zip").exists():
    raise SystemExit("État d'entrée déjà conservé.")
files = [p for p in ROOT.rglob("*") if p.is_file() and not p.is_relative_to(HERE)]
inventory = [{"path":str(p.relative_to(ROOT)).replace("\\","/"),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
(HERE / "INVENTAIRE_AVANT.json").write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding="utf-8")
with zipfile.ZipFile(HERE / "ETAT_AVANT.zip","w",zipfile.ZIP_DEFLATED) as archive:
    for p in files:
        if p.is_relative_to(EXPLORER) and not any(part in {"archives","99_archives","traces","apercus"} for part in p.relative_to(EXPLORER).parts):
            archive.write(p,p.relative_to(EXPLORER))
attachment = Path('C:/Users/Laetitia.Kouadria/.codex/attachments/a6f9bc36-7f60-4c9d-bfac-49378d5e6da9/Texte collé.txt')
shutil.copy2(attachment, EXPLORER / '12_maquette_html/documentation/RETOUR_UX_UTILISATEUR.md')
print("État d'entrée et retour utilisateur conservés.")
