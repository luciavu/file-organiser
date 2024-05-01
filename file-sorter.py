import os, shutil

def sort_directory(user, directory):
    full_path = os.path.join("C:\\Users", user, directory)

    # Check directory path exists
    if not os.path.exists(full_path):
        print(f"Error: Directory '{full_path}' does not exist.")
        return
    
    # Change current working directory to chosen
    os.chdir(full_path)  

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

    print("Sorting files...")

    # Create folders to sort files into if not exist already
    for folder in set(file_ext.values()):
        folder_path = os.path.join(full_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Sort files into respective folders
    try:
        # Get file path
        for file in os.listdir():
            src_path = os.path.join(full_path, file)

            # Get file format
            if os.path.isfile(src_path):
                name, ext = os.path.splitext(file)

                # If file format not in dictionary, move to Other
                if ext.lower() not in file_ext:
                    ext = "unknown"
                
                # Move file to matching extension folder
                dst_folder = file_ext[ext.lower()]
                dst_path = os.path.join(full_path, dst_folder, file)
                shutil.move(src_path, dst_path)
                print(f"Moved {file} to {dst_folder}")
                
        print("Done!")

    except OSError as e:
        print(f"Error {e}")

def welcome_message():
    print("-" * 50)
    print("Welcome to File Sorter!")
    print("This program helps you organise files on your desktop.")
    print("Please choose a directory path to clean up.")
    print("\nExamples of directory paths:\nDownloads\nDocuments" + r"\folder_name")
    print(r"OneDrive\Documents\folder_name")

def get_user_input():
    directory = input("\nEnter directory path: ")
    user = input("Enter username: ")
    return user, directory

def main():
    welcome_message()
    user, directory = get_user_input()
    sort_directory(user, directory)

if __name__ == "__main__":
    main()