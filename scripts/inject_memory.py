import json

# Charger la mémoire depuis le fichier JSON
with open("memoire_disobey.json", "r", encoding="utf-8") as f:
    memoire = json.load(f)

# Afficher les sections pour vérification
print("✔️ Mémoire Marius V3 chargée avec succès.")
print("Blocs intégrés :")
for bloc in memoire.keys():
    print(f"🔹 {bloc}")
