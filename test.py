from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import json
import pandas as pd
import numpy as np

# Nikola Jokić

career = playercareerstats.PlayerCareerStats(player_id='203999').get_data_frames()
season = pd.DataFrame(playergamelog.PlayerGameLog(player_id='203999', season = '2025', season_type_all_star = 'Regular Season').get_data_frames())



print(season)




def getParams(game_id, player_id):
   
    return 0
