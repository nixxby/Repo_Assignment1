#add ing or ly to a string

strng=input("Enter any String: ")

if len(strng)>=3:
    if strng.endswith("ing"):
        strng=strng + "ly"
    else:
        strng=strng + "ing"
    print("Changed String is : ",strng)
else:
    print("String Unchanged!!")
    