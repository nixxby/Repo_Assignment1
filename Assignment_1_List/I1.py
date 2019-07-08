print("Enter Various Strings (type <> to stop entering): ")
my_list =[]
plist=[]
string="q"
while True:
    string=input("String Input: ")
    if string=="<>":
        break
    my_list.append(string)
    if len(string)>2:
        if string[0]==string[-1]:
            plist.append(string)
print("\nStrings You Entered:")
print(my_list)
print("\nStrings that satisfy given Condition: ")
print(plist)