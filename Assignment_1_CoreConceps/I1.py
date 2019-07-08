# Swap with and without temp

a=4
b=7
temp=a
a=b
b=temp
print("Swapped with temp :")
print("a=",a,"  b=",b)

a=a+b
b=a-b
a=a-b
print("Swapped without temp :")
print("a=",a,"  b=",b)
