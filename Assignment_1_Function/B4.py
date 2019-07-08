string=input("Enter a String:")
flag=1
for i in range(0,int(len(string)/2)):
    if string[i]!=string[len(string)-i-1]:
        flag=0
if flag==1:
    print(string,"is a Palindrome.")
else:
    print(string,"is not a Palindrome.")
