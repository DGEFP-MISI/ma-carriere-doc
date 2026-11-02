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
