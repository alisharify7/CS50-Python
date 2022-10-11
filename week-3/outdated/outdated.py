############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################




dates = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user = input("Date: ").strip()
    # check if user input like this => 8/9/2021
    # then we split it
    if "/" in user :
        try:
                m,d,y = user.split("/")
                # m = month / d = day / y = year
                m = int(m)
                d = int(d)
                y = int(y)
                # check if day greater than 31 days
                if (d > 31 or d < 1):
                    # pass this round
                    continue
                # if month input is greater than 12   
                if( m > 12 or m < 1):
                    # pass this round
                    continue
                if y < 999:
                    continue    
                # print result and exit from loop
                print(f"{y:04}-{m:02}-{d:02}")
                break
         # if user input not correct like => 7/a/50as
         # do this loop agian   
        except ValueError:
            pass
    else:
        # if user input month name
        try:
            m,d,y = user.split(" ")
            if ("," in d):
                # if user type month name like => september 8, 2021
                # split with white space's and remove ',' from day
                d = d.replace(","," ")
            y = int(y)
            d = int(d)
            # if day input is greater than 31   
            if d > 31 or d < 1:
                # pass this round
                continue
            if y < 999:
                continue
            # search for index of month name use type it
            # with this condition first see is month name in list or not !
            if m.title() in dates:
                # store index of month in loc 
                location = dates.index(m.title())
                # if month and day are equal
                # increment month one
                if (location == d):
                    location+=1
                # print answer and break loop    
                print(f"{y}-{location:02}-{d:02}")
                break
            else:
                continue

        except:
            pass
