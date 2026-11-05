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
> - **Ce dépôt** (Valentin Périès) : notebooks d’expérimentation, monitoring MLflow, pipeline data, modèle IA et évaluation refaite.
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
- **WildAIprint** est un modèle de vision par ordinateur qui classe des photos d’empreintes animales en 13 espèces.
- Le modèle retenu par l’équipe (ResNet50, `model.keras`) est servi par l’API Flask (route `/predict`) du projet compagnon *WildAIprintApp*. Le modèle repris en novembre 2026 n’y est pas encore branché.
- Ce dépôt se concentre sur la dimension **IA / data engineering** : nettoyage du dataset, expérimentations de modélisation, évaluation et export des artefacts d’inférence.
- **Chiffre à retenir : 48 % de bonnes réponses sur 104 photos jamais vues** (au hasard : 8 %), avec le modèle repris en novembre 2026 : des réseaux pré-entraînés gelés et une régression logistique par-dessus. Le ResNet50 de l’équipe, ajusté sur le même jeu, fait 26 % sur les mêmes photos. Avec 250 photos d’origine, il faisait déjà 26 %, sur 38 photos de test. Les 83 % annoncés au départ venaient d’une fuite de données dans la séparation entre entraînement et validation. Le détail est dans [Résultats & évaluation](#resultats).
- Le dépôt GitLab de l’équipe (application et CI) : [gitlab.com/yasmine-sayad-group/wildaiprintapp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp).
- Contenu du dépôt :
  - sept notebooks : transfert d’apprentissage ResNet50, CNN from scratch avec MLflow, trois notebooks d’évaluation refaite en octobre 2026, et deux notebooks de sondes linéaires (le modèle repris) en novembre 2026,
  - cinq fichiers `resultats_*.json` avec les mesures de l’évaluation refaite et du modèle repris,
  - `fetch_inat.py` et `build_dataset.py` pour reconstruire le jeu agrandi, et `inat_attributions.csv` pour les crédits des photos iNaturalist,
  - `requirements-sondes.txt` pour les deux notebooks de sondes.
- `model.keras` et `class_names.json` sont produits par `pretrained_cnn_model.ipynb`. Ils ne sont pas versionnés ici. `model.keras` est dans le dépôt de l’application, via Git LFS.

### <a id="contexte"></a>Contexte pédagogique
- Projet mené en équipe dans le cadre de la formation **Simplon x Microsoft – Développeur IA**.
- Objectif pédagogique : concevoir, entraîner et déployer un pipeline de Deep Learning complet de bout en bout (data engineering, fine-tuning, tracking d’expériences, conteneurisation).
- Le modèle est entraîné sur 250 photos d’origine d’empreintes, soit 1 500 images après augmentation. Il est intégré dans une API Flask conteneurisée (Docker Compose) du projet compagnon.

### <a id="equipe"></a>Équipe & attribution des contributions
Ce projet est le fruit d’un travail d'équipe réunissant 4 développeurs IA :

| Contributeur | Profil GitHub | Rôles & Contributions principales |
|---|---|---|
| **Yasmine Sayad** | [@YasmineSAYAD](https://github.com/YasmineSAYAD) | **Conception & entraînement du modèle ResNet50 retenu pour la production** (Transfer Learning & Fine-Tuning en 2 phases, meilleure accuracy de validation à 0,83). Pilotage du dépôt applicatif principal. |
| **Valentin Périès** | [@Rateur](https://github.com/Rateur) | **Data engineering & pipeline d’expérimentation** : nettoyage automatique et déduplication MD5 du dataset, modélisation CNN custom avec suivi des runs sous MLflow (`modeling.ipynb`), packaging des artefacts (`model.keras`, `class_names.json`) et intégration de l’inférence locale Flask. Évaluation refaite, jeu agrandi, puis reprise du modèle avec des sondes linéaires (octobre et novembre 2026). |
| **Valentin Phan** | [@ValentinPhan](https://github.com/ValentinPhan) | Exploration des hyperparamètres, tests d'augmentation de données et évaluation comparative des métriques. |
| **Brunel** | [@Brunel-ops](https://github.com/Brunel-ops) | Préparation des jeux de données, tests de robustesse et benchmarking des temps d'inférence. |

> 📌 **Précision d'attribution** : Plusieurs architectures ont été expérimentées en parallèle par les membres de l’équipe. Le modèle final sélectionné pour l’application web est l'architecture **ResNet50 développée par Yasmine Sayad** (`pretrained_cnn_model.ipynb`). Le présent dépôt personnel documente les notebooks d’entraînement, l'instrumentation MLflow et les étapes de data engineering associées. L’évaluation refaite en octobre 2026 (`split_par_photo.ipynb`, `split_par_photo_preprocess.ipynb` et `split_par_photo_v2.ipynb`) et le modèle repris en novembre 2026 (`sondes_lineaires.ipynb` et `sondes_tour2.ipynb`) sont de Valentin Périès.

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

- **Suivi des expériences** : MLflow (autolog activé dans `modeling.ipynb`, pour le premier CNN uniquement).
- **Traitement d’images** : Pillow pour le nettoyage, l’audit d’intégrité et l’empreinte visuelle dHash ; couches Keras pour l’augmentation à la volée.
- **Évaluation** : scikit-learn (exactitude, F1 macro, rapport de classification, matrice de confusion) et intervalles à 95 % par bootstrap avec NumPy.
- **Modèle repris** : PyTorch, torchvision, transformers et scikit-learn (`requirements-sondes.txt`). Réseaux pré-entraînés gelés testés : ResNet50, ConvNeXt-Base, DINOv2, CLIP ViT-B/16, SigLIP-Base.
- **Export** : `model.keras` et `class_names.json` pour l’API Flask de *WildAIprintApp*.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="dataset"></a>Dataset & préparation

> Le dossier `dataset/` n’est plus distribué. Les photos viennent du web, avec des droits inconnus, et ont été retirées de l’historique du dépôt. Pour relancer les notebooks, il faut fournir son propre jeu de données (voir [Installation](#installation)). Les 465 photos iNaturalist du jeu agrandi ne sont pas non plus dans le dépôt : `fetch_inat.py` les retélécharge.

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
- 250 photos d’origine, 1 500 images après augmentation :
  - suppression des fichiers corrompus,
  - suppression des copies exactes par hachage MD5,
  - 5 variantes par photo (luminosité, miroir, bruit, rotation, zoom), soit 250 photos d’origine et 1 250 variantes.
- Les labels sont inférés directement depuis la structure des répertoires (`image_dataset_from_directory`).
- L’augmentation en ligne (RandomFlip, RandomZoom, RandomBrightness…) s’ajoute à l’augmentation hors ligne pendant l’entraînement.

| Espèce | Photos d’origine | Images après augmentation |
|--------|------------------|---------------------------|
| Castor | 16 | 96 |
| Chat | 18 | 108 |
| Chien | 24 | 144 |
| Coyote | 21 | 126 |
| Écureuil | 19 | 114 |
| Lapin | 11 | 66 |
| Loup | 18 | 108 |
| Lynx | 24 | 144 |
| Ours | 22 | 132 |
| Puma | 22 | 132 |
| Rat | 10 | 60 |
| Raton laveur | 23 | 138 |
| Renard | 22 | 132 |
| **Total** | **250** | **1 500** |

Deux séparations ont été utilisées, avec la graine 12 et des lots de 16 :
- **Évaluation d’origine** : 80 % entraînement, 20 % validation, faite sur les 1 500 images (1 200 et 300). Les variantes d’une même photo se retrouvent des deux côtés. C’est la source de la fuite décrite dans [Résultats](#resultats).
- **Évaluation refaite** : 70 % entraînement, 15 % validation, 15 % test, par photo d’origine et avant l’augmentation. Cela donne 1 044 images d’entraînement (174 photos et leurs variantes), 38 photos de validation et 38 photos de test.

**Jeu agrandi** (`split_par_photo_v2.ipynb`) : 715 photos d’origine, 55 par espèce, contre 250. Aux 250 photos du projet s’ajoutent 465 photos d’empreintes prises sur iNaturalist, marquées « empreinte », sous licence libre (CC0 : 9, CC BY : 50, CC BY-NC : 406) et triées à la main. La séparation est la même que pour l’évaluation refaite (70 / 15 / 15 par photo d’origine, variantes en entraînement seulement), avec les mêmes cinq variantes. Chaque photo garde son auteur et sa licence dans `inat_attributions.csv`.

Les photos de la galerie viennent de Wikimedia Commons. Ce sont des photos d’animaux, pour illustrer. Elles ne font pas partie du jeu d’entraînement.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="architecture"></a>Architecture IA

Le modèle retenu pour l'application finale repose sur un réseau **ResNet50** pré-entraîné (développé par Yasmine Sayad) :
- **Backbone** : ResNet50 pré-entraîné sur ImageNet (`include_top=False`).
- **Entrée** : images RGB redimensionnées en 256×256. Le modèle reçoit des pixels bruts de 0 à 255, sans `preprocess_input`. Augmentation à la volée : miroir, rotation, zoom, translation, luminosité, bruit gaussien.
- **Tête personnalisée** :
  - `GlobalAveragePooling2D`,
  - `Dropout(0.5)` + `Dense(128, relu)` + `Dropout(0.3)`,
  - `Dense(num_classes, softmax)` pour la classification multiclasse (13 classes).
- **Optimisation en deux phases** :
  - Phase 1 : backbone gelé, entraînement de la tête seule (`Adam`, `lr=1e-3`, 10 époques).
  - Phase 2 : fine-tuning avec dégel des 30 dernières couches de ResNet50 (`lr=1e-5`, 20 époques, callback `EarlyStopping` avec patience 10).
- **Suivi des métriques** : accuracy, loss, precision, recall, F1-score (macro) et matrice de confusion.
- **Export** : sauvegarde des poids dans `model.keras` et de l’ordre des classes dans `class_names.json`.
- **Limite connue** : ResNet50 attend des images centrées sur la moyenne d’ImageNet. Ce prétraitement a été testé ensuite, sans gain (voir [Résultats](#resultats)).
- **Modèle repris** (novembre 2026) : une autre méthode, décrite dans [Résultats, point 5](#resultats). Il n’est pas encore branché dans l’application, qui utilise toujours ce ResNet50.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="notebooks"></a>Notebooks & pipeline

| Notebook | Contenu & Auteur principal | Points clés |
|----------|---------------------------|-------------|
| `pretrained_cnn_model.ipynb` | Fine-tuning ResNet50 *(Yasmine Sayad)* | Pipeline d’entraînement en deux phases (gel puis dégel des 30 dernières couches), courbes d'apprentissage, 83 % en validation (séparation avec fuite), export du modèle retenu en production (`model.keras`) |
| `modeling.ipynb` | CNN custom from scratch + MLflow *(Valentin Périès)* | Nettoyage/augmentation du dataset, déduplication MD5, équilibrage des classes (`compute_class_weight`), scheduler `ReduceLROnPlateau`, monitoring des runs sous `mlflow ui`. Trois blocs de convolution (32, 64, 128). Plafond à 18 % en validation |
| `split_par_photo.ipynb` | Évaluation refaite par photo d’origine *(Valentin Périès, octobre 2026)* | Même architecture et même recette que `pretrained_cnn_model.ipynb`, modèle réentraîné. Rattache chaque variante à sa photo, regroupe les photos presque identiques (dHash), sépare par groupe en 70 / 15 / 15, utilise le test une seule fois, intervalles à 95 % par bootstrap. Écrit `resultats_split_par_photo.json` |
| `split_par_photo_preprocess.ipynb` | Piste 1 : `preprocess_input` *(Valentin Périès, octobre 2026)* | Même séparation, même test, une seule ligne en plus : `tf.keras.applications.resnet50.preprocess_input`. Écrit `resultats_split_par_photo_preprocess.json` |
| `split_par_photo_v2.ipynb` | Jeu agrandi : 715 photos d’origine *(Valentin Périès, octobre 2026)* | Même séparation (par photo d’origine, 70 / 15 / 15, variantes en entraînement seulement), même architecture et même recette, graine 12. Les 250 photos du projet et 465 photos iNaturalist, 104 photos de test. Écrit `resultats_split_par_photo_v2.json` |
| `sondes_lineaires.ipynb` | Le modèle repris, tour 1 *(Valentin Périès, novembre 2026)* | Caractéristiques de réseaux pré-entraînés gelés (ResNet50, ConvNeXt-Base, DINOv2-Base, CLIP ViT-B/16, SigLIP-Base), chacun avec son prétraitement, et une régression logistique par-dessus. Même jeu, même séparation, même graine. Réseau et réglage choisis sur la validation seulement : DINOv2-Base en tête (40 %). Test : 37,5 %. Écrit `resultats_sondes.json` |
| `sondes_tour2.ipynb` | Le modèle repris, tour 2 *(Valentin Périès, novembre 2026)* | DINOv2-Large, et DINOv2 avec la moyenne des zones de l’image, avec ou sans les variantes d’entraînement. DINOv2-Large en tête en validation (41,9 %). Test : 48 %. Écrit `resultats_sondes_tour2.json` |

Étapes de l’entraînement d’origine (`pretrained_cnn_model.ipynb`, `modeling.ipynb`) :
1. Chargement du dataset avec `image_dataset_from_directory` (split 80/20, batch 16, graine 12).
2. Augmentation à la volée (couches Keras de preprocessing).
3. Entraînement, avec validation sur les 20 % d’images mises de côté. Il n’y a pas de validation croisée.
4. Évaluation (courbes loss/accuracy, rapport de classification, matrice de confusion).
5. Export des artefacts pour l’API Flask de *WildAIprintApp* (`pretrained_cnn_model.ipynb`).

Étapes de l’évaluation refaite (`split_par_photo.ipynb`, `split_par_photo_preprocess.ipynb`, `split_par_photo_v2.ipynb`) :
1. Rattachement de chaque variante à sa photo d’origine.
2. Regroupement des photos d’origine presque identiques.
3. Séparation par groupe, espèce par espèce, avant l’augmentation.
4. Entraînement avec la même recette que le modèle retenu.
5. Mesure unique sur le jeu de test, avec intervalle à 95 %.

Étapes du modèle repris (`sondes_lineaires.ipynb`, `sondes_tour2.ipynb`) :
1. Extraction des caractéristiques de chaque photo avec un réseau pré-entraîné gelé, et son prétraitement.
2. Entraînement d’une régression logistique sur ces caractéristiques.
3. Choix du réseau et du réglage sur la validation seulement.
4. Mesure sur le jeu de test, une fois par tour.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="resultats"></a>Résultats & évaluation

| Évaluation | Séparation | Évaluée sur | Exactitude | F1 macro |
|------------|------------|-------------|------------|----------|
| Modèle retenu, évaluation d’origine | 80 / 20 sur 1 500 images (avec fuite) | 300 images de validation | 83 % | 0,83 |
| Évaluation refaite | 70 / 15 / 15 par photo d’origine | 38 photos de test | 26 % (13 à 39 %) | 0,26 (0,11 à 0,33) |
| Piste 1 : `preprocess_input` | idem | les mêmes 38 photos de test | 24 % (11 à 37 %) | 0,19 (0,07 à 0,26) |
| Jeu agrandi : 715 photos d’origine | 70 / 15 / 15 par photo d’origine | 104 photos de test (8 par espèce) | 26 % (18 à 35 %) | 0,24 (0,16 à 0,31) |
| Modèle repris, tour 1 : DINOv2-Base gelé + régression logistique | idem | les mêmes 104 photos de test | 37,5 % (28 à 47 %) | 0,38 |
| **Modèle repris, tour 2 : DINOv2-Large gelé + régression logistique** | idem | les mêmes 104 photos de test | **48 % (38 à 58 %)** | **0,48 (0,38 à 0,56)** |

Les intervalles sont à 95 %, par bootstrap (2 000 tirages). Au hasard, sur 13 espèces, l’exactitude serait de 8 %. Les trois dernières lignes portent sur les mêmes 104 photos de test.

### 1. Modèle retenu : 83 % en validation
Le ResNet50 de `pretrained_cnn_model.ipynb` obtient 83 % d’exactitude et un F1 macro de 0,83 sur 300 images de validation.

Ce score est trop optimiste, à cause d’une fuite de données :
- Chaque photo existe en six versions : l’originale et cinq variantes.
- La séparation 80 / 20 était faite sur les 1 500 images mélangées.
- Une photo pouvait donc être en entraînement, et sa variante en miroir en validation.
- Le modèle avait déjà vu, sous une autre forme, une partie de ce qu’on lui demandait de reconnaître.

Les 83 % mesurent en partie la mémoire des photos. Ils ne mesurent pas la reconnaissance d’une empreinte nouvelle.

### 2. Évaluation refaite : 26 % sur des photos jamais vues
`split_par_photo.ipynb` garde la même architecture et la même recette, et réentraîne le modèle. Seule la séparation change :
1. chaque variante est rattachée à sa photo d’origine ;
2. les photos d’origine presque identiques sont regroupées (empreinte visuelle dHash, 6 bits d’écart ou moins) ;
3. la séparation se fait par groupe, espèce par espèce, avant l’augmentation : 70 % entraînement, 15 % validation, 15 % test ;
4. les variantes ne vont qu’en entraînement ;
5. le test ne sert qu’une fois, à la fin.

Résultat sur 38 photos de test jamais vues :
- **26 %** de bonnes réponses (intervalle à 95 % : 13 % à 39 %),
- F1 macro de **0,26** (0,11 à 0,33),
- 8 % au hasard.

Le notebook n’a trouvé aucune paire de photos d’origine presque identiques. La fuite venait donc seulement de l’augmentation faite avant la séparation.

Les courbes montrent un écart net. L’exactitude d’entraînement monte vers 70 %. Celle de validation ne dépasse jamais 35 %. Le modèle apprend les photos d’entraînement et généralise mal. Chaque espèce n’a que 6 à 17 photos d’origine pour apprendre.

Les scores par espèce ne sont pas cités : le test compte 2 à 4 photos par espèce, c’est trop peu.

### 3. Piste 1 : `preprocess_input`, 24 %
ResNet50 attend des images centrées sur la moyenne d’ImageNet. Le modèle d’origine recevait des pixels bruts de 0 à 255. `split_par_photo_preprocess.ipynb` ajoute une seule ligne, `preprocess_input`, avec la même séparation et le même test. La piste était annoncée dans `split_par_photo.ipynb` avant d’être lancée.

Résultat sur les mêmes 38 photos de test :
- **24 %** de bonnes réponses (11 % à 37 %),
- F1 macro de **0,19** (0,07 à 0,26).

Les intervalles se recouvrent presque entièrement : aucun gain mesurable. L’exactitude d’entraînement monte vers 70 à 75 %, la validation reste sous 30 %.

### 4. Presque trois fois plus de photos : aucun gain visible
Après la première évaluation, le manque de photos semblait le premier frein : 10 à 24 photos d’origine par espèce. `split_par_photo_v2.ipynb` teste cette idée avec un jeu agrandi :
- **715 photos d’origine**, 55 par espèce, contre 250 ;
- les 250 photos du projet, plus **465 photos d’empreintes prises sur iNaturalist**, marquées « empreinte » et triées à la main ;
- licences libres : CC0 (9), CC BY (50), CC BY-NC (406) ;
- l’auteur et la licence de chaque photo sont dans `inat_attributions.csv` ; 406 photos sont en CC BY-NC : le jeu agrandi ne peut servir qu’à un usage non commercial.

Le reste ne change pas : séparation par photo d’origine (70 / 15 / 15), variantes en entraînement seulement, même architecture, même recette, mêmes cinq variantes. Le modèle est réentraîné une fois (graine 12), sur carte graphique.

Résultat sur 104 photos de test jamais vues (8 par espèce) :
- **26 %** de bonnes réponses (18 % à 35 %),
- F1 macro de **0,24** (0,16 à 0,31),
- 8 % au hasard.

Par source : 25 % sur les 48 photos d’origine du projet (13 % à 38 %), 27 % sur les 56 photos iNaturalist (16 % à 39 %). Ces deux scores ne se distinguent pas.

Le contrôle des quasi-doublons (dHash) a signalé deux paires de photos d’espèces différentes. Vérifiées à l’œil, ce sont des photos différentes, peu détaillées (neige, sol uniforme).

Les deux tests (38 puis 104 photos) ne sont pas les mêmes, et leurs intervalles se recouvrent : presque trois fois plus de photos n’apportent aucun gain visible, au plus quelques points. La mesure est seulement plus précise : 18 à 35 % au lieu de 13 à 39 %.

Une limite de la recette, la même qu’à l’origine : l’arrêt anticipé (`EarlyStopping`, `restore_best_weights`) garde les poids de la plus faible perte de validation. Ici, ce sont ceux de la première passe de fine-tuning : perte de validation 2,39 (2,56 au hasard), justesse de validation 20 %, alors qu’elle montait ensuite vers 30 %. Le modèle évalué est donc peu entraîné. Le nombre de photos n’était pas le seul frein. La section suivante change de méthode. Un seul entraînement : l’écart d’un entraînement à l’autre n’est pas mesuré.

### 5. Le modèle repris : 48 %
Après le jeu agrandi, Valentin Périès a repris le modèle avec une autre méthode (`sondes_lineaires.ipynb`, puis `sondes_tour2.ipynb`, novembre 2026). Au lieu d’ajuster le ResNet50 sur des pixels bruts, il extrait les caractéristiques de réseaux pré-entraînés gelés, chacun avec son propre prétraitement. Il entraîne ensuite dessus une régression logistique : une « sonde linéaire ».

Ce qui ne change pas :
- le même jeu (715 photos d’origine), la même séparation par photo d’origine, la même graine ;
- le choix du réseau et du réglage se fait **sur la validation seulement** ;
- le test ne sert qu’une fois par tour.

**Tour 1** (`sondes_lineaires.ipynb`). Cinq candidats : ResNet50, ConvNeXt-Base, DINOv2-Base, CLIP ViT-B/16, SigLIP-Base. DINOv2-Base arrive en tête sur la validation (40 %). Sur 104 photos de test :
- **37,5 %** de bonnes réponses (intervalle : 28 % à 47 %),
- F1 macro de **0,38**.

**Tour 2** (`sondes_tour2.ipynb`). DINOv2-Large, et DINOv2 avec la moyenne des zones de l’image, avec ou sans les variantes d’entraînement. DINOv2-Large arrive en tête sur la validation (41,9 %). Plusieurs réglages sont à égalité : le premier, dans l’ordre fixé d’avance, est retenu. Sur les mêmes 104 photos de test :
- **48 %** de bonnes réponses (intervalle : 38 % à 58 %),
- F1 macro de **0,48** (0,38 à 0,56),
- 8 % au hasard.

Par source : 48 % sur les 48 photos du projet (33 % à 63 %), 48 % sur les 56 photos iNaturalist (36 % à 61 %).

Les trois scores (26 % pour le ResNet50 ajusté, 37,5 % et 48 % pour le modèle repris) sont mesurés sur les mêmes 104 photos de test : la comparaison tient. Le test a servi deux fois, une fois par tour. Les deux résultats sont publiés.

Limites :
- un seul entraînement : l’écart d’un entraînement à l’autre n’est pas mesuré ;
- le test reste petit : 8 photos par espèce ;
- l’application Flask utilise encore l’ancien modèle (`model.keras`), pas le nouveau.

Fichiers : `sondes_lineaires.ipynb`, `sondes_tour2.ipynb`, `resultats_sondes.json`, `resultats_sondes_tour2.json` et `requirements-sondes.txt` (PyTorch, torchvision, transformers, scikit-learn).

### Conclusion
- Le modèle repris donne 48 % sur 104 photos de test jamais vues (38 % à 58 %), contre 8 % au hasard. C’est le meilleur résultat mesuré ici.
- Le ResNet50 ajusté de l’équipe donne 26 % sur les mêmes photos (18 % à 35 %), et déjà 26 % sur 38 photos avec 250 photos d’origine. Les intervalles de 26 % et de 48 % ne se recouvrent pas. Même jeu, même séparation, même graine : seule la méthode change.
- Les 83 % annoncés au départ venaient d’une fuite de données. Ce chiffre ne doit pas être cité comme la précision du modèle.
- Les trois mesures refaites du ResNet50 (26 %, 24 %, 26 %) restent dans leurs marges d’erreur. Aucun écart n’est établi entre elles.
- Ajouter des photos n’a pas suffi. L’arrêt anticipé sur la perte de validation a gardé, avec la recette ResNet50, un modèle peu entraîné.
- Limites : un seul entraînement par notebook, un test de 8 photos par espèce, et l’application qui utilise encore l’ancien modèle.

### Prochaines étapes
1. Recadrer l’empreinte avant de la classer.
2. Brancher le nouveau modèle dans l’application Flask.
3. Mesurer par validation croisée par groupes (`StratifiedGroupKFold`). Ce n’est pas encore fait. Elle donnerait une mesure plus stable qu’un seul test.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="installation"></a>Installation & prise en main

### 1. Prérequis
- Python **3.10+** (environnement virtuel recommandé). Les deux premiers notebooks d’octobre 2026 ont tourné sous Python 3.13.
- Les deux premiers notebooks d’octobre 2026 n’ont pas besoin de carte graphique : le processeur suffit, environ une heure chacun. `split_par_photo_v2.ipynb` a tourné sur carte graphique. Durée sur processeur : À confirmer. Matériel et durée de `sondes_lineaires.ipynb` et `sondes_tour2.ipynb` : À confirmer.
- Un jeu de données à fournir soi-même (étape 3).

### 2. Récupérer les notebooks et installer l’environnement
```bash
git clone https://github.com/Rateur/WildAIprint-Modele-CNN.git
cd WildAIprint-Modele-CNN
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```
`jupyter lab` ouvre l’interface dans le navigateur. Ouvrez ensuite le notebook voulu.

Pour `sondes_lineaires.ipynb` et `sondes_tour2.ipynb` : `pip install -r requirements-sondes.txt` (PyTorch, torchvision, transformers, scikit-learn).

### 3. Fournir son jeu de données
Le dossier `dataset/` n’est pas dans le dépôt. Créez-le à la racine, avec un sous-dossier par espèce et vos photos dedans : `dataset/<espèce>/*.jpg`.

Le projet utilisait 13 dossiers : `Castor`, `Chat`, `Chien`, `Coyote`, `Ecureuil`, `Lapin`, `Loup`, `Lynx`, `Ours`, `Puma`, `Rat`, `Raton laveur`, `Renard`.

Les notebooks `split_par_photo*.ipynb` attendent les variantes augmentées dans le même dossier, nommées `aug_bright_`, `aug_flip_`, `aug_noise_`, `aug_rot_` et `aug_zoom_` suivi du nom de la photo d’origine. Pour les créer, lancez une seule fois la cellule « Read and clean data » de `modeling.ipynb`. Elle modifie `dataset/` sur place : elle supprime les images corrompues et les doublons exacts, puis ajoute les variantes. Travaillez sur une copie.

Vos effectifs seront différents de ceux de la section [Dataset](#dataset), donc vos résultats aussi.

### 4. Reconstruire le jeu agrandi
Seulement pour `split_par_photo_v2.ipynb` et les deux notebooks de sondes, qui prennent le même jeu. Les images ne sont pas dans le dépôt : `fetch_inat.py` retélécharge les 465 photos iNaturalist, `build_dataset.py` reconstruit le jeu, avec les mêmes cinq variantes. Les 250 photos du projet restent à fournir (étape 3).
```bash
python fetch_inat.py
python build_dataset.py dataset inat dataset-v2
```
Crédits : les photos iNaturalist appartiennent à leurs auteurs. Chaque auteur et chaque licence (CC0, CC BY, CC BY-NC) sont dans `inat_attributions.csv`.

### 5. Lancer les notebooks
- `modeling.ipynb` : nettoyage, augmentation, premier CNN et suivi MLflow (`mlflow ui`).
- `pretrained_cnn_model.ipynb` : modèle retenu. Il écrit `model.keras` et `class_names.json` dans le dossier courant. Git les ignore.
- `split_par_photo.ipynb` puis `split_par_photo_preprocess.ipynb` : évaluation refaite. Ils écrivent les fichiers `resultats_*.json`.
- `split_par_photo_v2.ipynb` : jeu agrandi, après l’étape 4. Il écrit `resultats_split_par_photo_v2.json`.
- `sondes_lineaires.ipynb` puis `sondes_tour2.ipynb` : le modèle repris, après l’étape 4. Ils écrivent `resultats_sondes.json` et `resultats_sondes_tour2.json`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="structure"></a>Structure du dépôt

```text
.
├── README.md
├── requirements.txt                        # versions qui ont produit les résultats
├── requirements-sondes.txt                 # PyTorch, torchvision, transformers, scikit-learn
├── pretrained_cnn_model.ipynb              # ResNet50, modèle retenu
├── modeling.ipynb                          # nettoyage, augmentation, CNN from scratch, MLflow
├── split_par_photo.ipynb                   # évaluation refaite par photo d’origine
├── split_par_photo_preprocess.ipynb        # piste 1 : preprocess_input
├── split_par_photo_v2.ipynb                # jeu agrandi : 715 photos d’origine
├── sondes_lineaires.ipynb                  # modèle repris, tour 1 : cinq réseaux gelés
├── sondes_tour2.ipynb                      # modèle repris, tour 2 : DINOv2-Large, 48 %
├── fetch_inat.py                           # retélécharge les photos iNaturalist
├── build_dataset.py                        # reconstruit le jeu agrandi
├── inat_attributions.csv                   # auteur et licence de chaque photo iNaturalist
├── resultats_split_par_photo.json
├── resultats_split_par_photo_preprocess.json
├── resultats_split_par_photo_v2.json
├── resultats_sondes.json
├── resultats_sondes_tour2.json
└── dataset/                                # à fournir, ignoré par Git
```

Git ignore aussi `model.keras`, `class_names.json`, `mlruns/` et `outputs/`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="ressources"></a>Ressources & inspirations

- Application WildAIprint (API Flask, front, Docker Compose) : [github.com/Rateur/wildaiprint-App](https://github.com/Rateur/wildaiprint-App).
- Dépôt GitLab de l’équipe : [gitlab.com/yasmine-sayad-group/wildaiprintapp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp).
- ResNet50 pré-entraîné sur ImageNet, chargé avec `tf.keras.applications`.
- Réseaux pré-entraînés gelés du modèle repris : ResNet50, ConvNeXt-Base, DINOv2-Base et DINOv2-Large, CLIP ViT-B/16, SigLIP-Base.
- Photos de la galerie : Wikimedia Commons.
- Photos d’empreintes du jeu agrandi : [iNaturalist](https://www.inaturalist.org), photos sous licence libre. Auteurs et licences dans `inat_attributions.csv`.

<p align="right"><a href="#top">Retour en haut</a></p>
