def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    temp = d.replace("$","")
    temp = float(temp)
    return temp


def percent_to_float(p):
    temp = p.replace("%","")
    temp = (int(temp) / 100)
    return temp


main()


# another way with string sliceing method
#def main():
#    dollars = dollars_to_float(input("How much was the meal? "))
#    percent = percent_to_float(input("What percentage would you like to tip? "))
#    tip = dollars * percent
#    print(f"Leave ${tip:.2f}")


#def dollars_to_float(d):
#    d = d[1:]
#    d = float(d)
#    return d


#def percent_to_float(p):
#    temp = p
#    location = temp.find("%")
#    temp = temp[:location]
#   temp = int(temp)
#    return (temp / 100)


#main()
