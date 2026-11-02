# Règles statistiques, qualité et accessibilité

## Les règles non négociables
1. Identifier l'objet : ROME V3 n'est pas FAP225, FAP228 ou FAP87. Afficher `grain` et population, pas seulement métier de requête.
2. Distinguer BMO projets, offres, embauches; mesure projet BMO n'est pas emploi disponible.
3. `maille_reelle` prévaut sur le territoire demandé. Signaler tout repli sans placer une valeur régionale sur une carte départementale.
4. `null`, absent, zéro, liste vide, `secret_stat`, erreur et valeur non applicable sont sept états différents. **Ne pas convertir null en 0.** Ne pas interpoler les trous.
5. Unités : salaire annuel vs mensuel net; taux vs effectif; créations négatives; pas de mélange de doubles axes ambiguës.
6. Millésime : source et période affichées pour chacune; aucune courbe interpolée de 2019 à 2030.
7. Ne jamais calculer une moyenne de médianes territoriales ou sectorielles; médianes et quantiles non additifs.
8. Ne pas additionner familles qui se chevauchent ni comparer territoires avec des repli différents comme s'ils étaient de même niveau.
9. Éviter les classements « les meilleurs » qui combinent plusieurs dimensions; tri unidimensionnel descriptif autorisé et expliqué.
10. Les taux d'insertion ne sont pas tous sur la même population ni durée; vérifier chaque source/millésime.

## DSFR Chart, accessibilité et contrôles d'intégration ciblés
**Principe adopté : réutiliser les composants officiels DSFR Chart et les capacités d'accessibilité déjà fournies, sans reconstruire ni réauditer toute la bibliothèque.** DSFR demeure le socle de l'interface.

- Utiliser en priorité DataBox, les graphiques et les alternatives documentés de la version installée ; ne pas recréer ces mécanismes.
- Dans MaCarrière, vérifier uniquement l'assemblage : titre intelligible, unité, source et population, alternative tabulaire lorsqu'elle est nécessaire, lien entre filtres et résultats, focus et annonces des actualisations.
- Les valeurs doivent rester accessibles autrement que par le seul survol ; utiliser d'abord les mécanismes officiellement fournis par les composants.
- Vérifier l'usage de la palette et des thèmes DSFR, le responsive, l'utilisation au clavier avec les contrôles du parcours et le comportement à fort zoom **sur les écrans intégrés**.
- Ne pas commander systématiquement une nouvelle campagne complète de tests de conformité sur chaque graphique isolé. Déclencher des tests complémentaires ciblés lorsqu'une intégration ou un composant personnalisé introduit un risque identifié.
- La provenance gouvernementale d'une bibliothèque est une raison de la réutiliser, mais ne constitue pas une attestation automatique de conformité RGAA de l'application complète.

## Cas de tests statistiques
- Zéro véritable et liste vide; valeur sous secret; un seul territoire; territoire avec repli; valeur négative prospective; outlier; salaire FAP225 et recrutement FAP228; code region 11→IDF et 84→ARA après contrôle; certification sans indicateur; mélange 6m/12m; CSV respectant masquage; donnée non applicable.

## Messages UX recommandés
- « Cette donnée n'est pas disponible pour les critères sélectionnés. »
- « Les résultats concernent une famille professionnelle, et non uniquement le métier consulté. »
- « Pour préserver la confidentialité statistique, cette valeur n'est pas publiée. »
- « L'indicateur disponible porte sur une zone géographique plus large que celle sélectionnée. »
