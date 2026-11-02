import {readFileSync,writeFileSync,mkdirSync,existsSync} from 'node:fs';
import {resolve,dirname,extname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const pkg=resolve(root,'node_modules/@gouvfr');
const read=p=>readFileSync(p,'utf8');
function css(path){return read(path).replace(/url\((['"]?)([^)'"\s]+)\1\)/g,(whole,quote,url)=>{
 if(/^(data:|https?:|#)/.test(url))return whole;
 const target=resolve(dirname(path),url.split(/[?#]/)[0]);
 if(!existsSync(target))throw new Error('Ressource CSS manquante : '+target);
 const mime={'.woff2':'font/woff2','.woff':'font/woff','.svg':'image/svg+xml','.png':'image/png'}[extname(target)]||'application/octet-stream';
 return `url("data:${mime};base64,${readFileSync(target).toString('base64')}")`;
}).replace(/\/\*# sourceMappingURL=.*?\*\//g,'');}
mkdirSync(resolve(root,'dist'),{recursive:true});
const runtime='(()=>{\n'+read(resolve(pkg,'dsfr/dist/dsfr.module.min.js'))+'\n})();\n'+read(resolve(pkg,'dsfr-chart/dist/DSFRChart/DSFRChart.umd.cjs'));
const iconNames=['arrow-go-back-fill','arrow-right-line','fullscreen-line','more-line','pie-chart-2-fill','sparkling-2-line','table-2','briefcase-line','map-pin-2-line','money-euro-circle-line','bookmark-line','search-line'];
// Conserver les règles officielles des seules icônes utilisées par Chart.
const icons=[...css(resolve(pkg,'dsfr/dist/utility/icons/icons.min.css')).matchAll(/([^{}]+)\{([^{}]*)\}/g)].filter(m=>iconNames.some(n=>m[1].includes('.fr-icon-'+n+':'))).map(m=>m[0]).join('\n');
const styles=css(resolve(pkg,'dsfr/dist/dsfr.min.css'))+'\n'+icons+'\n'+css(resolve(pkg,'dsfr-chart/dist/DSFRChart/DSFRChart.css'));
const adapters=read(resolve(root,'src/adaptateurs.mjs')).replace(/export /g,'');
const controller=read(resolve(root,'src/composants.js'));
writeFileSync(resolve(root,'dist/runtime.js'),runtime);
writeFileSync(resolve(root,'dist/styles.css'),styles);
writeFileSync(resolve(root,'dist/composants.js'),`window.MaDataviz=(()=>{\n${adapters}\n${controller}\n})();\n`+read(resolve(root,'src/infographie.js')));
const meta={date:'2026-11-02',dsfr:JSON.parse(read(resolve(pkg,'dsfr/package.json'))).version,dsfrChart:JSON.parse(read(resolve(pkg,'dsfr-chart/package.json'))).version,runtimeSha256:createHash('sha256').update(runtime).digest('hex'),octets:{runtime:Buffer.byteLength(runtime),styles:Buffer.byteLength(styles)},reseauRequis:false};
writeFileSync(resolve(root,'dist/ASSEMBLAGE.json'),JSON.stringify(meta,null,2));
console.log(JSON.stringify(meta));
