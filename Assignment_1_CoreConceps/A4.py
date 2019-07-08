# Show true if equal or sum/diff is 5

n1= int(input("Enter Number 1: "))
n2= int(input("Enter Number 2: "))

if n1==n2 or n1+n2==5 or n1-n2==5 or n2-n1==5:
    print("True")
else:
    print("False")
