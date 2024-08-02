import os
import pandas as pd


gkLastSeasonDataPath = '/home/ruairi/FPL model/savedData/byPosition/GK_23_24_data.csv'
gkData = pd.read_csv(gkLastSeasonDataPath)

print([gkData.dtypes])
# Remove variables which are irrelevant to score

# Create if else loop to add to teams tally which will contribute to form which will contribute to chance of win

# Also record form on goals conceded

# x values are ones which will be used to predict points (y)
# x = gkData[['bps', 'clean_sheets', ]]


