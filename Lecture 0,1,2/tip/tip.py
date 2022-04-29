def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    temp = d.replace("$","")
    temp = temp.strip()
    temp = float(temp)
    temp = int(temp)
    return temp


def percent_to_float(p):
    temp = p.replace("%","")
    temp = temp.strip()
    temp = (int(temp) / 100)
    return temp


main()
