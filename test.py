from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import pandas as pd

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 
season = playergamelog.PlayerGameLog(player_id='203999', season = '2022', season_type_all_star = 'Regular Season')


# pandas data frames (optional: pip install pandas)
df = career.get_data_frames()[0]
stats = season.get_data_frames()[0]
#df = pd.DataFrame(career.get_data_frames())




# json
career.get_json()

# dictionary
career.get_dict()

#print(df)
print(stats.)

