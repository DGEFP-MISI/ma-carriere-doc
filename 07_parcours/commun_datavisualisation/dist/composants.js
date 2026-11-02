window.MaDataviz=(()=>{
/* Adaptateurs purs : aucune requête, aucun calcul d'indicateur métier. */
function valeur(value) {
  if (value === 'secret_stat') return {etat:'confidentiel', texte:'Non publié pour protéger les personnes'};
  if (value === null) return {etat:'null', texte:'Donnée non disponible'};
  if (value === undefined) return {etat:'absent', texte:'Information non fournie'};
  if (typeof value !== 'number' || !Number.isFinite(value)) return {etat:'invalide', texte:'Valeur non exploitable'};
  return {etat:'nombre', nombre:value, texte:new Intl.NumberFormat('fr-FR',{maximumFractionDigits:2}).format(value)};
}
function serie(rows, label, field, {pourcentage=false, negatif=false}={}) {
  return rows.map(row=>{
    let v=valeur(row[field]);
    if(v.etat==='nombre' && ((!negatif && v.nombre<0)||(pourcentage && v.nombre>100))) v={etat:'invalide',texte:'Valeur hors des bornes attendues'};
    return {libelle:String(typeof label==='function'?label(row):row[label]??'Libellé non fourni'),...v};
  });
}
function groupes(rows, field) {
  return [...new Set(rows.map(r=>r[field]))].filter(Boolean).map(code=>({code,rows:rows.filter(r=>r[field]===code)}));
}
function moisConsecutifs(rows) {
  if(rows.length<2) return false;
  const ids=rows.map(r=>/^\d{4}-\d{2}$/.test(r.periode_code)?Number(r.periode_code.slice(0,4))*12+Number(r.periode_code.slice(5)):NaN);
  return ids.every((id,i)=>Number.isFinite(id)&&(!i||id===ids[i-1]+1));
}
// Nomenclature technique des cartes DSFR Chart 2.1.1, rapprochée des libellés
// /territoires et des libellés des réponses /salaires et /recrutements.
const regionsCarte=Object.freeze({'84':'ARA','27':'BFC','53':'BRE','24':'CVL','44':'GES','32':'HDF','11':'IDF','28':'NOR','75':'NAQ','76':'OCC','52':'PDL','93':'PAC','94':'20R','01':'971','02':'972','03':'973','04':'974','06':'976'});
function carte(rows, field, zonage) {
  if(!['region','departement'].includes(zonage)) return null;
  const data={};
  for(const row of rows){
    const v=valeur(row[field]);
    const key=zonage==='region'?regionsCarte[row.territoire_code]:row.territoire_code;
    // Une valeur de repli ne colorie jamais le territoire demandé.
    if(v.etat==='nombre' && key && row.repli!==true && (!row.maille||row.maille===(zonage==='region'?'reg':'dep'))) data[key]=v.nombre;
  }
  return data;
}

// Compositions officielles DataBox / BarChart / LineChart / MapChart / TableChart.
const escape=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let sequence=0;
const registry=new Map();
function begin(){registry.clear();}
function html(model){
 model={...model,source:String(model.source).replace(/\bAPI\s*/g,'')};
 const id='ma-viz-'+(++sequence); registry.set(id,model);
 const fallback=`<div class="fr-table"><table><caption>${escape(model.title)} — ${escape(model.unit||'valeur')}</caption><thead><tr><th scope="col">Ce que l’on regarde</th><th scope="col">Valeur</th></tr></thead><tbody>${model.rows.map(r=>`<tr><th scope="row">${escape(r.libelle)}</th><td>${escape(r.texte)}${r.etat==='nombre'?' '+escape(model.unit||''):''}</td></tr>`).join('')}</tbody></table></div>`;
 return `<section class="ma-dataviz ${model.kind==='map'?'ma-viz-map':''} ${model.axisLabels?'ma-viz-compact':''}" data-viz="${id}"><h3>${escape(model.title)}</h3><p>${escape(model.description)}</p><p class="caption">Source : ${escape(model.source)} · Période : ${escape(model.date)}</p><details class="ma-chart-details"><summary>Voir ${model.kind==='key'?'le repère':'le graphique'} et son tableau</summary><p class="ma-small-screen">Le graphique peut défiler horizontalement. Vous pouvez aussi lire les chiffres dans le tableau.</p><div class="ma-chart-target" tabindex="0" role="region" aria-label="${escape(model.title)} : graphique et tableau"></div></details><details class="ma-fallback"><summary>Lire directement les chiffres</summary>${model.rows.length?fallback:'<p>Aucune donnée publiée pour cette sélection.</p>'}</details></section>`;
}
function hydrate(section){
 if(section.dataset.hydrated)return;
 const id=section.dataset.viz,m=registry.get(id);if(!m)return;
 section.dataset.hydrated='true';
 const target=section.querySelector('.ma-chart-target'),numbers=m.rows.map((r,index)=>({...r,index})).filter(r=>r.etat==='nombre');
 if(!numbers.length){target.innerHTML='<p>Aucune valeur chiffrée ne peut être représentée. Les raisons sont précisées dans le tableau.</p>';return;}
 if(m.kind==='key'){
  target.innerHTML=`<data-box id="${id}" name="${escape(m.title)}" heading-level="h3" value="${escape(numbers[0].texte+' '+m.unit)}" description="${escape(escape(m.description))}" source="${escape(m.source)}" date="${escape(m.date)}" segmented-control="false" fullscreen="false" screenshot="false" download="false"></data-box>`;
  return;
 }
 const attrs=`databox-id="${id}" databox-source="default"`;
 const x=numbers.map(r=>m.axisLabels?.[r.index]||r.libelle),y=numbers.map(r=>r.nombre);
 let chart;
 if(m.kind==='map'&&m.map&&Object.keys(m.map).length){
  const indicator=m.unit==='€ nets par mois'?'Salaire net médian par mois':m.unit==='projets'?'Projets de recrutement':'Postes à pourvoir d’ici à 2030';
  chart=`<map-chart ${attrs} databox-type="chart" level="${m.level||'reg'}" data="${escape(JSON.stringify(m.map))}" name="${escape(indicator)}" value="${escape(m.national?.etat==='nombre'?m.national.texte+' '+m.unit:'Non publié')}" date="${escape(m.date)}"></map-chart>`;
 }else if(m.kind==='line'){
  chart=`<line-chart ${attrs} databox-type="chart" x="${escape(JSON.stringify(x))}" y="${escape(JSON.stringify([y]))}" name="${escape(JSON.stringify([m.unit||'Nombre']))}" unit-tooltip="${escape(m.unit)}" aspect-ratio="1.5"></line-chart>`;
 }else{
  chart=`<bar-chart ${attrs} databox-type="chart" x="${escape(JSON.stringify([x]))}" y="${escape(JSON.stringify([y]))}" name="${escape(JSON.stringify([m.unit||'Nombre']))}" horizontal="true" stacked="false" unit-tooltip="${escape(m.unit)}" aspect-ratio="${numbers.length>8?'0.8':'1.5'}"></bar-chart>`;
 }
 // TableChart interprète le HTML : chaque chaîne provenant de l'API est échappée.
 const lines=m.rows.map(r=>[escape(r.libelle),escape(r.texte+(r.etat==='nombre'?' '+(m.unit||''):''))]);
 target.innerHTML=`<data-box id="${id}" name="${escape(m.title)}" heading-level="h3" description="${escape(escape(m.description))}" source="${escape(m.source)}" date="${escape(m.date)}" default-source="default" segmented-control="true" fullscreen="false" screenshot="false" download="false"></data-box>${chart}<table-chart ${attrs} databox-type="table" line="${escape(JSON.stringify(lines))}" name='["Ce que l’on regarde","Valeur"]'></table-chart>`;
 if(m.kind==='map'&&m.map&&Object.keys(m.map).length){
  // La carte native laisse certains territoires à leur couleur SVG initiale.
  // Neutraliser uniquement les géométries sans valeur : aucun tracé personnalisé.
  const neutraliser=()=>{
   const paths=target.querySelectorAll('svg path[class*="FR-"]');if(!paths.length)return false;
   for(const path of paths){const codes=(path.getAttribute('class')||'').split(/\s+/).filter(c=>c.startsWith('FR-')).map(c=>c.slice(3));path.toggleAttribute('data-ma-missing',!codes.some(c=>Object.hasOwn(m.map,c)));}
   return true;
  };
  const observer=new MutationObserver(()=>{if(neutraliser())observer.disconnect();});
  observer.observe(target,{childList:true,subtree:true});
  if(neutraliser())observer.disconnect();
  const legend=document.createElement('p');legend.className='ma-map-legend';legend.textContent='Gris : aucune valeur publiée pour cette zone dans la sélection. Cela ne signifie pas zéro.';target.append(legend);
 }
 setTimeout(()=>{
  const region=document.getElementById(id+'-chart-default');
  if(region){region.tabIndex=0;region.setAttribute('role','region');region.setAttribute('aria-label',m.title+' : graphique défilant');}
 },0);
}
function mount(root=document){
 for(const section of root.querySelectorAll('.ma-dataviz')){
  section.querySelector('.ma-chart-details').addEventListener('toggle',e=>{if(e.target.open)hydrate(section);});
 }
}
function hydrateAll(root=document){for(const section of root.querySelectorAll('.ma-dataviz')){section.querySelector('.ma-chart-details').open=true;hydrate(section);}}
return {begin,html,mount,hydrateAll,valeur,serie,groupes,carte,moisConsecutifs,regionsCarte};

})();
/* Compositions de présentation, sans route, état utilisateur ou règle statistique. */
window.MaInfographie=(()=>{
 const escape=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const icons=new Set(['briefcase-line','map-pin-2-line','money-euro-circle-line','bookmark-line','arrow-right-line','search-line']);
 function icon(name){return icons.has(name)?`<span class="fr-icon-${name} ma-icon" aria-hidden="true"></span>`:'';}
 function question({id,title,description,href,icon:illustration,preview=''}){
  return `<a class="question-card ma-question" data-question="${escape(id)}" href="${escape(href)}"><span class="ma-question-icon">${icon(illustration)}</span><strong class="ma-question-title">${escape(title)}</strong><span class="ma-question-description">${escape(description)}</span>${preview?`<div class="ma-question-preview">${preview}</div>`:''}<span class="ma-question-action">Approfondir cette question ${icon('arrow-right-line')}</span></a>`;
 }
 function repere({value,unit='',label='',context='',field='',measure=''}){
  const datum=MaDataviz.valeur(value);
  return `<div class="ma-repere" data-measure="${escape(measure)}" data-field="${escape(field)}"><span class="ma-value ma-value--${escape(datum.etat)}">${escape(datum.texte)}${datum.etat==='nombre'&&unit?`<span class="ma-unit">${escape(unit)}</span>`:''}</span>${label?`<span class="ma-repere-label">${escape(label)}</span>`:''}${context?`<span class="ma-repere-context">${escape(context)}</span>`:''}</div>`;
 }
 function provenance({source,place,date,population}){
  return `<span class="ma-provenance">${[place,date,population,source].filter(Boolean).map(escape).join(' · ')}</span>`;
 }
 function decorate(root){
  for(const card of root.querySelectorAll('.result-card')){
   card.classList.add('ma-result');
   if(!card.querySelector(':scope > .ma-result-icon')){const node=document.createElement('span');node.className='ma-result-icon';node.innerHTML=icon('briefcase-line');card.prepend(node);}
  }
  // Remplacer uniquement les anciennes flèches décoratives, jamais un nom de commande.
  for(const node of root.querySelectorAll('a.btn > span[aria-hidden="true"]'))if(node.textContent.trim()==='→'){node.textContent='';node.classList.add('fr-icon-arrow-right-line','ma-icon');}
 }
 return {escape,icon,question,repere,provenance,decorate};
})();
