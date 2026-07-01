# Projet de Fin d'Études — De la modélisation à la formation : création d’un standard d’engagement bobine pour laminoir à froid

> **Entreprise :** ArcelorMittal  
> **Ligne de production :** Laminoir à froid tandem — 5 cages de type Quarto  
> **Approche :** Analyse industrielle (A3, AMDEC, Ishikawa) + Machine Learning (XGBoost)  
> **Résultat :** 0 produit non-conforme sur 20 % de la production pendant 1 mois de test

---

## Sommaire

| # | Section | Description |
|---|---------|-------------|
| 1 | [Contexte et problématique](docs/01_contexte_et_problematique.md) | Présentation de la ligne, du process et du défaut observé |
| 2 | [Analyse A3 et Ishikawa](docs/02_analyse_A3_Ishikawa.md) | Démarche de résolution structurée du problème |
| 3 | [Modèle de Machine Learning](docs/03_modele_ML_XGBoost.md) | Développement et entraînement du modèle XGBoost |
| 4 | [Résultats et KPI](docs/04_resultats_et_KPI.md) | Validation, indicateurs qualité et techniques |
| 5 | [Livrables](docs/05_livrables.md) | Documents, rapports, code sources |

---

## Résumé du projet

### Contexte

ArcelorMittal, qui est le leader mondial de la production d'acier, est implanté dans plus d'une cinquantaine de pays, avec une forte présence en France, et notamment 11 sites de production sur le territoire. Pour mon stage de fin d'études, j'ai été affecté sur le site de Florange, précisément sur la ligne de laminage à froid. Le laminage à froid est une opération de mise en forme d'un produit — ici de l'acier — que l'on fait passer entre deux cylindres métalliques exerçant ainsi des efforts de compression sur le produit. Pour limiter les effets de bord, on dispose de deux cylindres de soutien. Un ensemble de deux cylindres de travail et de deux cylindres de soutien forme une cage de laminage de type Quarto.

<p align="center">
  <img src="https://github.com/user-attachments/assets/94b5a2c5-beff-4eef-b5d9-de134681cde8" width="450">
</p>

<p align="center">
  <strong>Figure 1 :</strong> Différents types de cages de laminoirs couramment utilisés. Les flèches indiquent les efforts exercés lors du processus de laminage.
</p>
Sur cette ligne de laminage à froid tandem (5 cages de type Quarto (Deux cylindres de travail et deux cylindres de soutien)) d'ArcelorMittal, le processus de laminage se déroule globalement en trois phases :

- **Phase d'engagement** : passage du produit cage par cage (C1 → C5) à vitesse réduite, sans régulation active
- **Phase de laminage** : montée en vitesse pour le laminage nominal
- **Phase de dégagement** : décélération et fin du passage produit

### Problème identifié

Pendant la phase d'engagement, l'absence de régulation combinée à la forte dépendance aux **presets d'efforts de serrage** générait des **défauts dimensionnels sur les premiers mètres** du produit — la zone qui s'enroule en tête d'enrouleuse. (Vue simplifiée de la ligne : https://app.diagrams.net/#G1SfCMVZST7MvXdP9abZaDZC4ATlHMqr8a#%7B%22pageId%22%3A%22T300FtAnsqmrBS-oEQUZ%22%7D)

La variabilité était amplifiée par :
- les différences de niveau entre équipes
- la présence d'intérimaires avec moins d'expérience

### Solution développée

Développement d'un **modèle de prédiction XGBoost** capable de fournir, en fonction des paramètres d'entrée influençant la conformité du produit, les **efforts à appliquer sur chaque cage** pour garantir un produit conforme dès la phase d'engagement.

### Résultats

- Test sur **20 % de la production** pendant **1 mois**
- **0 produit non-conforme** issu du périmètre de test
- Validation via KPI qualité (conformité produit) et KPI techniques (épaisseur mesurée)

---

## Structure du dépôt

```
PFE-ArcelorMittal-LaminageAFroid/
│
├── README.md                      ← Ce fichier (vue d'ensemble du projet)
├── .gitignore
│
├── docs/                          ← Documentation détaillée du projet
│   ├── 01_contexte_et_problematique.md
│   ├── 02_analyse_A3_Ishikawa.md
│   ├── 03_modele_ML_XGBoost.md
│   ├── 04_resultats_et_KPI.md
│   └── 05_livrables.md
│
├── assets/                        ← Ressources visuelles et livrables
│   ├── schemas/                   ← Schémas du laminoir, diagrammes process
│   ├── analyses/                  ← A3, Ishikawa, graphiques d'analyse
│   ├── resultats/                 ← Courbes de résultats, captures KPI
│   └── rapport/                   ← Rapport de projet et présentation de soutenance
│
└── code/                          ← Code source (analyse + modèle ML)
    ├── README.md                  ← Instructions d'installation et d'exécution
    ├── requirements.txt           ← Dépendances Python
    └── notebooks/                 ← Notebooks Jupyter (EDA, features, modèle, résultats)
```

---

## Compétences mobilisées

- Analyse industrielle et démarche de résolution de problèmes (A3, 5 Pourquoi, Ishikawa)
- Collecte et traitement de données de production
- Machine Learning supervisé (XGBoost, optimisation d'hyperparamètres)
- Définition et suivi de KPI qualité et techniques
- Communication et présentation de résultats à l'encadrement industriel
