def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
N=int(input("Enter a Number of your choice: "))
print("Factorial of",N,"is:",fact(N))