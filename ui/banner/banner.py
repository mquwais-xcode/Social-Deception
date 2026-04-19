import random
from ui.ansi.color.foreground import *
from ui.ansi.color.background import *

def Banner():
    logos = [
    f"""
{Fg.red}_________________  ________  ____________________  
 /   _____/\\_____  \\ \\______ \\ \\_   _____/\\_   ___ \\ 
 \\_____  \\  /   |   \\ |    |  \\ |    __)_ /    \\  \\/ 
 /        \\/    |    \\|    `   \\|        \\     \\____
/_______  /\\_______  /_______  /_______  / \\______  /
        \\/         \\/        \\/        \\/         \\/ 
    """,
    f"""
{Fg.yellow}┏┓   •  ┓            
┗┓┏┓┏┓┏┓┃            
┗┛┗┛┗┗┗┻┗            
       ┓        •    
      ┏┫┏┓┏┏┓┏┓╋┓┏┓┏┓
      ┗┻┗ ┗┗ ┣┛┗┗┗┛┛┗
             ┛       
    """
    ]
    print(random.choice(logos))
