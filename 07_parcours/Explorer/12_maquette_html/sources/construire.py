"""Assemble une maquette HTML autonome depuis les preuves locales, sans appel API."""
import csv
import hashlib
import json
from html import escape
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
HERE = SOURCE.parent
ROOT = HERE.parents[2]
CONTROLES = HERE / 'controles'
RESULTATS = CONTROLES / 'resultats'
PREUVES = HERE / 'preuves'
for directory in (CONTROLES, RESULTATS, PREUVES):
    directory.mkdir(parents=True, exist_ok=True)

def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8-sig"))

screens = read("07_parcours/Explorer/11_ux_ui/ECRANS_STRUCTURE.json")
metier = read("02_reponses_observees/metiers/response_metiers-rome.json")
r24 = ROOT / "06_controles/resultats/R24"
metiers = {metier["rome_code"]: metier}
for path in r24.glob("*.json"):
    for item in json.loads(path.read_text(encoding="utf-8-sig")).get("items", []):
        if item.get("rome_code"):
            metiers[item["rome_code"]] = item
r23 = ROOT / "06_controles/resultats/R23 test"
matches = {}
for path in r23.glob("*.json"):
    if "125416,103659" in path.name:
        matches["toutes" if "=toutes" in path.name else "au_moins_une"] = json.loads(path.read_text(encoding="utf-8-sig")).get("items", [])
for rows in matches.values():
    for item in rows:
        metiers.setdefault(item["rome_code"], item)

# Libellés observés, sans dictionnaire externe ni correspondance reconstruite.
labels = {}
label_proofs = {}
label_priorities = {}
def collect_labels(value, source):
    if isinstance(value, dict):
        for key, code in value.items():
            if key == "code":
                label_key = "libelle"
            elif key.endswith("_code"):
                label_key = key[:-5] + "_libelle"
            elif key.endswith("_codes"):
                label_key = key[:-6] + "_libelles"
            else:
                continue
            names = value.get(label_key)
            pairs = zip(code, names) if isinstance(code, list) and isinstance(names, list) and len(code) == len(names) else [(code, names)]
            for identifier, name in pairs:
                if isinstance(identifier, str) and isinstance(name, str) and name.strip():
                    priority = 30 if key.startswith(("fap_", "rome_", "competence_", "secteur_naf38_", "formacode_", "contexte_travail_")) else 10
                    if identifier not in labels or priority > label_priorities[identifier]:
                        labels[identifier] = name.strip()
                        label_priorities[identifier] = priority
                        label_proofs[identifier] = {"nom": name.strip(), "champ_code": key, "champ_nom": label_key, "preuve": source}
        for child in value.values():
            collect_labels(child, source)
    elif isinstance(value, list):
        for child in value:
            collect_labels(child, source)

for folder in [ROOT / "02_reponses_observees", ROOT / "06_controles/resultats"]:
    for path in sorted(folder.rglob("*.json")):
        collect_labels(json.loads(path.read_text(encoding="utf-8-sig")), str(path.relative_to(ROOT)).replace("\\", "/"))
