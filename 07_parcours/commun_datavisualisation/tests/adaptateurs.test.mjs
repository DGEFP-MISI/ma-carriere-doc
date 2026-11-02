import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {valeur,serie,groupes,carte,moisConsecutifs,regionsCarte} from '../src/adaptateurs.mjs';
const root=new URL('../../../',import.meta.url);
const json=p=>JSON.parse(readFileSync(new URL(p,root),'utf8').replace(/^\uFEFF/,''));
const salary=json('02_reponses_observees/indicateurs/salaires/response_regions.json');
const r16=json('06_controles/resultats/R16 test/GET_indicateurs__rome_F1610__zonage_commune__territoire_34172.json');
test('zéro publié conserve sa valeur',()=>assert.equal(valeur(0).nombre,0));
test('absence, null et secret statistique restent distincts',()=>assert.deepEqual([undefined,null,'secret_stat'].map(v=>valeur(v).etat),['absent','null','confidentiel']));
test('aucune coercition des nombres sous forme de chaînes',()=>assert.equal(valeur('12').etat,'invalide'));
test('NaN et infinis ne dessinent pas de barres',()=>assert.ok([NaN,Infinity,-Infinity].every(v=>valeur(v).etat==='invalide')));
test('pourcentage incohérent signalé sans écrêtage',()=>assert.equal(serie([{v:101}],()=>'', 'v',{pourcentage:true})[0].etat,'invalide'));
test('aucun zéro substitué au secret statistique',()=>assert.equal(serie([{v:'secret_stat'}],()=>'', 'v')[0].nombre,undefined));
test('projections négatives réellement publiées préservées',()=>{
 const m=r16.items.find(m=>m.mesure==='metiers_2030');
 assert.equal(serie(m.valeurs,'fap_87_libelle','nb_creations_nettes_emplois_2030',{negatif:true})[0].nombre,-1035);
});
test('FAP225 et FAP228 ne sont pas rapprochées',()=>assert.deepEqual(groupes(salary.items,'fap_228_code'),[]));
test('familles salariales séparées',()=>assert.equal(groupes(salary.items,'fap_225_code').length,2));
test('carte région : code Chart et montant JSON identiques',()=>assert.equal(carte(salary.items.filter(r=>r.fap_225_code==='B0Z21'),'salaire_net_mensuel_median','region').BRE,1900));
test('Corse et outre-mer gardent les codes Chart',()=>assert.deepEqual([regionsCarte['94'],regionsCarte['04']],['20R','974']));
test('CLPE ne devient pas une carte départementale',()=>assert.equal(carte([], 'v','clpe'),null));
test('un repli ne colorie pas la région demandée',()=>assert.deepEqual(carte([{territoire_code:'76',v:12,repli:true}], 'v','region'),{}));
test('maille incompatible exclue de la carte',()=>assert.deepEqual(carte([{territoire_code:'76',v:12,maille:'dep'}], 'v','region'),{}));
test('secret et null ne deviennent pas une zone à zéro',()=>assert.deepEqual(carte([{territoire_code:'76',v:null},{territoire_code:'11',v:'secret_stat'}],'v','region'),{}));
test('zéro géographique conservé et codes départementaux textuels',()=>assert.deepEqual(carte([{territoire_code:'01',v:0},{territoire_code:'2A',v:2}],'v','departement'),{'01':0,'2A':2}));
test('pas de courbe temporelle avec un mois manquant',()=>assert.equal(moisConsecutifs([{periode_code:'2025-12'},{periode_code:'2026-02'}]),false));
test('les vrais mois observés sont consécutifs',()=>assert.equal(moisConsecutifs([...r16.items.find(m=>m.mesure==='offres_emploi_mensuelles').valeurs].sort((a,b)=>a.periode_code.localeCompare(b.periode_code))),true));
test('les salaires ne sont pas divisés par douze',()=>{
 const r=r16.items.find(m=>m.mesure==='salaires').valeurs[0];
 assert.equal(r.salaire_net_mensuel_median,1690);assert.notEqual(r.salaire_net_annuel_median/12,r.salaire_net_mensuel_median);
});
test('aucune modification des réponses lors de l’adaptation',()=>{
 const before=JSON.stringify(salary);serie(salary.items,'territoire_libelle','salaire_net_mensuel_median');carte(salary.items,'salaire_net_mensuel_median','region');assert.equal(JSON.stringify(salary),before);
});
