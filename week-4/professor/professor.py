############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


from random import randint

def main():

    points = 0
    level = get_level()

    # print 10 question 10 times
    for i in range(10):

        # this variable is each iterate set 0 
        # this variable for keep track of wrong answer of user
        counter = 0

        # generate random number for problem
        fNumber = generate_integer(level)
        sNumber = generate_integer(level)
        answer = fNumber + sNumber

        while True:
            # get input and make sure to user input is integer
            try:
                check = int(input("{0} + {1} = ".format(fNumber,sNumber)))
            except ValueError:
                # if user input is not int 
                counter += 1
                continue
            else: 
                # if user enter three times wrong input
                if counter == 2:
                    # print answer and quit from this loop
                    print("{0} + {1} = {2}".format(fNumber,sNumber,answer))
                    break
                
                # if user input is not qual to random Number
                if answer != check:
                    print("EEE")
                    counter += 1
                    continue
                else:
                    # if user input and random number is qual 
                    # increment points
                    points += 1
                    break

    # print score result
    print(f"Score: {points}")



def get_level():

    while True:
        try:
            temp = int(input("Level: "))
        except ValueError:
            # pass this round and
            # ask again
            continue
        else:
            # check for invalid input
            if temp not in [1,2,3]:
                continue
            else:
                return temp


def generate_integer(level):

    if level == 1:
        return int(randint(0,10))
    elif level == 2:
        return int(randint(10,99))
    else:
        return int(randint(100,999))


if __name__ == "__main__":
    main()
