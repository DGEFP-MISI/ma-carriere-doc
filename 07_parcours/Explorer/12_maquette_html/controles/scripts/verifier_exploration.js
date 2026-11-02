// Scénarios exécutés dans le navigateur sur les réponses embarquées, pas sur un serveur API.
async function verifierExperience(check,errors,go,wait){
 const change=(el,value)=>{el.value=value;el.dispatchEvent(new Event('change',{bubbles:true}));};
 const setMode=mode=>{document.querySelector('.search-panel').open=true;const el=document.querySelector(`[name="search-mode"][value="${mode}"]`);el.focus();el.checked=true;el.dispatchEvent(new Event('change',{bubbles:true}));};
 const submit=async text=>{document.querySelector('#search-q').value=text;document.querySelector('#search-form').requestSubmit();await wait();};
 await go('essentiel');
 check('Quatre questions principales',document.querySelectorAll('#sidebar .four-questions > a').length===4);
 check('Mobilités et prospective restent accessibles',!!document.querySelector('#sidebar details a[href="#mobilites"]')&&!!document.querySelector('#sidebar details a[href="#prospective"]'));
 check('Pas de mur de chiffres en première lecture',document.querySelectorAll('main .decision-grid .question-card').length===4&&document.querySelectorAll('main .metric').length===0);
 check('Recherche disponible dans la fiche',!!document.querySelector('#search-form')&&document.querySelectorAll('[name="search-mode"]').length===3);
 const beforeSkip=location.hash;document.querySelector('.skip').click();
 check('Lien d’évitement sans changer de page',location.hash===beforeSkip&&document.activeElement.id==='main');
 document.querySelector('#search-q').value='couverture';document.querySelector('#search-q').dispatchEvent(new Event('input',{bubbles:true}));
 await go('competences');check('Saisie conservée entre les fiches',document.querySelector('#search-q').value==='couverture');
 check('Focus sur le titre après navigation',document.activeElement===document.querySelector('main h1'));
 setMode('certification');await submit('photovoltaïque');
 const cert=DATA.certifications.items.find(c=>normalize(c.certifinfo_libelle).includes('photovoltaique'));
 check('Recherche de certification issue du catalogue',!!cert&&state.results.mode==='certification'&&state.results.items.some(c=>c.certifinfo_code===cert.certifinfo_code));
 check('Focus conservé à la fin de la recherche',document.activeElement===document.querySelector('main h1'));
 const certLink=document.querySelector(`main a[href="#certification/${cert.certifinfo_code}"]`);check('Sélection explicite de la certification',!!certLink);certLink.click();await wait();
 check('Fiche du certificat sélectionné',document.querySelector('main h1').textContent===cert.certifinfo_libelle);
 check('Mode de recherche conservé',document.querySelector('[name="search-mode"][value="certification"]').checked);
 setMode('domaine');await submit('Second œuvre');
 check('Domaine trouvé par son nom',state.results.mode==='domaine'&&state.results.items.some(d=>d.domaine_code==='F16'));
 const domainLink=document.querySelector('main a[href="#domaine/F16"]');domainLink.click();await wait();
 check('Fiche du domaine sélectionné',document.querySelector('main h1').textContent===catalogue.domaine('F16').domaine_libelle);
 check('Les métiers restent dans le domaine choisi',document.querySelectorAll('main .result-card').length===catalogue.metiers.filter(m=>m.domaine_code==='F16').length);
 await go('guide');check('Filtres sans étapes numérotées',Array.from(document.querySelectorAll('main legend,main h2')).every(el=>!/^\s*\d+[.·]/.test(el.textContent)));
 check('Filtres accessibles simultanément',!!document.querySelector('[name="skill"]')&&!!document.querySelector('[name="match"]')&&!!document.querySelector('[name="context-300782"]'));
 await go('comparateur');change(document.querySelector('#compare-left'),'F1705');change(document.querySelector('#compare-right'),'I1604');
 check('Choix libre des deux métiers',state.compareIds.join('|')==='F1705|I1604'&&document.querySelector('main').textContent.includes(catalogue.metier('F1705').rome_libelle)&&document.querySelector('main').textContent.includes(catalogue.metier('I1604').rome_libelle));
 document.querySelector('[data-compare="marche"]').click();
 check('Pas de chiffres du couvreur attribués aux autres métiers',!document.querySelector('main').textContent.includes('1 690 € nets / mois'));
 check('Comparaison détaillée conservée',document.querySelector('main').textContent.includes('Les mobilités observées')&&document.querySelector('main').textContent.includes('Les salaires par secteur d’activité')&&document.querySelector('main').textContent.includes('Les perspectives à 2030'));
 document.querySelector('[data-swap-compare]').click();check('Inversion des métiers',state.compareIds.join('|')==='I1604|F1705');
 change(document.querySelector('#compare-right'),'I1604');check('Deux métiers identiques signalés',document.querySelector('main').textContent.includes('Choisissez deux métiers différents'));
 state.compareIds=['F1610','F1613'];
 await go('metier/F1705');document.querySelector('main [data-compare-add]').click();await wait();check('Comparer depuis la fiche prend le bon métier',state.compareIds[0]==='F1705');
 state.pistes=['F1610','F1613'];state.comparePistes=[];await go('pistes');
 for(const el of document.querySelectorAll('[name="compare-piste"]')){el.checked=true;el.dispatchEvent(new Event('change',{bubbles:true}));}
 document.querySelector('[data-compare-pistes]').click();await wait();check('Comparaison depuis deux pistes',readRoute().slug==='comparateur'&&state.compareIds.join('|')==='F1610|F1613');
 check('Territoire de référence observé',!!catalogue.territoire('commune:34172'));
 await go('salaires');document.querySelector('[data-lieu]').click();
 const other=catalogue.territoires.find(t=>t.zonage==='region'&&t.territoire_code!=='76');
 change(document.querySelector('#lieu'),other.zonage+':'+other.territoire_code);document.querySelector('[data-apply-territory]').click();
 check('Le lieu sélectionné change',state.territoryKey===other.zonage+':'+other.territoire_code&&document.querySelector('main').textContent.includes(other.territoire_libelle));
 check('Pas de transposition des chiffres de Montpellier',!document.querySelector('main').textContent.includes('1 690 € nets / mois')&&document.querySelector('main').textContent.includes('Les chiffres pour ce lieu ne sont pas disponibles ici'));
 check('Le choix territorial reste visible dans la recherche',document.querySelector('.location-button').textContent.includes(other.territoire_libelle));
 state.territoryKey='commune:34172';state.pistes=['F1610','F1613'];state.compareIds=['F1610','F1613'];saveSelection();
 if(state.storageAvailable){const saved=JSON.parse(sessionStorage.getItem(SELECTION_KEY));check('Sélection conservée dans la session',saved.metiers.join('|')==='F1610|F1613');state.pistes=[];restoreSelection();check('Reprise de la sélection en session',state.pistes.join('|')==='F1610|F1613');}
 else check('Reprise prévue sans stockage disponible',typeof importSelection==='function'&&typeof exportSelection==='function');
 const payload=selectionPayload();state.pistes=[];
 await importSelection(new File([JSON.stringify(payload)],'mes-pistes.json',{type:'application/json'}));await wait();
 check('Reprise d’un fichier de sélection',state.pistes.join('|')==='F1610|F1613'&&readRoute().slug==='pistes');
 let refused=false;try{validateSelection({...payload,metiers:['inconnu']});}catch{refused=true;}check('Un identifiant inconnu n’ajoute pas de données',refused);
 // Deux réponses différées provenant des vraies fiches : vérifier l'annulation logique, sans HTTP.
 const originalSearch=catalogue.rechercher,resolvers=[];
 try{catalogue.rechercher=()=>new Promise(resolve=>resolvers.push(resolve));state.mode='metier';await go('recherche');document.querySelector('#search-q').value='couvreur';launchSearch();document.querySelector('#search-q').value='étanchéité';launchSearch();resolvers[1]({mode:'metier',items:[catalogue.metier('F1613')]});await wait();resolvers[0]({mode:'metier',items:[DATA.metier]});await wait();check('Une réponse périmée ne remplace pas la nouvelle',state.results.items[0].rome_code==='F1613'&&state.submittedQuery==='étanchéité');}
 finally{catalogue.rechercher=originalSearch;}
 for(const slug of ['alternatives','certification/'+cert.certifinfo_code,'domaine/F16']){await go(slug);check('Reflow et titre '+slug,document.documentElement.scrollWidth<=innerWidth+1&&document.querySelectorAll('main h1').length===1);}
 state.mode='metier';state.query='';state.submittedQuery='';state.results=null;state.searchStatus='idle';state.compareIds=['F1610','F1613'];state.territoryKey='commune:34172';state.pistes=[];state.comparePistes=[];saveSelection();
}
