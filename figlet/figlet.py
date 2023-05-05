import sys
from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()
figlet.setFont(font = "slant")

def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font = sys.argv[2])
            fonter()
        else:
            sys.exit(1)
    elif len(sys.argv) == 1:
        fonter()
    else:
        sys.exit(1)
    #except:
        #print("Invalid usage")

def fonter():
    inputtxt = input("Input: ").strip()
    print("Output: ")
    print(figlet.renderText(inputtxt))


main()

