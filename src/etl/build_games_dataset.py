import os
import json
import pandas as pd

RAW_DIR = "data/raw/"
OUTPUT_DIR = "data/processed/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_raw_scoreboards():
    files = [f for f in os.listdir(RAW_DIR) if f.startswith("scoreboard")]
    data = []

    for filename in files:
        with open(os.path.join(RAW_DIR, filename), "r") as f:
            raw = json.load(f)

        games = raw.get("scoreboard", {}).get("games", [])
        if not games:
            print(f"Aucun match dans {filename}")
            continue

        for g in games:
            row = {
                "GAME_ID": g.get("gameId"),
                "GAME_DATE_EST": g.get("gameDate"),
                "HOME_TEAM_ID": g["homeTeam"]["teamId"],
                "VISITOR_TEAM_ID": g["awayTeam"]["teamId"],
                "HOME_TEAM_SCORE": g["homeTeam"].get("score", 0),
                "VISITOR_TEAM_SCORE": g["awayTeam"].get("score", 0),
            }
            data.append(row)

    return pd.DataFrame(data)


def clean_games(df):
    return df[[  
        "GAME_ID",
        "GAME_DATE_EST",
        "HOME_TEAM_ID",
        "VISITOR_TEAM_ID",
        "HOME_TEAM_SCORE",
        "VISITOR_TEAM_SCORE"
    ]]


def main():
    print("Chargement des fichiers RAW...")
    df = load_raw_scoreboards()
    print(f"{len(df)} matchs trouvés")

    print("Nettoyage...")
    df_clean = clean_games(df)

    output_path = os.path.join(OUTPUT_DIR, "games.csv")
    df_clean.to_csv(output_path, index=False)

    print(f"Dataset créé : {output_path}")


if __name__ == "__main__":
    main()