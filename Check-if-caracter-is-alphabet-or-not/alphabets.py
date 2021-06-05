import getch
print("Enter a caracter : ")
ch = getch.getch()
print(ch,'is an alphabet') if ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')) else print(ch,'is not an alphabet')
