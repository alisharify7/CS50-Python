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