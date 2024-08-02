import os
import shutil
import pandas as pd

# Define the path to the cloned repository
# repo_path = '//wsl.localhost/Ubuntu/home/ruairi/Fantasy-Premier-League/data/2023-24/players/'
repo_path = '/home/ruairi/Fantasy-Premier-League/data/2023-24/players/'
# Define the destination path to save renamed CSV files
# destination_path = '//wsl.localhost/Ubuntu/home/ruairi/FPL model/savedData/'
destination_path = '/home/ruairi/FPL model/savedData/playerDataIndiv'

# Ensure the destination path exists
os.makedirs(destination_path, exist_ok=True)

# Traverse through each subfolder in the repository
for root, subdirs, files in os.walk(repo_path):
    for subdir in subdirs:
        subdir_path = os.path.join(root, subdir)
        # Check if the subdir name ends with a number
        if subdir.split('_')[-1].isdigit():
            number = subdir.split('_')[-1]
            if number.isdigit():
                player_id = number
                for file in os.listdir(subdir_path):
                    if file.endswith('gw.csv'):
                        # Construct the new file name
                        new_file_name = f"p{file.rstrip('.csv')}_{number}.csv"
                        # Define the full file paths
                        old_file_path = os.path.join(subdir_path, file)
                        new_file_path = os.path.join(destination_path, new_file_name)
                        # Copy and rename the CSV file
                        df = pd.read_csv(old_file_path)
                        df['player_ID'] = player_id

                        df.to_csv(new_file_path, index=False)
                        print(f"Copied, modified, and renamed: {new_file_name}")
                        # shutil.copy2(old_file_path, new_file_path)
                        # print(f"Copied and renamed: {new_file_name}")

print("All files have been processed.")