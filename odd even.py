#odd/even game method 2
print("Lets Play odd/even game ")
a=int(input("enter the first number \n"))
b=int(input("Enter the second number \n"))
print(a,b)
if(a%2==0 and b%2==0) :
    print("Number is even and you won the game")
else:
    print("Number is odd and you lost the game \n you can try again")
