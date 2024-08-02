import shutil
import os

# Define the source path of the .csv file
# '//wsl.localhost/Ubuntu/home/ruairi/Fantasy-Premier-League/data/2023-24/players/'
source_file = '/home/ruairi/Fantasy-Premier-League/data/2023-24/players/Alejandro_Garnacho_382/gw.csv'

# Define the destination path where the .csv file should be copied
destination_folder = '/home/ruairi/FPL model/savedData/'

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Construct the full path for the destination file
destination_file = os.path.join(destination_folder, 'p382.csv')

# Copy the file from source to destination
shutil.copy2(source_file, destination_file)

print(f"Copied {source_file} to {destination_file}")