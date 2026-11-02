/* Présentation uniquement : mêmes réponses natives, paramètres, routes et état. */
function apercuQuestion(question){
 const P=MaInfographie,reference=state.territoryKey==='commune:34172';
 const meta=(measure,source,population='')=>{
  const scales={com:'Commune',dep:'Département',clpe:'Bassin d’emploi',reg:'Région',nat:'France entière'};
  const place=(scales[measure.maille_reelle]||'Lieu mesuré')+' : '+measure.territoire_libelle;
  return P.provenance({place,date:measure.millesime,source,population})+(measure.repli?'<span class="ma-family-note">Ces chiffres concernent un lieu plus large que la commune choisie.</span>':'');
 };
 if(question.id==='comprendre'){
  const contexts=(DATA.metier.contexte_travail_libelles||[]).filter(label=>['En extérieur','En grande hauteur','Sur chantier'].includes(label));
  return `<ul class="ma-context-list" aria-label="Quelques conditions mentionnées">${contexts.map(label=>`<li>${esc(label)}</li>`).join('')}</ul>`+P.provenance({source:'France Travail · description du métier'})+'<span class="ma-family-note">Les autres conditions restent à consulter dans la fiche.</span>';
 }
 if(question.id==='opportunites'){
  if(!reference)return '<span class="ma-family-note">Les repères correspondant au lieu choisi restent à vérifier. Aucun chiffre de Montpellier n’est attribué à un autre lieu.</span>';
  const measure=getMeasure('projets_recrutement');
  if(!measure)return '<span class="ma-family-note">Les projets de recrutement ne sont pas renseignés pour cette sélection.</span>';
  return (measure.valeurs||[]).map(row=>P.repere({value:row.nb_projets_recrutement,unit:'projets',label:row.fap_228_libelle,context:typeof row.nb_rome_famille==='number'?`Groupe de ${row.nb_rome_famille} métier${row.nb_rome_famille>1?'s':''}`:'Groupe de métiers',field:'nb_projets_recrutement',measure:measure.mesure})).join('')+meta(measure,'France Travail · BMO')+'<span class="ma-family-note">Des intentions déclarées, pas des offres disponibles. Les groupes ne s’additionnent pas.</span>';
 }
 if(question.id==='gagner'){
  if(!reference)return '<span class="ma-family-note">Consultez les salaires pour vérifier les informations disponibles dans votre lieu. Aucune valeur d’un autre lieu ne le remplace.</span>';
  const measure=getMeasure('salaires');
  if(!measure)return '<span class="ma-family-note">Le salaire n’est pas renseigné pour cette sélection.</span>';
  return (measure.valeurs||[]).map(row=>P.repere({value:row.salaire_net_mensuel_median,unit:'€ nets / mois',label:'Salaire médian',context:row.fap_225_libelle,field:'salaire_net_mensuel_median',measure:measure.mesure})+meta(measure,'INSEE · traitements RCO',`Groupe de ${row.nb_rome_famille} métiers · salariés à temps complet`)).join('')+'<span class="ma-family-note">La moitié des salaires est en dessous, l’autre moitié au-dessus. Ce montant ne décrit pas les seuls couvreurs.</span>';
 }
 const codes=DATA.metier.metiers_proches_codes||[],labels=DATA.metier.metiers_proches_libelles||[];
 const index=codes.indexOf('F1613'),name=index>=0?labels[index]:labels[0];
 return (name?`<span class="ma-family-note">Un des métiers signalés comme proches</span><span class="ma-nearby-name">${esc(name)}</span>`:'<span class="ma-family-note">Les liens reçus vers d’autres métiers sont présentés dans la fiche.</span>')+P.provenance({source:'France Travail · métiers proches'})+'<span class="ma-family-note">Comparez les tâches, les conditions et les formations. Un métier proche n’est pas une reconversion garantie.</span>';
}
function cartesQuestions(){
 const icons={comprendre:'briefcase-line',opportunites:'map-pin-2-line',gagner:'money-euro-circle-line',pistes:'bookmark-line'};
 return `<div class="question-grid decision-grid">${questions.map(q=>MaInfographie.question({id:q.id,title:q.title,description:q.text,href:'#'+(q.id==='comprendre'?'competences':q.to),icon:icons[q.id],preview:apercuQuestion(q)})).join('')}</div>`;
}
function disposerInfographie(slug,root){
 document.body.dataset.view=slug;
 MaInfographie.decorate(root);
 // Rapprocher les visualisations officielles de leur question, sans modifier
 // les modèles, l'ordre interne des séries ou leur ouverture à la demande.
 if(!['salaires','recrutements'].includes(slug))return;
 const sections=[...root.querySelectorAll(':scope > .ma-dataviz')];
 const tables=[...root.querySelectorAll(':scope > .table-wrap')];
 for(const section of sections){
  const title=section.querySelector('h3')?.textContent||'';let anchor;
  if(slug==='salaires'){
   if(title==='Un repère pour le salaire mensuel')anchor=root.querySelector('.metric-grid');
   if(title==='Trois repères pour comprendre les salaires')anchor=tables[0];
   if(title==='Les salaires selon l’activité de l’entreprise')anchor=tables[1];
  }else if(title==='Les intentions de recrutement'||title==='Les difficultés anticipées par les employeurs'||title==='La part des projets saisonniers')anchor=tables[0];
  if(anchor){
   // Un même emplacement peut recevoir plusieurs groupes : garder leur ordre.
   const last=anchor.__maPresentationTail||anchor;last.after(section);anchor.__maPresentationTail=section;
  }
 }
}
