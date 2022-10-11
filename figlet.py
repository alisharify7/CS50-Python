import time
import pyfiglet as fg

pyfig = fg.Figlet()

# get all fonts in format of list
fonts = pyfig.getFonts()


# iterate over all fonts
for i in range(len(fonts)):
    # each time print hello world with one font
    fg.print_figlet(text="hello world", font=fonts[i], colors="GREEN")
    time.sleep(0.3)