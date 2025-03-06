import random
import sys

from pyfiglet import Figlet


def get_font():

    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        return random.choice(font_list)

    elif len(sys.argv) == 3:
        if not sys.argv[1] in ["-f", "--font"]:
            sys.exit(
                "Please write '-f' or '--font' in command line to specify font argument"
            )
        elif not sys.argv[2] in font_list:
            sys.exit(f"{sys.argv[2]} is not a valid font")

        return sys.argv[2]

    else:
        sys.exit("Invalid usage")


def main():

    figlet = Figlet()
    figlet.setFont(font=get_font())

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
