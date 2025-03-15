import os
import subprocess
import winreg
from .path_change import Path
import datetime

class ADB:

    @staticmethod
    def date_insecs() -> str:
        now = datetime.datetime.now()
        seconds = int(now.timestamp())
        return str(seconds)
    
    @staticmethod
    def create_dump_file_folder() -> str:
        dump_folder = "dump_files"  # Define path
        try:
            os.makedirs(dump_folder)
            print(f"Directory '{dump_folder}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dump_folder}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{dump_folder}'.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Create folder if it doesn't exist
        return dump_folder

    @staticmethod
    def check_adb() -> bool:
        try:
            subprocess.run(["adb", "version"], capture_output=True, text=True, check=True)
            return True
        except FileNotFoundError:
            print("ADB not found. Ensure the path is correct.")
            return False


    @staticmethod
    def input_data():
        adb_path = r"C:\Users\jrpaglinawan\AppData\Local\Android\Sdk\platform-tools"
        # add_to_path(adb_path)
        
        checked_adb = ADB.check_adb()
        if(not checked_adb):
            Path.input_data(adb_path)
            print("""\033[91m
                    If adding path is success, please restart your CMD/PS to perform ADB test.
                Otherwise, you need to add it manually and restart your terminal. Thank you.
                  \033[0m""")
            return
        
        print("Please input your package name. Example: example.project:")
        package_name = input("---> com.")
        

        # Define package name and dump file details
        package_name = f"com.{package_name}"
        dump_file = f"/data/local/tmp/dump_{ADB.date_insecs()}.hprof"


        local_path = ADB.create_dump_file_folder()
        # local_path = r"C:\Users\jrpaglinawan\AppData\Local\DevFolder\dump_files"
       

        # # Find the process ID
        cmd_ps = f"adb shell ps | findstr {package_name}"
        result = subprocess.run(cmd_ps, shell=True, capture_output=True, text=True)
        lines = result.stdout.splitlines()
        print(lines)
        if lines:
            process_info = lines[0].split()
            pid = process_info[1]  # Typically, PID is the second column
            print(f"Process ID: \033[91m{pid}\033[0m")

            # #Dump the heap for the process
            cmd_dumpheap = f"adb shell am dumpheap {pid} {dump_file}"
            subprocess.run(cmd_dumpheap, shell=True)

            # # Pull the dump file to the local machine
            cmd_pull = f"adb pull {dump_file} {local_path}"
            subprocess.run(cmd_pull, shell=True)

            print(f"\033[92mHeap dump completed and pulled successfully. Path is in in this project directory in folder {local_path}.\033[0m")
        else:
            print(f"\033[91mProcess {package_name} not found.\033[0m")
