# 3. Modèle de Machine Learning — XGBoost

## 3.1 Objectif du modèle

À partir des **paramètres d'entrée disponibles avant ou pendant la phase d'engagement**, prédire les **efforts optimaux à appliquer sur chaque cage** (C1 à C5) pour obtenir un produit conforme à l'épaisseur cible.

```
Paramètres produit/process (entrée)
        ↓
  [Modèle XGBoost]
        ↓
Efforts préconisés par cage (sortie)
→ Produit conforme en tête de bobine
```

---

## 3.2 Données utilisées

### Source des données

- **Base de données de production** — historique des campagnes de laminage
- Chaque ligne = un passage produit avec ses paramètres d'engagement et ses mesures de conformité en sortie

### Variables étudiées

| Famille | Exemples de variables |
|---------|-----------------------|
| **Caractéristiques produit** | Nuance acier, épaisseur entrée, épaisseur cible, largeur bande |
| **Paramètres de laminage** | Effort appliqué par cage, vitesse d'engagement |
| **État machine** | Diamètre cylindres, tonnage depuis changement cylindres |
| **Cible (variable Y)** | Effort optimal par cage / conformité de l'épaisseur en sortie |

> 📎 *Le dictionnaire complet des variables peut être ajouté dans `assets/analyses/`*

---

## 3.3 Sélection des variables (Feature Engineering)

Une analyse de corrélation et d'importance des variables a été réalisée pour identifier les **paramètres qui influent significativement** sur la conformité du produit.

Les variables fortement corrélées ou redondantes ont été écartées pour éviter le surapprentissage (overfitting).

---

## 3.4 Le modèle XGBoost

### Pourquoi XGBoost ?

| Critère | Justification |
|---------|---------------|
| **Performance** | Excellent sur des données tabulaires industrielles |
| **Robustesse** | Gère bien les valeurs manquantes et les outliers |
| **Interprétabilité** | Permet d'analyser l'importance des variables |
| **Rapidité** | Temps d'entraînement et d'inférence faibles |

**XGBoost** (eXtreme Gradient Boosting) est un algorithme d'apprentissage par ensemble basé sur des arbres de décision optimisés par descente de gradient.

### Pipeline de modélisation

```
1. Collecte et nettoyage des données historiques
        ↓
2. Analyse exploratoire (EDA)
        ↓
3. Sélection des variables pertinentes
        ↓
4. Séparation Train / Validation / Test
        ↓
5. Entraînement XGBoost + optimisation des hyperparamètres
        ↓
6. Évaluation sur le jeu de test (métriques)
        ↓
7. Déploiement sur 20% de la production (test industriel)
```

### Hyperparamètres optimisés

| Hyperparamètre | Rôle |
|----------------|------|
| `n_estimators` | Nombre d'arbres |
| `max_depth` | Profondeur maximale des arbres |
| `learning_rate` | Taux d'apprentissage |
| `subsample` | Fraction des données utilisées par arbre |
| `colsample_bytree` | Fraction des variables par arbre |
| `reg_alpha` / `reg_lambda` | Régularisation L1 / L2 |

---

## 3.5 Évaluation du modèle

### Métriques utilisées

| Métrique | Description |
|----------|-------------|
| **MAE** (Mean Absolute Error) | Erreur moyenne absolue sur la prédiction des efforts |
| **RMSE** (Root Mean Square Error) | Pénalise davantage les grandes erreurs |
| **R²** | Part de variance expliquée par le modèle |
| **Taux de conformité** | % de produits dans la tolérance d'épaisseur cible |

> 📎 *Les courbes de résultats et matrices de performance peuvent être ajoutées dans `assets/resultats/`*

---

## 3.6 Importance des variables

L'analyse de l'importance des variables (feature importance) via XGBoost a permis de confirmer les causes identifiées lors de l'Ishikawa :
- Les caractéristiques du produit (nuance, épaisseur cible) sont les variables les plus prédictives
- L'état des cylindres (tonnage laminé depuis le changement) a également un impact significatif

---

## 3.7 Limitations et perspectives

| Limitation | Perspective |
|-----------|-------------|
| Le modèle est entraîné sur un périmètre de production donné | Réentraînement périodique à intégrer |
| Les presets prédits sont des recommandations — l'opérateur reste maître | Intégration possible dans un système d'aide à la conduite |
| Données limitées sur certaines nuances rares | Enrichissement progressif de la base |
