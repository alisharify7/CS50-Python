############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


user = input("Input: ").strip()

print("Output: ",end="")

for let in user:
    if (let.upper() in ['A', 'E', 'I', 'O', 'U']):
        # skip this round
        continue
    else:
        # print corrent character
        print(let, end="")
    
# print new line    
print()
