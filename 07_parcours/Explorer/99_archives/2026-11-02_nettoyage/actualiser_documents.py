"""Met à jour les documents de travail, sans toucher au contrat ou aux preuves API."""
import csv
import io
from pathlib import Path

EXPLORER = Path(__file__).resolve().parents[2]
stamp = "**Mise à jour du 2 novembre 2026 — dossier rangé.**"
for path in sorted(EXPLORER.glob("[0-9][0-9]_*.md")):
    text = path.read_text(encoding="utf-8-sig")
    if stamp in text:
        raise SystemExit(f"Déjà actualisé : {path.name}")
    first, rest = text.split("\n", 1)
    note = f"\n{stamp} Le lot L0 est terminé. La présentation actuelle est la [maquette HTML citoyenne](12_maquette_html/index.html), dont les [sources et contrôles](12_maquette_html/README.md) sont rangés séparément. Voir le [guide du dossier](README.md). Les noms du projet, identifiants et référentiels employés dans les documents techniques ne doivent pas apparaître dans les écrans citoyens. Les31 fonctionnalités restent conservées ; les captures locales ne valent pas des tests HTTP de l’API.\n"
    text = first + "\n" + note + rest
    text = text.replace("Résultats paginés : intitulé, référentiel, identifiant et indication de type", "Résultats paginés : nom du métier ou de la certification, domaine et type compréhensible ; identifiants et noms des référentiels conservés dans les traitements internes")
    text = text.replace("Le libellé public Secteur désigne un domaine professionnel ROME, distinct de la NAF38. Le wording et les modalités de stockage restent à préciser, pas l'inclusion des fonctions.", "L’entrée Domaine regroupe des métiers ; les secteurs d’activité décrivent les entreprises qui emploient. Cette distinction doit être expliquée sans afficher les codes ni les sigles des référentiels. La maquette emploie « Un domaine professionnel » ; l’interaction et les modalités de stockage restent à préciser, pas l’inclusion des fonctions.")
    text = text.replace("Le dossier actuel est une base documentaire et un ensemble de contrôles API, sans application identifiée.", "Le dossier contient une base documentaire, des contrôles API et une maquette HTML locale. Aucune application de production connectée à l’API n’est identifiée.")
    text = text.replace("Le dossier inspecté contient des sources, des JSON, des UML, des documents et des contrôles Python/PowerShell. Aucun projet applicatif identifié", "Lors de l’audit du 1er novembre, le dossier inspecté contenait des sources, des JSON, des UML, des documents et des contrôles Python/PowerShell. La maquette HTML a été ajoutée ensuite ; le constat historique était : aucun projet applicatif identifié")
    text = text.replace("**Le lot L0 actuel est documentaire : ne pas démarrer l'application sans instruction explicite de la maîtrise d'ouvrage.**", "**Le lot L0 est terminé. Une maquette HTML de conception a été autorisée et réalisée ; l’application connectée à l’API ne doit pas être démarrée sans instruction explicite de la maîtrise d’ouvrage.**")
    text = text.replace("Une recherche, trois modes **Métier / Diplôme / Secteur** ; « Secteur » reste libellé public du **domaine professionnel ROME** ; secteur économique NAF distinct.", "Une recherche, trois modes **Métier / Diplôme ou titre / Domaine professionnel** dans la maquette citoyenne ; domaine de métiers et secteur d’activité économique restent distincts. Les identifiants et sigles techniques ne sont pas des intitulés publics.")
    text = text.replace("expliquer « domaine professionnel ROME », distinct de NAF", "présenter le domaine professionnel sans sigle technique et le distinguer du secteur d’activité des entreprises")
    if path.name.startswith(("01_", "04_", "07_")):
        text += "\n## Règle de présentation citoyenne — décision produit du 2 novembre 2026\n\nLes écrans affichent les noms fournis par l’API, sans codes, noms de référentiels, version du projet ni notes de conception. Les paramètres techniques restent dans le code et la documentation. Expliquer les chiffres en langage courant : sens, personnes concernées, lieu, période, unité et limites. Une information manquante n’est pas zéro ; un projet de recrutement n’est pas une offre ; une projection n’est pas une garantie. Conserver les sources. Ne pas ajouter de score, de taux ou de calcul pour vulgariser. Cette règle s’applique aux31 fonctionnalités et à leurs critères de recette. La ligne éditoriale est [documentée ici](12_maquette_html/documentation/REDACTION_CITOYENNE.md).\n"
    if path.name.startswith(("06_", "10_")):
        text += "\n## Décisions de présentation actées le 2 novembre 2026\n\n- **D11 — Noms publics : acté.** Utiliser les libellés effectivement fournis ; conserver les codes et les référentiels dans les traitements internes. Ne pas inventer un nom manquant.\n- **D12 — Lecture citoyenne : acté.** Retirer des écrans les mentions de version, de maquette, de tests, de conception et d’intégration. Expliquer les chiffres à proximité de leur valeur, avec leur portée et leurs limites. Les sources restent consultables.\n\nD11/D12 ne rouvrent ni le périmètre D01 ni les questions fournisseur. D02–D10 restent ouverts pour leurs modalités non résolues ; D02 ne peut plus proposer des codes ou sigles comme libellés publics. Les questions RCO ouvertes restent Q01, Q06, Q07, Q11 et Q14 ; Q05 reste conditionnelle. Les108 contrôles de la maquette sur ordinateur et mobile sont des tests locaux d’interface, sans nouvelle validation HTTP ni certification RGAA. La production connectée reste à préparer.\n"
    path.write_text(text, encoding="utf-8")

path = EXPLORER / "03_TABLE_CONCEPTION.csv"
with path.open(encoding="utf-8-sig", newline="") as stream:
    reader = csv.DictReader(stream, delimiter=";")
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 31 and {r["Parcours_ID"] for r in rows} == {f"E{i:02}" for i in range(1, 32)}
for row in rows:
    row["Composant_UI"] += " ; Présentation citoyenne : noms plutôt que codes ; pas de version ou de détail interne ; explication du sens des chiffres, des personnes concernées, du lieu et de la période ; sources accessibles."
    row["Critere_acceptation"] += " ; Recette citoyenne : aucun identifiant ou sigle de référentiel imposé à l’usager ; nombres et unités inchangés ; explication des limites et des absences ; sources conservées, sans score supplémentaire."
with path.open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter=";", lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
print(f"9 documents techniques et {len(rows)} lignes de conception actualisés ; {len(fields)} colonnes conservées.")
