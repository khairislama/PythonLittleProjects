terms=None

while terms==None:
    try:
        terms = int(input("Enter how many terms you want to display : "))
    except:
        print("Please enter a valid number")

result = list(map(lambda x: x**2, range(terms)))

print("The total terms are :",terms)
for i in range(terms):
    print("2 raised to power",i,"is",result[i])