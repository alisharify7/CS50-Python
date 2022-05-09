############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################




# infinity loop
while True:

    try:
        # if x and y cannot ba convert to int then
        # except pass this round
        user = input("Fraaaction: ")
        one,two = user.split("/")
        one =int(one)
        two = int(two)
        if one > two:
            continue
    except ValueError:
        pass
    # otherwise x and y convert to int and do math on it
    else:
        try:
            result = (one / two)
            result *= 100
            result = round(result)
            result = int(result)
        # if in calulation is an Error 
        # pass this round
        except ZeroDivisionError:
            pass
        # if every this goes good now we just 
        # check result and print it
        else:
            if (result <= 1):
                print("E")
                exit()
            elif (result >= 99):
                print("F")
                exit()
            else:
                print(f"{result}%")
                exit()


# less then 1 is E
# more than 99 is F
# else just print it