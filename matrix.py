st=input("Enter a word: ")
sep=" "
L=[]
chunk=" "
for i in st:
    if i!=sep:
      chunk+=i
    else:
        L+=[chunk]
        chunk=" "
if chunk!=" ":
    L+=[chunk]
print(L)