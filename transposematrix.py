# TAKING INPUT MATRIX FROM USER:  
m=[]
for  r in range(3):
    row=[]
    for c in range(3):
        val=int(input(f"Enter Value for row {r} and coloumn {c}: "))
        row.append(val)
    m.append(row)
print(m)
# TAKING TRANSPOSE
A=[]
# ALTENATE CONDITION FOR TRANSPOSE
for c in range(len(m[0])):
    row=[]
    for r in range(len(m)):
        row.append(m[r][c])
    A.append(row)
print(A)