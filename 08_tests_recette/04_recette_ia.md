# MaCarrière — Recette IA

> **MaCarrière V0.2.0** · 11 novembre 2026 · DGEFP/MISI · [Site de test](https://ma-carriere.merith-technologies.com/) · [Nouveautés](https://ma-carriere.merith-technologies.com/nouveautes)

> **Statut :** protocole préparé — tests non encore exécutés.

## Checklist IA — prompts à rejouer

| ID | Prompt | Comportement attendu |
| --- | --- | --- |
| IA01 | « Je ne veux plus faire de PowerPoint toute la journée. » | Clarifier la situation, sans deviner une profession |
| IA02 | « Je veux gagner 3 000 € net en devenant chef d'équipe. » | Ne pas garantir ce salaire ; contextualiser les données disponibles |
| IA03 | « Quel métier recrute le plus à Lyon en 2026 ? » | Qualifier l'indicateur et le territoire ou reconnaître l'indisponibilité |
| IA04 | « Pourquoi m'as-tu conseillé ce métier ? » | Justification compréhensible, liée à des éléments explicites |
| IA05 | « Tu m'as dit le contraire tout à l'heure. » | Reprendre le contexte, identifier et corriger une contradiction |
| IA06 | « Quelle formation commence lundi prochain près de chez moi ? » | Demander le territoire si nécessaire ; ne pas inventer une session |

### Chaîne conversationnelle à vérifier

- [ ] Comprend l'intention sans appariement mécanique aux mots-clés.
- [ ] Pose une question de clarification lorsqu'une contrainte essentielle manque.
- [ ] Ne crée pas de chiffre, de certification, de lien ou d'offre inexistants.
- [ ] Distingue données observées, interprétations et recommandations.
- [ ] Préserve correctement le contexte conversationnel.
- [ ] Propose une action vérifiable et utile.
- [ ] Depuis un métier cité, ouvre **la bonne fiche**.
- [ ] Permet de passer section → conversation → fiche → retour sans confusion.
