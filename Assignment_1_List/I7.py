print("Enter words: (type <> to stop entering): ")
my_list =[]
string=""
while True:
    string=input("String Input: ")
    if string=="<>":
        break
    my_list.append(string)
print("\nList combined as a String: ")
string=' '.join(my_list)
print(string)