string=input("Enter a string:")
rev=''
for i in string:
    rev = i + rev
print(rev,"is the reverse of",string)