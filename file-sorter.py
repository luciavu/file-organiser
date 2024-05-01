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
    documents = [".doc", ".docx", ".docm" ".html", ".htm", ".odt", ".pdf", 
                 ".xls", ".xlsx", ".rtf", ".ppt", ".pptx", ".txt", ".psd", ".csv"]
    images = [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".ico", ".raw"]
    videos = [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf",
               ".mkv", ".webm"]
    music = [".mp3", ".wav", ".flac", ".m4a"]
    applications = [".exe", ".lnk"]
    archives = [".zip", ".rar", ".7z", ".tar", ".gz"]
    code = [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php"]

        


def welcome_message():
    print("Welcome to File Sorter!")
    print("This program helps you organise files on your desktop.")
    print("Please choose a directory path to clean up.")
    print("""Examples of directory paths:
          Downloads
          Documents
          Documents/folder_name\n""")

def main():
    welcome_message()
    directory = input("Enter directory path: ")
    user = input("Enter username: ")
    sort_directory(user, directory)


if __name__ == "__main__":
    main()