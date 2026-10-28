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
- Le modèle retenu est servi par l’API Flask (route `/predict`) du projet compagnon *WildAIprintApp*.
- Ce dépôt se concentre sur la dimension **IA / data engineering** : nettoyage du dataset, expérimentations de modélisation, évaluation et export des artefacts d’inférence.
- **Chiffre à retenir : 26 % de bonnes réponses sur des photos jamais vues** (au hasard : 8 %). Les 83 % annoncés au départ venaient d’une fuite de données dans la séparation entre entraînement et validation. Le détail est dans [Résultats & évaluation](#resultats).
- Le dépôt GitLab de l’équipe (application et CI) : [gitlab.com/yasmine-sayad-group/wildaiprintapp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp).
- Contenu du dépôt :
  - quatre notebooks : transfert d’apprentissage ResNet50, CNN from scratch avec MLflow, et deux notebooks d’évaluation refaite en octobre 2026,
  - deux fichiers `resultats_*.json` avec les mesures de l’évaluation refaite.
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
| **Valentin Périès** | [@Rateur](https://github.com/Rateur) | **Data engineering & pipeline d’expérimentation** : nettoyage automatique et déduplication MD5 du dataset, modélisation CNN custom avec suivi des runs sous MLflow (`modeling.ipynb`), packaging des artefacts (`model.keras`, `class_names.json`) et intégration de l’inférence locale Flask. |
| **Valentin Phan** | [@ValentinPhan](https://github.com/ValentinPhan) | Exploration des hyperparamètres, tests d'augmentation de données et évaluation comparative des métriques. |
| **Brunel** | [@Brunel-ops](https://github.com/Brunel-ops) | Préparation des jeux de données, tests de robustesse et benchmarking des temps d'inférence. |

> 📌 **Précision d'attribution** : Plusieurs architectures ont été expérimentées en parallèle par les membres de l’équipe. Le modèle final sélectionné pour l’application web est l'architecture **ResNet50 développée par Yasmine Sayad** (`pretrained_cnn_model.ipynb`). Le présent dépôt personnel documente les notebooks d’entraînement, l'instrumentation MLflow et les étapes de data engineering associées. L’évaluation refaite en octobre 2026 (`split_par_photo.ipynb` et `split_par_photo_preprocess.ipynb`) est de Valentin Périès.

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
- **Export** : `model.keras` et `class_names.json` pour l’API Flask de *WildAIprintApp*.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="dataset"></a>Dataset & préparation

> Le dossier `dataset/` n’est plus distribué. Les photos viennent du web, avec des droits inconnus, et ont été retirées de l’historique du dépôt. Pour relancer les notebooks, il faut fournir son propre jeu de données (voir [Installation](#installation)).

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

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="notebooks"></a>Notebooks & pipeline

| Notebook | Contenu & Auteur principal | Points clés |
|----------|---------------------------|-------------|
| `pretrained_cnn_model.ipynb` | Fine-tuning ResNet50 *(Yasmine Sayad)* | Pipeline d’entraînement en deux phases (gel puis dégel des 30 dernières couches), courbes d'apprentissage, 83 % en validation (séparation avec fuite), export du modèle retenu en production (`model.keras`) |
| `modeling.ipynb` | CNN custom from scratch + MLflow *(Valentin Périès)* | Nettoyage/augmentation du dataset, déduplication MD5, équilibrage des classes (`compute_class_weight`), scheduler `ReduceLROnPlateau`, monitoring des runs sous `mlflow ui`. Trois blocs de convolution (32, 64, 128). Plafond à 18 % en validation |
| `split_par_photo.ipynb` | Évaluation refaite par photo d’origine *(Valentin Périès, octobre 2026)* | Même modèle et même recette que `pretrained_cnn_model.ipynb`. Rattache chaque variante à sa photo, regroupe les photos presque identiques (dHash), sépare par groupe en 70 / 15 / 15, utilise le test une seule fois, intervalles à 95 % par bootstrap. Écrit `resultats_split_par_photo.json` |
| `split_par_photo_preprocess.ipynb` | Piste 1 : `preprocess_input` *(Valentin Périès, octobre 2026)* | Même séparation, même test, une seule ligne en plus : `tf.keras.applications.resnet50.preprocess_input`. Écrit `resultats_split_par_photo_preprocess.json` |

Étapes de l’entraînement d’origine (`pretrained_cnn_model.ipynb`, `modeling.ipynb`) :
1. Chargement du dataset avec `image_dataset_from_directory` (split 80/20, batch 16, graine 12).
2. Augmentation à la volée (couches Keras de preprocessing).
3. Entraînement, avec validation sur les 20 % d’images mises de côté. Il n’y a pas de validation croisée.
4. Évaluation (courbes loss/accuracy, rapport de classification, matrice de confusion).
5. Export des artefacts pour l’API Flask de *WildAIprintApp* (`pretrained_cnn_model.ipynb`).

Étapes de l’évaluation refaite (`split_par_photo.ipynb`, `split_par_photo_preprocess.ipynb`) :
1. Rattachement de chaque variante à sa photo d’origine.
2. Regroupement des photos d’origine presque identiques.
3. Séparation par groupe, espèce par espèce, avant l’augmentation.
4. Entraînement avec la même recette que le modèle retenu.
5. Mesure unique sur le jeu de test, avec intervalle à 95 %.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="resultats"></a>Résultats & évaluation

| Évaluation | Séparation | Évaluée sur | Exactitude | F1 macro |
|------------|------------|-------------|------------|----------|
| Modèle retenu, évaluation d’origine | 80 / 20 sur 1 500 images (avec fuite) | 300 images de validation | 83 % | 0,83 |
| Évaluation refaite | 70 / 15 / 15 par photo d’origine | 38 photos de test | 26 % (13 à 39 %) | 0,26 (0,11 à 0,33) |
| Piste 1 : `preprocess_input` | idem | les mêmes 38 photos de test | 24 % (11 à 37 %) | 0,19 (0,07 à 0,26) |

Les intervalles sont à 95 %, par bootstrap (2 000 tirages). Au hasard, sur 13 espèces, l’exactitude serait de 8 %.

### 1. Modèle retenu : 83 % en validation
Le ResNet50 de `pretrained_cnn_model.ipynb` obtient 83 % d’exactitude et un F1 macro de 0,83 sur 300 images de validation.

Ce score est trop optimiste, à cause d’une fuite de données :
- Chaque photo existe en six versions : l’originale et cinq variantes.
- La séparation 80 / 20 était faite sur les 1 500 images mélangées.
- Une photo pouvait donc être en entraînement, et sa variante en miroir en validation.
- Le modèle avait déjà vu, sous une autre forme, une partie de ce qu’on lui demandait de reconnaître.

Les 83 % mesurent en partie la mémoire des photos. Ils ne mesurent pas la reconnaissance d’une empreinte nouvelle.

### 2. Évaluation refaite : 26 % sur des photos jamais vues
`split_par_photo.ipynb` garde le même modèle et la même recette. Seule la séparation change :
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

### Conclusion
- Sur des photos jamais vues, le modèle donne 26 %, avec une marge de 13 % à 39 %. C’est au-dessus du hasard (8 %) et très loin de 83 %. Le chiffre de 83 % ne doit pas être cité comme la précision du modèle.
- Le test compte 38 photos. L’écart entre 26 % et 24 % est dans la marge d’erreur.
- Le premier levier est le nombre de photos, pas l’architecture.

### Prochaines étapes
1. Collecter plus de photos d’origine : une cinquantaine par espèce au moins, contre 10 à 24 aujourd’hui. Commencer par Rat (10) et Lapin (11), sur différents substrats (boue, neige, sable).
2. Mesurer par validation croisée par groupes (`StratifiedGroupKFold`). Ce n’est pas encore fait. Elle donnerait une mesure plus stable qu’un seul test de 38 photos.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="installation"></a>Installation & prise en main

### 1. Prérequis
- Python **3.10+** (environnement virtuel recommandé). Les deux notebooks d’octobre 2026 ont tourné sous Python 3.13.
- Pas de carte graphique nécessaire : le processeur suffit. Comptez environ une heure par notebook.
- Un jeu de données à fournir soi-même (étape 3).

### 2. Récupérer les notebooks et installer l’environnement
```bash
git clone https://github.com/Rateur/WildAIprint-Modele-CNN.git
cd WildAIprint-Modele-CNN
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install --upgrade pip
pip install jupyterlab tensorflow matplotlib seaborn scikit-learn mlflow pillow numpy pandas
jupyter lab
```
`jupyter lab` ouvre l’interface dans le navigateur. Ouvrez ensuite le notebook voulu.

### 3. Fournir son jeu de données
Le dossier `dataset/` n’est pas dans le dépôt. Créez-le à la racine, avec un sous-dossier par espèce et vos photos dedans : `dataset/<espèce>/*.jpg`.

Le projet utilisait 13 dossiers : `Castor`, `Chat`, `Chien`, `Coyote`, `Ecureuil`, `Lapin`, `Loup`, `Lynx`, `Ours`, `Puma`, `Rat`, `Raton laveur`, `Renard`.

Les notebooks `split_par_photo*.ipynb` attendent les variantes augmentées dans le même dossier, nommées `aug_bright_`, `aug_flip_`, `aug_noise_`, `aug_rot_` et `aug_zoom_` suivi du nom de la photo d’origine. Pour les créer, lancez une seule fois la cellule « Read and clean data » de `modeling.ipynb`. Elle modifie `dataset/` sur place : elle supprime les images corrompues et les doublons exacts, puis ajoute les variantes. Travaillez sur une copie.

Vos effectifs seront différents de ceux de la section [Dataset](#dataset), donc vos résultats aussi.

### 4. Lancer les notebooks
- `modeling.ipynb` : nettoyage, augmentation, premier CNN et suivi MLflow (`mlflow ui`).
- `pretrained_cnn_model.ipynb` : modèle retenu. Il écrit `model.keras` et `class_names.json` dans le dossier courant. Git les ignore.
- `split_par_photo.ipynb` puis `split_par_photo_preprocess.ipynb` : évaluation refaite. Ils écrivent les fichiers `resultats_*.json`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="structure"></a>Structure du dépôt

```text
.
├── README.md
├── pretrained_cnn_model.ipynb              # ResNet50, modèle retenu
├── modeling.ipynb                          # nettoyage, augmentation, CNN from scratch, MLflow
├── split_par_photo.ipynb                   # évaluation refaite par photo d’origine
├── split_par_photo_preprocess.ipynb        # piste 1 : preprocess_input
├── resultats_split_par_photo.json
├── resultats_split_par_photo_preprocess.json
└── dataset/                                # à fournir, ignoré par Git
```

Git ignore aussi `model.keras`, `class_names.json`, `mlruns/` et `outputs/`.

<p align="right"><a href="#top">Retour en haut</a></p>

---

## <a id="ressources"></a>Ressources & inspirations

- Application WildAIprint (API Flask, front, Docker Compose) : [github.com/Rateur/wildaiprint-App](https://github.com/Rateur/wildaiprint-App).
- Dépôt GitLab de l’équipe : [gitlab.com/yasmine-sayad-group/wildaiprintapp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp).
- ResNet50 pré-entraîné sur ImageNet, chargé avec `tf.keras.applications`.
- Photos de la galerie : Wikimedia Commons.

<p align="right"><a href="#top">Retour en haut</a></p>
