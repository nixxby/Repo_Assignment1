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

print("\nAfter Removing Duplicates: ")

def remove(f_list):
    plist=[]
    for s in f_list:
        if s not in plist:
            plist.append(s)
    return plist
print(remove(my_list))
