str = input("Please enter the text : ")
for i in str:
    if i in ("!","@","#","$","%","^","&","*","(",")"):
        print("String is not accepted")
        break
else:
    print("String is accepted")