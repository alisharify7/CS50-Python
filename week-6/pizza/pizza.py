
############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



import sys
from tabulate import tabulate
import csv

def main():
    check_command_line()
    read_content(sys.argv[1])



def check_command_line():
    if len(sys.argv) > 2:
        sys.exit("to many command-line argument")
    elif len(sys.argv) < 2:
        sys.exit("few command-line argument")

    # check input file is csv file or not
    if '.csv' not in sys.argv[1]:
        sys.exit("Not a Csv file")

def read_content(file):
    header = []
    body = []
    try:
        with open(file) as file:
            reader = csv.reader(file)
            for index,value in enumerate(reader):
                # get first row ==> headers
                if index == 0: 
                    # added to header list
                    # and skip this round
                    header.append(value)
                    continue
    
                body.append(value)
        # print table # unpack list  # set table format    
        print(tabulate(body,*header,tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File Not Found")

if __name__ == "__main__":
    main()