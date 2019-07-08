string=input("Enter a string: ")
list1=list(string)

for i in range(1,len(list1)):
    if list1[i]==list1[0]:
        list1[i]='$'
        string=''.join(list1)
print("Converted String is:",string)