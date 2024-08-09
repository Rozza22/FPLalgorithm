import os
import pandas as pd


gkLastSeasonDataPath = '/home/ruairi/FPL model/savedData/byPosition/GK_23_24_data.csv'
gkData = pd.read_csv(gkLastSeasonDataPath)

print([gkData.dtypes])
print([gkData.head()])
# Remove variables which are irrelevant to score

# Create if else loop to add to teams tally which will contribute to form which will contribute to chance of win

# Make it so all GKs are split into gameweeks into 'savedData/byGW/Players/GKs/GW#'
path = '/home/ruairi/FPL model/savedData/byGW/Players/GKs/'

for i in range(1,39,1):
    # try:
    #     os.chdir(path)
    #     newFolder = 'GW' + str(i+1)
    #     os.makedirs(newFolder)
    # except FileExistsError:
    #     pass
    
    gwData = gkData.loc[gkData["round"] == i]
    try:
        gwData.to_csv(path+"gw"+str(i)+".csv", index=False)
    except FileExistsError:
        pass

    
    

