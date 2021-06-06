print(" *** WELCOME TO SUM PRIME DIGITS *** ")
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
    if rem>1:
        for i in range(2, rem):
            if (rem%i)==0:                
                break
        else:
            result=result+rem    
    num=int(num/10)        

print("Sum of all digits of",hold,"is:",result)    