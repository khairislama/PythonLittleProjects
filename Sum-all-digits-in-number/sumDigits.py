print(" *** WELCOME TO SUM DIGITS *** ")
num=None
result=0
while num==None:
    try:
        num = int(input("Enter you number to calculate the sum of it's digits : "))
    except:
        print("Please enter a valid number! ")

hold=num
while num>0:
    rem=num%10
    result=result+rem
    num=int(num/10)        

print("Sum of all digits of",hold,"is:",result)    