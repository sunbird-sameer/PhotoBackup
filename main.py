import os
import shutil
from datetime import datetime

def organize_files_by_date(source_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"The folder {source_folder} does not exist.")
        return

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if it is a file
        if os.path.isfile(file_path):
            # Get the last modified time and convert it to a datetime object
            mod_time = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(mod_time)

            # Create year, month, and day directories
            year = str(date.year)
            month = f"{date.month:02}"  # Format month as two digits
            day = f"{date.day:02}"      # Format day as two digits

            year_month_day_folder = os.path.join(source_folder, year, month, day)

            # Create year/month/day directory if it does not exist
            os.makedirs(year_month_day_folder, exist_ok=True)

            # Move the file to the new directory
            shutil.move(file_path, os.path.join(year_month_day_folder, filename))
            print(f"Moved: {filename} to {year}/{month}/{day}")

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder to organize: ")
    organize_files_by_date(source_folder)
