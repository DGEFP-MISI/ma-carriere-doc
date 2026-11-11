# MaCarrière — Recette DATA

> **MaCarrière V0.2.0** · 11 novembre 2026 · DGEFP/MISI · [Site de test](https://ma-carriere.merith-technologies.com/) · [Nouveautés](https://ma-carriere.merith-technologies.com/nouveautes)

> **Statut :** protocole préparé — tests non encore exécutés.

## Checklist DATA — confrontation API ↔ UI

Pour chaque échantillon : conserver **code métier/certification**, URL ou endpoint/GET, paramètres, date de requête, réponse brute (si communicable), valeur affichée, résultat de comparaison et éventuel ticket.

| Contrôle | Question de recette | Critère |
| --- | --- | --- |
| Identification | Le métier et son code sont-ils corrects ? | Libellé et relation ROME V3/V4 documentés ; pas de confusion de code parent/enfant |
| Recherche | La correspondance est-elle pertinente ? | Pas de faux positif manifeste ; correspondances indirectes utiles explicables |
| Recrutements | Que mesure exactement le chiffre ? | Année, périmètre, territoire et population indiqués |
| Tensions et difficultés | S'agit-il bien du bon indicateur ? | Pas de confusion offres, projets de recrutements et difficultés |
| Salaires | Net/brut, temps de travail, période et source ? | Pas de conversion inventée ni d'affichage « actuel » d'une série ancienne |
| Contrats | Contrats occupés ou contrats des offres ? | Populations non mélangées |
| Secteurs | Le champ désigne-t-il branche, NAF, IDCC ou autre ? | Nomenclature et unité réellement fournies identifiées |
| Mobilités | Que signifient entrants/sortants ? | Sens des flux vérifié, pas d'interprétation abusive |
| Certifications/VAE | Le lien métier–certification est-il établi ? | Relation de référence vérifiée ; voies d'accès exactes |
| Formations/sessions | La session correspond-elle au bon diplôme et territoire ? | Dates et modalités factuelles, non supposées |
| Donnée absente | Comment le service réagit-il ? | « Donnée non disponible » ou bloc masqué ; zéro n'est pas substitué à une absence |

**Règle de vigilance salaires :** vérifier source, millésime, mode de calcul, population et robustesse avant toute validation. Si non robustes, **masquer ou qualifier** l'information ; ne pas inventer d'estimation 2025–2026.
