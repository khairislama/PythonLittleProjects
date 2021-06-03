print(" *** WELCOME TO LEAP YEAR PROGRAM *** ")
year=0
leap=False
while year<500:
    try:
        year = int(input("Enter the year : "))
    except:
        print("Please enter a valid year! ")
        
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            leap=True
    else:
        leap=True
    
if leap==True:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))