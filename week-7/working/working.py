import re
import sys


def main():
    print(convert(input("Hours: ")))
    

def convert(s):
    def is_valid_60_minute(m):
        m = int(m)
        return True if 59 >= m >= 0 else False

    def is_valid_12_hour(h):
        h = int(h)
        return True if 12 >= h >= 1 else False

    def convert_2_24h(flag, h, minute):
        if not minute:
            minute = 0
        hour = int(hour)

        if not is_valid_12_hour(hour):
            raise ValueError
        if not is_valid_60_minute(minute):
            raise ValueError

        if flag == "am":
            if hour == 12:
                hour = "00"
            else:
                hour = str(hour)
                new_hour = str(hour)
        if flag == "pm":
            if hour == 12:
                hour = "12"
            else:
                hour += 12
                hour = str(hour)
                new_hour = str(hour)

        minute = str(minute)
        new_hour = hour.zfill(2) # add 0 => 2 =>> 02
        new_minute = minute.zfill(2) # add 0
        return f"{new_hour}:{new_minute}"


    regex = r"^([0-9]{1,2})(\:)?([0-9]{2,2})? (AM|PM)" + " TO " + "([0-9]{1,2})(\:)?([0-9]{1,2})? (AM|PM)$"
    result = re.search(regex, s, flags=re.IGNORECASE)

    if result:
        hour1,colm1,minute1,flag1,hour2,colm2,minute2,flag2 = result.groups()
        if not flag1 or not flag2 or not hour1 or not hour2:
            raise ValueError
        first_time = convert_2_24h(flag1, hour1, minute1)
        second_time = convert_2_24h(flag2, hour2, minute2)
        return f"{first_time} to {second_time}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()