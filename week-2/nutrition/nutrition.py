############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################




#defind a doctionary for keep all fruits name and calories
fruits={
    'apple':'130',
    'avocado':'50',
    'banana':'110',
    'cantaloupe':'50',
    'grapefruit':'60',
    'grapes':'90',
    'honeydew melon':'50',
    'kiwifruit':'90',
    'lemon':'15',
    'lime':'20',
    'nectarine':'60',
    'orange': '80',
    'peach':'60',
    'pear':'100',
    'pineapple':'50',
    'pineapple':'70',
    'strawberries':'50',
    'sweet cherries':'100',
    'tangerine':'50',
    'watermelon':'80'
    }


# get input from user
in_put = input("Item: ").lower()
if in_put not in fruits:
    exit(0)
print(f'Calories: {fruits[in_put]}')
