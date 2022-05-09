############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



shop_item = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_bud = 0

while True:
    try:
        user = input("Item: ").strip().title()
        # if user input is in shop_item then calculate Price
        if user in shop_item:
            total_bud += shop_item[user]
            # print now total price
            print(f"${total_bud:.2f}")
    # if user input ctrl+d end program
    except EOFError:
        print("")
        break


