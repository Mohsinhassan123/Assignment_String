str = input("Enter text to count the number of vowels :")
count=0
for i in str:
    if i.lower() in ("a","e","i","o","u"):
        count+=1
    
print("Vowels =",count)
