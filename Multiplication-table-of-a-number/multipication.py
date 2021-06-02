print(" *** WELCOME TO MULTIPLICATION TABLE OF A NUMBER *** ")
num=None

while num==None:
    try:
        num = int(input("Enter the number : "))
    except:
        print("Please enter a valid number! ")
        
print("The multiplication table of", num)
for i in range(1,11):
    print(num,"X",i,"=",num*i)