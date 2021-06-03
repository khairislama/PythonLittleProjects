print(" *** WELCOME TO COUNT VOWLES *** ")

vowles = 'aeiou'
string = input("Enter your string : ")

string = string.casefold() # minuscule

count = {}.fromkeys(vowles,0)

for char in string:
    if char in count:
        count[char] +=1

print(count)