"""Cohérence locale des preuves R16/R17/R18/R19/R23/R24 (aucun appel réseau).
Les assertions ne démontrent pas l'exhaustivité générale des filtres ni des données.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'06_controles'/'resultats'

def source(path):
    p=P/path
    if not p.is_file(): raise AssertionError(f'Fichier preuve manquant : {p.relative_to(ROOT)}')
    return json.loads(p.read_text(encoding='utf-8-sig'))

def check(ok, why):
    if not ok: raise AssertionError(why)

# R16
territ=source('R16 test/GET_territoires__zonage_commune__code_34172.json')
indic=source('R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json')
check(territ['items'][0]['territoire_code']=='34172','R16 : commune')
check(indic['rome_code']=='F1610' and indic['zonage']=='commune' and indic['territoire']=='34172','R16 : filtre métier/territoire')
check(len(indic['items'])==14,'R16 : nombre de mesures')
print('R16 OK : commune Montpellier et 14 mesures pour F1610')

# R17
sans=source('R17 test/R17 verif GET secteurszonage=commune&territoire=34172.json')
avec=source('R17 test/R17GET secteurs.json')
region=source('R17 test/R17 verif GET secteursrome=F1610&zonage=region&territoire=76.json')
check(len(sans.get('items',[]))==35,'R17 : 35 secteurs sans filtre')
check(len(avec.get('items',[]))==0 and len(region.get('items',[]))==0,'R17 : deux filtres métier encore vides')
print('R17 PARTIEL : 35 secteurs sans filtre ; avec F1610 liste vide, point RCO ouvert')

# R18/R19 : dates, filtres non restitués dans chaque objet.
a=source('R18 test/R18 GET sessions_a_venircertifinfo=112561&zonage=region&territoire=76&onisep=exclure&page=1.json')
b=source('R19/R19 GET sessions_en_courscertifinfo=112561&zonage=region&territoire=76&onisep=exclure&page=1.json')
check(a['total']==10 and len(a['items'])==10, 'R18 : nombre de sessions')
check(b['total']==8 and len(b['items'])==8, 'R19 : nombre de sessions')
print('R18/R19 OK sur exemples : 10 futures / 8 en cours, identifiants de rattachement absents')

# R23 : competence_code -> ROME V3 ; modes toutes/au_moins_une
c=source('R23 test/GET_competences__code_103659__page_1.json')['items'][0]
check(c['competence_code']=='103659' and c['competence_libelle']=='Poser des panneaux solaires','R23 : competence 103659')
check(set(c['rome_codes'])=={'F1610','I1604'}, 'R23 : relation code 103659')
toutes=source('R23 test/R23 GET metierscompetence=125416,103659&mode_competence=toutes&page=1.json')
une=source('R23 test/R23 GET metierscompetence=125416,103659&mode_competence=au_moins_une&page=1.json')
check([x['rome_code'] for x in toutes['items']]==['F1610'],'R23 : intersection')
check({x['rome_code'] for x in une['items']}=={'F1610','F1705','I1604'},'R23 : union')
check({x['rome_code']:set(x['competences_trouvees_codes']) for x in une['items']}=={'F1610':{'125416','103659'},'F1705':{'125416'},'I1604':{'103659'}},'R23 : champs de correspondance')
print('R23 OK : competence 103659 et recherche multicompétences (1 / 3 métiers)')

# R24
avec=source('R24/R24 GET metiersdomaine=F16&contexte=300782&page=1.json')
sans=source('R24/R24 GET metiersdomaine=F16&sans_contexte=300782&page=1.json')
a={x['rome_code'] for x in avec['items']}; b={x['rome_code'] for x in sans['items']}
check(avec['total']==10 and sans['total']==3 and len(a)==10 and len(b)==3,'R24 : effectifs')
check(not a.intersection(b) and 'F1610' in a and 'F1610' not in b,'R24 : disjonction')
check(all('300782' in x['contexte_travail_codes'] and x['domaine_code']=='F16' for x in avec['items']),'R24 : inclusion')
check(all('300782' not in x['contexte_travail_codes'] and x['domaine_code']=='F16' for x in sans['items']),'R24 : exclusion')
print('R24 OK : inclusion 10 / exclusion 3 sur F16')
print('OK : preuves JSON cohérentes sur les cas testés, aucune requête API exécutée.')
