import sys
from PIL import Image, ImageOps


allowed_ext = ["png", "jpg", "jpeg"]


def check_command_line():
    """
        This function check if the input required 
        for command line argument if correct or not
    """
    if len(sys.argv) < 3:
        sys.exit("TOO Few command-line argument")
    if len(sys.argv) > 3:
        sys.exit("TOO Many command-line argument")


def check_arg_extension():
    # split from right and take last element result  list
    input_ext = sys.argv[1].rsplit(".")[-1]
    output_ext = sys.argv[2].rsplit(".")[-1]
    
    if output_ext.lower() not in allowed_ext:
        sys.exit(f"{output_ext} is not allowed")
    
    if input_ext.lower() not in allowed_ext:
        sys.exit(f"{input_ext} is not allowed")
    
    # check input and output extensions is same or not
    if input_ext.lower() != output_ext.lower():
        sys.exit("diffrent extenstion input and output") 


def main():
    # check command line
    check_command_line()
    
    # check user input file extensions is allowed or not
    check_arg_extension()

    # open shirt
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt can not open !")

    # open muppet image
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Shirt can not open !")

    # get size of shirt
    size = shirt.size

    # resize muppet image
    muppet = ImageOps.fit(muppet, size)

    # pase image
    muppet.paste(shirt, shirt)

    # save img
    muppet.save(sys.argv[2])

if __name__ == '__main__':
    main()


