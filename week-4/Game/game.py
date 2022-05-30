import random

def main():
    input_user = valid_input("Level: ")
    rand_number = random.randint(0,input_user)

    while True:
        user = valid_input("Guess: ")
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
        except ValueError:
            continue
        else:
            return temp


if __name__ == "__main__":
    main()