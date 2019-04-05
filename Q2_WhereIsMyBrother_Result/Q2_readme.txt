==Predict The Season==

Problem: 
- A custom league created between Teams Manchester United, Arsenal, Chelsea, Juventus, Real Madrid, Barcelona, Bayern Munchen and Liverpool
- This league is simulated for 8 seasons starting from 2018-2019
- You need to predict all game scores for the season 2022-2023 

Rules:
- Fill Home_Score and Away_Score columns in 'test_fixture.csv'
- Home_Score and Away_Score data should be integer

Submission:
- CSV File named as 'Q2_TeamName_Result.csv'
- Game_Id,Date,Home_Team,Away_Team,Season,Home_Score,Away_Score as columns
- 56 rows for each football match 
- See example : 'Q2_Team1_Result.csv'
- Zip your codes and Result File in 'Q2_TeamName_Result.zip'
- Email zip file to submission@algorunhackathon.com with subject 'Q2_TeamName_Result'

Scoring:
For each game:
- Guess winner 1 Point
- Guess winning margin +0.5 Point
- Guess exact score +1 Point

Dataset:
'fixture.csv' : All game scores for seasons 18-19, 19-20, 20-21, 21-22, 23-24, 24-25, 25-26
'player_data.csv' : Player performance data of each game for seasons 18-19, 19-20, 20-21, 21-22, 23-24, 24-25, 25-26
'stats_data.csv' : Game stats data of each game for seasons 18-19, 19-20, 20-21, 21-22, 23-24, 24-25, 25-26
'test_fixture.csv' : Fixture data for the season 22-23 (Test Season) without game scores
'2022_2023_season_squads.csv' : 22-23 Season beginning squands for the teams

