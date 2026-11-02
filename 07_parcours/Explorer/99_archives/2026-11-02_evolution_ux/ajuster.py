"""Ajustements des actions de comparaison et de la saisie, sans modifier les données."""
from pathlib import Path
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'12_maquette_html/sources'
path=SOURCE/'interface_citoyenne.js'
text=path.read_text(encoding='utf-8-sig')
old="${a('Comparer avec un autre métier','comparateur')}"
new='<button class="btn" data-compare-add="F1610">Comparer avec un autre métier</button>'
assert old in text
text=text.replace(old,new)
old="${a('Comparer avec la couverture','comparateur')}"
new='<button class="btn" data-compare-add="${esc(code)}">Comparer ce métier</button>'
assert old in text
text=text.replace(old,new)
path.write_text(text,encoding='utf-8')
path=SOURCE/'experience_exploration.js'
text=path.read_text(encoding='utf-8-sig').replace('minlength="2" required','minlength="2" maxlength="100" required')
for title in ['Que fait-on dans ce métier','Où sont les opportunités','Combien gagne-t-on','Quelles autres pistes']:
    text=text.replace(title+' ?',title+'\u00a0?')
path.write_text(text,encoding='utf-8')
print('Comparaisons liées au métier choisi, limites de saisie et typographie ajustées.')
