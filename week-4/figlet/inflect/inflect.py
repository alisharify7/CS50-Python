

############################################
#                                          #
#             by : Ali Sharify             #
#        Don't copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



import inflect

engine = inflect.engine()

# start message
adieu = 'Adieu, adieu, to'
# create a list for storage names
names_input= []

while True:
    try:
        # get input from user
        user = input("Name: ")
        # add each name to a list
        names_input.append(user)
    # if user enter Ctrl + D
    except EOFError:
        print('')
        break

# join name together
answer = engine.join(names_input)
print(adieu,answer)