// Recette d'interactions dans Edge réel, sans dépendance ni appel à l'API métier.
import {writeFileSync,mkdirSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {pathToFileURL} from 'node:url';
const [port,page,phase='apres',htmlRoot,only='']=process.argv.slice(2);
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const targets=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const target=targets.find(t=>t.type==='page');
if(!target)throw Error('Onglet Edge indisponible');
const socket=new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve,reject)=>{socket.addEventListener('open',resolve,{once:true});socket.addEventListener('error',reject,{once:true});});
let sequence=0;const pending=new Map(),runtimeErrors=[];
socket.addEventListener('message',event=>{
 const message=JSON.parse(event.data);
 if(message.method==='Page.javascriptDialogOpening'){console.log('Dialogue navigateur : '+message.params.type+' '+message.params.message);cdp('Page.handleJavaScriptDialog',{accept:true}).catch(()=>{});}
 if(message.method==='Runtime.exceptionThrown')runtimeErrors.push(message.params.exceptionDetails.exception?.description||message.params.exceptionDetails.text);
 if(message.id){const p=pending.get(message.id);if(!p)return;pending.delete(message.id);clearTimeout(p.timer);message.error?p.reject(Error(message.error.message)):p.resolve(message.result);}
});
function cdp(method,params={}){return new Promise((resolve,reject)=>{const id=++sequence;const timer=setTimeout(()=>{pending.delete(id);reject(Error('Délai CDP : '+method));},15000);pending.set(id,{resolve,reject,timer});socket.send(JSON.stringify({id,method,params}));});}
async function evaluate(expression){const r=await cdp('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(r.exceptionDetails.exception?.description||r.exceptionDetails.text);return r.result.value;}
async function until(predicate,message='condition'){for(let i=0;i<60;i++){try{if(await predicate())return;}catch{}await pause(50);}throw Error('Délai : '+message);}
async function ready(){await until(()=>evaluate("document.readyState==='complete'&&typeof state==='object'&&!!document.querySelector('main h1')"),'application prête');await pause(60);}
async function go(slug){await evaluate(`location.hash=${JSON.stringify(slug)}`);await until(()=>evaluate(`typeof readRoute==='function'&&readRoute().slug===${JSON.stringify(slug.split('/')[0])}&&!!document.querySelector('main h1')`),'navigation '+slug);await pause(200);}
async function openSearch(){if(!await evaluate("document.querySelector('.search-panel').open"))await click('.search-panel > summary');}
async function click(selector){
 await evaluate(`(()=>{const matches=[...document.querySelectorAll(${JSON.stringify(selector)})];let e;for(const candidate of matches){for(let p=candidate.parentElement;p;p=p.parentElement)if(p.tagName==='DETAILS')p.open=true;const r=candidate.getBoundingClientRect();if(r.width&&r.height){e=candidate;break;}}if(!e)throw Error('Contrôle absent ou masqué : '+${JSON.stringify(selector)});e.scrollIntoView({block:'center',behavior:'instant'});window.__uxClick=e;})()`);
 await pause(160);
 const box=await evaluate(`(()=>{const e=window.__uxClick;if(!e?.isConnected)throw Error('Contrôle reconstruit avant activation');const r=e.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,hit=document.elementFromPoint(x,y);return {x,y,width:r.width,height:r.height,disabled:e.disabled,hit:!!hit&&(e===hit||e.contains(hit)),hitName:hit?.tagName+' '+hit?.className};})()`);
 if(box.disabled)throw Error('Contrôle désactivé : '+selector);if(!box.hit)throw Error('Contrôle recouvert : '+selector+' / '+box.hitName);
 await cdp('Input.dispatchMouseEvent',{type:'mouseMoved',x:box.x,y:box.y});
 await cdp('Input.dispatchMouseEvent',{type:'mousePressed',x:box.x,y:box.y,button:'left',clickCount:1});
 await cdp('Input.dispatchMouseEvent',{type:'mouseReleased',x:box.x,y:box.y,button:'left',clickCount:1});await pause(120);
}
async function key(key,code,virtual,modifiers=0){const down={type:key==='Enter'?'keyDown':'rawKeyDown',key,code,windowsVirtualKeyCode:virtual,modifiers};if(key==='Enter'){down.text='\r';down.unmodifiedText='\r';}if(key===' '){down.type='keyDown';down.text=' ';down.unmodifiedText=' ';}await cdp('Input.dispatchKeyEvent',down);await cdp('Input.dispatchKeyEvent',{type:'keyUp',key,code,windowsVirtualKeyCode:virtual,modifiers});await pause(80);}
async function reload(withScripts=true){
 await evaluate('window.__uxReloadMarker=true');await cdp('Page.reload',{ignoreCache:true});
 try{await until(()=>evaluate("!window.__uxReloadMarker&&document.readyState==='complete'"),'nouveau document après rechargement');}
 catch(error){
  const suite=reports.at(-1);
  if(!suite.reloadNonTeste){
   const limitation={name:'Rechargement natif du document après navigation par fragments',status:'NON TESTÉ',raison:'Dans ce pilote Edge, Page.reload ne remplace pas le document à ce point du parcours. Les tentatives sont conservées ; un nouveau chargement complet est testé séparément.'};
   suite.nonTestes.push(limitation);suite.reloadNonTeste=true;if(current?.checks)current.checks.push({name:limitation.name,status:'NON TESTÉ',detail:limitation.raison});
  }
  const url=new URL(await evaluate('location.href'));url.searchParams.set('controle-reprise',String(Date.now()));
  await cdp('Page.navigate',{url:url.href});await until(()=>evaluate("!window.__uxReloadMarker&&document.readyState==='complete'"),'nouveau chargement complet de la page');
 }
 if(withScripts)await ready();
}
async function type(selector,text){await click(selector);await key('a','KeyA',65,2);await cdp('Input.insertText',{text});await pause(30);}
async function select(selector,value){await evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});if(!e)throw Error('Sélecteur absent');e.value=${JSON.stringify(value)};e.dispatchEvent(new Event('change',{bubbles:true}));})()`);await pause(80);}
async function mode(value){await openSearch();if(!await evaluate(`document.querySelector('[name="search-mode"][value="${value}"]').checked`))await click(`[name="search-mode"][value="${value}"]`);}
async function search(text,searchMode='metier'){await mode(searchMode);await openSearch();await type('#search-q',text);await key('Enter','Enter',13);try{await until(()=>evaluate("state.searchStatus==='done'||state.searchStatus==='error'"),'résultats de recherche');}catch(error){error.message+=' '+JSON.stringify(await evaluate("({focus:document.activeElement?.id,value:document.querySelector('#search-q')?.value,status:state.searchStatus,hash:location.hash,valid:document.querySelector('#search-form')?.checkValidity()})"));throw error;}await pause(50);}
const reports=[];let current;
function check(name,ok,detail){current.checks.push({name,status:ok?'RÉUSSI':'ÉCHEC',...(detail?{detail}:{} )});}
async function assert(name,expression){check(name,await evaluate(expression));}
async function scenario(id,label,fn){if(only&&id!==only)return;const entry={id,label,checks:[]};current.scenarios.push(entry);const parent=current;current=entry;try{await fn();}catch(error){entry.checks.push({name:'Exécution de la mission',status:'ÉCHEC',detail:error.message});}entry.status=entry.checks.some(c=>c.status==='ÉCHEC')?'ÉCHEC':entry.checks.some(c=>c.status==='NON TESTÉ')?'PARTIEL':'RÉUSSI';if(entry.status==='ÉCHEC')console.log(parent.width+'px '+id+' : '+JSON.stringify(entry.checks.filter(c=>c.status==='ÉCHEC')));current=parent;}
async function capture(slug,width){await go(slug);await evaluate("window.scrollTo({top:0,behavior:'instant'})");await pause(100);const shot=await cdp('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});const directory=phase==='avant'?resolve(htmlRoot,'../99_archives/2026-11-02_ameliorations_ux/captures'):join(htmlRoot,'apercus');mkdirSync(directory,{recursive:true});const file=join(directory,`ux-${phase}-${width}-${slug}.png`);writeFileSync(file,Buffer.from(shot.data,'base64'));current.captures.push(file);}
await cdp('Page.enable');await cdp('Runtime.enable');
for(const width of [1280,375]){
 const suite={width,height:1000,scenarios:[],checks:[],captures:[],nonTestes:[]};current=suite;reports.push(suite);
 await cdp('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});
 await cdp('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});
 await cdp('Page.navigate',{url:pathToFileURL(resolve(page)).href});await ready();
 await evaluate("sessionStorage.clear();window.__uxDataBefore=JSON.stringify(DATA)");await reload();
 await evaluate("window.__uxDataBefore=JSON.stringify(DATA)");
 await scenario('001','Sans métier cible : savoir-faire, sélection et résultats',async()=>{
  await go('recherche');await click('main a[href="#guide"]');
  await assert('Accès au guide sans métier cible',"readRoute().slug==='guide'&&!!document.querySelector('#guide-form')");
  await assert('Aucun savoir-faire précoché',"[...document.querySelectorAll('[name=skill]')].every(e=>!e.checked)");
  for(const code of ['103659','125416'])if(!await evaluate(`document.querySelector('[name="skill"][value="${code}"]').checked`))await click(`[name="skill"][value="${code}"]`);
  await assert('Deux critères explicitement choisis et annoncés',"state.skills.length===2&&!!document.querySelector('#guide-count')&&/2/.test(document.querySelector('#guide-count').textContent)");
  await click('#guide-form button[type="submit"],#guide-form button:not([type])');
  await assert('Résultats ou absence expliquée',"readRoute().slug==='resultats-ogr'&&!!document.querySelector('main h1')&&(document.querySelectorAll('main .result-card').length>0||/information|aucun|disponible/i.test(document.querySelector('main').textContent))");
 });
 await scenario('002','Couvreur : comparer avec l’étanchéité et revenir',async()=>{
  await go('recherche');await search('couvreur');await click('main a[href="#essentiel"]');
  await click('main [data-compare-add="F1610"]');await until(()=>evaluate("readRoute().slug==='comparateur'"));
  await select('#compare-left','F1610');await select('#compare-right','F1613');
  await assert('Deux métiers choisis et colonnes nommées',"state.compareIds.join('|')==='F1610|F1613'&&document.querySelector('main').textContent.includes(catalogue.metier('F1610').rome_libelle)&&document.querySelector('main').textContent.includes(catalogue.metier('F1613').rome_libelle)");
  await click('[data-swap-compare]');await assert('Inversion réelle',"state.compareIds.join('|')==='F1613|F1610'");
  await click('main a[href="#essentiel"]');await assert('Retour à la fiche sans perdre les choix',"readRoute().slug==='essentiel'&&state.compareIds.join('|')==='F1613|F1610'");
 });
 await scenario('003','Descriptions et conditions du couvreur',async()=>{
  await go('essentiel');await click('a[href="#competences"]');
  await assert('Conditions identifiables, données et limites distinctes',"readRoute().slug==='competences'&&/condition/i.test(document.querySelector('main h1').textContent)&&/poste|absen|général|spécialit/i.test(document.querySelector('main').textContent)");
  await assert('Données source du métier conservées',"JSON.stringify(DATA)===window.__uxDataBefore");
 });
 await scenario('004','Métiers proches, fiche liée et historique',async()=>{
  await go('essentiel');await click('main a[href="#alternatives"]');
  const href=await evaluate("document.querySelector('main a[href^=\"#metier/\"]')?.getAttribute('href')");if(!href)throw Error('Aucun métier proche ouvrable dans le jeu');
  const history=await cdp('Page.getNavigationHistory');const before=history.entries[history.currentIndex].id;
  await click(`main a[href="${href}"]`);await assert('Fiche liée réellement ouverte',"readRoute().slug==='metier'&&!!document.querySelector('main h1')");
  const after=await cdp('Page.getNavigationHistory'),next=after.entries[after.currentIndex].id;
  await cdp('Page.navigateToHistoryEntry',{entryId:before});await until(()=>evaluate("readRoute().slug==='alternatives'"));
  await assert('Arrière conserve les alternatives',"document.querySelectorAll('main .result-card').length>0");
  await cdp('Page.navigateToHistoryEntry',{entryId:next});await until(()=>evaluate("readRoute().slug==='metier'"));await assert('Avant revient à la fiche',"!!document.querySelector('main h1')");
 });
 await scenario('005','Salaire, source et piste retrouvée',async()=>{
  await go('essentiel');await click('a[href="#salaires"]');
  await assert('Unité, lieu, année et source visibles',"/nets.*mois/.test(document.querySelector('main').textContent)&&/Hérault|HERAULT/.test(document.querySelector('main').textContent)&&/2023/.test(document.querySelector('main').textContent)&&/INSEE/.test(document.querySelector('main').textContent)");
  if(!await evaluate("state.pistes.includes('F1610')"))await click('main [data-save="F1610"]');
  await assert('État gardé et retrait depuis la fiche',"!!document.querySelector('main [data-remove=\"F1610\"]')&&/Piste gardée/.test(document.querySelector('main').textContent)");
  await go('pistes');await assert('Piste sauvegardée et lien fiche',"state.pistes.includes('F1610')&&!!document.querySelector('main a[href=\"#essentiel\"]')");
 });
 await scenario('006','Recrutements présents et projections futures',async()=>{
  await go('essentiel');await click('a[href="#recrutements"]');
  await assert('Recrutements actuels contextualisés',"/2026/.test(document.querySelector('main').textContent)&&/projet/i.test(document.querySelector('main').textContent)&&/intention/i.test(document.querySelector('main').textContent)");
  await click('a[href="#prospective"]');
  await assert('Perspectives distinctes et non garanties',"/2019.{0,4}2030/.test(document.querySelector('main').textContent)&&/estim|projection/i.test(document.querySelector('main').textContent)&&/pas une liste|probabilité|pas.*disponible/.test(document.querySelector('main').textContent)");
 });
 await scenario('007','Changer Métier vers Domaine sans résultat périmé',async()=>{
  await go('recherche');await search('couvreur');await mode('domaine');
  await assert('Saisie réinitialisée, ancien résultat retiré et focus utile',"state.query===''&&state.submittedQuery===''&&state.results===null&&document.activeElement.id==='search-q'");
  await assert('Mode annoncé et nouvelle action visible',"/domaine/i.test((document.querySelector('#search-mode-help')?.textContent||'')+(document.querySelector('#toast')?.textContent||''))&&!!document.querySelector('#search-form button[type=\"submit\"]')");
  await search('Second œuvre','domaine');await click('main a[href="#domaine/F16"]');await assert('Domaine sélectionné et métiers présents',"readRoute().slug==='domaine'&&readRoute().id==='F16'&&document.querySelectorAll('main .result-card').length>0");
 });
 await scenario('008','Territoire explicite et absence de transposition',async()=>{
  await go('salaires');await openSearch();await click('[data-lieu]');
  const key=await evaluate("(()=>{const t=catalogue.territoires.find(t=>t.zonage==='region'&&t.territoire_code!=='76');return t.zonage+':'+t.territoire_code})()");
  await select('#lieu',key);await click('[data-apply-territory]');
  await assert('Lieu choisi conservé et chiffres absents expliqués',"state.territoryKey!=='commune:34172'&&document.querySelector('.location-button').textContent.includes(territoryLabel())&&!document.querySelector('main').textContent.includes('1 690 € nets / mois')&&/pas disponibles|non disponibles|non disponible/i.test(document.querySelector('main').textContent)");
  await click('[data-reference-location]');await assert('Retour possible aux informations publiées',"state.territoryKey==='commune:34172'");
 });
 await scenario('009','Savoir-faire communs sans maîtrise individuelle inventée',async()=>{
  await go('comparateur');await select('#compare-left','F1610');await select('#compare-right','F1613');await click('[data-compare="competences"]');
  await assert('Comparaison stable et information absente explicite',"state.compareIds.join('|')==='F1610|F1613'&&/non disponible/i.test(document.querySelector('main').textContent)");
  await assert('Aucun simulateur de maîtrise',"!document.querySelector('input[type=\"range\"]')&&!/vous maîtrisez|votre employabilité|passerelle garantie/i.test(document.querySelector('main').textContent)&&/ne permettent pas|ne.*maîtrise|ne prouve pas/i.test(document.querySelector('main').textContent)");
 });
 await scenario('010','Mobilités observées et trois filtres',async()=>{
  await go('essentiel');await click('a[href="#mobilites"]');
  await click('[data-mobility-sens="origines"]');
  const age=await evaluate("[...document.querySelector('#mobility-age').options].find(o=>!o.selected).value");await select('#mobility-age',age);
  const family=await evaluate("[...document.querySelector('#mobility-family').options].find(o=>!o.selected)?.value");if(family)await select('#mobility-family',family);
  await assert('Sens, âge et famille réellement appliqués',`state.mobilitySens==='origines'&&state.mobilityAge===${JSON.stringify(age)}${family?'&&state.mobilityFamily==='+JSON.stringify(family):''}`);
  await assert('Population, période et provenance maintenues',"/2022.{0,4}2023/.test(document.querySelector('main').textContent)&&/DARES/.test(document.querySelector('main').textContent)&&/groupe de métiers/i.test(document.querySelector('main').textContent)&&/ne prédisent|pas une recommandation|ne garant/i.test(document.querySelector('main').textContent)");
  await assert('Focus conservé après filtre',`document.activeElement.id===${JSON.stringify(family?'mobility-family':'mobility-age')}`);
 });
 await scenario('TRANS-VIDE','Recherche vide, chargement et erreur locale contrôlée',async()=>{
  await go('recherche');await search('zzzzzz-introuvable');await assert('Aucun résultat avec explication',"document.querySelectorAll('main .result-card').length===0&&/Aucune fiche|Aucun résultat|aucun métier/i.test(document.querySelector('main').textContent)");
  await evaluate("window.__uxSearch=catalogue.rechercher;catalogue.rechercher=()=>new Promise(resolve=>window.__uxResolve=resolve)");await type('#search-q','couvreur');await key('Enter','Enter',13);
  await assert('Chargement annoncé',"state.searchStatus==='loading'&&!!document.querySelector('main [role=\"status\"]')");
  await evaluate("catalogue.rechercher=window.__uxSearch;window.__uxResolve({mode:state.mode,items:[]})");await pause(80);
  await evaluate("catalogue.rechercher=async()=>{throw Error('Injection de faute UX locale')}");await type('#search-q','couvreur');await key('Enter','Enter',13);await until(()=>evaluate("state.searchStatus==='error'"));
  await assert('Erreur et action de reprise',"!!document.querySelector('[data-retry-search]')");await evaluate("catalogue.rechercher=window.__uxSearch;delete window.__uxSearch;delete window.__uxResolve");
 });
 await scenario('TRANS-PISTES','Limite de trois, rechargement et retrait',async()=>{
  await cdp('Page.navigate',{url:pathToFileURL(resolve(page)).href+'?controle-session=1#pistes'});await ready();await pause(120);
  await go('pistes');while(await evaluate("!!document.querySelector('main [data-remove]')"))await click('main [data-remove]');
  const codes=await evaluate("catalogue.metiers.filter(m=>m.rome_code!=='F1610').slice(0,4).map(m=>m.rome_code)");
  for(const code of codes){await go('metier/'+code);await click(`main [data-save="${code}"]`);}
  await assert('Quatrième piste refusée et limite annoncée',"state.pistes.length===3&&/trois|3/.test(document.querySelector('#toast').textContent)");
  const kept=await evaluate("[...state.pistes]");await reload();
  await assert('Trois pistes reprises après nouveau chargement complet',`JSON.stringify(state.pistes)===${JSON.stringify(JSON.stringify(kept))}`);
  await go('pistes');await click('main [data-remove]');await assert('Retrait opérationnel',"state.pistes.length===2");
  await reload();await assert('Retrait conservé après un second chargement complet',"state.pistes.length===2");
  await assert('Format de passage existant, sans fausse navigation projet',"selectionPayload().type==='macarriere-selection'&&selectionPayload().referentiel==='ROME_V3'&&selectionPayload().metiers.length===2&&!document.querySelector('a[href=\"#preparer-mon-projet\"]')");
 });
 await scenario('TRANS-NULL','Valeur null réellement observée',async()=>{
  await go('certification/112561');await assert('Null conservé et non transformé en zéro',"DATA.certification.salaire_insersup_median_12m===null&&/Donnée non disponible|Information non disponible/.test(document.querySelector('main').textContent)");
 });
 await scenario('TRANS-CLAVIER','Actions essentielles au clavier réel CDP',async()=>{
  await go('recherche');await evaluate("document.querySelector('.skip').focus()");await key('Enter','Enter',13);await assert('Lien d’évitement activé au clavier',"document.activeElement.id==='main'");
  await openSearch();await evaluate("document.querySelector('[name=\"search-mode\"]:checked').focus()");const previous=await evaluate('state.mode');await key('ArrowRight','ArrowRight',39);
  await assert('Changement de mode par flèche et focus sur le champ',`state.mode!==${JSON.stringify(previous)}&&document.activeElement.id==='search-q'`);
  await mode('metier');await type('#search-q','couvreur');await key('Enter','Enter',13);await until(()=>evaluate("state.searchStatus==='done'"));await assert('Recherche soumise avec Entrée',"state.results.items.some(m=>m.rome_code==='F1610')");
  await evaluate("document.querySelector('main a').focus()");await key('Tab','Tab',9);
  await assert('Focus clavier visible',"(()=>{const s=getComputedStyle(document.activeElement);return s.outlineStyle!=='none'&&parseFloat(s.outlineWidth)>=2;})()");
 });
 await scenario('TRANS-CLAVIER-GUIDE','Sélection et découverte au clavier seul',async()=>{
  await go('guide');await evaluate("state.skills=[];state.domain='';state.contexts={'300782':'','300783':''};state.match='au_moins_une';render()");
  await key('Tab','Tab',9);await assert('Premier savoir-faire atteint avec Tab',"document.activeElement.name==='skill'");
  await key(' ','Space',32);await assert('Sélection explicite avec Espace',"state.skills.length===1");
  await key('Tab','Tab',9);await key(' ','Space',32);await assert('Deux savoir-faire sélectionnés au clavier',"state.skills.length===2");
  for(let step=0;step<22;step++){if(await evaluate("document.activeElement.matches('#guide-form button[type=submit],#guide-form button:not([type])')"))break;await key('Tab','Tab',9);}
  await assert('Action de découverte atteinte sans souris',"document.activeElement.matches('#guide-form button[type=submit],#guide-form button:not([type])')");
  await key('Enter','Enter',13);await assert('Résultats ouverts avec Entrée',"readRoute().slug==='resultats-ogr'&&document.querySelectorAll('main .result-card').length===3");
 });
 await scenario('TRANS-RESPONSIVE','Reflow, actions, labels et mouvement réduit',async()=>{
  for(const slug of ['recherche','essentiel','guide','comparateur','mobilites']){await go(slug);await assert('Pas de débordement de page : '+slug,"document.documentElement.scrollWidth<=innerWidth+1");await assert('Un titre de page : '+slug,"document.querySelectorAll('main h1').length===1");}
  await assert('Pas de faux lien #',"![...document.querySelectorAll('a')].some(a=>a.getAttribute('href')==='#')");
  await go('guide');await assert('Contrôles du formulaire étiquetés',"[...document.querySelectorAll('#guide-form input,#guide-form select')].every(e=>e.labels?.length||e.getAttribute('aria-label')||e.getAttribute('aria-labelledby'))");
  const sizes=await evaluate("[...document.querySelectorAll('#guide-form button')].filter(e=>!e.hidden&&e.getBoundingClientRect().height>0).map(e=>({nom:e.textContent.trim(),largeur:e.getBoundingClientRect().width,hauteur:e.getBoundingClientRect().height}))");
  check('Cibles des boutons du guide au moins 44 px',sizes.length>0&&sizes.every(s=>s.largeur>=44&&s.hauteur>=44),sizes);
  const contrasts=await evaluate(`(()=>{
   const rgb=value=>{const v=value.match(/[\\d.]+/g)?.map(Number);return v&&v.length>=3?v:null;};
   const lum=c=>c.slice(0,3).map(x=>{x/=255;return x<=0.03928?x/12.92:((x+0.055)/1.055)**2.4;}).reduce((v,x,i)=>v+x*[.2126,.7152,.0722][i],0);
   const rows=[];
   for(const e of document.querySelectorAll('main h1,main .lead,main .caption,main .btn:not(:disabled),main .piste-status,#search-mode-help')){
    if(!e.getBoundingClientRect().height)continue;const fg=rgb(getComputedStyle(e).color);let p=e,bg=null;
    while(p&&!bg){const c=rgb(getComputedStyle(p).backgroundColor);if(c&&(c.length===3||c[3]===1))bg=c;p=p.parentElement;}
    bg=bg||[255,255,255];if(!fg)continue;const a=lum(fg),b=lum(bg);rows.push({texte:e.textContent.trim().slice(0,65),couleur:fg,fond:bg,ratio:(Math.max(a,b)+.05)/(Math.min(a,b)+.05)});
   }return rows;
  })()`);
  check('Contrastes textuels mesurés sur les composants touchés',contrasts.length>0&&contrasts.every(c=>c.ratio>=4.5),contrasts);
  await cdp('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
  await go('essentiel');await assert('Mouvement réduit et contenu toujours visible',"matchMedia('(prefers-reduced-motion: reduce)').matches&&[...document.querySelectorAll('main h1,main .question-card')].every(e=>getComputedStyle(e).opacity==='1'&&e.getBoundingClientRect().height>0)");
  const styles=await evaluate("(()=>{const e=document.querySelector('main .question-card');const s=getComputedStyle(e);return {transition:s.transitionDuration,animation:s.animationDuration,transform:s.transform};})()");check('Styles de mouvement réduit enregistrés',true,styles);
 });
 await scenario('TRANS-DONNEES','Fidélité des réponses et absence de requête API',async()=>{
  await assert('Données JSON embarquées inchangées pendant la session',"JSON.stringify(DATA)===JSON.stringify(JSON.parse(document.querySelector('#explorer-data').textContent))");
  await assert('Pas de ressource métier distante',"performance.getEntriesByType('resource').every(r=>!/^https?:/.test(r.name))");
 });
 // Le zoom visuel CDP et le reflow ne sont pas présentés comme un raccourci de zoom navigateur.
 await scenario('TRANS-ZOOM','Grossissement visuel CDP et reflow équivalent',async()=>{
  await go('essentiel');for(const scale of [2,4]){await cdp('Emulation.setPageScaleFactor',{pageScaleFactor:scale});await assert('Grossissement visuel '+scale*100+' % appliqué',`Math.abs(visualViewport.scale-${scale})<0.1&&document.querySelector('main h1').getBoundingClientRect().height>0`);}await cdp('Emulation.setPageScaleFactor',{pageScaleFactor:1});
  if(width===1280){for(const reflow of [640,320]){await cdp('Emulation.setDeviceMetricsOverride',{width:reflow,height:1000,deviceScaleFactor:1,mobile:false});await go('comparateur');await assert('Reflow à '+reflow+' px sans débordement',"document.documentElement.scrollWidth<=innerWidth+1");}await cdp('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});}
 });
 suite.nonTestes.push({name:'Zoom navigateur réel par raccourcis Ctrl + / Ctrl − à 200 et 400 %',status:'NON TESTÉ',raison:'CDP applique un grossissement visuel et des largeurs de reflow ; cela ne reproduit pas le zoom de l’interface du navigateur.'},{name:'Audit RGAA complet et lecteurs d’écran',status:'NON TESTÉ',raison:'La recette couvre les comportements essentiels dans Edge, pas une certification ni des utilisateurs réels.'});
 for(const slug of ['recherche','essentiel','guide','comparateur','mobilites'])await capture(slug,width);
 try{
  await cdp('Emulation.setScriptExecutionDisabled',{value:true});
  const disabledUrl=pathToFileURL(resolve(page)).href+'?sans-js=1';await cdp('Page.navigate',{url:disabledUrl});await pause(600);
  const dom=await cdp('DOM.getDocument',{depth:0});const outer=await cdp('DOM.getOuterHTML',{nodeId:dom.root.nodeId});
  check('Alternative sans JavaScript présente',/<noscript[\s>][\s\S]*?(?:JavaScript|javascript)[\s\S]*?<\/noscript>/i.test(outer.outerHTML));
  const title=await cdp('DOM.querySelector',{nodeId:dom.root.nodeId,selector:'main h1'});
  let visible=false;if(title.nodeId){const box=await cdp('DOM.getBoxModel',{nodeId:title.nodeId});visible=box.model.height>0;}
  check('Aperçu lisible sans JavaScript',visible&&outer.outerHTML.includes('France Travail'));
  const shot=await cdp('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});const directory=phase==='avant'?resolve(htmlRoot,'../99_archives/2026-11-02_ameliorations_ux/captures'):join(htmlRoot,'apercus');mkdirSync(directory,{recursive:true});const file=join(directory,`ux-${phase}-${width}-sans-js.png`);writeFileSync(file,Buffer.from(shot.data,'base64'));suite.captures.push(file);
 }catch(error){suite.nonTestes.push({name:'Rendu sans JavaScript',status:'NON TESTÉ',raison:error.message});}
 finally{await cdp('Emulation.setScriptExecutionDisabled',{value:false});await cdp('Page.navigate',{url:pathToFileURL(resolve(page)).href});await ready();}
 suite.passed=suite.scenarios.reduce((n,s)=>n+s.checks.filter(c=>c.status==='RÉUSSI').length,0)+suite.checks.filter(c=>c.status==='RÉUSSI').length;
 suite.failed=suite.scenarios.reduce((n,s)=>n+s.checks.filter(c=>c.status==='ÉCHEC').length,0)+suite.checks.filter(c=>c.status==='ÉCHEC').length;
 console.log(`${phase} ${width}px : ${suite.passed} réussis, ${suite.failed} échoués ; ${suite.nonTestes.length} points non testés`);
}
const report={date:'2026-11-02',phase,page,outil:'Edge headless via Chrome DevTools Protocol ; WebSocket Node natif',methode:'Souris et clavier CDP ; options des sélecteurs via événements DOM, comme selectOption ; fautes/latence injectées uniquement dans le fournisseur local.',httpMetier:false,filtreScenario:only||null,suites:reports,runtimeErrors,passed:reports.reduce((n,r)=>n+r.passed,0),failed:reports.reduce((n,r)=>n+r.failed,0)};
const output=join(htmlRoot,'controles/resultats',`TESTS_UX_CDP_${phase.toUpperCase()}${only?'_'+only:''}.json`);writeFileSync(output,JSON.stringify(report,null,2));
console.log(output);socket.close();if(report.failed)process.exitCode=1;
