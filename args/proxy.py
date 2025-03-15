
import time
import sys
import subprocess


class Proxy:
    

    @staticmethod
    def http_proxy_change(proxy):
        subprocess.run(['setx', 'http_proxy', proxy], check=True)
        print("\033[92m[HTTP]\033[0m: Successfully changed the http_proxy!")

    @staticmethod
    def https_proxy_change(proxy):
        subprocess.run(['setx', 'https_proxy', proxy], check=True)
        print("\033[92m[HTTPS]\033[0m: Successfully changed the https_proxy!")  



    #FOR MOBILE
    @staticmethod
    def create_gradle_properties_proxy(filePath, username='jrpaglinawan', password=None): 
        fileData = f'''
            systemProp.http.proxyHost=securewebgateway
            systemProp.http.proxyPort=9090
            systemProp.http.proxyUser={username}
            systemProp.http.proxyPassword={password}

            systemProp.https.proxyHost=securewebgateway
            systemProp.https.proxyPort=9090
            systemProp.https.proxyUser={username}
            systemProp.https.proxyPassword={password}'''

        with open(filePath, 'w') as file:
            file.write(fileData)
        print(f'\033[92m[GRADLE]\033[0m: Successfully created proxy gradle.properties file at {filePath}')

    @staticmethod
    def set_git_config(key, value, global_config=True):
        try:
            # CONSTRUCTION OF GIT COMMAND HERE
            command = ['git', 'config']
            check_list_command = ['git', 'config']
            
            # If global_config is True, apply configuration globally
            if global_config:
                command.append('--global')
                check_list_command.append('--global')
            

            
            command.append(key)
            command.append(value)
            

            check_list_command.append('--list')
            
            subprocess.run(command, check=True)
            subprocess.run(check_list_command, check=True)
            
            print(f'\033[92m[GIT-CONFIG]\033[0m: Successfully set {key} to {value}')
        
        except subprocess.CalledProcessError as e:
            print(f"\033[91m[GIT-CONFIG] Error setting git config: {e}\033[0m")
    @staticmethod
    def test_method(status):
        if status:
            time.sleep(2)
            print("DONE")

    @staticmethod
    def test_gradle(status):
        if status:
            time.sleep(1)
            print("DONE Gradle")

    @staticmethod
    def input_data():


        #**************************** CREDENTIALS
        username = "jrpaglinawan"
        password = input("Enter new password: ")



        if username is not None:
            change_username = input(f"\033[92m[{username}]\033[0m Username: Want to change this? (YES or NO): ")
            if change_username.lower() == "yes":
                username = input("Enter your new username: ")

        gradle_file_path = f'C:\\Users\\{username}\\AppData\\Local\\.gradle\\gradle.properties'
        http_proxy = f'http://{username}:{password}@securewebgateway:9090'
        https_proxy = f'https://{username}:{password}@securewebgateway:9090'



        if not password or str(password) == "":
            http_proxy = ""
            https_proxy =""
            print("")
            print(f"\033[38;5;214m[WARNING]: YOU DIDN'T SET ANY HTTP, HTTPS and GRADLE!\nHTTP: {http_proxy}\nHTTPS: {https_proxy}\033[0m\n")
        else:
            print("")
            print("\033[91m****** THESE ARE THE PROXY YOU WANT TO MODIFY ********\033[0m")
            print(f"\033[92m{http_proxy}\033[0m")
            print(f"\033[92m{https_proxy}\033[0m")
            print("")
            print("\033[91m****** THIS IS YOUR GRADLE PATH ********\033[0m")
            print(f"\033[92m{gradle_file_path}\033[0m")
            print("\n")



        question = input("Are you sure you want to proceed? (YES or NO): ")

        if question.lower() == "yes":
            print("Proceeding", end="", flush=True)

            for _ in range(5):  # Simple loading effect
                time.sleep(0.5)
                print(".", end="", flush=True)

            print("\n")
            if password or password !="":
                Proxy.create_gradle_properties_proxy(gradle_file_path, password=password)
            
                Proxy.http_proxy_change(http_proxy)
                Proxy.https_proxy_change(https_proxy)


                Proxy.set_git_config('http.proxy', http_proxy)
                Proxy.set_git_config('https.proxy', https_proxy)
                Proxy.print("\n\033[92mSUCCESS...\033[0m")

            # FOR MOBILE


            
        else:
            print("Try again!")


