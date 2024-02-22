# OPENFILE AND COUNT THE NO OF ALPHABETS
# f=open("E:/pythoncourse2.py/My File.txt")
# text=f.read()
# f.close()
# count=0
# for alp in text:
#     if alp.isalpha():
#         count+=1
# print("NO Of Alphabets: ", count)
f=open("E:/pythoncourse2.py/My Fil.txt","a+")
f.write(" My Friend is my best friend i want him to play with me")
f.seek(0)
f.write("I M UMER")