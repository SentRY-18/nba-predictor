import sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ROOT)

print("PYTHONPATH →", ROOT)

import json
import datetime
from src.api.nba_api_client import get_scoreboard


def daterange(start, end):
    for n in range((end - start).days + 1):
        yield start + datetime.timedelta(n)


def main():
    print("Début collecte saison 2024-25...")

    os.makedirs("data/raw", exist_ok=True)

    start = datetime.date(2024, 10, 24)
    end   = datetime.date(2025, 4, 17)

    for d in daterange(start, end):
        print(f"→ {d}")

        data = get_scoreboard(d)

        if "scoreboard" not in data or "games" not in data["scoreboard"]:
            continue
        
        if len(data["scoreboard"]["games"]) == 0:
            continue

        path = f"data/raw/scoreboard_{d}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"   ✔ Saved: {path}")

    print("\nSaison 2024-25 téléchargée !")


if __name__ == "__main__":
    main()