############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d[1:]
    d = float(d)
    return d


def percent_to_float(p):
    temp = p
    location = temp.find("%")
    temp = temp[:location]
    temp = int(temp)
    return (temp / 100)


main()

# -------------------------------------------------------------------------
# another way ===

# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     # replace $ with white space
#     temp = d.replace("$","")
#     temp = float(temp)
#     return temp


# def percent_to_float(p):
#     # in here we replace % with white space
#     temp = p.replace("%","")
#     # in here we divid temp to 100 to get us a decimal number like 15 ==> 0.15
#     return (int(temp) / 100)

# main()
