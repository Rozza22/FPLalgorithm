import os
import pandas as pd
import numpy as np

combinedPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(combinedPath)

# add in form based off weighted points in last 5 gameweeks
print(len(playerData.index))

# for i in range(len(playerData.index)):
#     if i == 0:
#         continue
#     elif i-1 == 0 & playerData.loc[i,'player_ID'] == playerData.loc[i-1,'player_ID']:
#         playerData.loc[i,'form'] = playerData.loc[i-1,'total_points']
#     elif i-2 == 0 & playerData.loc[i,'player_ID'] == playerData.loc[i-1,'player_ID'] == & playerData.loc[i-2,'player_ID']:
#         playerData.loc[i,'form'] = (playerData.loc[i-1,'total_points'] + playerData.loc[i-2,'total_points'])/2
#     elif i-3 == 0 & playerData.loc[i,'player_ID'] == playerData.loc[i-1,'player_ID'] == & playerData.loc[i-2,'player_ID'] == playerData.loc[i-3,'player_ID']:
#         playerData.loc[i,'form'] = (playerData.loc[i-1,'total_points'] + playerData.loc[i-2,'total_points'] + playerData.loc[i-3,'total_points'])/3
#     elif i-4 == 0 & playerData.loc[i,'player_ID'] == playerData.loc[i-1,'player_ID'] == & playerData.loc[i-2,'player_ID'] == playerData.loc[i-3,'player_ID'] == playerData.loc[i-4,'player_ID']:
#         playerData.loc[i,'form'] = (playerData.loc[i-1,'total_points'] + playerData.loc[i-2,'total_points'] + playerData.loc[i-3,'total_points'] + playerData.loc[i-4,'total_points'])/4

# playerData = playerData.fillna(0)
# more efficient:
playerData = playerData.sort_values(['total_points', 'round'])

def calculateForm(group):
    # calculate the rolling average for the last 4 matches or less
    group['form'] = group['total_points'].shift(1).rolling(window=4, min_periods=1).mean()
    # group.loc[1,'form'] = 0
    return group



# playerData = playerData.groupby('player_ID', group_keys=False).apply(calculateForm, include_groups=False)
playerData = playerData.groupby('player_ID', group_keys=False).apply(calculateForm)

playerData.loc[playerData['round'] == 1, 'form'] = 0.0

playerData = playerData.fillna(0)
newFilePath = '/home/ruairi/FPL model/savedData/CombinedDataWithRolling.csv'
playerData.to_csv(newFilePath, index=False)