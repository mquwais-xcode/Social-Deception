import sys
import time
try:
    from core.sodecs.program import *
    from core.menu.mainmenu import *
    from core.menu.sze import *
    from core.menu.social_engineering_attacks import *
    from core.menu.facebook.fbmain import *
    from ui.console.clearscreen import *
    from ui.ansi.color.foreground import *
    from ui.ansi.color.background import *
    from ui.ansi.style import *
    from ui.banner.banner import *
    from ui.banner.custom import *
    from lib.cleaner.cleancache import *
except ImportError as e:
    print(f"[!] '{e}' not found from main liblary. please update or reinstall tools")
    sys.exit()

print(f"{Style.info} Starting SODEC..")
time.sleep(3)

# scanning modules
try:
    from modules.facebook.phishing.local_login_page import *
except ImportError as ek:
    print(f"[-] error module not found: {ek}")
    sys.exit

try:
    MainMenu.mainmenu()
except KeyboardInterrupt:
    cleanup()
    sys.exit()
