print(" *** WELCOME TO CHECK ODD OR EVEN *** ")
num=None

while num==None:
    try:
        num = int(input("Enter you number to check if Odd or even : "))
    except:
        print("Please enter a valid number! ")
        
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")