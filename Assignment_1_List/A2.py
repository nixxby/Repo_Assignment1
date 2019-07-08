print("Enter list of Numbers. Any character to end.")
try:
    my_list1=[]
    while True:
        my_list1.append(int(input()))
except:
    print("List 1:",my_list1)
my_list1.remove(min(my_list1))
print("Second Smallest No. in list is",min(my_list1))