############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



import random

def main():
    input_user = valid_input("Level: ")
    rand_number = random.randint(0,input_user)

    while True:
        user = valid_input("Guess: ")
        if user == 1 and input_user == 1:
            print("Just right!")
            break

        if user < rand_number:
            print("Too small!")
        
        elif user > rand_number:
            print("Too Large!")
        
        else:
            print("Just right!")
            break

def valid_input(message_in):
    """ This function only return a int Number """
    while True:
        try:
            temp = int(input(message_in))
            if temp <= 0:
                continue
        except ValueError:
            continue
        else:
            return temp


if __name__ == "__main__":
    main()
