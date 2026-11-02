"""Télécharge les photos iNaturalist ajoutées au jeu (inat_attributions.csv) dans inat/<espèce>/.
Les images ne sont pas dans le dépôt : chacune garde sa licence et son auteur, listés dans le CSV.
Chaque fichier est écrit à part puis renommé, et son empreinte SHA-256 doit être celle du CSV :
une coupure ou une photo modifiée en ligne ne passe pas inaperçue.
Usage : python fetch_inat.py [dossier de sortie, par défaut inat]"""
import csv, hashlib, os, sys, time, urllib.request

root = sys.argv[1] if len(sys.argv) > 1 else "inat"
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "inat_attributions.csv"), encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
done, bad = 0, []
for r in rows:
    path = os.path.join(root, r["dossier"], r["fichier"])
    if os.path.exists(path) and hashlib.sha256(open(path, "rb").read()).hexdigest() == r["sha256"]:
        continue
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(r["photo_url"], headers={"User-Agent": "wildaiprint-dataset (github.com/Rateur)"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    if hashlib.sha256(data).hexdigest() != r["sha256"]:
        bad.append(r["photo_url"])   # changée ou retirée en ligne : on ne la garde pas
    else:
        with open(path + ".part", "wb") as out:
            out.write(data)
        os.replace(path + ".part", path)
        done += 1
    time.sleep(0.5)   # poli envers le serveur d'iNaturalist
print(f"{done} photos téléchargées, {len(rows) - done - len(bad)} déjà présentes")
if bad:
    print(f"{len(bad)} photos ne correspondent plus au CSV (changées ou retirées en ligne) :", *bad, sep="\n  ")
    sys.exit(1)
