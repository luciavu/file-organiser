import os, shutil

def sort_directory(user, directory):
    full_path = os.path.join("C:\\Users", user, directory)

    # Check directory path exists
    if not os.path.exists(full_path):
        print(f"Error: Directory '{full_path}' does not exist.")
        return
    
    # Change current working directory to chosen
    os.chdir(full_path)  

    # Lists of common file formats
    file_extensions = {
        "Documents": [".doc", ".docx", ".docm" ".html", ".htm", ".odt", ".pdf", 
                     ".xls", ".xlsx", ".rtf", ".ppt", ".pptx", ".txt", ".psd", ".csv"],
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".ico", ".raw"],
        "Videos": [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf",
                   ".mkv", ".webm"],
        "Music" :[".mp3", ".wav", ".flac", ".m4a"],
        "Applications": [".exe", ".lnk"],
        "Archives" : [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".ipynb"],
        "Other" : []
    }

    print("Sorting files...")

    # Create folders to sort files into if not exist already
    for folder in file_extensions:
        folder_path = os.path.join(full_path, folder)
        os.makedirs(folder_path, exist_ok=True)
    return

    #for file in os.listdir():

    print("Done!")


def welcome_message():
    print("-" * 50)
    print("Welcome to File Sorter!")
    print("This program helps you organise files on your desktop.")
    print("Please choose a directory path to clean up.")
    print("\nExamples of directory paths:\nDownloads\nDocuments" + r"\folder_name")
    print(r"OneDrive\Documents\folder_name")

def main():
    welcome_message()
    directory = input("\nEnter directory path: ")
    user = input("Enter username: ")
    sort_directory(user, directory)


if __name__ == "__main__":
    main()