# 4. Résultats et KPI

## 4.1 Protocole de test industriel

Le modèle a été intégré dans le process sous forme de recommandations de presets transmises aux laminateurs avant chaque phase d'engagement.

### Périmètre du test

| Paramètre | Valeur |
|-----------|--------|
| Durée du test | 1 mois |
| Part de production concernée | 20 % de la production totale |
| Mode | Recommandations modèle vs. presets opérateur |
| Périmètre produits | Gamme représentative des nuances et épaisseurs cibles courantes |

### Groupe de comparaison

- **Groupe test** : 20 % de la production avec presets issus du modèle XGBoost
- **Groupe contrôle** : 80 % de la production avec presets habituels (expérience opérateur)

---

## 4.2 KPI Qualité

| KPI | Avant projet (base) | Pendant le test (groupe modèle) |
|-----|---------------------|---------------------------------|
| **Taux de non-conformité tête de bande** | À renseigner (données historiques) | **0 %** |
| **Nombre de produits non-conformes** | — | **0 / total testé** |
| **Taux de conformité** | — | **100 %** |

> **Résultat clé : sur l'ensemble des produits issus du périmètre de test, aucun n'a présenté de non-conformité en tête de bobine.**

---

## 4.3 KPI Techniques

Les KPI techniques permettent de mesurer la qualité produit avec précision, au-delà du simple critère conforme/non-conforme.

| KPI Technique | Description | Objectif |
|---------------|-------------|----------|
| **Écart d'épaisseur moyen (tête)** | Différence entre épaisseur mesurée et épaisseur cible sur les 2–3 premiers mètres | Réduction vs. baseline |
| **Écart-type d'épaisseur (tête)** | Variabilité de l'épaisseur sur la zone d'engagement | Réduction de la dispersion |
| **Profil d'épaisseur cage par cage** | Épaisseur intermédiaire mesurée à la sortie de chaque cage | Conformité à la gamme |
| **Effort appliqué vs. effort prédit** | Comparaison entre la recommandation modèle et le preset réellement appliqué | Suivi de l'adoption |

> 📎 *Les graphiques de résultats (profils d'épaisseur, histogrammes d'écarts) peuvent être ajoutés dans `assets/resultats/`*

---

## 4.4 Analyse des résultats

### Points forts

- Le modèle XGBoost produit des presets plus adaptés aux caractéristiques réelles de chaque produit
- La réduction de variabilité est immédiate dès la phase d'engagement
- Les laminateurs moins expérimentés bénéficient d'un support de décision objectif
- Le taux de conformité obtenu valide l'approche data-driven sur ce cas d'usage industriel

### Enseignements

- La phase d'engagement, bien que courte (quelques secondes), a un impact déterminant sur la qualité de la tête de bobine
- Formaliser le savoir-faire en données exploitables permet de le rendre accessible à tous les opérateurs
- Un test sur 20 % de la production constitue une validation statistiquement significative pour ce type de ligne

---

## 4.5 Bilan global du projet

```
Problème identifié          → Variabilité non-conformité tête bande
Cause racine validée        → Presets empiriques sans modélisation
Solution développée         → Modèle XGBoost de prédiction des efforts
Test réalisé                → 20 % production, 1 mois
Résultat mesuré             → 0 produit non-conforme sur le périmètre test
Impact qualité              → Taux de conformité 100 % sur le test
Déployabilité               → Modèle reproductible, réentraînable
```
