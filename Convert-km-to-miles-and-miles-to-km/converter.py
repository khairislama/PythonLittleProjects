
print(" *** WELCOME TO KM->MI OR MI->KM CONVERTOR *** ")
method=0
km=0
mi=0
ratio= 0.621371  #1Km = 0.621371 miles
while (method!=1 and method !=2):
    print("Enter 1 to convert Kilometers to Miles")
    print("Enter 2 to convert Miles to Kilometers")
    try:
        method = int(input("Your choice : "))
    except:
        print("Please enter a valid number! ")

if (method==1):
    while km==0:
        try:
            km = int(input("Enter the value in kilometers to convert : "))
        except:
            print("Please enter a valid number! ")    
    mi = km*ratio
    format_mi = "{:.2f}".format(mi) # format our value to only have 2 decimals 
    print(km, "km in miles : ", format_mi, "mile")
    
if (method==2):
    while mi==0:
        try:
            mi = int(input("Enter the value in miles to convert : "))
        except:
            print("Please enter a valid number! ")     
    km = mi/ratio
    format_km = "{:.2f}".format(km)
    print(mi, "mile in kilometers : ", format_km, "km")