# get input from user and strip it and force it to be UPPER case
user = input("Greeting: ").strip().upper()


if ("HELLO" in user):
    print("$0")
# if user input start with H so print 20 $ 
   
elif(user[0] == 'H'):
    print("$20")

# else just print $100    
else:
    print("$100")