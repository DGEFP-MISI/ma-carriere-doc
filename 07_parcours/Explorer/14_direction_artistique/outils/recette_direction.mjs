// Recette de présentation sur l'application existante, sans GET métier distant.
import {writeFileSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {resolve,join} from 'node:path';
import {pathToFileURL} from 'node:url';
const [port,page,directory]=process.argv.slice(2),pause=ms=>new Promise(r=>setTimeout(r,ms));
const targets=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const socket=new WebSocket(targets.find(t=>t.type==='page').webSocketDebuggerUrl);
await new Promise((resolve,reject)=>{socket.addEventListener('open',resolve,{once:true});socket.addEventListener('error',reject,{once:true});});
let next=0;const pending=new Map(),errors=[],checks=[],captures=[];
socket.addEventListener('message',event=>{const m=JSON.parse(event.data);if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails.exception?.description||m.params.exceptionDetails.text);if(m.id){const p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timeout);m.error?p.reject(Error(m.error.message)):p.resolve(m.result);}}});
function cdp(method,params={}){return new Promise((resolve,reject)=>{const id=++next,timeout=setTimeout(()=>{pending.delete(id);reject(Error('Délai '+method));},15000);pending.set(id,{resolve,reject,timeout});socket.send(JSON.stringify({id,method,params}));});}
async function evaluate(expression){const r=await cdp('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(r.exceptionDetails.exception?.description||r.exceptionDetails.text);return r.result.value;}
async function until(test){for(let i=0;i<80;i++){try{if(await test())return;}catch{}await pause(50);}throw Error('État attendu absent');}
async function test(name,expression){let value;try{value=await evaluate(expression);checks.push({name,status:value?'RÉUSSI':'ÉCHEC',value});}catch(error){checks.push({name,status:'ÉCHEC',error:error.message});}if(checks.at(-1).status==='ÉCHEC')console.log(JSON.stringify(checks.at(-1)));}
async function go(slug){await evaluate(`location.hash===${JSON.stringify('#'+slug)}?render():location.hash=${JSON.stringify(slug)}`);await until(()=>evaluate(`document.body.dataset.view===${JSON.stringify(slug.split('/')[0])}`));await pause(80);}
async function shot(name,full=false){await evaluate("window.scrollTo({top:0,behavior:'instant'})");await pause(50);const metrics=await cdp('Page.getLayoutMetrics');const params={format:'png',captureBeyondViewport:full};if(full)params.clip={x:0,y:0,width:metrics.cssContentSize.width,height:metrics.cssContentSize.height,scale:1};const r=await cdp('Page.captureScreenshot',params);writeFileSync(join(directory,name),Buffer.from(r.data,'base64'));captures.push(name);}
await cdp('Page.enable');await cdp('Runtime.enable');
await cdp('Emulation.setDeviceMetricsOverride',{width:1440,height:1100,deviceScaleFactor:1,mobile:false});
await cdp('Page.navigate',{url:pathToFileURL(resolve(page)).href});
await until(()=>evaluate("typeof state==='object'&&!!document.querySelector('main h1')"));
await test('Entrée et recherche préservées',"readRoute().slug==='recherche'&&!!document.querySelector('#search-form')&&document.querySelectorAll('[name=search-mode]').length===3");
await shot('RECHERCHE_DESKTOP.png');
for(const width of [1440,375,320]){
 await cdp('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});
 await evaluate("state.territoryKey='commune:34172';document.documentElement.setAttribute('data-fr-theme','light')");
 await go('essentiel');
 await test(width+'px : quatre portes, même ordre et mêmes routes',"[...document.querySelectorAll('.ma-question')].map(e=>e.getAttribute('href')).join('|')==='#competences|#recrutements|#salaires|#alternatives'");
 await test(width+'px : aucun lien imbriqué',"![...document.querySelectorAll('.ma-question')].some(e=>e.querySelector('a,button,input,select'))");
 await test(width+'px : deux familles BMO conservées sans somme',"[...document.querySelectorAll('[data-measure=projets_recrutement] .ma-value')].map(e=>e.textContent.replace(/\\s/g,'')).join('|')==='26projets|81projets'");
 await test(width+'px : salaire natif et bonne population',"(()=>{const e=document.querySelector('[data-question=gagner]');return e.textContent.includes('1 690')&&e.textContent.includes('HERAULT')&&e.textContent.includes('2023')&&e.textContent.includes('8 métiers')&&e.textContent.includes('ouvriers non qualifiés')===false&&e.textContent.includes('Ouvriers non qualifiés')&&e.textContent.includes('temps complet')})()");
 await test(width+'px : conditions natives sans score',"[...document.querySelectorAll('.ma-context-list li')].every(e=>DATA.metier.contexte_travail_libelles.includes(e.textContent))&&!document.querySelector('meter,progress,.bar-track,.bar-fill')");
 await test(width+'px : icônes officielles réellement chargées',"[...document.querySelectorAll('.ma-question-icon .ma-icon')].length===4&&[...document.querySelectorAll('.ma-question-icon .ma-icon')].every(e=>getComputedStyle(e,'::before').maskImage.includes('data:image/svg+xml'))");
 await test(width+'px : aucune étiquette prédictive ajoutée',"!document.querySelector('main').textContent.match(/Métier qui recrute|Métier d’avenir|score d’attractivité/)");
 await test(width+'px : titre et quatre questions au clavier',"document.activeElement===document.querySelector('main h1')&&[...document.querySelectorAll('.ma-question')].every(e=>e.tabIndex===0)");
 await test(width+'px : thèmes profonds accessibles',"['#mobilites','#prospective','#formations','#secteurs'].every(h=>document.querySelector('.ma-passages a[href=\"'+h+'\"]'))");
 await shot(width===1440?'FICHE_DESKTOP.png':`FICHE_MOBILE_${width}.png`,true);
 for(const slug of ['recherche','essentiel','salaires','recrutements','competences','certification','comparateur','pistes','mobilites','prospective','domaine']){
  await go(slug);await test(width+'px : reflow '+slug,"document.documentElement.scrollWidth<=innerWidth+1");
 }
 await go('comparateur');
 await test(width+'px : comparateur intact',"!!document.querySelector('#compare-left')&&!!document.querySelector('#compare-right')&&document.querySelectorAll('.compare-identity').length===2");
 await evaluate("state.compareTab='marche';render()");
 await test(width+'px : colonne statistique absente non remplacée',"[...document.querySelector('.table-wrap tbody').rows].every(r=>r.cells[2].textContent==='Donnée non disponible')");
 if(width===1440)await shot('COMPARATEUR_DESKTOP.png',true);
 const unavailable=await evaluate("catalogue.territoires.find(t=>t.zonage==='region'&&t.territoire_code!=='76')?.zonage+':'+catalogue.territoires.find(t=>t.zonage==='region'&&t.territoire_code!=='76')?.territoire_code");
 await evaluate(`state.territoryKey=${JSON.stringify(unavailable)}`);await go('essentiel');
 await test(width+'px : aperçus non transposés à un autre lieu',"!document.querySelector('[data-measure=salaires],[data-measure=projets_recrutement]')");
 await evaluate("state.territoryKey='commune:34172'");await go('essentiel');
 await evaluate("document.documentElement.setAttribute('data-fr-theme','dark')");await pause(100);
 await test(width+'px : thème sombre applique les tokens',"getComputedStyle(document.body).backgroundColor!=='rgb(255, 255, 255)'&&getComputedStyle(document.querySelector('.ma-question')).backgroundColor!=='rgb(255, 255, 255)'");
 const contrast=await evaluate(`(()=>{
  const luminance=c=>{const a=c.match(/[\\d.]+/g).slice(0,3).map(v=>{v=Number(v)/255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return a[0]*.2126+a[1]*.7152+a[2]*.0722};
  return ['.ma-question-title','.ma-repere-context','.ma-provenance','.ma-question-action','.four-questions a[aria-current]','.ma-question-icon .ma-icon'].map(s=>{const e=document.querySelector(s);let p=e,bg;while(p){bg=getComputedStyle(p).backgroundColor;if(bg!=='rgba(0, 0, 0, 0)')break;p=p.parentElement}const a=luminance(getComputedStyle(e).color),b=luminance(bg);return {selector:s,ratio:(Math.max(a,b)+.05)/(Math.min(a,b)+.05)}})
 })()`);
 checks.push({name:width+'px : contraste des textes de repère en sombre',status:contrast.every(c=>c.ratio>=4.5)?'RÉUSSI':'ÉCHEC',values:contrast});
 if(width===1440)await shot('FICHE_SOMBRE_DESKTOP.png');
 await evaluate("document.documentElement.setAttribute('data-fr-theme','light')");
}
await cdp('Emulation.setDeviceMetricsOverride',{width:1440,height:1100,deviceScaleFactor:1,mobile:false});
await go('salaires');
await test('DataBox rapprochées, charge à la demande conservée',"document.querySelector('.metric-grid').nextElementSibling?.classList.contains('ma-dataviz')&&!document.querySelector('bar-chart')");
await evaluate("[...document.querySelectorAll('.ma-dataviz')].find(s=>s.querySelector('h3').textContent.includes('Trois repères')).querySelector('details').open=true");
await until(()=>evaluate("!!document.querySelector('bar-chart canvas')||!!document.querySelector('bar-chart')&&!!document.querySelector('.ma-dataviz canvas')"));
await test('Quartiles natifs et tableau accessibles',"JSON.parse(document.querySelector('bar-chart').getAttribute('y'))[0].join('|')==='17400|20300|22000'&&!!document.querySelector('table-chart')&&!!document.querySelector('.ma-fallback table caption')");
await shot('SALAIRES_DESKTOP.png',true);
await test('Zéro, null, absence et secret inchangés dans les nouveaux repères',"MaInfographie.repere({value:0}).includes('>0<')&&MaInfographie.repere({value:null}).includes('Donnée non disponible')&&MaInfographie.repere({value:undefined}).includes('Information non fournie')&&MaInfographie.repere({value:'secret_stat'}).includes('Non publié pour protéger les personnes')");
await go('essentiel');
const keyboard=[];
for(let i=0;i<22;i++){
 await cdp('Input.dispatchKeyEvent',{type:'rawKeyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 await cdp('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 const item=await evaluate("document.activeElement?.matches('.ma-question')?{question:document.activeElement.dataset.question,outline:getComputedStyle(document.activeElement).outlineStyle}:null");
 if(item&&!keyboard.some(k=>k.question===item.question))keyboard.push(item);
 if(keyboard.length===4)break;
}
checks.push({name:'Quatre portes atteintes par la touche Tab, focus visible',status:keyboard.length===4&&keyboard.every(k=>k.outline==='solid')?'RÉUSSI':'ÉCHEC',values:keyboard});
await cdp('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
await test('Réduction du mouvement respectée',"getComputedStyle(document.querySelector('.ma-question')).transitionDuration==='0s'&&getComputedStyle(document.documentElement).scrollBehavior==='auto'");
await cdp('Emulation.setEmulatedMedia',{features:[]});
await test('Aucun accès API métier ajouté',"performance.getEntriesByType('resource').filter(r=>r.name.startsWith('http')).length===0");
for(const file of ['01_FICHE_METIER_DESKTOP.svg','01_FICHE_METIER_MOBILE.svg','02_COMPARATEUR_DESKTOP.svg']){
 const width=file.includes('MOBILE')?375:file.includes('COMPARATEUR')?1280:1440;
 await cdp('Emulation.setDeviceMetricsOverride',{width,height:1000,deviceScaleFactor:1,mobile:false});
 await cdp('Page.navigate',{url:pathToFileURL(resolve(directory,'../maquettes',file)).href});
 await until(()=>evaluate("document.documentElement.tagName==='svg'"));
 await shot(file.replace('.svg','_MAQUETTE.png'),true);
}
const report={date:'2026-11-02',applicationSha256:createHash('sha256').update(readFileSync(page)).digest('hex'),checks,passed:checks.filter(c=>c.status==='RÉUSSI').length,failed:checks.filter(c=>c.status==='ÉCHEC').length,errors,captures,HTTP_metier:false,RGAA_complet:false};
writeFileSync(join(directory,'RECETTE_DIRECTION.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:report.passed,failed:report.failed,errors,captures:captures.length}));
socket.close();if(report.failed||errors.length)process.exitCode=1;
