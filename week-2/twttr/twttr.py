user = input("Input: ").strip()

print("Output: ",end="")
for letter in user:
    if (letter.upper() in ['A', 'E', 'I', 'O', 'U']):
        continue
    print(letter,end="")
print("")
