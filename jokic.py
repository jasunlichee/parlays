from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import pandas as pd
from datetime import datetime

# Nikola Jokić
id = '203999'


# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()[0]
years = career['SEASON_ID'].unique()
games = []

for yr in years:
    season = pd.DataFrame(playergamelog.PlayerGameLog(player_id='203999', season = yr, season_type_all_star = 'Regular Season').get_data_frames()[0])
    games.append(season)

games = pd.concat(games, ignore_index=True)
print(games)



"""
Now we have games df with every single game in the player's history
need to extract: 

- avg l10 games
- avg l5 games
- avg l10 VS OPP
- avg l5 VS OPP
- curr team ORt
- opp team DRt
- Minutes Avg
- Season Avg
- Days between last game
- Player Age
- starting Y/N
- Home/Away

"""

def extract_stats(games, ):
