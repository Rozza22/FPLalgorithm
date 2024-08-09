import os
import pandas as pd
import numpy as np

combinedPath = '/home/ruairi/FPL model/savedData/CombinedDataWithRolling.csv'
playerData = pd.read_csv(combinedPath)

# Instead of points, target should be value for money:

playerData['valueForMoney'] = playerData['total_points']/(playerData['value']/10)

print(playerData.head())

playerData.to_csv(combinedPath, index=False)