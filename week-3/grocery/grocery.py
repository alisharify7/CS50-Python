############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



temp_list = {}

while True:
    try:
        user = input().strip().title()
        if user not in temp_list:
            # if user not in our dic so we add it
            temp_list[user] = 1
            continue
        # if in the dic we increment it
        temp_list[user] += 1

    except EOFError:

        # first iterate in each k,v in dictionary
        # and with sorted method sorted by alphabetic
        for key,value in sorted(temp_list.items()):
            print(f"{value} {key.upper()}")
        # in the end just exit
        break