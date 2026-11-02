"""Applique les évolutions ciblées sans reconstruire les vues de données."""
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
EXPLORER=HERE.parents[1]
SOURCE=EXPLORER/'12_maquette_html/sources'
path=SOURCE/'interface_citoyenne.js'
text=path.read_text(encoding='utf-8-sig')
def replace_function(name, body, following=r'^function '):
    global text
    pattern=r'^function '+re.escape(name)+r'\([^\n]*?\)\{.*?(?='+following+r')'
    text,n=re.subn(pattern,lambda _:body+'\n',text,count=1,flags=re.S|re.M)
    if n!=1:raise ValueError('Fonction non trouvée : '+name)
replace_function('overview',"function overview(){return experienceOverview();}")
replace_function('search',"function search(){return experienceHome();}")
replace_function('results',"function results(){return experienceResults();}")
replace_function('pistes',"function pistes(){return experiencePistes();}")
replace_function('comparatorPage',"function comparatorPage(){return experienceComparator();}")
replace_function('domaine',"function domaine(){return experienceDomaine(readRoute().id);}")
replace_function('card', '''function card(m){return `<article class="result-card"><p class="eyebrow">${esc(m.domaine_libelle||'Un métier à découvrir')}</p><h2>${esc(m.rome_libelle)}</h2><div class="actions">${a('Découvrir ce métier',route(m.rome_code),true)}<button class="btn" data-save="${esc(m.rome_code)}">Garder cette piste</button><button class="btn small" data-compare-add="${esc(m.rome_code)}">Comparer ce métier</button></div></article>`;}''')
render=r'''function render(options={}){
 const {slug,id}=readRoute(),isMetier=nav.some(n=>n[0]===slug)||['transitions','alternatives'].includes(slug),title=titles[slug]||metier(id)?.rome_libelle||'Votre exploration';
 document.title=title+' · MaCarrière';updateSearch();
 document.querySelector('#layout').className='layout'+(isMetier?'':' wide');
 const sidebar=document.querySelector('#sidebar');sidebar.hidden=!isMetier;
 sidebar.innerHTML=`<h2>Vos questions</h2>${groupedNav(slug)}<div class="side-more"><a href="#sources">Sources et explications</a></div>`;
 document.querySelector('#breadcrumb').innerHTML=`<a href="#recherche">Explorer</a> / ${isMetier&&slug!=='essentiel'?`<a href="#essentiel">${esc(DATA.metier.rome_libelle)}</a> / `:''}${esc(title)}`;
 const views={essentiel:overview,competences,recrutements,salaires,territoires,mobilites,prospective,secteurs,formations,recherche:search,resultats:results,guide,'resultats-ogr':guideResults,pistes,certification:()=>experienceCertification(id),comparateur:comparatorPage,formacodes:formacodesPage,transitions,domaine,sources,alternatives:experienceAlternatives,menu:()=>intro('menu')+groupedNav(slug)};
 let html=slug==='metier'?otherMetier(id):views[slug]?views[slug]():`<h1 tabindex="-1">Cette page n’est pas disponible</h1>${a('Revenir à la recherche','recherche',true)}`;
 const t=selectedTerritory(),reference=state.territoryKey==='commune:34172',localBasin=state.territoryKey==='clpe:CLPE34003'||(t?.clpe_code==='CLPE34003'&&t?.departement_code==='34');
 const supported={recrutements:reference||localBasin,salaires:reference||state.territoryKey==='departement:34'||t?.departement_code==='34',prospective:reference||state.territoryKey==='region:76'||t?.region_code==='76',secteurs:reference||localBasin};
 if(Object.hasOwn(supported,slug)&&!supported[slug])html=unavailableTerritory(slug);
 document.querySelector('#main').innerHTML=(isMetier?`<details class="mobile-summary"><summary>Les quatre questions sur ce métier</summary>${groupedNav(slug)}</details>`:'')+html;
 if(!document.querySelector('#lieu-dialog').open)updateTerritoryChoices();
 if(options.focus!==false){document.querySelector('#main h1')?.focus({preventScroll:true});window.scrollTo(0,0);}
}
'''
replace_function('render',render,following=r'^document\.addEventListener')
text=text.replace('<strong>Montpellier</strong> et ses alentours','<strong>${esc(territoryLabel())}</strong> · votre lieu choisi')
text=text.replace("menu:'Les questions sur ce métier'", "menu:'Les questions sur ce métier',alternatives:'Quelles autres pistes explorer ?'")
text=text.replace('1. Quels savoir-faire voulez-vous retrouver ?', 'Quels savoir-faire voulez-vous retrouver ?').replace('2. Qu’aimeriez-vous découvrir ?', 'Qu’aimeriez-vous découvrir ?').replace('3. Quelles conditions comptent pour vous ?', 'Quelles conditions comptent pour vous ?')
old="document.addEventListener('submit',e=>{if(e.target.id==='search-form'){e.preventDefault();state.query=document.querySelector('#search-q').value;state.lastSearch=true;location.hash='resultats';}if(e.target.id==='guide-form'){e.preventDefault();location.hash='resultats-ogr';}});"
new="document.addEventListener('submit',e=>{if(e.target.id==='search-form'){e.preventDefault();launchSearch();}if(e.target.id==='guide-form'){e.preventDefault();location.hash='resultats-ogr';}});"
if old not in text:raise ValueError('Gestionnaire de recherche non trouvé')
text=text.replace(old,new)
path.write_text(text,encoding='utf-8')

