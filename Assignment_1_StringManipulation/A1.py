string=input("Enter the String: ")
if len(string)>2:
    l=len(string)
    out=string[0:2]+string[l-2:l]
elif len(string)==2:
    out=string+string
else:
    out='Empty String!!'

print(out)