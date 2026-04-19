from core.sodecs.program import *
from ui.banner.banner import *
from ui.ansi.color.foreground import *
from ui.ansi.color.background import *
from ui.console.clearscreen import *

import random

SOCIAL_ENGINEERING_METHODS = 0

hints = [
    "This Framework is created By Muhammad Quwais Saputra",
    "The weakest point of system is the human it self",
]

def Custom():
    clearscreens()
    Banner()
    print(f"""    {Fg.white}=[ {Sodec.name} {Fg.cyan}{Sodec.version} {Fg.white}({Fg.yellow}{Sodec.codename}{Fg.white}{Bg.black})
{Fg.red}+{Fg.white}====[ {Fg.black}{Bg.white}GITHUB{Bg.green}{Fg.black} https://github.com/mquwais-xcode/sodec{Fg.white}{Bg.black}
{Fg.red}+{Fg.white}====[ {Fg.red}{SOCIAL_ENGINEERING_METHODS} {Bg.red}{Fg.black}Total Social Engineering Methods{Bg.black}
{Fg.red}+{Fg.white}====[ {Fg.green}[{Bg.green}{Fg.black}HINT{Bg.black}{Fg.green}] {Fg.yellow}{random.choice(hints)}
    {Fg.white}=[ {Fg.green}© {Fg.red}{Sodec.author}
    """)
