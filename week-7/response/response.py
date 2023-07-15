from validator_collection import email
from validator_collection.errors import InvalidEmailError



def main():
    x = (IS_VALID_EMAIL(input("What's your email address? ")))
    if x:
        print("Valid")
    else:
        print("Invalid")


def IS_VALID_EMAIL(s):
    """This Function Validation s is valid email or not"""
    try:
        email(s)
    except InvalidEmailError:
        return False

    return True




if __name__ == "__main__":
    main()