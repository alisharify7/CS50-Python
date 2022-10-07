############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


"""
This is simple version
"""
import sys
def main():

    # get input from user
    user = input()
    #iterate to each charactor
    for i in range(len(user)):

        if (user[i] == ":"):
            # get corecctly char with + 1 to function
            tmp = user[i] + user[i+1]
            convert(tmp)
            continue

        if (user[i] in [")","("]):
            continue

        else:
            print(user[i],end="")
    # orint new line
    print()
# defind convertor function of emojies
def convert(inp):

    if (inp == ":)"):
        print("🙂",end="")
    elif (inp == ":("):
        print("🙁",end="")
main()





# this is a better version of program using regex library 
"""

x = input("")
import re
def better_version(input):
    # this function using regex for find :) and :(  from text 
    if not input:
        return "empty input"
    
    # regex for find all :) in str
    regex_smile_face = ":\)"
    # replace all str via regex 
    result = re.sub(regex_smile_face,"🙂",input)

    # regex for find all :( in str
    regex_sad_face = ":\("
    # replace all str via regex 
    result = re.sub(regex_sad_face,"🙁",result)
    
    return (result)



print(better_version(x)) 

"""