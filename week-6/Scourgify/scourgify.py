############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################

import os,sys, csv


# header of new csv file
file_headers = ["first", "last", "house"]  


def check_command_line():
    """
        This function check the command line argument is correct by the rule
    """
    if len(sys.argv) > 3:
        sys.exit("to many")
    
    if len(sys.argv) < 3:
        sys.exit("to Few")


def nomalize_data(oldfile):
    """
        This function take an csv and return all data in correct format in list  
    """
    db = []
    reader = csv.DictReader(oldfile)
    
    for each in reader:
        temp = {}
        temp["last"], temp["first"] = each["name"].split(",")
        
        # remove white spaces
        temp["first"] = temp["first"].strip()
        temp["last"] = temp["last"].strip()
        
        temp["house"] = each["house"]
        db.append(temp)
    return db


def cr_csv(data, filename):
    """
        This function take an data in form of list and create new csv
         and write to ot
    """
    with open(filename, "w", encoding="UTF8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=file_headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    check_command_line()
    try:
        file = open(sys.argv[1], "r", encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} not found")

    # clean data
    data = nomalize_data(file)

    # create new file
    cr_csv(data, sys.argv[2])


    file.close()







if __name__ == "__main__":
    main()


