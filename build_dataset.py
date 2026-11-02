"""dataset-v2 = le jeu d'origine (photos et variantes, tel quel) + les photos iNaturalist gardées au tri, chacune avec
ses cinq variantes faites par le même code que modeling.ipynb (cellule 4), bruit compris.
Usage : python fetch_inat.py, puis python build_dataset.py dataset inat dataset-v2"""
import os, random, shutil, sys
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

src, inat, out = sys.argv[1:4]
random.seed(12); np.random.seed(12)   # la graine du projet : le jeu se reconstruit à l'identique
assert not os.path.exists(out), "la sortie existe déjà"
shutil.copytree(src, out)
added = {}
for class_name in sorted(os.listdir(inat)):
    cdir = os.path.join(inat, class_name)
    if not os.path.isdir(cdir): continue
    assert os.path.isdir(os.path.join(out, class_name)), f"espèce inconnue : {class_name}"
    for filename in sorted(f for f in os.listdir(cdir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))):
        file_path = os.path.join(out, class_name, filename)
        with Image.open(os.path.join(cdir, filename)) as im: im.convert('RGB').save(file_path, quality=95)
        with Image.open(file_path) as img:
            img.rotate(random.uniform(-30, 30)).save(os.path.join(out, class_name, f"aug_rot_{filename}"))
            ImageOps.mirror(img).save(os.path.join(out, class_name, f"aug_flip_{filename}"))
            w, h = img.size
            img.crop((int(w*0.1), int(h*0.1), int(w*0.9), int(h*0.9))).resize((w, h)).save(os.path.join(out, class_name, f"aug_zoom_{filename}"))
            arr = np.array(img)
            noise = np.random.normal(0, 25, arr.shape).astype(np.uint8)   # tel quel : le cast replie les valeurs négatives, comme l'original
            Image.fromarray(np.clip(arr + noise, 0, 255).astype(np.uint8)).save(os.path.join(out, class_name, f"aug_noise_{filename}"))
            ImageEnhance.Brightness(img).enhance(random.uniform(0.6, 1.4)).save(os.path.join(out, class_name, f"aug_bright_{filename}"))
        added[class_name] = added.get(class_name, 0) + 1
for c in sorted(os.listdir(out)):
    o = [f for f in os.listdir(os.path.join(out, c)) if not f.startswith('aug_')]
    print(f"{c:13} {len(o):3d} photos d'origine (+{added.get(c, 0)} iNaturalist)")
