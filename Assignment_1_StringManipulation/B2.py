# no. of characters in a string

strng=input("Enter the String: ")
l=0
for i in strng:
    if i==' ':
        l=l+1

print("Number of characters = ",len(strng)-l)
