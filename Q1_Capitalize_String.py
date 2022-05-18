str = input("Please enter the text : ")
str1=str.title()
for i in str1.split():
    i = i[:-1]+i[-1].upper()+" "
    print(i,end=" ")