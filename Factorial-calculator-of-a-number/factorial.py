print(" *** WELCOME *** ")
num=None
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

while num==None:
    try:
        num = int(input("Enter you number to calculate factorial : "))
    except:
        print("Please enter a valid number! ")
        
if num <0:
    print("Factorial cannot be found for negative numbers")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))