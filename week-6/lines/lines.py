############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################

import sys


def main():
    """
    From main we call all other function for run
    """
    # check command line argument
    check_command_line_file()

    # read file and return number of line of code in it
    line = read_content(sys.argv[1])
    print(line)

def check_command_line_file():
    """
    This function check command line argument
    """
    if len(sys.argv) > 2:
        print("to Many command-line argument ")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("to few command-line argument ")
        sys.exit(1)

    # check input file is a python file or nots
    if ".py" not in sys.argv[1]:
        print("Not a python file")
        sys.exit(1)


def read_content(FileInput):
    """
    This function read all content of file and split comments and codes
    """
    line_counter = 0
    try:
        with open(FileInput,encoding='utf8') as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        print("File Not Found")
        sys.exit(1)

    # remove all white spaces and comments
    for line in file_lines:
        if line.strip().startswith("#"):
            pass
        elif line.strip() == "":
            pass
        else:
            line_counter +=1
    return line_counter


if __name__ == "__main__":
    main()
