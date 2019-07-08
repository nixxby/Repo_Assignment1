print("Enter LIST of Numbers. Any character to end.")
try:
    my_list1=[]
    while True:
        my_list1.append(int(input()))
except:
    print("List:",my_list1)
print("\nEnter SUBLIST of Numbers. Any character to end.")
try:
    my_list2=[]
    while True:
        my_list2.append(int(input()))
except:
    print("SubList:",my_list2)
flag=1
for i in my_list2:
    if i not in my_list1:
        flag=0
if flag==0:
    print("NOT a SUBLIST")
else:
    print(my_list2,"is a subset of",my_list1)