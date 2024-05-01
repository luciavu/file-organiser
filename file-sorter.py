import os, shutil

def sort_directory(user, directory):
    full_path = os.path.join("C:\\Users", user, directory)

    # Check directory path exists
    if not os.path.exists(full_path):
        print(f"Error: Directory '{full_path}' does not exist.")
        return
    
    os.chdir(full_path)  
    for file in os.listdir():
        print(file)


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