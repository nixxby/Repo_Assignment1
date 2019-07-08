#Merge 2 strings with swap and space functionlities

strng1=list(input("Enter String 1: "))
strng2=list(input("Enter String 2: "))

print("Your Combined String is: ")
temp=strng1[0]
strng1[0]=strng2[0]
strng2[0]=temp
strng=strng1 + [" "] + strng2
print("".join(strng))
