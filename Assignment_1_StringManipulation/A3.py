string1=input("Enter main string: ")
string2=input("Enter the string to be added: ")
stringf=""
for i in range(0,int(len(string1)/2)):
    stringf = stringf + string1[i]

stringf=stringf + string2

for i in range(int(len(string1)/2),len(string1)):           
    stringf = stringf + string1[i]

print(stringf)