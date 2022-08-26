#odd/even game method 1
import random
a=random.randint(1,9)
b=random.randint(1,9)
print(a,b)

if(a%2 ==0 and b%2 ==0):
    print("Number is even and you won the game")
else:
    print("Number is odd and you lost the game \n Try again")
