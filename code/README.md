# Instructions pour les notebooks

## Prérequis

Python 3.9 ou supérieur, puis installer les dépendances :

```bash
pip install -r requirements.txt
```

## Dépendances

```
xgboost>=1.7
pandas>=1.5
scikit-learn>=1.2
matplotlib>=3.6
seaborn>=0.12
jupyter>=1.0
numpy>=1.24
```

## Ordre d'exécution

1. `notebooks/01_exploration.ipynb` — Analyse exploratoire des données
2. `notebooks/02_feature_engineering.ipynb` — Préparation des variables
3. `notebooks/03_modele_xgboost.ipynb` — Entraînement et optimisation
4. `notebooks/04_resultats.ipynb` — Résultats et visualisation KPI

## Note sur les données

Les données de production réelles d'ArcelorMittal sont confidentielles.
Pour exécuter les notebooks en démonstration, des données synthétiques
peuvent être générées via le notebook 01.
