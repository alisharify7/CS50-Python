############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


in_put = input("camelCase: ").strip()

print("snake_case: ", end="")
for char in in_put:
    if(char.isupper()):
        print("_",end="")
    print(char.lower(),end="")

print()
