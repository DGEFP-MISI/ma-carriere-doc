# MaCarrière — Suivi GitHub et anomalies

> **MaCarrière V0.2.0** · 11 novembre 2026 · DGEFP/MISI · [Site de test](https://ma-carriere.merith-technologies.com/) · [Nouveautés](https://ma-carriere.merith-technologies.com/nouveautes)

> **Statut :** protocole préparé — tests non encore exécutés.

## Suivi dans GitHub

**Documentation source :** le dossier `08_tests_recette/`.  
**Issues :** une issue par anomalie reproductible ou par tâche de recette, avec lien au scénario.  
**GitHub Project :** tableau partagé couvrant toutes les versions, avec champs **Version**, **Axe**, **Priorité**, **Responsable**, **Résultat**, **Statut** et **Scénario**.

### Statuts recommandés

`À tester` → `En test` → `À corriger` → `À retester` → `Validé`  
Si anomalie découverte : créer/lier l'issue, puis la traiter selon cette même chaîne. Conserver `Non reproductible`, `Hors périmètre` et `Reporté` comme décisions explicites plutôt que masquer les cas.

### Priorités

- **P0 — Bloquant :** donnée matériellement trompeuse sur un point critique, fuite d'information, fonction indispensable inutilisable.
- **P1 — Majeur :** empêche l'utilisateur d'accomplir sa mission ou erreur de correspondance grave.
- **P2 — Important :** forte incompréhension, navigation problématique, contenu peu exploitable.
- **P3 — Mineur :** amélioration de lisibilité ou de confort sans obstacle majeur.

### Modèle d'issue

```markdown
## Contexte
- Version : V0.2.0
- Axe : UX / DATA / IA / PASSERELLE
- Scénario : Txx / IAxx
- URL / écran :
- Appareil / navigateur :

## Étapes pour reproduire
1.
2.
3.

## Résultat observé

## Résultat attendu

## Preuves
- Capture anonymisée / log non sensible / référence API :

## Impact et priorité
- Priorité proposée : P0 / P1 / P2 / P3
- Utilisateurs affectés :

## Décision et recette de correction
- Responsable :
- Correction / arbitrage :
- Date du retest :
- Résultat du retest :
```

**Confidentialité :** le dépôt étant susceptible d'être public, ne pas y inscrire noms de testeurs, coordonnées, enregistrements identifiants, prompts personnels non anonymisés, secrets techniques ou réponses API sensibles.
