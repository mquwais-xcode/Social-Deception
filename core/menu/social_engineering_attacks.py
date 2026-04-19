from core.menu.main import *
from ui.ansi.color.foreground import *
from ui.ansi.color.background import *
from ui.ansi.style import *
from ui.banner.custom import *
from lib.cleaner.cleancache import *

import time

def MenuSoceng():
    while True:
        Custom()
        print(f"""{Style.info}Oh the Main Core function. please tell me which you want you wanna hack?
    {Fg.white}[{Fg.green}0001{Fg.white}] Facebook
    {Fg.white}[{Fg.red}9999{Fg.white}] Back To Main Menu
        """)
        x = input(f"{Style.ask} Pick just one : ")
        if x == "0001": pass
        elif x == "9999": return 1
        else: print(f"{Style.error} Invalid input! get certificates it you want to learn sodec!"); time.sleep(3)
