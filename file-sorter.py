import os, shutil

TOTAL_FOLDERS = 8

def sort_directory(path):
    # Check directory path exists
    print(path)
    if not os.path.exists(path):
        print(f"Error: Directory '{path}' does not exist.")
        return
    
    # Change current working directory to chosen
    os.chdir(path)  

    # Dictionary of common file formats
    file_ext = {
    ".doc": "Documents", ".docx": "Documents", ".docm": "Documents",
    ".html": "Documents", ".htm": "Documents", ".odt": "Documents",
    ".pdf": "Documents", ".xls": "Documents", ".xlsx": "Documents",
    ".rtf": "Documents", ".ppt": "Documents", ".pptx": "Documents",
    ".txt": "Documents", ".psd": "Documents", ".csv": "Documents",
    ".jpeg": "Images", ".jpg": "Images", ".png": "Images",
    ".gif": "Images", ".tiff": "Images", ".ico": "Images", ".raw": "Images",
    ".mp4": "Videos", ".mov": "Videos", ".wmv": "Videos", ".avi": "Videos",
    ".avchd": "Videos", ".flv": "Videos", ".f4v": "Videos", ".swf": "Videos",
    ".mkv": "Videos", ".webm": "Videos",
    ".mp3": "Music", ".wav": "Music", ".flac": "Music", ".m4a": "Music",
    ".exe": "Applications", ".lnk": "Applications",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
    ".c": "Code", ".py": "Code", ".java": "Code", ".cpp": "Code",
    ".js": "Code", ".html": "Code", ".css": "Code", ".php": "Code", ".ipynb": "Code", 
    "unknown": "Other"
    }

    print("\nSorting files...")
    # Create folders to sort files into if not exist already
    for folder in set(file_ext.values()):
        folder_path = os.path.join(path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Count sorted files
    total_files = -TOTAL_FOLDERS
    sorted = 0 

    # Sort files into respective folders
    try:
        # Get file path
        for file in os.listdir():
            total_files += 1
            src_path = os.path.join(path, file)

            # Get file format
            if os.path.isfile(src_path):
                name, ext = os.path.splitext(file)

                # If file format not in dictionary, move to Other
                if ext.lower() not in file_ext:
                    ext = "unknown"
                else:
                    sorted += 1
                
                # Move file to matching extension folder
                dst_folder = file_ext[ext.lower()]
                dst_path = os.path.join(path, dst_folder, file)
                shutil.move(src_path, dst_path)
                print(f"Moved {file} to {dst_folder}")
                
        print("Done!") 
        print(f"Sorted: {sorted}/{total_files} files.\n")
    
    except OSError as e:
        print(f"Error {e}")

def welcome_message():
    print("Welcome to File Sorter!")
    print("Please copy the directory path you would like to organise, " + r"for example: C:\Users\your_username\Documents")

def main():
    welcome_message()
    path = input("Paste the directory path here: ")
    sort_directory(path)

if __name__ == "__main__":
    main()