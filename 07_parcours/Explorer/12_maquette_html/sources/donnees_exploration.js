// Adaptateurs de présentation. Aucun appel réseau : seules les réponses observées sont lues.
// La vue consomme des objets identifiés, pas un métier/certificat figé dans son composant.
const adapters={
  metiers(response){return (response.items||[]).filter(r=>typeof r.rome_code==='string'&&typeof r.rome_libelle==='string');},
  certifications(response){return (response.items||[]).filter(r=>typeof r.certifinfo_code==='string'&&typeof r.certifinfo_libelle==='string');},
  domaines(response){return (response.items||[]).flatMap(g=>(g.domaines||[]).filter(d=>typeof d.domaine_code==='string'&&typeof d.domaine_libelle==='string').map(d=>({...d,grand_domaine_code:g.grand_domaine_code,grand_domaine_libelle:g.grand_domaine_libelle})));},
  territoires(response){return (response.items||[]).filter(r=>typeof r.territoire_code==='string'&&typeof r.territoire_libelle==='string'&&typeof r.zonage==='string');}
};
function creerCatalogueObserve(data){
  const jobs=adapters.metiers({items:data.metiers}),certs=adapters.certifications(data.certifications);
  // Le JSON /domaines n'est pas disponible : la liste locale vient des domaines des métiers observés.
  // Il ne s'agit pas d'une réponse /domaines reconstruite et ses effectifs ne sont pas fabriqués.
  const domains=[...new Map(jobs.filter(m=>m.domaine_code&&m.domaine_libelle).map(m=>[m.domaine_code,{domaine_code:m.domaine_code,domaine_libelle:m.domaine_libelle,grand_domaine_code:m.grand_domaine_code,grand_domaine_libelle:m.grand_domaine_libelle}])).values()];
  const territories=[...new Map(data.territoires.flatMap(adapters.territoires).map(t=>[t.zonage+':'+t.territoire_code,t])).values()];
  const matches=(texts,q)=>{const words=normalize(q).trim().split(/\s+/).filter(Boolean),hay=normalize(texts.filter(Boolean).join(' '));return words.every(w=>hay.includes(w));};
  return {
    metiers:jobs,certifications:certs,domaines:domains,territoires:territories,
    async rechercher(mode,q){
      if(mode==='certification')return {mode,items:certs.filter(c=>matches([c.certifinfo_libelle,c.fiche_libelle,c.type_certification_libelle],q)),provenance:'JSON /certifications observé'};
      if(mode==='domaine')return {mode,items:domains.filter(d=>matches([d.domaine_libelle,d.grand_domaine_libelle],q)),provenance:'Domaines portés par les métiers observés, sans réponse /domaines réelle'};
      return {mode:'metier',items:jobs.filter(m=>matches([m.rome_libelle,...(m.appellations||[])],q)),provenance:'JSON /metiers et fiches observés'};
    },
    metier(code){return jobs.find(j=>j.rome_code===code);},
    certification(code){return code===data.certification.certifinfo_code?data.certification:certs.find(c=>c.certifinfo_code===code);},
    domaine(code){return domains.find(d=>d.domaine_code===code);},
    territoire(key){return territories.find(t=>t.zonage+':'+t.territoire_code===key);}
  };
}
const catalogue=creerCatalogueObserve(DATA);
const BINDINGS_RECHERCHE={metier:{endpoint:'/metiers',parametres:['q','page']},certification:{endpoint:'/certifications',parametres:['q','page']},domaine:{endpoint:'/domaines',parametres:['grand_domaine'],rechercheTexte:'filtre local des libellés reçus'},territoire:{endpoint:'/territoires',parametres:['q','zonage','page']}};
