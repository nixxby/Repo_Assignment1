# To find n + nn + nnn

n=int(input("Enter any Number"))
sum1=0
for i in range(1,4):
    print(n,end="")
    if i!=3: 
        print(" + ",end="")
    sum1=sum1+n
    n=n+(n*10)
    
print(" = ",sum1) 
    