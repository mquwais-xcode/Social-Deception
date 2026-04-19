from ui.ansi.color.foreground import *
from ui.ansi.color.background import *
from ui.ansi.style import *

import time

class Sze:
    def introduce(text):
        print(f"{Fg.green}{text}")
    def addcolumn(columns, text):
        print(f"     {Fg.red}{columns}.{Fg.green} {text}")
    def backcolumn():
        print(f"     {Fg.red}99. BACK{Fg.white}")
    def invalidinput():
        print(f"{Style.error} Invalid input!")
        print(f"{Style.info} If you are newbie to this, Get SODEC certifactes! learn more with SODEC")
        time.sleep(3)
