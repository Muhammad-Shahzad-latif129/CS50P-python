import sys
from pyfiglet import Figlet
import random

figlet = Figlet()


def main():
    fonts = figlet.getFonts()
    if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in fonts:
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output:\n", figlet.renderText(s))
        else:
            sys.exit("Invalid Usage")
        return

    elif len(sys.argv) == 1:
        s = input("Input: ")
        ran = random.choice(fonts)
        figlet.setFont(font=ran)
        print("Output:\n", figlet.renderText(s))
    else:
        sys.exit("Usage: python figlet.py [-f FONTNAME]")


if __name__ == "__main__":
    main()
