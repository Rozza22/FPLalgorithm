import os
import pandas as pd
import numpy as np

combinedPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(combinedPath)

dtypes = playerData.dtypes
print(dtypes)
print(playerData.head())

# # Add in 'strength_for_fixture' variable for overall, attack and defence to account for whether team is home or away
overallStrength = [0] * playerData.shape[0]
defenceStrength = [0] * playerData.shape[0]
attackStrength = [0] * playerData.shape[0]

playerData.insert(9, "overallStrength", overallStrength)
playerData.insert(10, "defenceStrength", defenceStrength)
playerData.insert(11, "attackStrength", attackStrength)

# computationally cheaper than doing for loop through all rows
homePlayerData = playerData[playerData['was_home']]
awayPlayerData = playerData[~playerData['was_home']]

homePlayerData['overallStrength'] = homePlayerData['strength_overall_home']
homePlayerData['defenceStrength'] = homePlayerData['strength_defence_home']
homePlayerData['attackStrength'] = homePlayerData['strength_attack_home']

awayPlayerData['overallStrength'] = awayPlayerData['strength_overall_away']
awayPlayerData['defenceStrength'] = awayPlayerData['strength_defence_away']
awayPlayerData['attackStrength'] = awayPlayerData['strength_attack_away']

playerData = pd.concat([awayPlayerData, homePlayerData], axis=0)
playerData = playerData.sort_values(by=['player_ID'],ascending=True)

print(playerData.head())

playerData = playerData.drop(columns=['position'])
playerData.rename(columns={'element_type':'position'}, inplace=True)
if 'position' in playerData.columns:
    playerData['position'] = playerData['position'].astype('str')
    print("Converted position column to string")
else:
    print("Error: 'position' column not found. Please check if it was renamed correctly.")
    exit()
# print([playerData['position'].unique()])

duplicates = playerData.columns[playerData.columns.duplicated()].tolist()

if duplicates:
    print("Duplicate indices found:\n", duplicates)
else:
    print("No duplicate indices found.")

gkString = 'GK'
fwdString = 'FWD'
midString = 'MID'
defString = 'DEF'

# Check if the 'position' column is correctly set
# print(["Data type of 'position' column:", playerData.dtypes])

print(playerData.head())

gkDF = playerData[playerData['position'].str.contains(gkString)]
fwdDF = playerData[playerData['position'].str.contains(fwdString)]
midDF = playerData[playerData['position'].str.contains(midString)]
defDF = playerData[playerData['position'].str.contains(defString)]

fwdDF = fwdDF.drop(columns=['strength_overall_away','strength_defence_away','strength_attack_away','strength_overall_home','strength_defence_home','strength_attack_away', 'name','fixture','element','kickoff_time', 'penalties_saved', 'saves', 'selected', 'transfers_out', 'transfers_out', 'transfers_balance', 'expected_goals_conceded'])
midDF = midDF.drop(columns=['strength_overall_away','strength_defence_away','strength_attack_away','strength_overall_home','strength_defence_home','strength_attack_away','name','fixture','element','kickoff_time', 'penalties_saved', 'saves', 'selected', 'transfers_out', 'transfers_out', 'transfers_balance', 'expected_goals_conceded'])
defDF = defDF.drop(columns=['strength_overall_away','strength_defence_away','strength_attack_away','strength_overall_home','strength_defence_home','strength_attack_away','name','fixture','element','kickoff_time', 'penalties_saved', 'saves', 'selected', 'transfers_out', 'transfers_out', 'transfers_balance', 'expected_goals_conceded'])

gkDF = gkDF.drop(columns=['strength_overall_away','strength_defence_away','strength_attack_away','strength_overall_home','strength_defence_home','strength_attack_away','name','fixture', 'element', 'kickoff_time', 'selected', 'transfers_out', 'transfers_out', 'transfers_balance', 'expected_goals', 'expected_assists', 'expected_goal_involvements'])
print(gkDF.head())

fwdDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/FWD_23_24_data.csv', index=False)
midDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/MID_23_24_data.csv', index=False)
defDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/DEF_23_24_data.csv', index=False)
gkDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/GK_23_24_data.csv', index=False)