import argparse
import os
import subprocess

from banner import Banner
from args.test.sum import MyScripts
from args.proxy import Proxy
from args.path_change import Path
from args.adb import ADB



def main():
    parser = argparse.ArgumentParser(description="Run specific functions in MyScripts.")
    parser.add_argument("--test", action="store_true", help="Run the test function.")
    parser.add_argument("--adb", action="store_true", help="Run the adb function.")
    parser.add_argument("--path", action="store_true", help="Run the add function")
    parser.add_argument("--proxy", action="store_true", help="Run the adding_to_path function.")
    parser.add_argument("--do", action="store_true", help="Run the adding_to_path function.")

    args = parser.parse_args()
    Banner.print_big_jp()

    if args.test:
        MyScripts.test()
    elif args.proxy:
        Proxy.input_data()
    elif args.path:
        Path.input_data()
    elif args.adb:
        ADB.input_data()
    else:
        # Interactive mode if no arguments are provided
        print("No argument provided. Choose an option:")
        print("1. Run test")
        print("2. You want to change your Proxy")
        print("3. You want to add Path in Environment")
        print("4. You want to Test your adb and get the HEAP Memory")
        

        choice = input("Choose Number from 1 to 4:").strip()
        
        if choice == "1":
            MyScripts.test()
        elif choice == "2":
            Proxy.input_data()
        elif choice == "3":
            Path.input_data()
        elif choice == "4":
            ADB.input_data()
        else:
            print("Invalid option. Exiting.")

if __name__ == "__main__":
    main()