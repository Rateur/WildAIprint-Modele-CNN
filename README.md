# WildAIprint – Modèle IA

## Description
Ce dépôt contient tout ce qui concerne le **modèle IA** utilisé par l’application WildAIprint :

- le notebook d’entraînement du modèle CNN pré-entraîné (`pretrained_cnn_model.ipynb`),
- le **dataset** (13 classes d’animaux, ~250 images d’empreintes),
- le modèle entraîné exporté au format `.keras`.

Ce modèle est ensuite intégré au back-end Flask du dépôt [WildAIprintApp](https://gitlab.com/yasmine-sayad-group/wildaiprintapp.git).

---

## Table des matières

- [Documentation complète](#documentation-complète)
- [Structure du dépôt](#structure-du-dépôt)
- [Dataset](#dataset)
- [Architecture du modèle](#architecture-du-modèle)
- [Entraînement et fine-tuning](#entrainement-et-fine-tuning)
- [Résultats et évaluation](#resultats-et-evaluation)
- [Export et intégration](#export-et-intégration)
- [Licences et crédits](#licences-et-crédits)

---

## Documentation complète

Consulter la documentation complète du projet (données, modèle IA, fine-tuning, résultats, architecture) :  
[WildAIprint Documentation Projet](https://www.notion.so/WildAIprint-Documentation-Projet-261b73b4f1d480ed8a6ef05ea84e85f3?source=copy_link)

---

## Structure du dépôt
```
/
├── pretrained_cnn_model.ipynb # Notebook d'entraînement du modèle ResNet50 + fine-tuning
├── dataset/ # Dossier contenant les images d’empreintes (13 classes)
│ ├── Castor/
│ ├── Chat/
│ ├── Chien/
│ ├── Coyote/
│ ├── Ecureuil/
│ ├── Lapin/
│ ├── Loup/
│ ├── Lynx/
│ ├── Ours/
│ ├── Puma/
│ ├── Rat/
│ ├── Raton_laveur/
│ └── Renard/
└── model.keras # Modèle entraîné exporté
```

---

## Dataset

- **13 classes** : Castor, Chat, Chien, Coyote, Écureuil, Lapin, Loup, Lynx, Ours, Puma, Rat, Raton laveur, Renard.
- **250 images** au total, réparties dans les sous-dossiers par espèce.
- **Images nettoyées** (suppression doublons et fichiers corrompus) et prétraitées avant l’entraînement.
- **Pipeline de data augmentation** appliqué au chargement pour enrichir artificiellement le dataset.

---

## Architecture du modèle

- **Backbone :** ResNet50 pré-entraîné sur ImageNet, `include_top=False`.
- **Entrée :** `Input(shape=(256,256,3))` → pipeline de data augmentation → ResNet50.
- **Tête personnalisée :**
  - `GlobalAveragePooling2D`
  - `Dropout(0.5)`
  - `Dense(128, activation='relu')`
  - `Dropout(0.3)`
  - `Dense(num_classes, activation='softmax')` (classification multiclasse)

<details><summary>Code modèle</summary>

```python
inputs = Input(shape=(256, 256, 3))
x = data_augmentation(inputs)
base_model = ResNet50(weights='imagenet', include_top=False, input_tensor=x)
base_model.trainable = False
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.5)(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.3)(x)
predictions = Dense(num_classes, activation='softmax')(x)
model = Model(inputs=inputs, outputs=predictions)
```
</details>

## Entraînement et fine-tuning
* **Framework** : `TensorFlow/Keras`.
* **Input size** : 256×256 px, `Batch size` : 16.
* **Optimiseur** : `Adam`, Perte : `categorical crossentropy`.
* **Métriques** : `accuracy`, `precision`, `recall`, `F1-score`.
* Phase 1 : entraînement avec `backbone` gelé.
* Phase 2 : `fine-tuning` – dégel progressif des couches du `backbone`, taux d’apprentissage réduit, `early-stopping`.

<details><summary>Code fine-tuning</summary>

```python
base_model.trainable = True

# Only the final layers are fine-tuned.
for layer in base_model.layers[:-30]:
    layer.trainable = False

model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Retraining
history_finetune = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=20,
    callbacks=[early_stop],
    verbose=1
)
```
</details>

## Résultats et évaluation
* `Accuracy` **de validation** : 0.83
* Courbes d’`accuracy` et de `loss` : progression régulière et parallèle (bonne généralisation).
* Matrice de confusion et rapport de classification : bonnes performances globales, quelques classes plus difficiles (Castor, Raton laveur, Chat).

<details><summary>Courbes d’accuracy</summary>

![](https://imgur.com/Nb0OGSx.png)
</details>

<details><summary>Courbes de loss</summary>

![](https://imgur.com/VHFeAP8.png)
</details>

<details><summary>Matrice de confusion</summary>

![](https://imgur.com/GH3XmAz.png)
</details>

## Export et intégration
* Modèle exporté au format `.keras` (`model.keras`).
* Utilisé par l’API Flask du dépôt [WildAIprintApp](https://www.notion.so/WildAIprint-Documentation-Projet-261b73b4f1d480ed8a6ef05ea84e85f3?source=copy_link) pour servir les prédictions.
* Pipeline pré/post-traitement identique entre entraînement et inférence pour cohérence.

## Licences et crédits
* Code : Licence MIT (Exemple)
* Images, dataset : WildAIprint + sources (NatureTracking, iNaturalist, etc.)
* Remerciements à l’équipe pédagogique et à tous les contributeurs