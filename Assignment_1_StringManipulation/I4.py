

big=1
i=0
print("Enter List of Words(* to stop entering)")
lst=[]
while True:
    sg=input("Enter Word: ") 
    lst.insert(i,sg)
    if '*' not in lst:
        if len(lst[i])>big:
            big=len(lst[i])
    else:
        break
    i=i+1
print("Length of longest Word is : ",big)
