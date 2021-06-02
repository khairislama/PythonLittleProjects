print(" *** WELCOME TO CHECK PRIME *** ")
num=None

while num==None:
    try:
        num = int(input("Enter you number to calculate factorial : "))
    except:
        print("Please enter a valid number! ")

if num>1:
    for i in range(2, num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is nor a prime number cause it's less than 1")