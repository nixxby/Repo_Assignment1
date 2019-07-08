def findsum(n,d):
    if d==1:
        return 1
    elif n%d==0:
        return d
    else:
        return 0

N=int(input("Enter a Number:"))
sum = 0

for i in range(N-1,0,-1):
    sum = sum + findsum(N, i)
if sum==N:
    print(N,"is a Perfect Number.")
else:
    print(N,"is NOT a perfect number.")
