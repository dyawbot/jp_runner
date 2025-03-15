import os
import sys
import subprocess
import winreg

class Path:

    @staticmethod
    def add_to_path(directory):
        if directory.startswith("%"):
            pub_cache_bin = os.path.expandvars(fr"{directory}")
            directory = pub_cache_bin
        
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            return
        
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment')
        
        path, _ = winreg.QueryValueEx(key, 'PATH')
        
        winreg.CloseKey(key)
        
        if directory in path:
            print(f"Directory {directory} is already in the PATH.")
            return
        
        newPath = f"{directory};{path}"
        subprocess.run(['REG', 'ADD',  'HKEY_CURRENT_USER\\Environment',
        '/v', 'PATH', '/t', 'REG_EXPAND_SZ', '/f', '/d', newPath], check=True, capture_output=True)
        print(f"Directory {directory} added to the PATH.")

    @staticmethod
    def input_data(path = None):
        
        adb_path = r"C:\Users\jrpaglinawan\AppData\Local\Android\Sdk\platform-tools"

        print("""
              These are the paths, you can choose these paths or you can enter your own path,
              You can type q and enter to cancel:""")
        print(f"1. ADB - {adb_path}")
        path_name = input("Please enter number or your path: ")
        if(path is not None):
            Path.add_to_path(path)
            return
        if(path_name == "1"):
            Path.add_to_path(adb_path)
        elif(path_name == "q" or path_name == "Q"):
            return
        else:
            Path.add_to_path(path_name)
