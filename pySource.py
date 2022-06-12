from colorama import Fore, Fore

def banner():
    print(Fore.LIGHTBLUE_EX+"""  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
 | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
 | |   ______     | || |  ____  ____  | || |  ___  ____   | || |      __      | || |   _____      | || |     _____    | |
 | |  |_   __ \   | || | |_  _||_  _| | || | |_  ||_  _|  | || |     /  \     | || |  |_   _|     | || |    |_   _|   | |
 | |    | |__) |  | || |   \ \  / /   | || |   | |_/ /    | || |    / /\ \    | || |    | |       | || |      | |     | |
 | |    |  ___/   | || |    \ \/ /    | || |   |  __'.    | || |   / ____ \   | || |    | |   _   | || |      | |     | |
 | |   _| |_      | || |    _|  |_    | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _| |__/ |  | || |     _| |_    | |
 | |  |_____|     | || |   |______|   | || | |____||____| | || ||____|  |____|| || |  |________|  | || |    |_____|   | |
 | |              | || |              | || |              | || |              | || |              | || |              | |
 | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n"""+Fore.LIGHTBLACK_EX)

def Help():
    print(Fore.LIGHTGREEN_EX+'\n [pykali # Help]'+Fore.RESET)
    print("""
 To make better use of this tool, you need to pay attention to a series of points so that you do not run into problems
 After reading this guide, you can use all the capabilities of the tool

 [1] All Kali Linux commands are in this tool and you can use them and see the result on your Windows operating system.
 [2] In addition to these commands, we have added additional commands for personalizing the user interface, which are as follows

 ** change tool background color
     [$] pykali -bg --(color)
    
 ** change font color
     [$] pykali -font --(color)
    
 ** change background opacity
     [$] pykali -opacity --(value)
    
 * Example:
     --> pykali -bg --RED
     --> pykali -opacity --80""")

def programmer(name,mail,insta,twitter):
    print(Fore.LIGHTBLUE_EX+f" [{name}]\n ---------"+Fore.RESET)
    print(Fore.LIGHTBLACK_EX+" [ Email ] "+Fore.RESET+mail)
    print(Fore.LIGHTBLACK_EX+" [ Instagram ] "+Fore.RESET+insta)
    print(Fore.LIGHTBLACK_EX+" [ twitter ] "+Fore.RESET+twitter)

# Developers
def developers():
    print(Fore.LIGHTGREEN_EX+"\n [Developers]\n")
    programmer('SHAYAN STX','shayanstx@gmail.com','shaayaan.io','shayanstx')
    print('\n')
    programmer('MWMD01','mr.ptogrammer.2222@gmail.com','mwmd_01','Mwmd010')