amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    in_put = int(input("Insert Coin: "))

    if (in_put in [5,10,25]):
        amount -= in_put


print(f"Chane owed: {abs(amount)}")
