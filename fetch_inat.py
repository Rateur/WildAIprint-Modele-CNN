"""Télécharge les photos iNaturalist ajoutées au jeu (inat_attributions.csv) dans inat/<espèce>/.
Les images ne sont pas dans le dépôt : chacune garde sa licence et son auteur, listés dans le CSV.
Usage : python fetch_inat.py [dossier de sortie, par défaut inat]"""
import csv, os, sys, time, urllib.request

root = sys.argv[1] if len(sys.argv) > 1 else "inat"
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "inat_attributions.csv"), encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
done = 0
for r in rows:
    path = os.path.join(root, r["dossier"], r["fichier"])
    if os.path.exists(path):
        continue
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(r["photo_url"], headers={"User-Agent": "wildaiprint-dataset (github.com/Rateur)"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(path, "wb") as out:
        out.write(resp.read())
    done += 1
    time.sleep(0.5)   # poli envers le serveur d'iNaturalist
print(f"{done} photos téléchargées, {len(rows) - done} déjà présentes")
