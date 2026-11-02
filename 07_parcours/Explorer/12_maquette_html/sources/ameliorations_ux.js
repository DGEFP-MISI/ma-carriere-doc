// Petites compositions d'interaction. Aucune donnée métier ni recommandation créée.
function pageTitle(slug,id){
 if(slug==='resultats')return {metier:'Les métiers à découvrir',certification:'Les diplômes et titres à découvrir',domaine:'Les domaines professionnels à découvrir'}[state.mode];
 if(slug==='certification'&&id)return catalogue.certification(id)?.certifinfo_libelle||'Certification non disponible';
 if(slug==='domaine'&&id)return catalogue.domaine(id)?.domaine_libelle||'Domaine non disponible';
 return titles[slug]||catalogue.metier(id)?.rome_libelle||'Votre exploration';
}
function pisteControl(code,primary=false){
 const saved=state.pistes.includes(code),label=catalogue.metier(code)?.rome_libelle||name(code);
 return `<span class="piste-control" data-piste-control="${esc(code)}" data-primary="${primary}">${saved?`<span class="piste-status">Piste gardée</span><button type="button" class="btn fr-btn fr-btn--secondary" data-remove="${esc(code)}" aria-label="Retirer ${esc(label)} de mes pistes">Retirer cette piste</button><a href="#pistes">Retrouver Mes pistes</a>`:`<button type="button" class="btn fr-btn ${primary?'primary':'fr-btn--secondary'}" data-save="${esc(code)}" aria-label="Garder ${esc(label)} dans mes pistes">Garder cette piste</button>`}</span>`;
}
function updatePisteControls(){
 const focused=document.activeElement?.closest('[data-piste-control]')?.dataset.pisteControl;
 for(const wrapper of document.querySelectorAll('[data-piste-control]')){
  const holder=document.createElement('div');holder.innerHTML=pisteControl(wrapper.dataset.pisteControl,wrapper.dataset.primary==='true');wrapper.replaceWith(holder.firstElementChild);
 }
 document.querySelector('#piste-count').textContent=state.pistes.length;
 if(focused)document.querySelector(`[data-piste-control="${focused}"] button`)?.focus({preventScroll:true});
}
function guideSkills(){
 return (DATA.competencesRecherche||[]).flatMap(response=>response.items||[]).filter(item=>item.categorie_competence_code==='savoir_faire');
}
function guideCount(){return state.skills.length+Object.values(state.contexts).filter(Boolean).length+(state.domain?1:0);}
function guideChips(){return guideSkills().filter(item=>state.skills.includes(item.competence_code)).map(item=>`<span class="chip">${esc(item.competence_libelle)}<button type="button" data-remove-skill="${esc(item.competence_code)}" aria-label="Retirer le critère : ${esc(item.competence_libelle)}">×</button></span>`).join('');}
function updateGuideSelection(){
 const count=document.getElementById('guide-count'),chips=document.getElementById('guide-selection');
 if(count)count.textContent=`${guideCount()} critère${guideCount()>1?'s':''} choisi${guideCount()>1?'s':''}, dont ${state.skills.length} savoir-faire.`;
 if(chips)chips.innerHTML=guideChips();
 if(guideCount()){const error=document.getElementById('guide-error');if(error)error.hidden=true;document.getElementById('guide-skills')?.removeAttribute('aria-invalid');}
}
function experienceGuide(){
 const skills=guideSkills(),domains=catalogue.domaines;
 return intro('guide','Partez des activités que vous connaissez ou que vous aimeriez apprendre. Vous n’avez pas besoin d’avoir un métier cible.')+
 `<p id="guide-help">La recherche proposée ici porte sur les ${skills.length===2?'deux':skills.length} savoir-faire ci-dessous et les fiches disponibles. Elle ne couvre pas tous les métiers. Choisir un savoir-faire ne signifie pas que vous le maîtrisez.</p><form id="guide-form"><fieldset id="guide-skills" aria-describedby="guide-help guide-count guide-error"><legend>Quels savoir-faire voulez-vous retrouver ?</legend>${skills.map(item=>`<label class="choice"><input type="checkbox" name="skill" value="${esc(item.competence_code)}" ${state.skills.includes(item.competence_code)?'checked':''}>${esc(item.competence_libelle)}</label>`).join('')}<p id="guide-count" role="status" aria-live="polite">${guideCount()} critère${guideCount()>1?'s':''} choisi${guideCount()>1?'s':''}, dont ${state.skills.length} savoir-faire.</p><p id="guide-error" class="field-error" role="alert" hidden>Choisissez au moins un savoir-faire, un domaine ou une condition pour explorer.</p><div id="guide-selection">${guideChips()}</div></fieldset><fieldset><legend>Comment chercher les métiers ?</legend>${[['au_moins_une','Les métiers qui utilisent au moins un de ces savoir-faire'],['toutes','Les métiers qui utilisent tous ces savoir-faire']].map(([v,l])=>`<label class="choice"><input type="radio" name="match" value="${v}" ${state.match===v?'checked':''}>${l}</label>`).join('')}</fieldset><label for="guide-domain">Dans quel domaine ?</label><select id="guide-domain" name="domain" aria-describedby="guide-coverage"><option value="">Tous les domaines disponibles</option>${domains.map(d=>`<option value="${esc(d.domaine_code)}" ${state.domain===d.domaine_code?'selected':''}>${esc(d.domaine_libelle)}</option>`).join('')}</select><p id="guide-coverage" class="caption">Certaines combinaisons de domaine, de savoir-faire et de conditions ne sont pas renseignées dans les données consultables.</p><h2>Quelles conditions comptent pour vous ?</h2>${Object.keys(state.contexts).map(c=>`<fieldset><legend>${esc(name(c))}</legend><div class="choices-inline">${[['','Pas de préférence'],['avec','Je recherche cette condition'],['sans','Je préfère l’éviter']].map(([v,t])=>`<label class="choice"><input type="radio" name="context-${c}" value="${v}" ${state.contexts[c]===v?'checked':''}>${t}</label>`).join('')}</div></fieldset>`).join('')}${info('À vérifier sur le poste qui vous intéresse','Les fiches décrivent les métiers en général. Une condition absente de la fiche peut exister dans certains emplois.')}<button class="btn primary" type="submit">Découvrir les métiers associés</button></form>`+source('France Travail, savoir-faire et liens avec les métiers');
}
function guideMatches(){
 const ids=[...new Set(state.skills)].sort(),available=guideSkills();
 if(!guideCount())return {status:'selection',items:[]};
 if(state.domain||Object.values(state.contexts).some(Boolean)||ids.some(id=>!available.some(s=>s.competence_code===id)))return {status:'unavailable',items:[]};
 if(ids.length===1){
  const skill=available.find(s=>s.competence_code===ids[0]);
  return skill?{status:'covered',items:(skill.rome_codes||[]).map(code=>catalogue.metier(code)).filter(Boolean)}:{status:'unavailable',items:[]};
 }
 if(ids.join('|')==='103659|125416'&&['toutes','au_moins_une'].includes(state.match))return {status:'covered',items:DATA.r23[state.match]||[]};
 return {status:'unavailable',items:[]};
}
function experienceGuideResults(){
 const result=guideMatches();
 let html=intro('resultats-ogr','Ces métiers sont liés aux savoir-faire choisis dans les données disponibles. Ils peuvent vous donner des idées, sans décider à votre place.');
 if(result.status==='selection')html+=info('Par quoi aimeriez-vous commencer ?','Choisissez au moins un savoir-faire, un domaine ou une condition. Aucun choix n’est fait à votre place.');
 else if(result.status==='unavailable')html+=info('Cette combinaison n’est pas renseignée ici','Vos choix sont conservés. Les données consultables ne permettent pas de présenter des métiers pour cette combinaison. Cela ne prouve pas qu’aucun métier ne correspond.',true);
 else if(!result.items.length)html+=`<div class="empty"><h2>Aucun métier dans les fiches disponibles</h2><p>Essayez un autre savoir-faire. Ce résultat concerne les fiches consultables ici, pas l’ensemble des métiers.</p></div>`;
 else html+=`<p class="result-count">${result.items.length} métier${result.items.length>1?'s':''} à découvrir dans les fiches disponibles.</p>`+result.items.map(card).join('');
 return html+info('Un lien avec le métier ne mesure pas votre maîtrise','La présence d’un savoir-faire dans un métier ne signifie pas que vous le maîtrisez. Les tâches, les formations et les conditions du poste restent à examiner.')+`<div class="actions">${a('Modifier mes choix','guide',true)}${a('Rechercher un métier','recherche')}</div>`+source('France Travail, liens entre savoir-faire et métiers');
}
function submitGuide(){
 if(!guideCount()){
  const error=document.getElementById('guide-error');error.hidden=false;document.getElementById('guide-skills').setAttribute('aria-invalid','true');document.querySelector('[name="skill"]')?.focus();return;
 }
 location.hash='resultats-ogr';
}
