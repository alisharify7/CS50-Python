############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharify7             #
#                                          #
############################################



import sys
import time

# get user input
user= int(input("Enter Kilogram: "))

# calculate answer
ans = user * 300000000 ** 2

for i in range(1,4):
    print("W",end="")
    print("." * i)
    time.sleep(0.5)

print(ans)
