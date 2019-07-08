print("Enter list 1 of Numbers. Any character to end.")
try:
    my_list1=[]
    while True:
        my_list1.append(int(input()))
except:
    print("List 1:",my_list1)
print("\nEnter list 2 of Numbers. Any character to end.")
try:
    my_list2=[]
    while True:
        my_list2.append(int(input()))
except:
    print("List 2:",my_list2)
flag=0
for i in my_list1:
    if i in my_list2:
        flag=1
if flag==1:
    print("True.Both lists have at least one member in common.")
else:
    print("False.Both lists have no member in common.")