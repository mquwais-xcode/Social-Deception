from ui.ansi.color.foreground import *
from ui.ansi.color.background import *

x_default = f"{Fg.white}{Bg.black}"

class Style:
    info		= f"{Bg.green}{Fg.black}INFO{x_default}"
    ask			= f"{Bg.yellow}{Fg.white}ASK{x_default}"
    success		= f"{Bg.blue}{Fg.black}SUCCESS{x_default}"
    error		= f"{Bg.red}{Fg.black}ERROR{x_default}"
    warning		= f"{Bg.white}{Fg.green}WARNING{x_default}"
