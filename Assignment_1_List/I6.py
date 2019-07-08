print("Enter Various Strings (type <> to stop entering): ")
my_list =[]
string=""
while True:
    string=input("String Input: ")
    if string=="<>":
        break
    my_list.append(string)
print("\nStrings You Entered: ")
print(my_list)

print("\nUnique elements of list: ")

def unique(f_list):
    plist=[]
    for s in f_list:
        if f_list.count(s)<=1:
            plist.append(s)
    return plist
print(unique(my_list))
