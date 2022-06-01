############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################




import requests
import sys


if len(sys.argv) == 2:

    # covert command line argument to float Number
    try:    
        user_input = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not number")
    # if yser input in not Number
        sys.exit(1)
else:
    # if user not cooperate and Enter a Number
    print("Missing command-line argument")
    sys.exit(1)

try:
    # calling api
    answer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price = float(answer['bpi']['USD']['rate_float'])
    price = price * user_input
    print(f"${price:,.4f}")
    sys.exit(0)

except (requests.RequestException,ValueError):
    print("Error")
    sys.exit(1)
