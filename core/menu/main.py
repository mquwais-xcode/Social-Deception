from core.menu.social_engineering_attacks import *
from ui.console.clearscreen import *
from ui.ansi.color.foreground import *
from ui.ansi.color.background import *
from ui.ansi.style import *
from ui.banner.custom import *
from lib.cleaner.cleancache import *

import sys, time

def mainmenu():
    while True:
        Custom()
        print(f"""{Style.info} Welcome to sodec. please select action you want to play
   {Fg.red}1. {Fg.white}Social Engineering Attacks
   {Fg.red}2. {Fg.white}Update Sodec
   {Fg.blue}3. {Bg.blue}{Fg.white}Get SODEC Certificates! (If its your first time){Bg.black}
   {Fg.red}4. CREDITS
   {Fg.yellow}5. exit
        """)
        x = input(f"{Style.ask} Pick one: ")
        if x == "1":
            MenuSoceng()
        elif x == "2":
            print(f"{Style.error} This feature isnt created yet")
            sys.exit()
        elif x == "3":
            print(f"{Style.error} This feature isnt created yet")
            sys.exit()
        elif x == "4":
            print(f"{Style.error} This feature isnt created yet")
            sys.exit()
        elif x == "5":
            print("{Style.success} Exiting.. success see ya!")
            cleanup()
            sys.exit()
        else:
            print(f"{Style.error} {x} is not a valid input. are you newbie? Choose 3!")
            time.sleep(4)
