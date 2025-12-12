import time
import logging
from datetime import datetime
from nba_api.stats.endpoints import scoreboardv3, leaguegamefinder, boxscoretraditionalv2

logger = logging.getLogger(__name__)


def safe_call(fn, *args, **kwargs):
    """
    Appel robuste avec retries.
    """
    for i in range(3):
        try:
            return fn(*args, **kwargs).get_dict()
        except Exception as e:
            logger.warning(f"nba_api error (attempt {i+1}): {e}")
            time.sleep(1 + i * 2)
    raise RuntimeError("nba_api unreachable after retries")


def get_scoreboard(date_obj):
    """
    Scoreboard fiable utilisant ScoreboardV3 (V2 est cassé).
    Retourne un dict contenant :
    {
        "scoreboard": {
            "games": [...]
        }
    }
    """
    date_str = date_obj.strftime("%Y-%m-%d")
    print(f"→ Appel API ScoreboardV3 pour {date_str}")

    try:
        sb = scoreboardv3.ScoreboardV3(game_date=date_str)
        return sb.get_dict()
    except Exception as e:
        print("Erreur ScoreboardV3 :", e)
        return {"scoreboard": {"games": []}}


def find_games(team_id=None, season='2024-25'):
    params = {}
    if team_id:
        params["team_id_nullable"] = team_id

    return safe_call(leaguegamefinder.LeagueGameFinder,
                     **params,
                     season_nullable=season)


def get_boxscore(game_id):
    return safe_call(boxscoretraditionalv2.BoxScoreTraditionalV2,
                     game_id=game_id)