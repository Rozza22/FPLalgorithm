# add team stats to players

import os
import pandas as pd

playerDataPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(playerDataPath)

teamDataPath = '/home/ruairi/FPL model/savedData/teamData.csv'
teamData = pd.read_csv(teamDataPath)

teamData.rename(columns={'id':'team'}, inplace=True)

mergedData = pd.merge(teamData, playerData, on=['team'], how='inner')

teamStrength = teamData[['team', 'strength']]
teamStrength.rename(columns={'team':'opponent_team', 'strength':'oppStrength'}, inplace=True)
print(teamStrength.head)

mergedData = mergedData.merge(teamStrength, on='opponent_team', how='left')

# Look at next 5 games opponent strength
def calculateOpponentStrength(group):
    weights = [0.4,0.3,0.2,0.1,0]

    def weightedAverage(x):
        n = min(len(x), len(weights)) # will do for when there aren't 5 matches left
        weighted_sum = sum(x[i] * weights[i] for i in range(n))
        return weighted_sum / sum(weights[:n])
        # return (x[:n] * weights[:n]).sum()/sum(weights[:n])

    # Calculate the weighted average for the next 5 games
    group['next5Strength'] = (group['oppStrength']
    .shift(-1)
    .rolling(window=5, min_periods=1)
    .apply(weightedAverage, raw=True))

    group['next5Strength'] = group['next5Strength'].shift(-4)
    group['next5Strength'] = group['next5Strength'].fillna(method='ffill')
    group['next5Strength'] = group['next5Strength'].round(2) # round to 2 decimals

    return group

mergedData = mergedData.sort_values(['player_ID', 'round'])
resultDF = mergedData.groupby('player_ID', group_keys=False).apply(calculateOpponentStrength)
print(resultDF.head())

# mergedData = pd.merge(teamData, playerData, on='strength', how='inner')

resultDF.to_csv(playerDataPath, index=False)

print(['Team stats merged to:' , playerDataPath])