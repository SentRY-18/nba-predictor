import os
import json

HOME_ID = 1610612747  # L.A. Lakers
AWAY_ID = 1610612744  # Golden State

RAW_DIR = "data/raw/"

match_found = False

for filename in os.listdir(RAW_DIR):
    if not filename.startswith("scoreboard"):
        continue

    filepath = os.path.join(RAW_DIR, filename)
    with open(filepath, "r") as f:
        data = json.load(f)

    games = data.get("scoreboard", {}).get("games", [])
    for game in games:
        if game["homeTeam"]["teamId"] == HOME_ID and game["awayTeam"]["teamId"] == AWAY_ID:
            match_found = True
            print("Match trouvé !")
            print("Date :", game.get("gameDateEst", "inconnue"))
            print("Score :", game["homeTeam"].get("score", "N/A"), "-", game["awayTeam"].get("score", "N/A"))

if not match_found:
    print("Aucun match trouvé entre ces équipes dans les fichiers RAW.")
