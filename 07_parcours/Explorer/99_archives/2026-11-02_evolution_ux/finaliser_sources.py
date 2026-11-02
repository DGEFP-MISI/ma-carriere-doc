"""Harmonise les cellules de compétences et les unités des tranches ouvertes."""
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[2]/'12_maquette_html/sources'
path=SOURCE/'experience_exploration.js'
text=path.read_text(encoding='utf-8-sig')
for label, code in [('Poser des panneaux solaires','103659'),('Réaliser un raccordement d’étanchéité','125416')]:
    old="['"+label+"',left==='F1610'?'Mentionné':'Information non disponible',right==='F1610'?'Mentionné':'Information non disponible']"
    new="['"+label+"',mentionCompetence(left,'"+code+"'),mentionCompetence(right,'"+code+"')]"
    assert old in text
    text=text.replace(old,new)
text=text.replace("r.salaire_net_mensuel_median===null?r.tranche_salaire_median_libelle:fmt(r.salaire_net_mensuel_median)+' €'", "r.salaire_net_mensuel_median===null?(r.tranche_salaire_median_libelle?'Tranche annuelle : '+r.tranche_salaire_median_libelle:'Information non disponible'):typeof r.salaire_net_mensuel_median==='number'?fmt(r.salaire_net_mensuel_median)+' €':fmt(r.salaire_net_mensuel_median)")
path.write_text(text,encoding='utf-8')
print('Compétences observées et unités affichées de façon cohérente.')
