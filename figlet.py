import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


def main():

    str = input("Input: ")
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        f = random.choice(font_list)

    elif len(sys.argv) == 3:
        if not sys.argv[1] in ["-f", "--font"]:
            sys.exit(
                "Please write '-f' or '--font' in command line to specify font argument"
            )
        elif not sys.argv[2] in font_list:
            sys.exit(f"{sys.argv[2]} is not a valid font")

        f = sys.argv[2]

    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=f)

    print(figlet.renderText(str))


main()
