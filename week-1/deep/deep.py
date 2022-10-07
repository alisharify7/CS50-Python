############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



# get input from user and strip it and force it to be UPPER case
user = input("What is the Answer to the Great Question of Life, the universe, and Everything? ").strip().upper()

# searching for 4222222222222222222
if (user in ['42','FORTY-TWO', 'FORTY TWO']):
    print("Yes")
else:
    print("No")    
