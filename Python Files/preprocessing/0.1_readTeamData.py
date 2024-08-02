# Use 'teams.csv' for data on teams at beginning of season to help with predicted points for players

import os
import pandas as pd

teamDataPath = '/home/ruairi/Fantasy-Premier-League/data/2023-24/teams.csv'
teamData = pd.read_csv(teamDataPath)

teamData = teamData.drop(columns=['team_division', 'unavailable', 'pulse_id', 'code'])

teamData.to_csv('/home/ruairi/FPL model/savedData/teamData.csv', index=False)

print(teamData)