A=[]
B=[]
print("Enter Value for Matric A: ")
for r in range(3):
    row1=[]
    for c in range(3):
        val=int(input(f"Enter Row Number {r} and Column Number {c}: "))
        row1.append(val)
    A.append(row1)
print("Enter Value for Matric B: ")
for r in range(3):
    row2=[]
    for c in range(3):
        val=int(input(f"Enter Row Number {r} and Column Number {c}: "))
        row2.append(val)
    B.append(row2)
print(A)
print(B)
# adding up a matric:
Sum = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    Sum.append(row)
print(Sum)