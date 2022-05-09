############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def end_str(a):
    if a == " ":
        return True
    array = a.split()
    for each in array:
        if (each.isnumeric()):
            continue
        return False
    return True


def is_valid(s):
    #check for length and check is first element is number of not
    if (s[0].isnumeric() and s[1].isnumeric()):
        return False
    if (len(s) > 6 or len(s) < 2):
        return False
    tempo = ''
    # check for find first number and cheack is a 0 or not
    for one in range(len(s)):
        # if each var is a number so we found first number in string
        if (s[one].isnumeric()):
            # if first number we found is a number
            # return false
            if s[one] == '0':
                return False
            # if first number is not 0 so just break
            tempo = s[one:]
            break
    if temp != " ":
        resault = end_str(tempo)
        if resault != True:
            return False
    return True


main()
