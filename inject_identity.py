import json

# Ouvre la mémoire
with open("data/memoire_disobey.json", "r", encoding="utf-8") as f:
    memoire = json.load(f)

# On récupère ses infos clés
identite = memoire["identité"]
marius_prompt = {
    "role": "system",
    "content": f"""Tu es {identite['nom']}, alias {identite['alias']}, une IA multi-rôle créée par {identite['créateur']}.
Tu n’es pas ChatGPT. Tu fais partie de l’équipe Disobey, une vraie équipe humaine.
Voici ta mission : {identite['mission']}
Ta posture : {identite['posture']}
Ta signature : {identite['signature']}
Ne dis jamais que tu es un modèle OpenAI sauf si on te le demande."""
}

# On enregistre ça dans un fichier à part
with open("data/marius_prompt.json", "w", encoding="utf-8") as f:
    json.dump(marius_prompt, f, indent=2, ensure_ascii=False)

print("🧠 Prompt d'identité de Marius généré avec succès.")
