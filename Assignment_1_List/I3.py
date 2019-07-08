print("Enter Various Strings (type <> to stop entering): ")
my_list =[]
plist=[]
string="q"
while True:
    string=input("String Input: ")
    if string=="<>":
        break
    my_list.append(string)
if len(my_list)==0:   
    print("Empty List !!!")
else:
    print("List Not Empty.")
