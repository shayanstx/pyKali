import pySource
import math
import os
import pyautogui
from colorama import Fore
import signal

# clear console
os.system('cls')

# change opacity
for _ in range(15):
    pyautogui.hotkey("ctrl", "shift", "+")

for _ in range(1):
    pyautogui.hotkey("ctrl", "shift", "-")

os.system('color 08')

# Remove extra command
def remove(a):
    return command_input.strip(a)

pySource.banner()

# console design
while True:
    Directory_Now = os.getcwd() # Path
    user = os.path.expanduser('~') # C:\Users\SHAYAN
    root = "C:'\\Users" # root directory

    # Directory Rename
    if user in Directory_Now:
        if Directory_Now == user:
            Directory_Now = '~'
        else:
            Directory_Now = Directory_Now.strip(user)
    else:
        pass
    
    # command Input
    print(' ')
    command_input = input(Fore.LIGHTBLUE_EX+' ┌── '+Fore.LIGHTGREEN_EX+'(root@pykali)'+Fore.LIGHTBLACK_EX+' ~ '+Fore.LIGHTBLUE_EX+f'[{Directory_Now}]\n'+Fore.LIGHTBLUE_EX+' └── # '+Fore.RESET)

    # Enter
    def enter():
        print('\n')

    ## commands

    # Blink
    if command_input == '':
        pass
    
    # Clear
    elif command_input == 'clear':
        os.system('cls')
        pySource.banner()

    # python Run
    elif command_input == 'python':
        os.system('python')

    # Developer
    elif command_input == 'pykali --developers':
        pySource.developers()

    # --Help
    elif (command_input == 'pykali --help') or (command_input == 'pykali -h'):
        pySource.Help()

    # Ls
    elif command_input == 'ls':
        os.system('dir')
        enter()

    # Shutdown Tool
    elif command_input == 'power --0':
        exit(1)

    # Cd
    elif 'cd' in command_input:
        aa = remove("cd ")
        try:
            os.chdir(aa)
        except:
            print(Fore.LIGHTRED_EX+'\n [ Error ] '+Fore.RESET+f"'{aa}' ; The system cannot find the path specified")

    # Ping
    elif 'ping' in command_input:
        aa = remove('ping ')
        os.system(f'ping {aa}')
        enter()

    # make dir
    elif 'mkdir' in command_input:
        aa = remove('mkdir ')
        os.mkdir(aa)

    # Git
    elif 'git' in command_input:
        aa = remove('git ')
        if 'clone' in aa:
            bb = aa.strip('clone ')
            os.system(f'git clone {bb}')

    # Error
    else:
        print(Fore.LIGHTRED_EX+f"\n '{command_input}' is not recognized as an internal or external command,\n operable program or batch file.")
        # enter()