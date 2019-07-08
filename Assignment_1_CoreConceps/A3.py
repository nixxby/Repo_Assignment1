# If 2 numbers are equal, return sum 0

n1=int(input("Enter Number 1 : "))
sum1=n1
n2=int(input("Enter Number 2 : "))
if n1==n2:
    sum1=0
else:
    sum1=sum1+n2
    n3=int(input("Enter Number 3 : "))
    if n3==n2 or n3==n1:
        sum1=0
    else:
        sum1=sum1+n3
print("Sum = ",sum1)