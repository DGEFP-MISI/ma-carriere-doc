/* Adaptateurs purs : aucune requête, aucun calcul d'indicateur métier. */
export function valeur(value) {
  if (value === 'secret_stat') return {etat:'confidentiel', texte:'Non publié pour protéger les personnes'};
  if (value === null) return {etat:'null', texte:'Donnée non disponible'};
  if (value === undefined) return {etat:'absent', texte:'Information non fournie'};
  if (typeof value !== 'number' || !Number.isFinite(value)) return {etat:'invalide', texte:'Valeur non exploitable'};
  return {etat:'nombre', nombre:value, texte:new Intl.NumberFormat('fr-FR',{maximumFractionDigits:2}).format(value)};
}
export function serie(rows, label, field, {pourcentage=false, negatif=false}={}) {
  return rows.map(row=>{
    let v=valeur(row[field]);
    if(v.etat==='nombre' && ((!negatif && v.nombre<0)||(pourcentage && v.nombre>100))) v={etat:'invalide',texte:'Valeur hors des bornes attendues'};
    return {libelle:String(typeof label==='function'?label(row):row[label]??'Libellé non fourni'),...v};
  });
}
export function groupes(rows, field) {
  return [...new Set(rows.map(r=>r[field]))].filter(Boolean).map(code=>({code,rows:rows.filter(r=>r[field]===code)}));
}
export function moisConsecutifs(rows) {
  if(rows.length<2) return false;
  const ids=rows.map(r=>/^\d{4}-\d{2}$/.test(r.periode_code)?Number(r.periode_code.slice(0,4))*12+Number(r.periode_code.slice(5)):NaN);
  return ids.every((id,i)=>Number.isFinite(id)&&(!i||id===ids[i-1]+1));
}
// Nomenclature technique des cartes DSFR Chart 2.1.1, rapprochée des libellés
// /territoires et des libellés des réponses /salaires et /recrutements.
export const regionsCarte=Object.freeze({'84':'ARA','27':'BFC','53':'BRE','24':'CVL','44':'GES','32':'HDF','11':'IDF','28':'NOR','75':'NAQ','76':'OCC','52':'PDL','93':'PAC','94':'20R','01':'971','02':'972','03':'973','04':'974','06':'976'});
export function carte(rows, field, zonage) {
  if(!['region','departement'].includes(zonage)) return null;
  const data={};
  for(const row of rows){
    const v=valeur(row[field]);
    const key=zonage==='region'?regionsCarte[row.territoire_code]:row.territoire_code;
    // Une valeur de repli ne colorie jamais le territoire demandé.
    if(v.etat==='nombre' && key && row.repli!==true && (!row.maille||row.maille===(zonage==='region'?'reg':'dep'))) data[key]=v.nombre;
  }
  return data;
}
