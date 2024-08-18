import shutil
import os
import schedule
import time
from datetime import datetime

def backup_project(source_folder, backup_folder):
    """
    Backs up the source folder to the backup folder.
    
    :param source_folder: The folder to be backed up.
    :param backup_folder: The destination folder where backup will be saved.
    """
    # Extract the source folder name to use as the backup folder name
    source_folder_name = os.path.basename(os.path.normpath(source_folder))

    # Create a folder inside the backup folder based on the source folder name
    project_backup_folder = os.path.join(backup_folder, source_folder_name)
    
    # Ensure the project-specific backup folder exists
    if not os.path.exists(project_backup_folder):
        os.makedirs(project_backup_folder)

    # Create a timestamped subfolder for each backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(project_backup_folder, f"backup_{timestamp}")
    
    try:
        # Copy the source folder to the destination subfolder
        shutil.copytree(source_folder, destination)
        print(f"Backup completed successfully at {timestamp} to {destination}")
    except Exception as e:
        print(f"Backup failed: {str(e)}")

# Function to schedule the backup job
def schedule_backup(source_folder, backup_folder, interval_minutes):
    schedule.every(interval_minutes).minutes.do(backup_project, source_folder, backup_folder)
    print("Hello there!")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Paths to your project folder and backup destination
    source_folder = "/Users/dev1/Documents/Reusable-Code-Collection/"  
    backup_folder = "/Users/dev1/Desktop/Backups"

    # Schedule the backup every 30 minutes
    schedule_backup(source_folder, backup_folder, 1) 
