from core.menu.mainmenu import *
from ui.banner.custom import *
from core.menu.sze import *
from lib.cleaner.cleancache import *

from core.menu.facebook.fbmain import *

class SocialEngineeringAttacks:

    def menu():
        Custom()
        Sze.introduce("Select which one you want to hack")
        Sze.addcolumn("0001", "Facebook")
        Sze.backcolumn()
        while True:
            x = input(f"{Style.ask} Pick one: ")
            if x == "0001":
                SocialEngineeringAttacks.facebook()
            elif x == "99":
                MainMenu.mainmenu()
            else:
                Sze.invalidinput()

    def facebook():
        Custom()
        Sze.introduce("Select the social engineering strategy")
        Sze.addcolumn("0001", "Phishing")
        Sze.backcolumn()
        while True:
            x = input(f"{Style.ask} Pick one: ")
            if x == "0001":
                Facebook.Phishing()
            elif x == "99":
                SocialEngineeringAttacks.menu()
            else:
                Sze.invalidinput()
