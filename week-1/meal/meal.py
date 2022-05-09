############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


user = input("What time is it? ").strip()

hour,time =user.split(":")
hour = int(hour)

if(7 <= hour <= 8):
    print("Breakfast time")
elif(12 <= hour <= 13):
    print("lunch time")
elif(18 <= hour <= 19):
    print("dinner time")
