import os
import pandas as pd
import numpy as np

combinedPath = '/home/ruairi/FPL model/savedData/CombinedDataWithRolling.csv'
# combinedPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'
playerData = pd.read_csv(combinedPath)

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

fwdDF = fwdDF.drop(columns=['penalties_saved', 'saves', 'expected_goals_conceded'])
midDF = midDF.drop(columns=['penalties_saved', 'saves', 'expected_goals_conceded'])
defDF = defDF.drop(columns=['penalties_saved', 'saves', 'expected_goals_conceded'])

gkDF = gkDF.drop(columns=['expected_goals', 'expected_assists', 'expected_goal_involvements'])
print(gkDF.head())

fwdDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/FWD_23_24_data.csv', index=False)
midDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/MID_23_24_data.csv', index=False)
defDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/DEF_23_24_data.csv', index=False)
gkDF.to_csv('/home/ruairi/FPL model/savedData/byPosition/GK_23_24_data.csv', index=False)