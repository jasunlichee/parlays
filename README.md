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
player_id | avg l10 games | avg l5 games | opp team ort | opp team drt |opp playerids | pt trend | b2b? | curr team ort | curr team drt | starting y/n 
ex. Nikola Jokić
203999    | 

endpoints to use:
- nba_api/stats/endpoints/playergamelog.py
- 
