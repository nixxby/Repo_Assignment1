sng=input("Enter string: ")

i1=sng.find('not')
i2=sng.find('poor')

if i1<i2:
    i2+=4
    s=""
    for i in range(0,i1):
        s+=sng[i]
    s=s+"good"
    for i in range(i2,len(sng)):
        s+=sng[i]
print("New String is: ",s)    
    