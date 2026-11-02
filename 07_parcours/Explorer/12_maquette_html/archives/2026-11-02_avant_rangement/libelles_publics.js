// Présentation uniquement : les identifiants techniques restent intacts dans DATA et les interactions.
function publicText(value){
  let text=String(value??'');
  const fixed=[
    ['ROME V3 uniquement','Des noms de métiers, sans jargon'],
    ['Un domaine professionnel ROME','Un domaine professionnel'],
    ['Référentiel ROME : métiers et domaines professionnels.','Découvrez les métiers et les domaines professionnels.'],
    ['Explorer un métier · ROME V3 F1610','Explorer un métier'],
    ['Métier · ROME V3','Métier'],
    ['Choisissez des codes OGR','Choisissez des compétences'],
    ['codes OGR rattachés aux métiers ROME V3','compétences associées aux métiers'],
    ['codes OGR du métier','compétences du métier'],
    ['référentiel OGR','liste de compétences'],
    ['Compétences RNCP / OGR','Compétences du diplôme / du métier'],
    ['Quatre blocs de compétences RNCP','Quatre blocs de compétences à valider'],
    ['FAP225 × NAF38','groupes de métiers et secteurs d’activité'],
    ['familles FAP228 séparées','groupes de métiers présentés séparément'],
    ['Les valeurs FAP87 B0Z et B2Z restent séparées.','Les deux groupes de métiers sont présentés séparément.'],
    ['Les FAP ne sont pas des codes ROME ouvrables automatiquement.','Une situation professionnelle ne correspond pas nécessairement à un métier précis à ouvrir.'],
    ['Si deux métiers partagent la même FAP','Si deux métiers appartiennent au même groupe statistique'],
    ['Extraits des JSON de référence','Exemples de données disponibles'],
    ['Non référencé dans le JSON fourni','Non indiqué dans les données disponibles'],
    ['Le filtre F1610 ne restitue pas le résultat attendu.','Le détail local attendu pour ce métier est indisponible dans les données reçues.'],
    ['Sélection disponible dans l’exemple R23.','Deux compétences disponibles pour essayer cette maquette.'],
    ['Résultat observé R23, codes125416 et103659.','Exemple disponible pour les deux compétences choisies.'],
    ['R23','le jeu d’exemple'],['R24','le test des conditions de travail'],['R17','l’anomalie connue du fournisseur'],
    ['125416 · 103659',"Réaliser un raccordement d’étanchéité · Poser des panneaux solaires"],
    ['Code Formacode observé','Thème de formation'],
    ['Thèmes Formacode','Thèmes de formation'],
    ['Un thème n\'est pas un domaine ROME','Un thème de formation et un domaine professionnel sont deux choses différentes'],
    ['Les libellés seront ceux de /formacodes. Aucun intitulé n\'est inventé ici ; les codes sont issus de la fiche métier.','Les thèmes portent les noms fournis par les données disponibles. Les liens vers les certifications restent à vérifier.'],
    ['Certif Info 112561 · RNCP36101 · Niveau 3','Certification professionnelle · Niveau 3'],
    ['Textes certifiants, sans équivalence automatique avec les codes OGR du métier.','Ces compétences à valider pour le diplôme ne sont pas automatiquement équivalentes aux compétences décrites dans les fiches métiers.'],
    ['BMO','Besoins en main-d’œuvre'],
    ['Famille B0Z21 :','Groupe de métiers :'],
    ['famille B0Z21,','groupe de métiers :'],
    ['Famille B0Z21 ·','Groupe de métiers : B0Z21 ·'],
    ['famille professionnelle','groupe de métiers'],
    ['familles professionnelles','groupes de métiers'],
    ['Famille professionnelle','Groupe de métiers'],
    ['Même famille','Même groupe de métiers'],
    ['même famille','même groupe de métiers'],
    ['sans agrégation entre familles','sans additionner les groupes de métiers'],
    ['familles séparées','groupes de métiers présentés séparément'],
    ['commune34172','commune de Montpellier'],
    ['commune — Hérault','Hérault'],
    ['Second œuvre · F16','Second œuvre'],
    ['Domaine professionnel ROME F16','Domaine professionnel : Second œuvre'],
    ['secteur économique NAF','secteur d’activité économique'],
    ['métiers ROME associés','métiers associés'],
    ['Code ROME V3','Identifiant du métier'],
    ['ROME V3 · F1610','Métier'],
    ['ROME V3 F1610','Métier'],
    ['ROME V3 ·',''],
    ['ROME V3','métiers'],
    ['· ROME F16','· Second œuvre'],
    ['Tag vrai dans la fiche F1610.','Métier signalé comme concerné dans les données.'],
    ['Tag faux dans le jeu reçu.','Métier non signalé comme concerné dans les données.'],
    ['Tag faux','Non signalé'],
    ['FAP87','groupe de métiers'],['FAP225','groupe de métiers'],['FAP228','groupe de métiers'],
  ];
  for(const [from,to] of fixed)text=text.split(from).join(to);
  const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/œ/g,'oe').replace(/[’']/g,' ').replace(/\s+/g,' ').toLowerCase();
  // Seuls les codes alphabétiques connus sont remplacés dans le texte courant.
  // Les nombres (montants, dates, effectifs) ne passent jamais dans cette substitution.
  const codes=Object.keys(DATA.labels).filter(c=>/^(?:[A-Z]\d{2,4}|[A-Z]\d[A-Z]\d{0,2}|RNCP\d+|RS\d+)$/.test(c)).sort((a,b)=>b.length-a.length);
  for(const code of codes){
    const name=DATA.labels[code],re=new RegExp('(?<![A-Za-z0-9])'+code+'(?![A-Za-z0-9])','g');
    if(!re.test(text))continue;re.lastIndex=0;
    text=text.replace(re,normalize(text).includes(normalize(name))?'':name);
  }
  text=text.replace(/\b(?:FAP\s?\d*|OGR|NAF\s?\d*)\b/g,'').replace(/\bROME\b/g,'métiers').replace(/\bRNCP\b/g,'certification professionnelle').replace(/\bFormacodes?\b/g,'thèmes de formation');
  text=text.replace(/\s*·\s*·\s*/g,' · ').replace(/\(\s*\)/g,'').replace(/^\s*[·:,]\s*|\s*[·:]\s*$/g,'').replace(/\s{2,}/g,' ').trim();
  return text;
}
function publicize(root){
  const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode(n){return n.parentElement.closest('script,style,[data-technical]')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT;}});
  const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes)if(node.textContent.trim()){const original=node.textContent;const label=publicText(original);node.textContent=(/^\s/.test(original)?' ':'')+label+(/\s$/.test(original)?' ':'');}
  for(const input of root.querySelectorAll('input[readonly]'))input.value=publicText(input.value);
}
