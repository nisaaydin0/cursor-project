import os
import shutil
from datetime import datetime

def organize_desktop():
    # Get the desktop path
    desktop_path = os.path.expanduser("~/Desktop")
    
    # Dictionary to map file extensions to folder names
    extension_folders = {
        # Images
        '.png': 'Screenshots',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.gif': 'Images',
        # Documents
        '.pdf': 'PDFs',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        # Other common types
        '.xlsx': 'Spreadsheets',
        '.xls': 'Spreadsheets',
        '.zip': 'Archives',
        '.dmg': 'Installers'
    }
    
    # Create folders if they don't exist
    for folder in set(extension_folders.values()):
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get all files on desktop
    desktop_files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
    
    for file in desktop_files:
        # Get the full file path
        file_path = os.path.join(desktop_path, file)
        
        # Skip if it's a hidden file
        if file.startswith('.'):
            continue
        
        # Get file extension
        _, extension = os.path.splitext(file)
        extension = extension.lower()
        
        # If we know how to handle this extension
        if extension in extension_folders:
            destination_folder = extension_folders[extension]
            
            # Special handling for screenshots
            if extension == '.png' and file.lower().startswith('screen shot'):
                destination_folder = 'Screenshots'
            
            destination_path = os.path.join(desktop_path, destination_folder)
            
            # Move the file
            try:
                shutil.move(file_path, os.path.join(destination_path, file))
                print(f"Moved {file} to {destination_folder}")
            except Exception as e:
                print(f"Error moving {file}: {str(e)}")

if __name__ == "__main__":
    print("Starting desktop organization...")
    organize_desktop()
    print("Desktop organization complete!")
