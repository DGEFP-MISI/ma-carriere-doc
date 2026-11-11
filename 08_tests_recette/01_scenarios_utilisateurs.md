# MaCarrière — Scénarios utilisateurs

> **MaCarrière V0.2.0** · 11 novembre 2026 · DGEFP/MISI · [Site de test](https://ma-carriere.merith-technologies.com/) · [Nouveautés](https://ma-carriere.merith-technologies.com/nouveautes)

> **Statut :** protocole préparé — tests non encore exécutés.

## Scénarios utilisateurs — missions à jouer

| ID | Profil/situation | Mission à lire au testeur | Parcours de référence (observateur seulement) | Axes dominants |
| --- | --- | --- | --- | --- |
| T01 | Automaticien, 40 ans | « Je voudrais mieux gagner ma vie sans reprendre trois années d'études. » | IA → métiers → salaires → certifications → projet | UX, DATA, IA |
| T02 | Technicien maintenance agroalimentaire | « On me propose d'encadrer une équipe de 20 personnes. Est-ce intéressant pour moi ? » | IA → comparaison → conditions de travail | UX, IA, DATA |
| T03 | Aide aux devoirs à domicile, 35 ans | « Je cherche un emploi plus stable en utilisant mon expérience. » | Accueil → Explorer → métier → projet | UX, IA, DATA |
| T04 | Éducatrice spécialisée | « Je veux continuer à aider les autres, mais avec des horaires moins difficiles. » | IA → conditions de travail → pistes | IA, DATA |
| T05 | Lycéen, 17 ans | « Je voudrais devenir avocat. Quel diplôme faut-il ? » | Explorer → certification/métier → IA | UX, DATA |
| T06 | Étudiante en deuxième année de prépa | « Je ne sais pas vers quels métiers m'orienter. » | Accueil → IA → Explorer → pistes | UX, IA |
| T07 | Actif expérimenté sans diplôme | « Je voudrais faire reconnaître mes dix années d'expérience. » | Métier → certification → VAE | DATA, passerelles |
| T08 | Actif envisageant Lyon | « Mon métier recrute-t-il à Lyon ? » | Métier → territoire → recrutements → offres | DATA, passerelles |
| T09 | Actif en reconversion | « J'hésite entre technicien de maintenance et responsable de production. » | Recherche → comparaison → Mes pistes | UX, DATA |
| T10 | Personne peu à l'aise avec le numérique | « Je ne veux plus travailler la nuit, sans savoir quoi faire d'autre. » | Entrée libre → réponse → prochaine action | UX, IA |

> **Attention :** les profils sont des situations de test, pas des déclarations sur des personnes. Les tests réels précédents ont notamment mis en évidence une faible visibilité du panneau latéral, des difficultés avec « Voir les sections », « Ajouter à votre page » et l'historique. Rejouer précisément ces points pour mesurer la correction.

## Modèle de fiche de test (à dupliquer)

```markdown
### TEST Txx — [Nom du scénario]
- Version / environnement : V0.2.0 / [URL]
- Date / observateur :
- Testeur : [identifiant anonymisé]
- Appareil / navigateur :
- Mission donnée :
- Parcours réellement suivi :
- Premier clic :
- Première information utile : [temps ou non atteinte]
- Aides données : [nombre et type]
- Gestes / hésitations observés :
- Verbatim exact : « ... »
- Donnée ou réponse IA contrôlée :
- Prochaine action identifiée :
- Résultat : [réussi sans aide / réussi avec aide / échec]
- Sévérité éventuelle : [P0 / P1 / P2 / P3]
- Issue GitHub / preuve anonymisée :
- Analyse et décision :
```
