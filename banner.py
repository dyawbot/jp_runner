class Banner:
    @staticmethod
    def print_big_jp():
        """Prints a big 'JP' ASCII Art"""
        print("""
           ██╗ ██████╗ 		      
           ██║ ██╔══██╗          \033[92m ███\033[0m═╗
           ██║ ██████╔╝	         \033[92m█████\033[0m║
    ██     ██║ ██╔═══╝           \033[92m█████\033[0m║
    ╚█████╔╝   ██║               \033[92m███████████████████\033[0m╗
     ╚════╝    ╚═╝     \033[92m█████████████████ \033[0m╔══════════╝
                       \033[92m█████████████████ \033[0m║
                                 \033[92m████\033[0m╔═══╝
    \033[92m███████████████████████████████████████████████████████████\033[0m╗
    ╚══════════════════════════════════════════════════════════╝
    \033[91mThis is a runner. It can change your proxys, add path to environments, 
              run test, use as a pentest for mobile devices.   \033[0m       
    You can run the program using args.
        \033[92m* python jp_runner.py --proxy (for changing proxy)
        * python jp_runner.py --adb   (for testing mobile device such getting heap memory)
        * python jp_runner.py --path  (adding command path to environments)\033[0m
        """)