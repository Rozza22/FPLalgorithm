import os
import pandas as pd
import numpy as np

combinedPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(combinedPath)

# add in form based off weighted points in last 5 gameweeks
print(len(playerData.index))


# playerData = playerData.fillna(0)
# more efficient:
playerData = playerData.sort_values(['total_points', 'round'])

def calculateRolling(group):
    # calculate the rolling average for the last 4 matches or less
    group['form'] = group['total_points'].shift(1).rolling(window=4, min_periods=1).mean()
    group['expectedAssistHistory'] = group['expected_assists'].shift(1).rolling(window=4, min_periods=1).mean()
    group['expectedGIsHistory'] = group['expected_goal_involvements'].shift(1).rolling(window=4, min_periods=1).mean()
    group['expectedGoalsHistory'] = group['expected_goals'].shift(1).rolling(window=4, min_periods=1).mean()
    group['expectedGsConcededHistory'] = group['expected_goals_conceded'].shift(1).rolling(window=4, min_periods=1).mean()
    group['BPShistory'] = group['bps'].shift(1).rolling(window=4, min_periods=1).mean()
    group['ictHistory'] = group['ict_index'].shift(1).rolling(window=4, min_periods=1).mean()
    # group.loc[1,'form'] = 0
    return group

# playerData = playerData.groupby('player_ID', group_keys=False).apply(calculateRolling, include_groups=False)
playerData = playerData.groupby('player_ID', group_keys=False).apply(calculateRolling)

playerData.loc[playerData['round'] == 1, ['form', 'expectedAssistHistory', 'expectedGIsHistory', 'expectedGoalsHistory','expectedGsConcededHistory', 'BPShistory', 'ictHistory']] = 0.0 # in round 1, there is no form, so assign 0

playerData = playerData.fillna(0)

# Will do this but weighted for other variables to contribute to predictions:
# Expected goals conceded, expected goals scored etc


newFilePath = '/home/ruairi/FPL model/savedData/CombinedDataWithRolling.csv'
playerData.to_csv(newFilePath, index=False)