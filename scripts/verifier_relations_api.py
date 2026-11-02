#!/usr/bin/env python3
"""Audit local des relations de l'API DGEFP-RCO : aucun appel réseau.

Entrées : 01_sources/openapi/docs_json_interface.json,
          04_relations/matrice_liens_controles.csv,
          02_reponses_observees/inventaire_echantillons.csv et JSON.
Sorties : 06_controles/resultats/controle_relations_api.csv,
          06_controles/resultats/preuves_correspondances_json.csv.

Les correspondances constatées NE prouvent NI un appel effectif avec le filtre,
NI l'existence de clés étrangères ou de jointures SQL physiques.
"""
from pathlib import Path
from collections import defaultdict
import csv
import json

BASE = Path(__file__).resolve().parents[1]
DOCS = BASE / '01_sources/openapi/docs_json_interface.json'
MATRIX = BASE / '04_relations/matrice_liens_controles.csv'
SAMPLES = BASE / '02_reponses_observees'
OUT = BASE / '06_controles/resultats'
OUT.mkdir(parents=True, exist_ok=True)

with DOCS.open(encoding='utf-8') as f:
    openapi = json.load(f)
with MATRIX.open(encoding='utf-8-sig', newline='') as f:
    links = list(csv.DictReader(f, delimiter=';'))
with (SAMPLES / 'inventaire_echantillons.csv').open(encoding='utf-8-sig', newline='') as f:
    manifest = list(csv.DictReader(f, delimiter=';'))

raw = defaultdict(list)
for e in manifest:
    path = SAMPLES / e['fichier_relatif']
    try:
        with path.open(encoding='utf-8') as f:
            value = json.load(f)
        raw[e['endpoint_associe']].append((e['fichier_relatif'], value))
    except (OSError, ValueError) as ex:
        print('ERREUR lecture:', path, ex)
        raise


def at_path(node, dotted):
    """Extrait des valeurs avec notation items[].valeurs[].code."""
    keys = dotted.split('.')
    vals = [node]
    for key in keys:
        is_array = key.endswith('[]')
        field = key[:-2] if is_array else key
        result = []
        for val in vals:
            if isinstance(val, dict) and field in val:
                v = val[field]
                if is_array:
                    if isinstance(v, list):
                        result.extend(v)
                else:
                    result.append(v)
        vals = result
    return vals


def as_codes(vals):
    out = set()
    for v in vals:
        if isinstance(v, (str, int)) and str(v).strip():
            out.add(str(v).strip())
    return out


def samples_codes(endpoint, key):
    codes = set()
    found = False
    for _, data in raw.get(endpoint, []):
        if at_path(data, key):
            found = True
            codes.update(as_codes(at_path(data, key)))
    return codes, found


# Chemins évaluables avec les échantillons réels disponibles.
# Une intersection est une CORRESPONDANCE DE VALEURS, pas un test d'appel.
EVIDENCE = {
    'R01': ('/metiers/{rome}', 'rome_code', '/metiers/{rome}/competences', 'rome_code'),
    'R02': ('/metiers/{rome}', 'rome_code', '/certifications', 'items[].rome_codes[]'),
    'R03': ('/metiers/{rome}', 'rome_code', '/formacodes', 'items[].rome_codes[]'),
    'R04': ('/metiers/{rome}', 'rome_code', '/prospective/regions', 'rome_code'),
    'R05': ('/metiers/{rome}', 'rome_code', '/recrutements', 'rome_code'),
    'R06': ('/metiers/{rome}', 'rome_code', '/salaires', 'rome_code'),
    'R07': ('/metiers/{rome}', 'rome_code', '/mobilites', 'rome_code'),
    'R08': ('/metiers/{rome}', 'rome_code', '/indicateurs', 'rome_code'),
    'R09': ('/metiers/{rome}', 'rome_code', '/secteurs', 'rome_code'),
    'R10': ('/certifications', 'items[].certifinfo_code', '/certifications/{certifinfo}', 'certifinfo_code'),
    'R11': ('/certifications', 'items[].certifinfo_code', '/certifications/blocs', 'items[].certifinfo_codes[]'),
    'R12': ('/certifications', 'items[].fiche_code', '/certifications/blocs', 'items[].fiche_code'),
    'R13': ('/certifications', 'items[].bloc_competences_codes[]', '/certifications/blocs', 'items[].bloc_code'),
    'R14': ('/certifications', 'items[].formacode_codes[]', '/formacodes', 'items[].formacode_code'),
    'R15': ('/metiers/{rome}', 'formacode_codes[]', '/formacodes', 'items[].formacode_code'),
    'R20': ('/indicateurs', 'items[].mesure', '/mesures', 'items[].code'),
    'R21': ('/metiers/{rome}', 'fap228_codes[]', '/indicateurs', 'items[].valeurs[].fap_228_code'),
    'R22': ('/prospective/metiers', 'items[].rome_codes[]', '/metiers/{rome}', 'rome_code'),
}

SOURCE_PATTERNS = {
    'R16': [('/territoires', 'items[].zonage'), ('/territoires', 'items[].territoire_code')],
    'R17': [('/territoires', 'items[].zonage'), ('/territoires', 'items[].territoire_code')],
    'R18': [('/certifications', 'items[].certifinfo_code'), ('/territoires', 'items[].zonage'), ('/territoires', 'items[].territoire_code')],
    'R19': [('/certifications', 'items[].certifinfo_code'), ('/territoires', 'items[].zonage'), ('/territoires', 'items[].territoire_code')],
    'R23': [('/metiers/{rome}/competences', 'items[].competence_code')],
    'R24': [('/metiers/{rome}', 'contexte_travail_codes[]')],
}

