import time
import logging
from nba_api.stats.endpoints import scoreboard, leaguegamefinder, boxscoretraditionalv2

logger = logging.getLogger(__name__)

def safe_call(fn, *args, **kwargs):
    for i in range(3):
        try:
            return fn(*args, **kwargs).get_dict()
        except Exception as e:
            logger.warning(f"nba_api error (attempt {i+1}): {e}")
            time.sleep(1 + i * 2)
    raise RuntimeError("nba_api unreachable after retries")

def get_scoreboard(date=None):
    return safe_call(scoreboard.ScoreBoard, game_date=date)

def find_games(team_id=None, season='2024-25'):
    params = {}
    if team_id:
        params["team_id_nullable"] = team_id
    return safe_call(leaguegamefinder.LeagueGameFinder, **params, season_nullable=season)

def get_boxscore(game_id):
    return safe_call(boxscoretraditionalv2.BoxScoreTraditionalV2, game_id=game_id)