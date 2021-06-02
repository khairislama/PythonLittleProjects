print(" *** WELCOME *** ")
num1=None
num2=None
num3=None
print("Please enter your three numbers to compare")
while num1==None:
    try:
        num1 = int(input("First number : "))
    except:
        print("Please enter a valid number! ")
        
while num2==None:
    try:
        num2 = int(input("Second number : "))
    except:
        print("Please enter a valid number! ")
        
while num3==None:
    try:
        num3 = int(input("Third number : "))
    except:
        print("Please enter a valid number! ")
        
if (num1<=num2) and (num1<=num3):
    min_number=num1
    if num2<=num3:
        max_number=num3
    else:
        max_number=num2
elif (num2<=num1) and (num2<=num3):
    min_number=num2
    if num1<=num3:
        max_number=num3
    else:
        max_number=num1
else:
    min_number=3
    if num1<=num2:
        max_number=num2
    else:
        max_number=num1

print("The smallest number among ",num1, ", ",num2," and ",num3," is: ", min_number)
print("And the max number is: ",max_number)