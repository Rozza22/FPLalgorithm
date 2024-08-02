import os
import pandas as pd

# Define the destination path where the modified CSV files are saved
destinationPath = '/home/ruairi/FPL model/savedData/playerDataIndiv/'
# Define the path to save the final concatenated CSV file
finalCsvPath = '/home/ruairi/FPL model/savedData/CombinedData.csv'

# List to hold all DataFrames
allDataFrames = []

# Iterate over each file in the destination directory
for file in os.listdir(destinationPath):
    if file.endswith('.csv'):
        filePath = os.path.join(destinationPath, file)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filePath)
        # Append the DataFrame to the list
        allDataFrames.append(df)

# Concatenate all DataFrames vertically
finalDf = pd.concat(allDataFrames, ignore_index=True)

# print(finalDf.head())

# read in to find link between ID and each player's team
rawPlayerData = pd.read_csv('/home/ruairi/Fantasy-Premier-League/data/2023-24/players_raw.csv')
idPosition = pd.read_csv('/home/ruairi/FPL model/savedData/IDposition.csv')
dfPlayerIDlist = pd.read_csv("/home/ruairi/Fantasy-Premier-League/data/2023-24/player_idlist.csv")
# print(dfPlayerIDlist.head())

selectedColumns = rawPlayerData[['id', 'team']]
# print(selectedColumns.head())

idPosition.rename(columns={'id':'player_ID'}, inplace=True)
selectedColumns.rename(columns={'id':'player_ID'}, inplace=True)
dfPlayerIDlist.rename(columns={'id':'player_ID'}, inplace=True)

mergedData = pd.merge(finalDf, selectedColumns, on='player_ID', how='inner')

mergedData = pd.merge(mergedData, idPosition, on='player_ID', how='inner')

# Save the final concatenated DataFrame to a new CSV file
mergedData.to_csv(finalCsvPath, index=False)

print(f"All CSV files have been concatenated and saved to {finalCsvPath}")

