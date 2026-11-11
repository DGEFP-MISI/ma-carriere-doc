# MaCarrière — Tests & recette V0.2.0

> **Version :** 0.2.0 · **Date :** 11 novembre 2026 · **Pilote :** DGEFP / MISI  
> **Site :** https://ma-carriere.merith-technologies.com/  
> **Nouveautés :** https://ma-carriere.merith-technologies.com/nouveautes  
> **Statut :** campagne à exécuter — aucun résultat présumé validé.

## Objectif

Vérifier qu'un utilisateur peut partir d'une question sur sa carrière, accéder à des informations compréhensibles et fiables, explorer des pistes pertinentes puis identifier une action concrète. La recette couvre **UX, DATA, IA et passerelles**.

## Documents de test

| Fichier | Utilité | Pour qui ? |
| --- | --- | --- |
| [01_scenarios_utilisateurs.md](01_scenarios_utilisateurs.md) | 10 missions + modèle d'observation | Testeurs et observateurs |
| [02_recette_ux.md](02_recette_ux.md) | Navigation, fiches, accessibilité, mobile | UX, produit |
| [03_recette_data.md](03_recette_data.md) | Confrontation des indicateurs API ↔ UI | DATA, RCO |
| [04_recette_ia.md](04_recette_ia.md) | Prompts, cohérence, hallucinations | IA, produit |
| [05_recette_passerelles.md](05_recette_passerelles.md) | Liens et transferts vers les services | Produit, technique |
| [06_suivi_github.md](06_suivi_github.md) | Issues, priorités, statuts et modèle d'anomalie | Toute l'équipe |
| [07_synthese_validation.md](07_synthese_validation.md) | Indicateurs et arbitrage MVP | Pilotage / direction |

## Méthode

1. Choisir un scénario dans **01** et donner uniquement la mission au testeur.
2. Observer sans guider ; noter gestes et verbatims exacts, anonymisés.
3. Rejouer les contrôles spécialisés **02 à 05** selon les fonctionnalités réellement livrées.
4. Ouvrir une Issue par anomalie reproductible et suivre son traitement selon **06**.
5. Consolider les résultats et arbitrer dans **07** ; retester les corrections.

### Déroulement type d'une session (25–30 min)

| Durée indicative | Phase |
| --- | --- |
| 2 min | Accueil et accord pour observation |
| 3 min | Premier regard, sans aide |
| 12–15 min | Mission utilisateur |
| 5 min | Exploration d'une autre entrée |
| 3–5 min | Débrief : compréhension et prochaine étape |

**À relever :** version/URL, appareil/navigateur, premier clic, délai avant première information utile, aides demandées, gestes, mots exacts, erreurs, résultat, prochaine action et preuve anonymisée.

## Règles communes

- Distinguer **fait observé**, **interprétation** et **correction proposée**.
- Une donnée non disponible ou non robuste ne doit jamais devenir une estimation certaine.
- Une fonctionnalité non livrée doit être classée **évolution**, pas anomalie.
- Ne pas publier de données personnelles, secrets API ou captures identifiantes dans le dépôt.
- Une correction n'est validée qu'après **retest** sur la version corrigée.

**Emplacement GitHub proposé :** `DGEFP-MISI/ma-carriere-doc/08_tests_recette/`. Les scénarios sont documentés ici, les anomalies sont suivies dans les Issues et la campagne dans un GitHub Project transversal à toutes les versions.
