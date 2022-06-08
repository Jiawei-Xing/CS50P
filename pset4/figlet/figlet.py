import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(sys.argv) > 1:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font = sys.argv[2])
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    figlet.setFont(font = choice(figlet.getFonts()))

print(figlet.renderText(input("Input: ")))