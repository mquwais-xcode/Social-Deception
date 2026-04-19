from ui.ansi.color.foreground import *
from ui.ansi.color.background import *

class Style:
    info		= f"{Fg.green}[{Fg.yellow}+{Fg.green}]{Fg.white}"
    ask			= f"{Fg.yellow}[?]{Fg.white}"
    success		= f"{Fg.green}[*]"
    error		= f"{Fg.red}[!]"
    warning		= f"{Fg.white}[{Bg.red}{Fg.black}WARN{Bg.black}{Fg.white}"
    results		= f"{Fg.white}[{Fg.yellow}-{Fg.white}]"
