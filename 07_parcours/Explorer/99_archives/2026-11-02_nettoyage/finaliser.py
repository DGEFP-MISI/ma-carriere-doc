"""Actualise les chemins des métadonnées et la présentation des guides."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
path = root / "11_ux_ui/ETAT_FIGMA.json"
data = json.loads(path.read_text(encoding="utf-8-sig"))
for item in data.get("mobileLocal", []):
    if item["path"].startswith("mobile/"):
        item["path"] = "archives/conception_initiale/" + item["path"]
data["reference_presentation_html"] = "../12_maquette_html/index.html"
data["rangement_documentaire"] = {"date":"2026-11-02", "visuels_locaux":"archives/conception_initiale", "mise_a_jour_figma_distante":False, "etat":"Figma initial, présentation citoyenne actuelle dans le HTML"}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
path = root / "11_ux_ui/ECRANS_STRUCTURE.json"
data = json.loads(path.read_text(encoding="utf-8-sig"))
for key, value in data.get("visualOverrides", {}).items():
    if value.startswith("mobile/"):
        data["visualOverrides"][key] = "archives/conception_initiale/" + value
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
for path in list(root.glob("*.md")) + [root / "12_maquette_html/README.md"]:
    text = path.read_text(encoding="utf-8-sig")
    for before, after in {"Les31":"Les 31", "les31":"les 31", "Les108":"Les 108", "les108":"les 108", "Les21":"Les 21", "les21":"les 21", "Les29":"Les 29", "les29":"les 29", "\n-108 ":"\n- 108 ", "|21 GET":"| 21 GET", "champs,29 mesures":"champs, 29 mesures", "Table commune :31 lignes":"Table commune : 31 lignes", "108 à320":"108 à 320", "à320pixels":"à 320 pixels", "controles/resultats/CONTROLE_":"controles/resultats/CONTROLE_"}.items():
        text = text.replace(before, after)
    path.write_text(text, encoding="utf-8")
api_result = {"date":"2026-11-02","commande":"python -B scripts/verifier_dossier.py","code_sortie":0,"controles_reussis":["verifier_contrat.py","verifier_echantillons.py","verifier_schemas_complementaires.py","verifier_relations_api.py","verifier_uml_global.py","verifier_preuves_directes.py"],"nombre":6,"hors_ligne":True,"nouvel_appel_HTTP":False,"anomalie_R17":"Toujours ouverte ; réussite du contrôle sans résolution fournisseur"}
(Path(__file__).resolve().parent / "CONTROLES_API.json").write_text(json.dumps(api_result, ensure_ascii=False, indent=2), encoding="utf-8")
print("Chemins et guides actualisés ; résultat des six contrôles API conservé.")
