# m=[[1,2,3],[4,5,6],[7,8,9]]
# for r in m:
#     for c in r:
#         print(c,end=" ")
#     print()
# GENERAL WAY TO REPRESENT MATRIX:
# m=[[1,2,3],[4,5,6],[7,8,9]]
# for r in range (len(m)):
#     for c in range (len(m[0])):
#         print(m[r][c],end=" ")
#     print()
# TAKING INPUT FROM USER FOR 3X3 MATRIX:
# m=[]
# for r in range(3):
#     row=input("Enter a value for rows: ")
#     row = row.split()
#     row=[int(i) for i in row]
#     m.append(row)
# print(m)
# ITS ALTERNATIVE WITHOUT USING SPLIT FUNCTION:
# m=[]
# for  r in range(3):
#     row=[]
#     for c in range(3):
#         val=int(input(f"Enter Value for row {r} and coloumn {c}: "))
#         row.append(val)
#     m.append(row)
# print(m)
# INCREMENT A MATRIX AND STORE THE RESULT IN A NEW MATRIX:
# m=[[1,2,3],[4,5,6],[7,8,9]]
# m1=[]
# for r in m:
#     row=[]
#     for c in r:
#         row.append(c+1)
#     m1.append(row)
# print(m1)
# INCREMENT A MATRIX AND STORE THE RESULT IN A SAME MATRIX:
m=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(m)):
    for c in range (len(m[0])):
     m[r][c]+=1
print(m)