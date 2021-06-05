
print(" *** WELCOME TO Celsius->Fahrenheit OR Fa->Ce CONVERTOR *** ")
method=0
celsius=0
fahrenheit=0
ratio= 32 
while (method!=1 and method !=2):
    print("Enter 1 to convert Celsius to Fahrenheit")
    print("Enter 2 to convert Fahrenheit to Celsius")
    try:
        method = int(input("Your choice : "))
    except:
        print("Please enter a valid number! ")

if (method==1):
    while celsius==0:
        try:
            celsius = int(input("Enter the value in celsius to convert : "))
        except:
            print("Please enter a valid number! ")    
    fahrenheit = ( celsius * 9/5 ) + ratio
    print('%0.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
    
if (method==2):
    while fahrenheit==0:
        try:
            fahrenheit = int(input("Enter the value in fahrenheit to convert : "))
        except:
            print("Please enter a valid number! ")     
    celsius = (fahrenheit-ratio) * 5/9    
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))