# Contrôle des noms, pas des contraintes conditionnelles ou de la validité d'une valeur.
PARAMS = {
    'R01': ['rome'], 'R02': ['rome'], 'R03': ['rome'], 'R04': ['rome'],
    'R05': ['rome'], 'R06': ['rome'], 'R07': ['rome'], 'R08': ['rome'], 'R09': ['rome'],
    'R10': ['certifinfo'], 'R11': ['certifinfo'], 'R12': ['fiche'],
    'R14': ['code'], 'R15': ['code'], 'R16': ['zonage', 'territoire'],
    'R17': ['zonage', 'territoire'], 'R18': ['zonage', 'territoire', 'certifinfo'],
    'R19': ['zonage', 'territoire', 'certifinfo'], 'R22': ['rome'],
    'R23': ['competence'], 'R24': ['contexte', 'sans_contexte'],
}

reports, proofs = [], []
for relation in links:
    rid = relation['id']
    dest = relation['endpoint_cible']
    defined = openapi.get('paths', {}).get(dest, {}).get('get', {})
    names = {p['name'] for p in defined.get('parameters', [])}
    expected = PARAMS.get(rid)
    if expected is None:
        param_status = 'SANS_PARAMETRE_CIBLE'
        missing = ''
    elif rid == 'R24':
        missing_names = set(expected) - names
        missing = ','.join(sorted(missing_names))
        param_status = 'DOCUMENTE' if not missing_names else 'PARAMETRE_ABSENT'
    else:
        missing_names = set(expected) - names
        missing = ','.join(sorted(missing_names))
        param_status = 'DOCUMENTE' if not missing_names else 'PARAMETRE_ABSENT'

    src_status = 'NON_EVALUABLE'
    observed = 'NON_COMPARABLE'
    matching = set()
    src_values, dst_values = set(), set()
    evidence_detail = ''
    if rid in EVIDENCE:
        src_ep, src_path, dst_ep, dst_path = EVIDENCE[rid]
        src_values, src_found = samples_codes(src_ep, src_path)
        dst_values, dst_found = samples_codes(dst_ep, dst_path)
        matching = src_values & dst_values
        src_status = 'OBSERVE' if src_found else 'CHAMP_ABSENT_ECHANTILLON'
        if not src_found or not dst_found:
            observed = 'ECHANTILLON_MANQUANT_OU_CHAMP_ABSENT'
        elif matching:
            observed = 'CORRESPONDANCE_CODES_OBSERVEE'
        else:
            observed = 'PAS_DE_CORRESPONDANCE_DANS_LES_ECHANTILLONS'
        evidence_detail = f'{src_ep}:{src_path} = {len(src_values)} codes ; {dst_ep}:{dst_path} = {len(dst_values)} codes'
        proofs.append({
            'relation': rid, 'source': src_ep, 'chemin_source': src_path,
            'cible': dst_ep, 'chemin_cible': dst_path,
            'nb_codes_source': len(src_values), 'nb_codes_cible': len(dst_values),
            'nb_codes_communs': len(matching), 'exemples_codes_communs': ', '.join(sorted(matching)[:8]),
            'constat': observed,
            'limite': 'Intersection sur JSON collectes uniquement. Ne prouve ni un appel filtre reussi ni une jointure SQL.'
        })
    elif rid in SOURCE_PATTERNS:
        spec = SOURCE_PATTERNS[rid]
        ok = all(samples_codes(endpoint, path)[1] for endpoint, path in spec)
        src_status = 'OBSERVE' if ok else 'CHAMP_ABSENT_ECHANTILLON'
        observed = 'NON_COMPARABLE_SANS_URL_REQUETE_OU_REPONSE_CIBLE'
        evidence_detail = 'Champs de sortie identifiables, mais enchainement non trace dans les fichiers collectes'

    reports.append({
        'id': rid,
        'endpoint_source': relation['endpoint_source'],
        'champ_sortie': relation['champ_sortie'],
        'endpoint_cible': dest,
        'parametre_entree': relation['parametre_entree'],
        'parametres_declares_docs_json': param_status,
        'parametres_manquants': missing,
        'champ_source_dans_echantillons': src_status,
        'correspondance_codes_dans_echantillons': observed,
        'nb_codes_communs': len(matching) if rid in EVIDENCE else '',
        'exemples_codes_communs': ', '.join(sorted(matching)[:6]),
        'preuve_echantillons': evidence_detail,
        'appel_avec_ce_filtre_execute_et_trace': 'NON',
        'jointure_sql_physique_verifiee': 'NON',
        'limite': relation['limite'],
    })


def write_report(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';')
        w.writeheader()
        w.writerows(rows)

p1 = OUT / 'controle_relations_api.csv'
p2 = OUT / 'preuves_correspondances_json.csv'
write_report(p1, reports)
write_report(p2, proofs)
print('Relations de la matrice analysees :', len(reports))
print('Parametres de destination documentes :', sum(r['parametres_declares_docs_json'] == 'DOCUMENTE' for r in reports), '(autres : correspondances sans filtre)')
print('Correspondances de codes observees :', sum(r['correspondance_codes_dans_echantillons'] == 'CORRESPONDANCE_CODES_OBSERVEE' for r in reports))
print('Relations sans correspondance testable :', sum(r['correspondance_codes_dans_echantillons'] != 'CORRESPONDANCE_CODES_OBSERVEE' for r in reports))
print('Rapports :', p1, 'et', p2)
print('ATTENTION : preuves statiques des codes, aucune requete API lancee et aucune jointure SQL verifiee.')
