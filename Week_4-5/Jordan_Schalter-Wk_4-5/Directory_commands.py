import sys
import os
import shutil
from datetime import datetime

def log_command(command):
    """
    Logs the executed command along with a timestamp to a system log file.

    Args:
        command (str): The command to be logged.

    Returns:
        None
    """
    log_path = 'C:\\Python_Log\\system_log.txt'
    with open(log_path, 'a') as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp}: {command}\n")

def basic_mode():
    """
    Basic mode of the file manager. Allows users to change the current directory
    and list items in the current directory.

    Returns:
        None
    """
    cwd = os.getcwd()
    print("Current Working Directory: %s" % cwd)
    
    change_dir = input("Would you like to change the directory? (yes/no): ")
    
    if change_dir.lower() == "yes":
        try:
            new_dir = input("Enter Directory: ")
            os.chdir(new_dir)
            print(f"Changed directory to: {os.getcwd()}")
            print("Items in the directory:")
            for item in os.listdir():
                print(f"- {item} {'(Directory)' if os.path.isdir(item) else '(File)'}")
            
            log_command(f"Changed directory to: {os.getcwd()}")
        except FileNotFoundError:
            print("Directory not found. Please enter a valid directory.")
    else:
        print("Items in the current directory:")
        for item in os.listdir():
            print(f"- {item} {'(Directory)' if os.path.isdir(item) else '(File)'}")

def elevated_mode():
    """
    Elevated mode of the file manager. Inherits basic mode functionalities and
    allows users to copy files and directories.

    Returns:
        None
    """
    basic_mode()
    
    copy_option = input("Would you like to copy a file or directory? (yes/no): ")
    
    if copy_option.lower() == "yes":
        try:
            source = input("Enter source path: ")
            destination = input("Enter destination path: ")
            
            if not os.path.exists(destination):
                print("Destination directory does not exist. Please try again.")
                return
            
            if os.path.isdir(source):
                shutil.copytree(source, os.path.join(destination, os.path.basename(source)))
                print(f"Directory '{source}' copied to '{destination}'.")
                log_command(f"Directory '{source}' copied to '{destination}'.")
            elif os.path.isfile(source):
                shutil.copy2(source, destination)
                print(f"File '{source}' copied to '{destination}'.")
                log_command(f"File '{source}' copied to '{destination}'.")
            else:
                print("Invalid source path. Please provide a valid file or directory.")
        except Exception as e:
            print(f"Error: {e}")

def admin_mode():
    """
    Admin mode of the file manager. Inherits elevated mode functionalities and
    allows users to move and delete files and directories.

    Returns:
        None
    """
    elevated_mode()

    delete_option = input("Would you like to move and delete files or directories? (yes/no): ")

    if delete_option.lower() == "yes":
        try:
            source = input("Enter source path: ")
            destination = 'C:\\Python_Log\\backups'
            backup_prefix = 'deleted_'
            
            if os.path.exists(source):
                backup_path = os.path.join(destination, backup_prefix + os.path.basename(source))
                shutil.copytree(source, backup_path)
                shutil.rmtree(source)
                
                print(f"Moved and deleted '{source}'. Backup stored in '{backup_path}'.")
                log_command(f"Moved and deleted '{source}'. Backup stored in '{backup_path}'.")
            else:
                print("Source path does not exist. Please provide a valid file or directory.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if "-m" in sys.argv:
        privilege_level_index = sys.argv.index("-m") + 1
        if privilege_level_index < len(sys.argv):
            privilege_level = sys.argv[privilege_level_index].lower()

            if ".." in privilege_level:
                print("Cannot move up the filesystem using '..'.")
                exit()
            
            if privilege_level not in ["basic", "elevated", "admin"]:
                print("Invalid privilege level. Please specify basic, elevated, or admin.")
                exit()

            if "-d" in sys.argv:
                directory_index = sys.argv.index("-d") + 1
                if directory_index < len(sys.argv):
                    directory_path = sys.argv[directory_index]
                    try:
                        os.chdir(directory_path)
                    except FileNotFoundError:
                        print("Directory not found. Please enter a valid directory.")
                        exit()
            else:
                directory_path = os.getcwd()

            if privilege_level == "basic":
                basic_mode()
            elif privilege_level == "elevated":
                elevated_mode()
            elif privilege_level == "admin":
                admin_mode()
        else:
            print("Please provide a privilege level after the -m option.")
    else:
        print("Missing -m option. Please specify basic, elevated, or admin.")