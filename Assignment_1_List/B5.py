print("Enter list of Numbers. Any character to end.")
try:
    my_list1=[]
    while True:
        my_list1.append(int(input()))
except:
    print("List of Numbers:",my_list1)
print("Smallest:",min(my_list1))
print("Largest:",max(my_list1))
summ=0
for i in my_list1:
    summ+=i
print("Sum:",summ)
