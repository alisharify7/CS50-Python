amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    user = int(input("Insert Coin: "))

    if (user in [5,10,25]):
        amount -= user

#    print(f"Amount Due: {amount}")

print(f"Chane owed: {abs(amount)}")
