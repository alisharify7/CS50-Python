import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    res = re.search(regex, ip)
    if not res:
        return False
    
    # check for find 4 section in ip
    if len(res.groups()) == 4:
        
        for gp in res.groups():
            # check each section of ip should be number
            try:
                gp = int(gp)
            except ValueError:
                return None
            
            # check each section of ip should between 0-255 ==>  2^8 - 1
            if gp >= 0 and gp <= 255:
                pass
            else:
                return False
        return True
    
    # section1 . section2 . section3 .section4
    # if ip is not 4 section
    else:
        return False


if __name__ == "__main__":
    main()
