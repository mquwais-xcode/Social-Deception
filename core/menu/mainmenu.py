from ui.banner.custom import *
from ui.ansi.style import *
from core.menu.sze import *
from core.menu.social_engineering_attacks import *
from lib.cleaner.cleancache import *
import sys

class MainMenu():

    def mainmenu():
        Custom()
        Sze.introduce("Welcome to Social Deception. pick one ot these below to do some action")
        Sze.addcolumn("1", "Social Engineering Attacks")
        Sze.addcolumn("2", "Update Social Deception")
        Sze.addcolumn("3", "Get Certificates (if you want to be pro)")
        Sze.addcolumn("4", "Exit")
        while True:
            x = input(f"{Style.ask} Pick one: ")
            if x == "1":
                SocialEngineeringAttacks.menu()
            elif x == "2":
                pass
            elif x == "3":
                pass
            elif x == "4":
                cleanup()
                sys.exit()
            else:
                print(f"{Style.error} Input error")
                time.sleep(3)
