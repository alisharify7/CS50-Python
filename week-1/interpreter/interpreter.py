#solve this problem with two way :)

user = input("Expression: ").strip()

if ("/" in user):
    temp = user.index("/")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) / float(seccond))
elif ("*" in user):
    temp = user.index("*")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) * float(seccond))
elif ("+" in user):
    temp = user.index("+")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) + float(seccond))
elif ("-" in user):
    temp = user.index("-")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) - float(seccond))


# seccond way to solve this problem

# user = input("Expression: ")
# split_variable = user.split()

# first = int(split_variable[0])
# seccond = float(split_variable[2])

# if (split_variable[1] == '*'):
#     print(first * seccond)
# elif(split_variable[1] == '/'):
#     print(first / seccond)
# elif(split_variable[1] == '+'):
#     print(first + seccond)
# elif(split_variable[1] == '-'):
#     print(first - seccond)
