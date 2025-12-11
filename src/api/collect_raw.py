import json, os, datetime
from src.ingestion.nba_api_client import get_scoreboard

def main():
    d = datetime.date.today().strftime("%Y%m%d")
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/scoreboard_{d}.json", "w") as f:
        json.dump(get_scoreboard(), f, indent=2)
    print("Saved:", f"data/raw/scoreboard_{d}.json")

if __name__ == "__main__":
    main()