print(" *** WELCOME TO SUM PRIME DIGITS *** ")
print("First things first, Enter your list : ")
myList = []
counter = 1
num=None
div=None
while True:
    num = input("Enter your value number {0} in the list ( '%' to end ) : ".format(counter))
    if num == '%':
        break
    try:
        num = int(num)
        myList.append(num)
        counter+=1
    except:
        print('Please enter a valid number')

while div==None:
    try:
        div = int(input("Enter the number to ty and divid on : "))
    except:
        print("Please enter a valid number")

result = list(filter(lambda x: (x%div==0), myList))
print("Numbers divisible by",div,"are",result)