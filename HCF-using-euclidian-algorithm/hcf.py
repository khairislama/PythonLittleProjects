print(" *** WELCOME TO HCF CALCULATOR USING EUCLIDIAN ALGORITHM *** ")
x=None
y=None
def calcule_hcf(x,y):
    while(y):
        x, y = y, x%y
    return x

while x==None:
    try:
        x = int(input("Enter x : "))
    except:
        print("Please enter a valid number! ")
        
while y==None:
    try:
        y = int(input("Enter y : "))
    except:
        print("Please enter a valid number! ")
        
if (x>y):
    x, y = y, x

print("The hcf of",x,"and",y,"is : ", calcule_hcf(x,y))