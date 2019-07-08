N=int(input("Enter a Number of your choice: "))
L=int(input("Enter a Lower Limit: "))
M=int(input("Enter an Upper Limit: "))
if L>=M:
    print("Invalid Range Entered.")
elif N==L or N==M:
    print(N,"lies on Boundary.")
elif N>L and N<M:
    print(N,"lies inside given Range.")
else:
    print(N,"does NOT lie in given range.")