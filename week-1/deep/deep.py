# get input from user and strip it and force it to be UPPER case
user = input("What is the Answer to the Great Question of Life, the universe, and Everything? ").strip().upper()

#condition for check user input
if (user in ['42','FORTY-TWO', 'FORTY TWO']):
    print("Yes")
else:
    print("No")    
