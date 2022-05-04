import sys
import time


user= int(input("Enter Kilogram: "))

ans = user * 300000000 ** 2
for i in range(1,4):
    print("W",end="")
    print("." * i)
    time.sleep(0.5)

print(ans)