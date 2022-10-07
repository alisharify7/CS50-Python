############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



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




# better version of this program using regex
"""
import re 


x = input("")
def better_version(input):
    if not input:
        return "Empty"

    result = re.sub(" ","...",input)
    return result

print(better_version(x))
"""