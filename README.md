# parlays
nba over/under predictive models

brainstorm:
things to consider:
1. recent game performance
2. performance against certain teams
3. performance against certain players
4. injuries to teammates
5. trend in playing time
6. second night of a b2b?
7. oppponent's defensive/offensive rating
8. current team's defensive/offensive rating
9. starting y/n

api: https://github.com/swar/nba_api
call pip install nba_api


first steps:
1. get training data using nba_api
2. train ML algorithm
3. obtain ML model
4. run new data through model
5. obtain predictions

data format:
player_id | avg l10 games | avg l5 games | avg l10 VS OPP | avg l5 VS OPP | curr team ORt | opp team DRt | Minutes Avg | Season Avg | Days between last game | Player Age | starting Y/N | Home/Away


endpoints to use:
- nba_api/stats/endpoints/playergamelog.py
- DefenseHubStat4 defense_hub_stat4

iterate through all the years that the player played
append all of their stats into one table


- player_id - input
- game_id - input

- avg l10 games - playercareerstats 
- avg l5 games - playercareerstats 
- avg l10 VS OPP - playercareerstats
- avg l5 VS OPP - playercareerstats
- curr team ORt - 
- opp team DRt
- Minutes Avg
- Season Avg
- Days between last game
- Player Age
- starting Y/N
- Home/Away