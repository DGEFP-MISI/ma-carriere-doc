// Captures reproductibles, activées seulement par ?apercu=salaires/territoires.
(()=>{
 let params=new URLSearchParams(location.search);
 try{if(window.parent!==window)params=new URLSearchParams(parent.location.search);}catch{}
 const view=params.get('apercu');if(!['salaires','territoires'].includes(view))return;
 state.territoryKey='commune:34172';location.hash=view;
 setTimeout(()=>{
  render();const sections=[...document.querySelectorAll('.ma-dataviz')];
  const section=sections.find(s=>s.querySelector('h3').textContent.includes(view==='salaires'?'Trois repères':'sur une carte'));
  if(!section)return;section.querySelector('details').open=true;
  setTimeout(()=>{section.scrollIntoView({block:'start',behavior:'instant'});window.scrollBy(0,innerWidth>760?-210:-24);},300);
 },100);
})();
async function verifierDSFRChart(check,errors,go){
 const pause=ms=>new Promise(r=>setTimeout(r,ms));
 const until=async predicate=>{for(let n=0;n<25;n++){if(predicate())return true;await pause(50);}return false;};
 check('Bibliothèques officielles enregistrées',!!customElements.get('data-box')&&!!customElements.get('bar-chart')&&!!customElements.get('map-chart')&&!!customElements.get('table-chart'));
 check('Zéro, absence, confidentialité distincts',MaDataviz.valeur(0).nombre===0&&MaDataviz.valeur(null).etat==='null'&&MaDataviz.valeur(undefined).etat==='absent'&&MaDataviz.valeur('secret_stat').etat==='confidentiel');
 state.territoryKey='commune:34172';
 await go('salaires');
 check('Graphiques chargés à la demande',document.querySelectorAll('bar-chart').length===0&&document.querySelectorAll('.ma-dataviz').length>=3);
 const section=[...document.querySelectorAll('.ma-dataviz')].find(s=>s.querySelector('h3').textContent.includes('Trois repères'));section.querySelector('details').open=true;
 check('Barres réellement dessinées',await until(()=>section.querySelector('canvas')?.width>0));
 const chart=section.querySelector('bar-chart');
 check('Quantiles annuels issus du JSON',JSON.parse(chart.getAttribute('y'))[0].join('|')==='17400|20300|22000');
 const id=section.dataset.viz;
 check('Table officielle réellement rendue',await until(()=>section.querySelector('table-chart')&&document.getElementById(id+'-table-default')?.querySelector('table')));
 const tableControl=document.getElementById('segmented-table-'+id);tableControl?.click();await pause(50);
 const icon=section.querySelector('.fr-icon-table-2');
 check('Icône officielle du tableau chargée',!!icon&&getComputedStyle(icon,'::before').getPropertyValue('mask-image')!=='none');
 check('Bascule accessible vers tableau',tableControl?.checked&&document.getElementById(id+'-table-default')?.getAttribute('aria-hidden')!=='true');
 check('Table : mêmes valeurs et en-têtes',document.getElementById(id+'-table-default')?.textContent.includes('17 400')&&document.getElementById(id+'-table-default')?.querySelector('th[scope="col"]'));
 check('Reflow graphique salaires',document.documentElement.scrollWidth<=innerWidth+1);
 await go('recrutements');
 const lineSection=[...document.querySelectorAll('.ma-dataviz')].find(s=>s.textContent.includes('Les offres collectées chaque mois'));
 if(lineSection){lineSection.querySelector('details').open=true;check('Courbe mensuelle réelle',await until(()=>lineSection.querySelector('canvas')?.width>0));}
 else check('Courbe mensuelle présente',false);

 await go('territoires');
 const mapSection=[...document.querySelectorAll('.ma-dataviz')].find(s=>s.querySelector('h3').textContent.includes('sur une carte'));
 mapSection.querySelector('details').open=true;
 check('Carte officielle réellement dessinée',await until(()=>mapSection.querySelector('svg path.FR-BRE')));
 check('Codes carte vérifiés et valeurs conservées',JSON.parse(mapSection.querySelector('map-chart').getAttribute('data')).BRE===1900);
 check('Zone sans donnée neutralisée visuellement',await until(()=>mapSection.querySelector('svg path.FR-971')?.hasAttribute('data-ma-missing')));
 check('Absence sur la carte ne signifie pas zéro',mapSection.textContent.includes('Cela ne signifie pas zéro')&&getComputedStyle(mapSection.querySelector('svg path.FR-971')).fill==='rgb(206, 206, 206)');
 
 check('Reflow carte',document.documentElement.scrollWidth<=innerWidth+1);
 check('Repère national publié sans NaN',!mapSection.textContent.includes('NaN')&&mapSection.querySelector('map-chart').getAttribute('value').includes('€ nets par mois'));
 const deptMap=[...document.querySelectorAll('.ma-dataviz')].find(s=>s.textContent.includes('département')&&s.textContent.includes('sur une carte'));
 // Les titres de carte sont communs ; le niveau effectif est porté par le modèle.
 const maps=[...document.querySelectorAll('.ma-dataviz')].filter(s=>s.querySelector('h3').textContent.includes('sur une carte'));
 if(maps[2]){maps[2].querySelector('details').open=true;check('Carte départementale rendue',await until(()=>maps[2].querySelector('svg path.FR-34')));}
 const linkForm=document.querySelector('#viz-territory-form');
 check('Passerelle territoriale utilise les lieux observés',!!linkForm&&[...linkForm.querySelectorAll('option')].every(o=>catalogue.territoire(o.value)));
 document.getElementById('viz-region-0').value='11';document.getElementById('viz-region-1').value='76';
 document.getElementById('viz-region-compare').dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));
 check('Deux régions filtrées sans fusion de grains',state.vizRegionCompare.join('|')==='11|76'&&document.querySelector('.ma-dataviz .ma-fallback tbody').children.length===2);
 document.querySelector('[data-viz-all-regions]').click();
 check('Retour au classement régional complet',!state.vizRegionCompare&&document.querySelector('.ma-dataviz .ma-fallback tbody').children.length>2);
 await go('prospective');state.prospectiveTab='composantes';render();
 const projection=document.querySelector('.ma-dataviz');projection.querySelector('details').open=true;
 check('Projection réellement dessinée',await until(()=>projection.querySelector('canvas')?.width>0));
 
 check('Valeurs négatives conservées',JSON.parse(projection.querySelector('bar-chart').getAttribute('y'))[0].includes(-1035));
 const scrollRegion=projection.querySelector('[id$="-chart-default"]');scrollRegion?.focus();
 check('Zone graphique atteignable au clavier',document.activeElement===scrollRegion&&scrollRegion?.getAttribute('aria-label'));
 state.prospectiveTab='regions';render();
 const prospectiveMap=document.querySelector('.ma-viz-map');prospectiveMap.querySelector('details').open=true;
 check('Carte prospective réelle',await until(()=>prospectiveMap.querySelector('svg path.FR-IDF')));
 check('Perspective conserve le chiffre régional',JSON.parse(prospectiveMap.querySelector('map-chart').getAttribute('data')).IDF===7155);
 await go('mobilites');state.mobilitySens='origines';render();
 const mobility=document.querySelector('.ma-dataviz');mobility.querySelector('details').open=true;
 check('Mobilités origines réellement dessinées',await until(()=>mobility.querySelector('canvas')?.width>0));
 check('Aucune barre personnalisée restante',!document.querySelector('.bar-track,.bar-fill'));
 await go('certification/112561');
 check('Insertion : populations séparées',document.querySelectorAll('.ma-dataviz').length>=6&&document.querySelector('main').textContent.includes('314 sortants'));
 check('Null n’est pas représenté par zéro',document.querySelector('main').textContent.includes('Donnée non disponible'));
 const zero=[...document.querySelectorAll('.ma-dataviz')].find(s=>s.textContent.includes('Les abandons de formation'));
 zero.querySelector('details').open=true;
 check('DataBox chiffre clé affiche zéro',await until(()=>zero.querySelector('data-box')?.getAttribute('value')==='0 %'));
 check('Table toujours accessible sans graphique',!!zero.querySelector('.ma-fallback table caption')&&!!zero.querySelector('.ma-fallback th[scope="row"]'));
 await go('comparateur');check('Comparateur conserve les deux sélecteurs',!!document.querySelector('#compare-left')&&!!document.querySelector('#compare-right'));
 const previous=[...state.compareIds];state.compareIds=catalogue.metiers.filter(m=>m.rome_code!=='F1610').slice(0,2).map(m=>m.rome_code);render();
 check('Comparaison : aucun chiffre emprunté à un autre métier',document.querySelectorAll('.ma-dataviz').length===0);
 state.compareIds=previous;
}
