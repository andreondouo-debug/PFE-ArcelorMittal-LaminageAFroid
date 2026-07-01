# 1. Contexte et Problématique

## 1.1 L'entreprise — ArcelorMittal

ArcelorMittal est le premier groupe sidérurgique mondial. Le site concerné par ce projet est le site de FLORANGE situé en LORRAINE. Le site possède une ligne de **laminage à froid**, utilisée pour réduire l'épaisseur de bandes d'acier après un premier laminage à chaud sur les lignes précédentes, afin d'obtenir des produits plats de précision (précis au dixième de mm).

---

## 1.2 La ligne de production — Le laminoir à froid tandem 5 cages Quarto

Le laminoir à froid tandem est constitué de **5 cages successives de type Quarto**.

> Une cage **Quarto** est un assemblage de 4 cylindres : 2 cylindres de travail (qui déforment la bande) et 2 cylindres d'appui (qui rigidifient l'ensemble).

```
Dérouleuse → [C1] → [C2] → [C3] → [C4] → [C5] → Enrouleuse
```

La bande d'acier traverse les 5 cages en continu, chaque cage appliquant un effort de compression pour réduire progressivement l'épaisseur de la bande jusqu'à l'épaisseur cible.

---

## 1.3 Les trois phases du process de laminage

### Phase 1 — Engagement

- Passage du produit cage par cage, à **vitesse réduite**
- La bande entre cage par cage : de C1 jusqu'à C5
- À la sortie de C5, la tête de bande est envoyée sur l'**enrouleuse**
- ⚠️ **Aucune régulation active** pendant cette phase : les efforts appliqués sur chaque cage sont définis manuellement par l'opérateur via des **presets**

### Phase 2 — Laminage

- Après l'engagement complet, **montée en vitesse** de la ligne
- La régulation automatique se met en place
- Le laminage nominal s'effectue avec contrôle continu de l'épaisseur

### Phase 3 — Dégagement

- **Décélération** progressive de la ligne
- Passage de la queue de bande hors des cages
- Fin de l'enroulement

---

## 1.4 Le problème identifié

### Observation

Des **défauts dimensionnels** (non-conformité d'épaisseur) étaient systématiquement observés sur les **2 à 3 premiers mètres** de la bande — correspondant exactement à la zone traitée pendant la phase d'engagement.

Cette zone défectueuse est enroulée en **tête de bobine** et constitue une perte matière récurrente.

### Causes racines identifiées

La phase d'engagement est la seule phase **sans boucle de régulation active**. Les efforts appliqués par cage reposent entièrement sur des **presets définis par l'expérience de l'opérateur laminateur**.

Or :

- Plusieurs équipes se succèdent sur la ligne (rotations 3x8 ou 4x8)
- Les niveaux d'expérience varient fortement d'un laminateur à l'autre
- La présence régulière d'**intérimaires** accentue cette variabilité
- Il n'existe pas de base de connaissance formalisée pour définir les presets optimaux

La conséquence directe est une **forte variabilité des presets d'entrée**, entraînant une variabilité du produit en sortie.

---

## 1.5 Enjeux

| Axe | Enjeu |
|-----|-------|
| **Qualité** | Réduire les non-conformités sur les têtes de bande |
| **Efficacité** | Réduire les chutes matière en début de bobine |
| **Standardisation** | Réduire la dépendance à l'expérience individuelle des opérateurs |
| **Industrialisation** | Fournir un outil objectif et répétable de définition des presets |
