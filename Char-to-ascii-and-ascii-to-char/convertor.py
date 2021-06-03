print(" *** WELCOME TO CHAR->ASCII//ASCII->CHAR CONVERTOR *** ")
num=-5
method=0
char="test123"
while (method!=1 and method !=2):
    print("Enter 1 to convert CHAR to ASCII")
    print("Enter 2 to convert ASCII to CHAR")
    try:
        method = int(input("Your choice : "))
    except:
        print("Please enter a valid number! ")

if (method==1):
    char = input("Enter a character : ")
    try:
        print(char,"in ascii is = ",ord(char), "in ASCII")
    except:
        print("We cannot transfert {0} to ascii".format(char))

if (method==2):
    while num<0:
        try:
            num = int(input("Enter your ascii number : "))
        except:
            print("Please enter a valid number! ")
    try:
        print(num,"in ascii is = ",chr(num), "in char")
    except:
        print("We cannot transfert {0} to char".format(num))