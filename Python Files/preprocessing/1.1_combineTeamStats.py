# add team stats to players

import os
import pandas as pd

playerDataPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(playerDataPath)

teamDataPath = '/home/ruairi/FPL model/savedData/teamData.csv'
teamData = pd.read_csv(teamDataPath)

teamData.rename(columns={'id':'team'}, inplace=True)

mergedData = pd.merge(teamData, playerData, on='team', how='inner')

mergedData.to_csv(playerDataPath, index=False)

print(['Team stats merged to:' , playerDataPath])