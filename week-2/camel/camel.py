user = input("camelCase: ").strip()

# iterrate in each character in user input string
for char_each in user:
    if(char_each.isupper()):
        # if i character in user string is uppercase
        #  so we print _ before print it
        print("_",end="")
    print(char_each.lower(),end="")

# print new line
print("")