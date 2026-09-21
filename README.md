<div id="top"></div>

<h1 align="center">
  <img src="https://imgur.com/y9j7iMy.png" alt="WildAIprint logo" width="96" style="vertical-align: middle; margin-right: 12px;">
  WildAIprint – Modèle IA
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Simplon%20x%20Microsoft-D%C3%A9veloppeur%20IA-ee2e5d?style=for-the-badge" alt="Simplon x Microsoft – Développeur IA">
  <img src="https://img.shields.io/github/stars/Rateur/WildAIprint-Modele-CNN.svg?style=for-the-badge&color=ffd700" alt="Étoiles GitHub">
</p>

<p align="center">
  Modèle de classification d’empreintes animales pour la webapp WildAIprint.<br>
  Projet collaboratif réalisé dans le cadre de la formation <strong>Simplon x Microsoft – Développeur IA</strong>.
</p>

> La documentation du projet est répartie sur deux dépôts complémentaires :
> - **Ce dépôt** (Valentin Périès) : notebooks d’expérimentation, monitoring MLflow, pipeline data et modèle IA.
> - **WildAIprint App** (Front/Back) : [https://github.com/Rateur/wildaiprint-App](https://github.com/Rateur/wildaiprint-App)

---

## Sommaire
1. [À propos](#a-propos)  
   1.1. [Pitch & objectifs](#pitch)  
   1.2. [Contexte pédagogique](#contexte)  
   1.3. [Équipe & attribution des contributions](#equipe)  
2. [Technologies & outils](#technologies)  
3. [Dataset & préparation](#dataset)  
4. [Architecture IA](#architecture)  
5. [Notebooks & pipeline](#notebooks)  
6. [Résultats & évaluation](#resultats)  
7. [Installation & prise en main](#installation)  
8. [Structure du dépôt](#structure)  
9. [Ressources & inspirations](#ressources)

---

## <a id="a-propos"></a>À propos

### <a id="pitch"></a>Pitch & objectifs
- **WildAIprint** est un système de vision par ordinateur capable de reconnaître 13 espèces fauniques à partir de photographies d’empreintes animales.
- Il alimente l’API Flask du projet compagnon *WildAIprintApp* pour fournir des prédictions en temps réel sur le terrain.
- Ce dépôt se concentre sur la dimension **IA / data engineering** : nettoyage du dataset, expérimentations de modélisation, évaluation comparative et export des artefacts d’inférence.
- L’application web complète (interface utilisateur & API) est hébergée sur GitLab : [gitlab.com/yasmine-sayad-group/wildaiprintapp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp).
- Livrables clés :
  - `model.keras` (poids du modèle retenu),
  - `class_names.json` (ordre des classes pour l’inférence Flask),
  - deux notebooks documentés couvrant le transfert d’apprentissage ResNet50 et l’expérimentation CNN from scratch avec MLflow.

### <a id="contexte"></a>Contexte pédagogique
- Projet mené en équipe dans le cadre de la formation **Simplon x Microsoft – Développeur IA**.
- Objectif pédagogique : concevoir, entraîner et déployer un pipeline de Deep Learning complet de bout en bout (data engineering, fine-tuning, tracking d’expériences, conteneurisation).
- Le modèle est entraîné sur un jeu de données de ~1 500 images d'empreintes et illustre la mise en production d’un modèle TensorFlow/Keras dans un microservice Flask conteneurisé.

### <a id="equipe"></a>Équipe & attribution des contributions
Ce projet est le fruit d’un travail d'équipe réunissant 4 développeurs IA :

| Contributeur | Profil GitHub | Rôles & Contributions principales |
|---|---|---|
| **Yasmine Sayad** | [@YasmineSAYAD](https://github.com/YasmineSAYAD) | **Conception & entraînement du modèle ResNet50 retenu pour la production** (Transfer Learning & Fine-Tuning en 2 phases, meilleure accuracy de validation à 0,83). Pilotage du dépôt applicatif principal. |
| **Valentin Périès** | [@Rateur](https://github.com/Rateur) | **Data engineering & pipeline d’expérimentation** : nettoyage automatique et déduplication MD5 du dataset, modélisation CNN custom avec suivi des runs sous MLflow (`modeling.ipynb`), packaging des artefacts (`model.keras`, `class_names.json`) et intégration de l’inférence locale Flask. |
| **Valentin Phan** | [@ValentinPhan](https://github.com/ValentinPhan) | Exploration des hyperparamètres, tests d'augmentation de données et évaluation comparative des métriques. |
| **Brunel** | [@Brunel-ops](https://github.com/Brunel-ops) | Préparation des jeux de données, tests de robustesse et benchmarking des temps d'inférence. |

> 📌 **Précision d'attribution** : Plusieurs architectures ont été expérimentées en parallèle par les membres de l’équipe. Le modèle final sélectionné pour l’application web est l'architecture **ResNet50 développée par Yasmine Sayad** (`pretrained_cnn_model.ipynb`). Le présent dépôt personnel documente les notebooks d’entraînement, l'instrumentation MLflow et les étapes de data engineering associées.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="technologies"></a>Technologies & outils

<table align="center">
  <tr>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" height="48"><br>
      <sub><strong>Python 3.10+</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" alt="TensorFlow" height="48"><br>
      <sub><strong>TensorFlow / Keras</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" alt="scikit-learn" height="48"><br>
      <sub><strong>scikit-learn</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="NumPy" height="48"><br>
      <sub><strong>NumPy</strong></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" height="48"><br>
      <sub><strong>Pandas</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matplotlib/matplotlib-original.svg" alt="Matplotlib" height="48"><br>
      <sub><strong>Matplotlib / Seaborn</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="Jupyter" height="48"><br>
      <sub><strong>Jupyter Lab</strong></sub>
    </td>
    <td align="center" width="120">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git" height="48"><br>
      <sub><strong>Git & GitHub</strong></sub>
    </td>
  </tr>
</table>

- **Suivi des expériences** : MLflow (autolog activé dans `modeling.ipynb`, suivi des paramètres et courbes loss/accuracy).
- **Traitement d’images** : Pillow pour le nettoyage et l'audit d'intégrité, couches Keras pour l’augmentation à la volée.
- **Stack déploiement** : export `.keras` + `class_names.json` pour intégration dans l'API Flask de *WildAIprintApp*.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="dataset"></a>Dataset & préparation

- 13 classes d’animaux (empreintes) :

  <table align="center">
    <tr>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/American_Beaver.jpg" alt="Castor" width="90" loading="lazy"><br>
        <sub><strong>Castor</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1200px-Cat_August_2010-4.jpg" alt="Chat" width="90" loading="lazy"><br>
        <sub><strong>Chat</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Huskiesatrest.jpg/1200px-Huskiesatrest.jpg" alt="Chien" width="90" loading="lazy"><br>
        <sub><strong>Chien</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/2009-Coyote-Yosemite.jpg" alt="Coyote" width="90" loading="lazy"><br>
        <sub><strong>Coyote</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Sciuridae.jpg" alt="Écureuil" width="90" loading="lazy"><br>
        <sub><strong>Écureuil</strong></sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/969px-Oryctolagus_cuniculus_Rcdo.jpg" alt="Lapin" width="90" loading="lazy"><br>
        <sub><strong>Lapin</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Eurasian_wolf_2.jpg/1200px-Eurasian_wolf_2.jpg" alt="Loup" width="90" loading="lazy"><br>
        <sub><strong>Loup</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/1f/Lynx_heads_collage.jpg" alt="Lynx" width="90" loading="lazy"><br>
        <sub><strong>Lynx</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Ours_brun_parcanimalierpyrenees_1.jpg" alt="Ours" width="90" loading="lazy"><br>
        <sub><strong>Ours</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Mountain_Lion_in_Glacier_National_Park.jpg/1200px-Mountain_Lion_in_Glacier_National_Park.jpg" alt="Puma" width="90" loading="lazy"><br>
        <sub><strong>Puma</strong></sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Brown_Rat_%28Rattus_norvegicus%29.jpg/1200px-Brown_Rat_%28Rattus_norvegicus%29.jpg" alt="Rat" width="90" loading="lazy"><br>
        <sub><strong>Rat</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Raccoon_in_Central_Park_%2835264%29.jpg/1200px-Raccoon_in_Central_Park_%2835264%29.jpg" alt="Raton laveur" width="90" loading="lazy"><br>
        <sub><strong>Raton laveur</strong></sub>
      </td>
      <td align="center" width="120">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Vulpes_vulpes_ssp_fulvus.jpg/1200px-Vulpes_vulpes_ssp_fulvus.jpg" alt="Renard" width="90" loading="lazy"><br>
        <sub><strong>Renard</strong></sub>
      </td>
      <td align="center" width="120">
        &nbsp;
      </td>
      <td align="center" width="120">
        &nbsp;
      </td>
    </tr>
  </table>
- 1 500 images après nettoyage automatique :
  - suppression des fichiers corrompus,
  - détection et suppression des doublons via hachage MD5,
  - génération d’images augmentées (rotation, symétrie, zoom, bruit, luminosité).
- Les labels sont inférés directement depuis la structure des répertoires (`image_dataset_from_directory`).
- L’augmentation en ligne (RandomFlip, RandomZoom, RandomBrightness…) complète l’enrichissement offline pour améliorer l'invariance et la généralisation.

| Classe | Images | Classe | Images |
|--------|--------|--------|--------|
| Castor | 96 | Ours | 132 |
| Chat | 108 | Puma | 132 |
| Chien | 144 | Rat | 60 |
| Coyote | 126 | Raton laveur | 138 |
| Écureuil | 114 | Renard | 132 |
| Lapin | 66 | Loup | 108 |
| Lynx | 144 | **Total** | **1 500** |

> 📁 Les images sont organisées dans `dataset/<classe>/*.jpg|.png`.  
> Le partitionnement reproductible utilise un split 80% entraînement / 20% validation avec une graine fixe (seed 12, batch 16).

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="architecture"></a>Architecture IA

Le modèle retenu pour l'application finale repose sur un réseau **ResNet50** pré-entraîné (développé par Yasmine Sayad) :
- **Backbone** : ResNet50 pré-entraîné sur ImageNet (`include_top=False`).
- **Entrée** : images RGB redimensionnées en 256×256, normalisées et augmentées à la volée.
- **Tête personnalisée** :
  - `GlobalAveragePooling2D`,
  - `Dropout(0.5)` + `Dense(128, relu)` + `Dropout(0.3)`,
  - `Dense(num_classes, softmax)` pour la classification multiclasse (13 classes).
- **Optimisation en deux phases** :
  - Phase 1 : backbone gelé, entraînement de la tête seule (`Adam`, `lr=1e-3`).
  - Phase 2 : fine-tuning contrôlé avec dégel des 30 dernières couches de ResNet50 (`lr=1e-5`, callback `EarlyStopping`).
- **Suivi des métriques** : accuracy, loss, precision, recall, F1-score (macro) et matrice de confusion.
- **Export** : sauvegarde des poids dans `model.keras` + génération de `class_names.json`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="notebooks"></a>Notebooks & pipeline

| Notebook | Contenu & Auteur principal | Points clés |
|----------|---------------------------|-------------|
| `pretrained_cnn_model.ipynb` | Fine-tuning ResNet50 *(Yasmine Sayad)* | Pipeline d’entraînement en deux phases (gel puis dégel des 30 dernières couches), courbes d'apprentissage, export du modèle retenu en production (`model.keras`) |
| `modeling.ipynb` | CNN custom from scratch + MLflow *(Valentin Périès)* | Nettoyage/augmentation du dataset, déduplication MD5, équilibrage des classes (`compute_class_weight`), scheduler `ReduceLROnPlateau`, monitoring des runs sous `mlflow ui` |

Étapes communes :
1. Chargement du dataset avec `image_dataset_from_directory` (split 80/20, batch 16, graine 12).
2. Prétraitement et augmentation (couches Keras preprocessing).
3. Entraînement et validation croisée.
4. Évaluation approfondie (courbes loss/acc, classification report, matrice de confusion).
5. Export des artefacts pour l'API Flask de *WildAIprintApp*.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="resultats"></a>Résultats & évaluation

- Accuracy de validation du modèle sélectionné : **0,83 (83%)**.
- Courbes d’apprentissage (accuracy & loss) stables et parallèles → bonne capacité de généralisation, absence d'overfitting marqué.
- Classes les plus complexes : Castor, Raton laveur, Chat (proximité morphologique des coussinets et des empreintes digitales).
- Matrice de confusion et rapport de classification visualisables dans les notebooks via Seaborn/Matplotlib.
- Pistes d'amélioration :
  - Enrichir les classes minoritaires (Rat : 60, Lapin : 66) avec des prises de vue complémentaires sur différents substrats (boue, neige, sable).
  - Évaluer d'autres architectures de transfert (EfficientNetV2, ConvNeXt) pour affiner la séparation des classes ambiguës.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="installation"></a>Installation & prise en main

### 1. Prérequis
- Python **3.10+** (environnement virtuel recommandé).
- GPU compatible CUDA 11.x (recommandé pour accélérer le fine-tuning).
- Dépendances : `pip install tensorflow matplotlib seaborn scikit-learn mlflow pillow numpy`.

### 2. Préparation de l’environnement
```bash
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt    # ou installation directe des packages ci-dessus
