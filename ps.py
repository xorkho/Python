# l=[]
# val=input("Enter 5 integer: ")
# val=val.split()
# for i in val:
#     l.extend([int(i)])
# print(l)
#version 3
# val=input("Enter 5 integer: ")
# val=val.split()
# val=[int(i) for i in val]
# print(val)
# version 4
# l=[]
# val=input("enter an integer: ")
# val=val.split()
# for i in val:
#     i=int(i)
#     l+=[i]
# print(l)
# version 5
# val=input("enter an integer: ")
# val=val.split()
# for i in range(len(val)):
#     val[i]=int(val[i])
# print(val)
# ACRONYM
term=input("enter a word: ")
term=term.split()
acr=" "
for i in term:
    acr+=i[0]
acr=acr.upper()
print(acr)