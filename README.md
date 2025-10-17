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
  Réalisé dans le cadre de ma formation <strong>Simplon x Microsoft – Développeur IA</strong>.
</p>

---

## Sommaire
1. [À propos](#a-propos)  
   1.1. [Pitch & objectifs](#pitch)  
   1.2. [Contexte pédagogique](#contexte)  
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
- **WildAIprint** est un modèle de vision par ordinateur capable de reconnaître 13 espèces à partir de photos d’empreintes animalières.
- Il alimente l’API Flask du projet compagnon *WildAIprintApp* pour fournir des prédictions en temps réel.
- Ce dépôt se concentre sur la partie **IA / data** : nettoyage du dataset, entraînement, évaluation et export du modèle.
- Livrables clés :
  - `model.keras` (poids entraînés),
  - `class_names.json` (ordre des classes pour l’inférence),
  - deux notebooks reproductibles couvrant les scénarios *from scratch* et transfert d’apprentissage.

### <a id="contexte"></a>Contexte pédagogique
- Projet mené dans le cadre de la formation **Simplon x Microsoft – Développeur IA**.
- Objectif pédagogique : démontrer la maîtrise d’un pipeline de Deep Learning de bout en bout (data engineering, fine-tuning, monitoring).
- Le modèle entraîne un jeu de données propriétaire (~1 500 images) et illustre la mise en production d’un modèle Keras dans un environnement Flask.

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
      <sub><strong>Git & GitLab</strong></sub>
    </td>
  </tr>
</table>

- **Suivi des expériences** : MLflow (autolog activé dans `modeling.ipynb`).
- **Traitement d’images** : Pillow pour le nettoyage, générateurs Keras pour l’augmentation.
- **Stack déploiement** : export `.keras` pour intégration Flask + fichier JSON de mapping classes.

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
  - détection de doublons via hash MD5,
  - génération d’images augmentées (rotation, symétrie, zoom, bruit, luminosité).
- Les labels sont inférés directement depuis la structure des dossiers (`image_dataset_from_directory`).
- L’augmentation en ligne (RandomFlip, RandomZoom, RandomBrightness…) complète l’enrichissement offline pour améliorer la généralisation.

| Classe | Images | Classe | Images |
|--------|--------|--------|--------|
| Castor | 96 | Ours | 132 |
| Chat | 108 | Puma | 132 |
| Chien | 144 | Rat | 60 |
| Coyote | 126 | Raton laveur | 138 |
| Écureuil | 114 | Renard | 132 |
| Lapin | 66 | Loup | 108 |
| Lynx | 144 | **Total** | **1 500** |

> 📁 Les images sont stockées dans `dataset/<classe>/*.jpg|.png`.  
> Une structure cohérente est indispensable pour reproduire l’entraînement (split 80/20 avec graine fixe).

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="architecture"></a>Architecture IA

- **Backbone** : ResNet50 pré-entraîné sur ImageNet (`include_top=False`).
- **Entrée** : images RGB redimensionnées en 256×256, normalisées et augmentées à la volée.
- **Tête personnalisée** :
  - `GlobalAveragePooling2D`,
  - `Dropout(0.5)` + `Dense(128, relu)` + `Dropout(0.3)`,
  - `Dense(num_classes, softmax)` pour la classification multiclasse.
- **Optimisation** :
  - Phase 1 : backbone gelé, entraînement de la tête seulement (`Adam`, `lr=1e-3`).
  - Phase 2 : fine-tuning contrôlé (dégel des 30 dernières couches, `lr=1e-5`, `EarlyStopping`).
- **Suivi des métriques** : accuracy, loss, precision, recall, F1-score (macro) et matrice de confusion.
- **Export** : sauvegarde du modèle Keras + écriture du fichier `class_names.json`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="notebooks"></a>Notebooks & pipeline

| Notebook | Contenu principal | Points clés |
|----------|------------------|-------------|
| `pretrained_cnn_model.ipynb` | Fine-tuning d’un ResNet50 pré-entraîné | Pipeline complet d’entraînement en deux phases, visualisation des courbes, export du modèle |
| `modeling.ipynb` | CNN custom entraîné from scratch + suivi MLflow | Nettoyage/augmentation offline, équilibrage des classes (`compute_class_weight`), scheduler `ReduceLROnPlateau`, lancement automatique de `mlflow ui` |

Étapes communes :
1. Chargement du dataset avec `image_dataset_from_directory` (split 80/20, batch 16, graine 12).
2. Prétraitement et augmentation (Keras preprocessing layers).
3. Entraînement + fine-tuning.
4. Évaluation (courbes, classification report, matrice de confusion).
5. Export des artefacts pour le back-end Flask.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="resultats"></a>Résultats & évaluation

- Accuracy de validation : **0,83**.
- Courbes d’apprentissage (accuracy & loss) stables et parallèles → généralisation satisfaisante, pas de sur-apprentissage observé.
- Classes les plus délicates : Castor, Raton laveur, Chat (empreintes visuellement proches).
- Confusion matrix et classification report disponibles dans les notebooks (visualisations Matplotlib/Seaborn).
- Recommandations :
  - Enrichir les classes minoritaires (Rat, Lapin) avec des prises de vues variées.
  - Tester d’autres backbones (EfficientNet, DenseNet) pour améliorer la robustesse sur les empreintes ambiguës.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="installation"></a>Installation & prise en main

### 1. Prérequis
- Python **3.10+** (environnement virtuel recommandé).
- GPU compatible CUDA 11.x pour accélérer l’entraînement (optionnel mais conseillé).
- `pip install tensorflow matplotlib seaborn scikit-learn mlflow pillow numpy`.

### 2. Préparation de l’environnement
```bash
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt    # si vous générez un fichier de dépendances
```

### 3. Lancer un entraînement
1. Ouvrir le notebook de votre choix (`modeling.ipynb` ou `pretrained_cnn_model.ipynb`) dans Jupyter Lab / VS Code.
2. Adapter `dataset_path` si votre dataset est stocké ailleurs.
3. Exécuter les cellules séquentiellement :
   - le notebook `modeling.ipynb` peut lancer `mlflow ui` automatiquement.
4. Vérifier les courbes et la matrice de confusion.
5. Récupérer `model.keras` & `class_names.json` pour les brancher sur l’API Flask.

### 4. Utilisation côté API Flask
- Charger le modèle Keras (`tf.keras.models.load_model("model.keras")`).
- Utiliser `class_names.json` pour décoder l’entier retourné en label lisible.
- Appliquer les mêmes étapes de prétraitement qu’à l’entraînement (redimensionnement 256×256, normalisation, augmentation optionnelle).

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="structure"></a>Structure du dépôt

```
/
├── .gitignore                 # Ignorer les artefacts lourds et temporaires
├── modeling.ipynb              # CNN personnalisé + suivi MLflow
├── pretrained_cnn_model.ipynb  # Fine-tuning ResNet50
├── dataset/                    # Images d’empreintes (ignorées par Git, à placer localement)
├── model.keras                 # Modèle entraîné (généré après entraînement, hors suivi Git)
└── class_names.json            # Mapping des classes (généré après entraînement, hors suivi Git)
```

<p align="right"><a href="#top">Retour en haut</a></p>

---

### Fichiers ignorés (.gitignore)

Pour alléger le dépôt, le fichier `.gitignore` exclut les dossiers et artefacts volumineux générés pendant les entraînements :

```gitignore
# Données et artefacts lourds
dataset/
model.keras
class_names.json
mlruns/
outputs/

# Environnements et caches
.venv/
env/
venv/
__pycache__/
*.py[cod]
.ipynb_checkpoints/

# Outils & IDE
.DS_Store
.vscode/
.idea/
```

Après avoir mis à jour le `.gitignore`, exécutez les commandes suivantes pour retirer les gros fichiers déjà suivis :

```bash
git rm -r --cached dataset
git rm --cached model.keras class_names.json  # Ignore si ces fichiers n'existent pas encore
git commit -m "Nettoie les artefacts lourds hors Git"
```

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="ressources"></a>Ressources & inspirations
- [Documentation TensorFlow / Keras](https://www.tensorflow.org/api_docs) – couches, callbacks et pipelines d’augmentation.
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html) – suivi des expériences.
- [Guide scikit-learn](https://scikit-learn.org/stable/) – métriques de classification.
- [Simplon.co](https://simplon.co/) – référentiel de la formation Développeur IA.
- Études terrain sur la reconnaissance d’empreintes animales (NatureTracking, iNaturalist) ayant inspiré la composition du dataset.

<p align="right"><a href="#top">Retour en haut</a></p>

---
