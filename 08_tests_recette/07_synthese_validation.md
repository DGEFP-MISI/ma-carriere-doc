# MaCarrière — Synthèse et décision MVP

> **MaCarrière V0.2.0** · 11 novembre 2026 · DGEFP/MISI · [Site de test](https://ma-carriere.merith-technologies.com/) · [Nouveautés](https://ma-carriere.merith-technologies.com/nouveautes)

> **Statut :** protocole préparé — tests non encore exécutés.

## Indicateurs et synthèse d'arbitrage

Les seuils suivants sont des **cibles proposées pour la recette**, à valider avec l'équipe ; ce ne sont **pas** des résultats mesurés.

| Indicateur | Cible indicative |
| --- | --- |
| Première information utile atteinte sans aide | ≥ 80 % des sessions |
| Prochaine action comprise | ≥ 70 % des sessions |
| Indicateurs DATA échantillonnés justifiés par une source | 100 % |
| Liens critiques testés corrects | 100 % |
| Hallucinations critiques dans les scénarios IA contrôlés | 0 |
| Anomalies P0 encore ouvertes au passage de jalon | 0 |

### Tableau de synthèse à compléter

| Axe | Tests prévus | Exécutés | Réussis | Partiels | Échecs | Issues P0/P1 | Décision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| UX | À préciser | — | — | — | — | — | Non évalué |
| DATA | À préciser | — | — | — | — | — | Non évalué |
| IA | 6 prompts de base + parcours | — | — | — | — | — | Non évalué |
| PASSERELLES | 9 chaînes de base | — | — | — | — | — | Non évalué |

**Décision MVP (cible 15 décembre 2026) :** `Validé / Validé sous réserves / À corriger avant MVP / Reporté`, avec justification et responsable d'arbitrage. Ne pas confondre un test fonctionnel réussi avec la preuve qu'un service est utile : confronter les deux.

## Définition de « terminé » pour un test

Un test est terminé uniquement lorsque **la mission est exécutée ou l'échec documenté**, la preuve est associée, le résultat est qualifié, les anomalies ont des issues et une décision est renseignée. Un correctif n'est **validé** qu'après retest sur la version corrigée, idéalement accompagné d'un contrôle de non-régression.

---

**À actualiser à chaque version :** nouveautés réellement livrées, écrans disponibles, paramètres de l'API, scénarios impactés, anomalies ouvertes et décisions de recette. Conserver ce protocole transversal et filtrer les résultats par version dans le GitHub Project.
