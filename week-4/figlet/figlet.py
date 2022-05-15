
############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


import random as RAN 
import pyfiglet as fig
import  sys

# start figlet 
figlet = fig.Figlet()
# get all fonts
fonts = figlet.getFonts()

if len(sys.argv) > 3 or len(sys.argv) > 1 and len(sys.argv) < 3:
    print('Invalid usage')
    sys.exit(1)

if len(sys.argv) == 3:
    
    font = sys.argv[2]
    # check for valid font
    if font not in fonts:
        print('Invalid usage')
        sys.exit(1)
    
    font_flag = sys.argv[1]
    # check for valid flag
    if font_flag not in ['-f','--font']:
        print('invlaid usage')
        sys.exit(1)

    # set font to user input
    figlet.setFont(font=font)

    user_input = input("Input: ")
    print(figlet.renderText(user_input))
    sys.exit(0)

# if user just run program with out flag and command line argument

# create a Random number
rand_number = RAN.randint(0,len(fonts))
# choice Random Font and Set it
figlet.setFont(font=fonts[rand_number])
user_input = input("Input: ")
print(figlet.renderText(user_input))
sys.exit(0)
