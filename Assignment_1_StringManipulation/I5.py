s=input("Enter a string: ")
srev=""
if len(s)%4==0:
    print("Reversed String is :")
    for i in range(len(s),0,-1):
        srev+=s[i-1]
    print(srev)

else:
    print("String NOT Reversed.")