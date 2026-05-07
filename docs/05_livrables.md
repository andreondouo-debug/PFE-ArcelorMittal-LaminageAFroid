# 5. Livrables du projet

## 5.1 Documents produits

| Livrable | Format | Emplacement |
|----------|--------|-------------|
| Rapport de projet complet | PDF | À ajouter dans `assets/rapport/` |
| Présentation soutenance | PDF / PPTX | À ajouter dans `assets/rapport/` |
| A3 complet (analyse problème) | PDF / image | À ajouter dans `assets/analyses/` |
| Diagramme Ishikawa | PDF / image | À ajouter dans `assets/analyses/` |
| Schéma ligne laminoir | image | À ajouter dans `assets/schemas/` |
| Courbes résultats / KPI | images | À ajouter dans `assets/resultats/` |

---

## 5.2 Code source

| Fichier | Description |
|---------|-------------|
| `code/notebooks/01_exploration.ipynb` | Analyse exploratoire des données (EDA) |
| `code/notebooks/02_feature_engineering.ipynb` | Sélection et transformation des variables |
| `code/notebooks/03_modele_xgboost.ipynb` | Entraînement, optimisation et évaluation du modèle |
| `code/notebooks/04_resultats.ipynb` | Visualisation des résultats et KPI |

> ⚠️ *Les données de production ArcelorMittal sont confidentielles. Les notebooks peuvent contenir des données anonymisées ou synthétiques à des fins de démonstration.*

---

## 5.3 Comment utiliser ce dépôt

### Prérequis

```bash
Python >= 3.9
pip install xgboost pandas scikit-learn matplotlib seaborn jupyter
```

### Lancer les notebooks

```bash
cd code/
jupyter notebook
```

---

## 5.4 Confidentialité

> Ce projet a été réalisé dans le cadre d'un stage en entreprise chez **ArcelorMittal**.  
> Certaines données, paramètres spécifiques et résultats détaillés ont été **anonymisés ou omis** pour respecter la confidentialité industrielle.  
> Les méthodes, approches et résultats généraux sont présentés dans un but pédagogique et de valorisation du travail réalisé.
