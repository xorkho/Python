# Input number from user and put in list
# L=[]
# for i in range(5):
#     n=int(input("Enter intger"))
#     L.extend([n])
# print(L)
# SPLIT INTO SPACES:
# L=[]
# n=input("Enter intger: ")
# n=n.split()
# for i in n:
#     L.extend([int(i)])
# print(L)
# ACRONYM OF A GIVEN WORD:
# name=input("Enter a word ")
# name=name.split()
# acr=""
# for i in name:
#     word=i[0]+"."
#     acr+=word
# acr=acr.upper()
# print("ACRONYM: ", acr)
D={3:"biryani",2:"Qorma",5:"Pulao"}
print(D.update(4,"item"))