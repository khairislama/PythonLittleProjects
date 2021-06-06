print(" *** WELCOME TO REMOVE PUNCTUATIONS *** ")
punctuations = '!{()}[]-;:\,<>./?@#\'"$%^&*_~'
string = input('Enter your string to remove punctuations : ')

newString = ''
for char in string:
    if char not in punctuations:
        newString+=char
        
print('You\'re new string without punctuations ')
print(newString)