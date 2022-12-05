import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    res = re.search(regex, ip)
    if not res:
        return False
    if len(res.groups()) != 4:
        return False

    for gp in res.groups():
        try:
            gp = int(gp)
        except ValueError:
            return None

        if gp >= 0 and gp <= 255:
            pass
        else:
            return False
    return True



if __name__ == "__main__":
    main()