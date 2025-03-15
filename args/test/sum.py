class MyScripts:

    @staticmethod
    def print_big_jp():
        """Prints a big 'JP' ASCII Art"""
        print(r"""
           ██╗ ██████╗ 		      
           ██║ ██╔══██╗          ████╗
           ██║ ██████╔╝	         █████║
    ██     ██║ ██╔═══╝           █████║
    ╚█████╔╝   ██║               ███████████████████╗
     ╚════╝    ╚═╝     █████████████████ ╔══════════╝
                       █████████████████ ║
                                 ████╔═══╝
    ███████████████████████████████████████████████████████████╗
    ╚══════════════════════════════════════════════════════════╝
    This is a runner. It will can change your proxys, add path to environments, 
              run test, use as a pentest for mobile devices.
       You can run the program using args.
              * python jp_runner.py --proxy
              * python jp_runner.py --adb
              * python jp_runner.py --path
        """)
    
    @staticmethod
    def test():
        print("Running test function...")
        # Add your test logic here
        print("Test function executed!")

    @staticmethod
    def adding_to_path():
        print("Running adding path function...")
        # Add your test logic here
        print("Adding path function executed!")
       