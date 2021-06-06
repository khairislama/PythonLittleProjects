print(" *** WELCOME TO ADD TWO BINARY NUMBERS *** ")

num1 = input("Enter your first binary number to add : ")
num2 = input("Enter your second binary number to add : ")

try:
    sum = bin(int(num1, 2) + int(num2, 2))
    print(sum)
except:
    print("Please enter a valid binary number")