# 2. Analyse du problème — A3 et Ishikawa

## 2.1 La démarche A3

L'**A3** est une méthode de résolution structurée de problèmes issue du Toyota Production System. Elle tient son nom du format de feuille A3 sur laquelle l'ensemble de l'analyse doit tenir.

Elle force à poser clairement :
- la situation actuelle
- la situation cible
- l'analyse des causes racines
- les contre-mesures
- le plan d'action et le suivi

### Structure de l'A3 appliqué au projet

| Bloc A3 | Contenu |
|---------|---------|
| **Titre** | Réduction de la variabilité produit en phase d'engagement — Laminoir 5 cages |
| **Contexte / background** | Défauts dimensionnels sur les 2–3 premiers mètres à chaque engagement |
| **Situation actuelle** | Presets d'effort définis par expérience opérateur, sans base de données formalisée, forte variabilité inter-équipes |
| **Situation cible** | Presets standardisés, objectifs, prédits automatiquement en fonction des paramètres produit |
| **Analyse des causes** | Voir diagramme Ishikawa ci-dessous |
| **Contre-mesures** | Modèle de prédiction XGBoost des efforts optimaux par cage |
| **Plan d'action** | Collecte données → Analyse → Modèle → Test 20% production → Déploiement |
| **Suivi / KPI** | Taux de conformité, écart d'épaisseur, nombre de têtes non-conformes |

> 📎 *Le document A3 complet (format PDF ou image) peut être ajouté dans `assets/analyses/`*

---

## 2.2 Cartographie des acteurs impliqués

Pour bien comprendre le problème, les acteurs en interaction avec la phase d'engagement ont été identifiés :

| Acteur | Rôle dans le process |
|--------|----------------------|
| **Laminateur** | Fixe les presets d'effort avant engagement |
| **Chef de poste** | Supervise la conduite de la ligne |
| **Service Qualité** | Contrôle les non-conformités en sortie |
| **Service Méthodes / Process** | Définit les gammes de laminage théoriques |
| **Maintenance** | Gère l'état mécanique des cages et cylindres |
| **Intérimaires** | Remplacent les laminateurs — expérience variable |

---

## 2.3 Diagramme Ishikawa (5M)

Le diagramme Ishikawa (ou arête de poisson) a permis de classer les causes potentielles de non-conformité en 5 familles.

```
                    EFFET : Défauts sur les 2-3 premiers mètres
                              en phase d'engagement
                                      |
        ┌─────────────────────────────┼──────────────────────────────┐
        │                             │                              │
      MILIEU                      MÉTHODE                        MATIÈRE
  ─────────────               ─────────────                   ─────────────
  - Conditions                - Pas de régulation             - Variabilité
    thermiques                  active en engagement            des coils
    variables                 - Presets empiriques              entrants
  - Usure des                 - Absence de base               - Nuance acier
    cylindres                   de connaissance                 variable
                                formalisée

        │                             │                              │
     MACHINE                       MAIN D'ŒUVRE
  ─────────────               ─────────────────────────────
  - État des                  - Niveaux d'expérience
    cages variable              hétérogènes (équipes)
  - Rigidité cage             - Présence d'intérimaires
  - Corrections               - Absence de standard
    mécaniques                  de formation
    non tracées
```

### Cause racine retenue

Après qualification des causes (fréquence, impact, maîtrisabilité) :

> **Cause principale : les presets d'effort appliqués en phase d'engagement reposent exclusivement sur le savoir-faire individuel des laminateurs, sans support de décision objectif et standardisé.**

---

## 2.4 Méthode des 5 Pourquoi

| # | Pourquoi ? | Réponse |
|---|-----------|---------|
| 1 | Pourquoi a-t-on des défauts sur les 2–3 premiers mètres ? | Les efforts appliqués ne sont pas optimaux pendant l'engagement |
| 2 | Pourquoi les efforts ne sont pas optimaux ? | Les presets sont fixés par l'opérateur selon son expérience |
| 3 | Pourquoi les opérateurs se basent sur leur expérience ? | Il n'existe pas de modèle prédictif ni de référentiel de presets |
| 4 | Pourquoi n'existe-t-il pas de référentiel ? | Les données historiques n'ont jamais été exploitées pour en créer un |
| 5 | Pourquoi les données n'ont pas été exploitées ? | Pas de démarche data/ML formalisée sur ce sujet jusqu'à présent |

**Conclusion :** Le levier d'action est la valorisation des données historiques pour construire un modèle prédictif des efforts optimaux.
