import sys
import time
try:
    from core.sodecs.program import *
    from core.menu.main import *
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
try:
    mainmenu()
except KeyboardInterrupt:
    cleanup()
    sys.exit()
