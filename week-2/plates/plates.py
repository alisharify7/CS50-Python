def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def num_in_str(a):
    if a == " ":
        return True
    array = a.split()
    for each in array:
        if (each.isnumeric()):
            continue
        return False
    return True


def is_valid(s):
    #cheack for length
    if (len(s) > 6 or len(s) < 2):
        return False
    temp = ''
    # check for find first number and cheack is a 0 or not
    for let in range(len(s)):
        # if each var is a number so we found first number in string
        if (s[let].isnumeric()):
            # if first number we found is a number
            # return false
            if s[let] == '0':
                return False
            # if first number is not 0 so just break
            temp = s[let:]
            break
    if temp != " ":
        res = num_in_str(temp)
        if res != True:
            return False
    return True


if __name__ == "__main__":
    main()