payload = {
    "labels": labels,
    "formacodes": read("02_reponses_observees/certifications/response_formacode.json")["items"],
    "screens": screens["screens"],
    "metier": metier,
    "metiers": list(metiers.values()),
    "r23": matches,
    "competencesRecherche": [read("06_controles/resultats/R23 test/GET_competences__code_103659__page_1.json"), read("06_controles/resultats/R23 test/R23 GET competencescode=125416&page=1.json")],
    "competences": read("02_reponses_observees/metiers/response_metiers{rome}competences.json"),
    "certification": read("02_reponses_observees/certifications/response_certifications-certifinfo.json"),
    "certifications": read("02_reponses_observees/certifications/response_certifications.json"),
    "territoires": [read(str(path.relative_to(ROOT))) for path in sorted((ROOT / "02_reponses_observees/territoires").glob("*.json"))] + [read("06_controles/resultats/R16 test/GET_territoires__zonage_commune__code_34172.json")],
    "blocs": read("02_reponses_observees/certifications/response_certificationsblocs.json")["items"],
    "sessions": {"avenir": read("02_reponses_observees/sessions/response_sessions_a_venir.json")["items"], "encours": read("02_reponses_observees/sessions/response_sessions_en_cours.json")["items"]},
    "catalogue": read("02_reponses_observees/indicateurs/Recrutementregions/response_mesures.json")["items"],
    "visualisations": list(csv.DictReader((ROOT / "07_parcours/Explorer/11_ux_ui/MATRICE_VISUALISATIONS.csv").open(encoding="utf-8-sig"), delimiter=";")),
    "indicateurs": read("06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json"),
    "salairesSecteurs": read("02_reponses_observees/indicateurs/response_salairessecteurs.json"),
    "mobilites": [read(str(path.relative_to(ROOT))) for path in sorted((ROOT / "02_reponses_observees/indicateurs/mobilites").glob("*.json"))],
    "prospectiveRegions": read("02_reponses_observees/indicateurs/prospectiveregions/response_postes_a_pourvoir.json"),
    "prospectiveMetiers": read("02_reponses_observees/indicateurs/ProspectiveMetier/response_prospectivemetiers_poste a  pourvoir.json"),
}
payload["cartographies"] = {key: read(path) for key, path in {
    "salairesRegions": "02_reponses_observees/indicateurs/salaires/response_regions.json",
    "salairesDepartements": "02_reponses_observees/indicateurs/salaires/response_departement.json",
    "recrutementsRegions": "02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement france region Projet.json",
    "recrutementsDepartements": "02_reponses_observees/indicateurs/Recrutementregions/response_Recrutement France departement projet.json",
}.items()}
payload["citizenSources"] = {
    m["code"]: m["source"].replace("API Offres d'emploi", "offres d’emploi").replace("RNCP et RS (via Certif Info)", "certifications enregistrées, via Certif Info").replace("Formacode V14", "thèmes de formation").replace("fichier salariés open data", "données sur les salaires").replace("fichier détail individus", "données sur les personnes en emploi")
    for m in payload["catalogue"]
}
encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
html = (SOURCE / "modele.html").read_text(encoding="utf-8")
assert html.count("__EXPLORER_DATA__") == 1
html = html.replace("__EXPLORER_DATA__", encoded)
no_js = '<style>.nav-main,.search-container,.breadcrumb,.side{display:none!important}.layout{display:block!important}</style><h1 id="recherche">Explorer les métiers</h1><p>Sans JavaScript, vous pouvez lire cet aperçu. Pour rechercher, comparer des métiers et garder des pistes, activez JavaScript dans votre navigateur.</p>'
no_js += '<article><h2>' + escape(metier['rome_libelle']) + '</h2>' + ''.join('<p>' + escape(text) + '</p>' for text in metier.get('definitions', [])) + '</article><h2 id="sources">Sources et limites</h2><p>Source : France Travail, descriptions des métiers. Cette fiche décrit un métier en général. Les activités et les conditions peuvent varier selon le poste et l’entreprise. Aucun résultat individuel n’est prédit.</p>'
html = html.replace("__EXPLORER_NOSCRIPT__", no_js)
shared = ROOT / "07_parcours/commun_datavisualisation"
styles = (shared / "dist/styles.css").read_text(encoding="utf-8")
custom_styles = (shared / "src/styles.css").read_text(encoding="utf-8") + "\n" + (SOURCE / "ameliorations_ux.css").read_text(encoding="utf-8") + "\n" + (shared / "src/infographie.css").read_text(encoding="utf-8")
html = html.replace("<style>", "<style>" + styles + "</style><style>", 1)
html = html.replace("</head>", "<style>" + custom_styles + "</style></head>")
runtime = (shared / "dist/runtime.js").read_text(encoding="utf-8")
components = (shared / "dist/composants.js").read_text(encoding="utf-8")
# Les distributions officielles précompilées restent utilisables en file://.
html = html.replace("<script>", "<script>window.__earlyErrors=[];window.addEventListener('error',e=>window.__earlyErrors.push(e.error?.stack||e.message));</script><script>" + runtime.replace("</script", "<\\/script") + "\n" + components + "\n</script><script>", 1)
citizen_js = (SOURCE / "interface_citoyenne.js").read_text(encoding="utf-8")
extension = (SOURCE / "experience_exploration.js").read_text(encoding="utf-8")
provider = (SOURCE / "donnees_exploration.js").read_text(encoding="utf-8")
citizen_js = citizen_js.replace("window.addEventListener('hashchange',render);render();", provider + "\n" + extension + "\n" + (SOURCE / "ameliorations_ux.js").read_text(encoding="utf-8") + "\n" + (SOURCE / "visualisations_dsfr.js").read_text(encoding="utf-8") + "\n" + (SOURCE / "infographie_explorer.js").read_text(encoding="utf-8") + "\nwindow.addEventListener('hashchange',render);initialiserExploration();")
assert html.count("__EXPLORER_INTERFACE__") == 1
html = html.replace("__EXPLORER_INTERFACE__", citizen_js)
html = html.rsplit("</body>", 1)[0] + "<script>\n" + (CONTROLES / "scripts/verifier_dsfr_chart.js").read_text(encoding="utf-8") + "\n" + (CONTROLES / "scripts/verifier_exploration.js").read_text(encoding="utf-8") + "\n" + (CONTROLES / "scripts/verifier_navigateur.js").read_text(encoding="utf-8") + "\n</script>\n</body></html>"
(HERE / "index.html").write_text(html, encoding="utf-8")
mobile_html = '''<!doctype html><html lang="fr"><meta charset="utf-8"><title>Contrôle de reflow320 — Explorer V2</title><style>body{margin:0;background:#eee}iframe{width:320px;height:844px;display:block;border:0;background:white}</style><iframe title="Explorer V2 — largeur320pixels" srcdoc="PAYLOAD"></iframe><script>window.addEventListener('message',e=>{if(e.source!==document.querySelector('iframe').contentWindow||e.data?.type!=='explorer-v2-controle')return;const p=document.createElement('pre');p.id='verification-result';p.hidden=true;p.textContent=JSON.stringify(e.data.report);document.body.append(p);});</script></html>'''
mobile_source = html.replace("if(new URLSearchParams(location.search).get('verification')!=='1')return;", "if(new URLSearchParams(parent.location.search).has('apercu'))return;")
(CONTROLES / "controle-mobile.html").write_text(mobile_html.replace("PAYLOAD", escape(mobile_source, quote=True)), encoding="utf-8")
(CONTROLES / "controle-desktop-apercu.html").write_text(mobile_html.replace("320px", "1410px").replace("844px", "1100px").replace("PAYLOAD", escape(mobile_source, quote=True)), encoding="utf-8")
manifest = {"date": "2026-11-02", "ecrans_reference": len(payload["screens"]), "vues_navigation":22, "fiches_identifiees":"métiers, certifications et domaines issus des JSON observés", "mesures": len(payload["catalogue"]), "appels_http": 0, "sha256": hashlib.sha256(html.encode()).hexdigest()}
(RESULTATS / "ASSEMBLAGE.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
(PREUVES / "PREUVES_LIBELLES.json").write_text(json.dumps(label_proofs, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False))