path=SOURCE/'modele.html'
text=path.read_text(encoding='utf-8-sig')
text=text.replace('<div class="container"><div class="breadcrumb"', '<div class="search-container"><div class="container" id="persistent-search"></div></div>\n<div class="container"><div class="breadcrumb"',1)
text,n=re.subn(r'<dialog id="lieu-dialog".*?</dialog>', '<dialog id="lieu-dialog" aria-labelledby="lieu-title"><h2 id="lieu-title">Où souhaitez-vous regarder ?</h2><p>Choisissez un lieu identifié. Chaque chiffre indiquera ensuite le lieu qu’il décrit réellement.</p><div id="territory-choices"></div><p class="caption">Si une information manque pour ce lieu, elle n’est pas remplacée par les chiffres d’un autre lieu.</p><div class="actions"><button class="btn primary" type="button" data-apply-territory>Choisir ce lieu</button><form method="dialog"><button class="btn">Annuler</button></form></div></dialog>',text,count=1,flags=re.S)
if n!=1:raise ValueError('Dialogue territorial non trouvé')
css='''
.search-container{background:#f6f6fe;border-bottom:1px solid #ddd;position:sticky;top:0;z-index:4}.search-panel{border:0;margin:0}.search-panel>summary{display:none}.persistent-form{padding:16px 0 20px}.search-modes{display:flex;flex-wrap:wrap;gap:8px 24px;margin:0 0 8px}.search-modes .choice{min-height:32px;margin:0;font-size:14px}.search-modes input{margin-top:4px}.persistent-fields{display:flex;align-items:end;gap:12px}.query-field{flex:1;min-width:0}.query-field label{font-size:14px}.location-button{min-width:150px;max-width:260px;min-height:48px}.field-spaced{margin-top:20px}.decision-grid .question-card{min-height:140px}.side .four-questions a{font-size:15px;padding-top:16px;padding-bottom:16px}.side details{margin:24px 0}.side summary{font-size:14px}.side details a{font-size:13px}.side{top:205px}.four-questions{border-left:1px solid #ddd}.four-questions a{display:block;padding:14px 16px;text-decoration:none}.four-questions a[aria-current="page"]{background:#ececfe;color:#000091;font-weight:bold}#main h1{scroll-margin-top:220px}#lieu-dialog{max-height:90vh;overflow:auto}#lieu[size]{min-height:180px}main,article,.query-field{min-width:0}
@media(max-width:760px){.search-container{position:static}.search-panel>summary{display:block;padding-left:0}.search-panel:not([open])>summary{padding-bottom:16px}.persistent-form{padding-top:4px}.persistent-fields{display:grid;grid-template-columns:1fr}.persistent-fields .btn{justify-self:start}.search-modes{display:block}.search-modes .choice{min-height:40px}.location-button{max-width:100%}.mobile-summary .four-questions{padding:0 8px}.mobile-summary details{margin:0 12px 16px}.decision-grid .question-card{min-height:112px}#main h1{scroll-margin-top:24px}}
'''
text=text.replace('</style>',css+'</style>',1)
path.write_text(text,encoding='utf-8')
print('Point d’entrée, navigation et composants reliés aux vues existantes.')
