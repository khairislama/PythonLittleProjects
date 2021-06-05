print(" *** WELCOME TO CALCULATOR *** ")
num1=None
num2=None
while num1==None:
    try:
        num1 = float(input("Enter your first number : "))
    except:
        print("Please enter a valid number! ")

while num2==None:
    try:
        num2 = float(input("Enter your second number : "))
    except:
        print("Please enter a valid number! ")

switcher = {
    '+': num1+num2,
    '-': num1-num2,
    '*': num1*num2,
    '/': num1/num2,
}
print("Enter which operation would you like to perform? ")
operator = input("Enter your operator (+,-,*,/) here : ")

print("{:.3f}".format(switcher.get(operator, 'Invalid operator')))