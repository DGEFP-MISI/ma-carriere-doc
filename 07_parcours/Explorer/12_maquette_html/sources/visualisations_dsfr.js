/* Pont Explorer -> composants mutualisés. Les réponses locales restent natives. */
function visualisationsExplorer(slug){
 const V=MaDataviz,parts=[];
 const add=(title,rows,label,field,meta={},options={})=>parts.push(V.html({title,rows:V.serie(rows,label,field,options),source:meta.source_libelle||meta.source||'Source non précisée',date:meta.millesime||meta.date||'Période non précisée',description:meta.description||'',unit:meta.unit||'',kind:meta.kind,map:meta.map,level:meta.level,national:meta.national,axisLabels:meta.axisLabels}));
 const local=code=>{const m=getMeasure(code);return m?{...m,description:`${m.territoire_libelle} · ${m.repli?'Chiffres disponibles à une échelle plus large que la commune choisie. ':''}`} : null;};
 const reference=state.territoryKey==='commune:34172';
 if(slug==='salaires'&&reference){
  const m=local('salaires');for(const r of m?.valeurs||[]){
   add('Un repère pour le salaire mensuel',[r],()=>r.fap_225_libelle,'salaire_net_mensuel_median',{...m,kind:'key',unit:'€ nets par mois',description:m.description+r.fap_225_libelle+` · groupe de ${r.nb_rome_famille} métiers · salariés à temps complet. La moitié des salaires se situe en dessous de ce montant, l’autre moitié au-dessus.`});
   const meta={...m,unit:'€ nets par an',axisLabels:['Un quart','La moitié','Trois quarts'],description:m.description+r.fap_225_libelle+` · groupe de ${r.nb_rome_famille} métiers · salariés à temps complet. Les repères indiquent le montant en dessous duquel se situent un quart, la moitié et trois quarts des salaires. Ce ne sont ni le minimum ni le maximum.`};
   add('Trois repères pour comprendre les salaires',[{l:'Un quart des salaires en dessous',v:r.salaire_net_annuel_q1},{l:'La moitié en dessous',v:r.salaire_net_annuel_median},{l:'Trois quarts en dessous',v:r.salaire_net_annuel_q3}],'l','v',meta);
  }
 }
 if(['salaires','comparateur'].includes(slug)){
  const d=DATA.salairesSecteurs;
  if(slug!=='comparateur'||state.compareIds?.includes(d.rome_code))for(const g of V.groupes(d.items,'fap_225_code')){
   add('Les salaires selon l’activité de l’entreprise',g.rows,'secteur_naf38_libelle','salaire_net_mensuel_median',{...d,unit:'€ nets par mois',description:`France entière · ${g.rows[0].fap_225_libelle} · groupe de ${g.rows[0].nb_rome_famille} métiers · salariés à temps complet. Les secteurs publiés peuvent être incomplets.`});
  }
 }
 if(slug==='recrutements'&&reference){
  const m=local('projets_recrutement');for(const r of m?.valeurs||[]){
   add('Les intentions de recrutement',[{l:'Tous les projets',v:r.nb_projets_recrutement},{l:'Projets jugés difficiles',v:r.nb_projets_recrutement_difficiles},{l:'Projets saisonniers',v:r.nb_projets_recrutement_saisonniers}],'l','v',{...m,unit:'projets',description:m.description+r.fap_228_libelle+` · groupe de ${r.nb_rome_famille} métiers. Les catégories se recoupent : ne pas additionner les barres. Une intention n’est pas une embauche.`});
   add('Les difficultés anticipées par les employeurs',[r],()=>r.fap_228_libelle,'tx_projets_recrutement_difficiles',{...m,unit:'%',description:m.description+'Part publiée des projets jugés difficiles. Elle ne mesure pas vos chances de trouver un emploi.'},{pourcentage:true});
   add('La part des projets saisonniers',[r],()=>r.fap_228_libelle,'tx_projets_recrutement_saisonniers',{...m,unit:'%',kind:'key',description:m.description+r.fap_228_libelle+'. Part publiée des projets liés à une saison. Elle n’est pas recalculée à partir des nombres arrondis.'},{pourcentage:true});
   if(r.nb_projets_recrutement_saisonniers===0&&typeof r.tx_projets_recrutement_saisonniers==='number'&&r.tx_projets_recrutement_saisonniers>0)parts.push(`<p>Pour ${esc(r.fap_228_libelle)}, la source publie zéro projet saisonnier et une part de ${esc(fmt(r.tx_projets_recrutement_saisonniers))} %. Ces deux valeurs ne concordent pas ; une explication reste attendue. Elles sont conservées sans les corriger.</p>`);
  }
  const monthly=local('offres_emploi_mensuelles');
  if(monthly)for(const [field,title,unit] of [['nb_offres_emploi_mois','Les offres collectées chaque mois','offres'],['nb_postes_offres_emploi_mois','Les postes annoncés chaque mois','postes']]){
   const rows=[...monthly.valeurs].sort((a,b)=>a.periode_code.localeCompare(b.periode_code));
   const complete=V.moisConsecutifs(rows)&&rows.every(r=>V.valeur(r[field]).etat==='nombre');
   add(title,rows,'periode_code',field,{...monthly,unit,kind:complete?'line':'bar',description:monthly.description+'Offres et postes sont présentés séparément. Aucun mois manquant n’est reconstitué.'});
  }
 }
 if(slug==='territoires'){
  parts.push('<h2>Comparer les lieux avec les mêmes repères</h2><p>Chaque groupe de métiers est présenté séparément. Les cartes montrent les valeurs publiées ; une zone sans chiffre ne vaut pas zéro.</p>');
  const regions=[...new Map(DATA.cartographies.salairesRegions.items.map(r=>[r.territoire_code,r.territoire_libelle])).entries()];
  const selected=state.vizRegionCompare||[];
  parts.push(`<form id="viz-region-compare"><fieldset><legend>Comparer deux régions</legend>${[0,1].map((i)=>`<label for="viz-region-${i}">${i?'Deuxième':'Première'} région</label><select class="fr-select" id="viz-region-${i}">${regions.map(([code,label],n)=>`<option value="${esc(code)}" ${(selected[i]||regions[i]?.[0])===code?'selected':''}>${esc(label)}</option>`).join('')}</select>`).join('')}<button class="fr-btn fr-btn--secondary" type="submit">Voir ces deux régions</button> <button class="fr-btn fr-btn--tertiary" type="button" data-viz-all-regions>Voir toutes les régions</button></fieldset><p>Les recrutements et les salaires restent séparés : les groupes de métiers et les années peuvent être différents.</p></form>`);
  for(const [key,field,title,unit] of [['salairesRegions','salaire_net_mensuel_median','Les salaires selon la région','€ nets par mois'],['salairesDepartements','salaire_net_mensuel_median','Les salaires selon le département','€ nets par mois'],['recrutementsRegions','nb_projets_recrutement','Les intentions de recrutement selon la région','projets'],['recrutementsDepartements','nb_projets_recrutement','Les intentions de recrutement selon le département','projets']]){
   const d=DATA.cartographies[key],family=d.grain+'_code';
   const rows=d.zonage==='region'&&selected.length===2?d.items.filter(r=>selected.includes(r.territoire_code)):d.items;
   for(const g of V.groupes(rows,family)){
    const description=`${g.rows[0][d.grain+'_libelle']} · groupe de ${g.rows[0].nb_rome_famille} métiers. ${unit==='projets'?'Intentions déclarées, pas embauches réalisées.':'Salariés à temps complet.'}${d.zonage==='region'&&selected.length===2?' Seules les deux régions choisies sont représentées.':''}`;
    const meta={...d,description,unit};
    add(title,g.rows,'territoire_libelle',field,meta);
    add('Voir ces lieux sur une carte',g.rows,'territoire_libelle',field,{...meta,kind:'map',level:d.zonage==='region'?'reg':'dep',map:V.carte(g.rows,field,d.zonage),national:V.valeur(d.france?.find(r=>r[family]===g.code)?.[field])});
   }
  }
  const destinations=catalogue.territoires.filter(t=>['region','departement'].includes(t.zonage));
  parts.push(`<form id="viz-territory-form"><label for="viz-territory">Choisir un lieu pour consulter ses repères</label><select class="fr-select" id="viz-territory">${destinations.map(t=>`<option value="${esc(t.zonage+':'+t.territoire_code)}">${esc(t.territoire_libelle)}</option>`).join('')}</select><button class="fr-btn fr-btn--secondary" type="submit">Voir les salaires dans ce lieu</button></form>`);
  parts.push('<p><a class="fr-btn fr-btn--secondary" href="#comparateur">Comparer deux métiers</a></p>');
 }
 if(slug==='prospective'&&reference&&state.prospectiveTab==='composantes'){
  const m=local('metiers_2030');
  for(const r of m?.valeurs||[]){
   const fields=[['nb_creations_nettes_emplois_2030','Évolution du nombre d’emplois'],['nb_departs_fin_carriere_2030','Départs en fin de carrière'],['nb_postes_a_pourvoir_2030','Postes à pourvoir'],['nb_jeunes_debutants_2030','Jeunes débutants'],['nb_desequilibre_potentiel_2030','Écart entre besoins et arrivées']];
   add('Les changements possibles d’ici à 2030',fields.map(([field,l])=>({l,v:r[field]})),'l','v',{...m,unit:'personnes ou emplois selon la ligne',description:m.description+r.fap_87_libelle+` · groupe de ${r.nb_rome_famille} métiers. Projections entre 2019 et 2030. Les barres ne s’additionnent pas. Un signe moins indique une baisse ou un excédent d’arrivées selon la ligne.`},{negatif:true});
  }
 }
 if(slug==='prospective'&&state.prospectiveTab==='regions'){
  const d=DATA.prospectiveRegions;
  for(const g of V.groupes(d.items,'fap_87_code')){
   const meta={...d,unit:'postes',description:g.rows[0].fap_87_libelle+' · projections 2019–2030. Des besoins estimés, pas des offres déjà disponibles.'};
   add('Les postes à pourvoir selon la région',g.rows,'territoire_libelle','nb_postes_a_pourvoir_2030',meta);
   add('Les perspectives sur une carte',g.rows,'territoire_libelle','nb_postes_a_pourvoir_2030',{...meta,kind:'map',map:V.carte(g.rows,'nb_postes_a_pourvoir_2030','region'),national:V.valeur(d.france?.find(r=>r.fap_87_code===g.code)?.nb_postes_a_pourvoir_2030)});
  }
 }
 if(slug==='prospective'&&state.prospectiveTab==='metiers'){
  const d=DATA.prospectiveMetiers;
  const page=Math.min(state.vizProspectivePage||0,Math.max(0,Math.ceil(d.items.length/15)-1)),start=page*15,rows=d.items.slice(start,start+15);
  parts.push(`<p>Graphique : groupes ${start+1} à ${start+rows.length} sur ${d.items.length}, dans l’ordre publié. Le tableau complet reste disponible ci-dessus.</p><div class="actions"><button class="fr-btn fr-btn--secondary" data-viz-prospective-page="${page-1}" ${page===0?'disabled':''}>Groupes précédents</button><button class="fr-btn fr-btn--secondary" data-viz-prospective-page="${page+1}" ${start+15>=d.items.length?'disabled':''}>Groupes suivants</button></div>`);
  add('Les besoins estimés par groupe de métiers',rows,'fap_87_libelle','nb_postes_a_pourvoir_2030',{...d,unit:'postes',description:(d.region_libelle||'France entière')+' · projections 2019–2030. Les groupes sont plus larges qu’un métier. Aucun score d’attractivité n’est calculé.'});
 }
 if(slug==='secteurs'&&reference){
  const m=local('emploi_secteurs');for(const g of V.groupes(m?.valeurs||[],'fap_225_code'))add('Les secteurs où travaillent les personnes',g.rows,'secteur_naf38_libelle','tx_actifs_secteur',{...m,unit:'%',description:m.description+g.rows[0].fap_225_libelle+` · groupe de ${g.rows[0].nb_rome_famille} métiers. Seuls les secteurs publiés sont représentés ; aucun complément à 100 % n’est calculé.`},{pourcentage:true});
 }
 if(slug==='certification'&&(!readRoute().id||String(readRoute().id)===String(DATA.certification.certifinfo_code))){
  const d=DATA.certification;
  for(const [field,title,date,description] of [
   ['tx_ij_apprentissage_emploi_12m','L’emploi un an après un apprentissage','2023–2024',`${d.nb_ij_apprentissage_emploi_12m} personnes en emploi salarié parmi ${d.nb_ij_apprentissage_sortants} sortants suivis. Les personnes en poursuite d’études ne font pas partie de ce groupe.`],
   ['tx_ij_apprentissage_poursuite_etudes','Continuer ses études après un apprentissage','2023–2024',`${d.nb_ij_apprentissage_poursuite_etudes} personnes parmi ${d.nb_ij_apprentissage_annee_terminale} en année terminale. Ce groupe diffère de celui du taux d’emploi.`],
   ['tx_de_acces_emploi_6m','L’accès à un emploi après une formation','2024',`${d.nb_de_acces_emploi_6m} demandeurs d’emploi parmi ${d.nb_de_sortants} sortants. Accès à un emploi dans les six mois ; ce n’est pas l’emploi à une date donnée.`],
   ['tx_de_abandons','Les abandons de formation','2024','Demandeurs d’emploi formés. Zéro publié reste zéro.'],
   ['tx_examen_reussite','La réussite aux examens','Session 2023','Personnes présentées à l’examen. Ce résultat ne mesure pas les chances individuelles de réussite ou d’emploi.'],
   ['tx_ij_scolaire_emploi_12m','L’emploi après une formation scolaire','2023–2024','Anciennes personnes formées par la voie scolaire ; emploi salarié douze mois après.'],
   ['tx_insersup_emploi_salarie_12m','L’emploi après des études supérieures','2025_S2 · promotion 2024','Diplômés du supérieur suivis douze mois après le diplôme.']]){
   add(title,[d],()=>d.certifinfo_libelle,field,{source:d.source_libelle,date,unit:'%',kind:'key',description},{pourcentage:true});
  }
  add('Les salaires après des études supérieures',[d],()=>d.certifinfo_libelle,'salaire_insersup_median_12m',{source:d.source_libelle,date:'2025_S2 · promotions 2021–2022',unit:'€ nets par mois',kind:'key',description:'Diplômés du supérieur suivis douze mois après le diplôme. Cette donnée est distincte des salaires de tous les salariés. Une valeur absente ne vaut pas zéro.'});
 }
 if(slug==='comparateur')parts.push('<p class="caption">Les graphiques ne sont affichés que pour les métiers dont une réponse statistique est disponible. Un groupe de métiers commun ne prouve pas une égalité des résultats entre deux métiers. Les données du second métier restent nécessaires pour une comparaison chiffrée complète.</p>');
 return parts.join('');
}
document.addEventListener('submit',e=>{
 if(e.target.id==='viz-region-compare'){
  e.preventDefault();const codes=[document.getElementById('viz-region-0').value,document.getElementById('viz-region-1').value];
  if(codes[0]===codes[1]){notify('Choisissez deux régions différentes.');return;}
  const known=new Set(DATA.cartographies.salairesRegions.items.map(r=>r.territoire_code));
  if(codes.every(c=>known.has(c))){state.vizRegionCompare=codes;render();document.getElementById('viz-region-0').focus();}return;
 }
 if(e.target.id!=='viz-territory-form')return;e.preventDefault();
 const key=document.getElementById('viz-territory').value;
 if(!catalogue.territoire(key))return;
 state.territoryKey=key;saveSelection();location.hash='salaires';
});
document.addEventListener('click',e=>{
 if(e.target.closest('[data-viz-all-regions]')){state.vizRegionCompare=null;render();document.getElementById('viz-region-0').focus();}
 const button=e.target.closest('[data-viz-prospective-page]');if(button&&!button.disabled){state.vizProspectivePage=Math.max(0,Number(button.dataset.vizProspectivePage));render();}
});
