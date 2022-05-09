############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


import sys

# get input from user and strip all white space
s = input().strip()

# iterate of each character
for i in range(len(s)):
    if (s[i] == " "):
        print("...",end="")
        continue
    print(s[i],end="")

# new line in end program
print("")
