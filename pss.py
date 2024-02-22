# val=input("Enter integer value with spaces: ")
# val=val.split()
# f=open("Value.txt","w+")
# for enetries in val:
#     if enetries.isdigit():
#         f.write(enetries+" ")
# choice=input("press y to see the content: ")
# if choice=="Y" or "y":
#     f.seek(0)
#     print(f.read())
# f.close()
# L=[2,3,4,5,6]
# f=open("E:/pythoncourse2.py/Value.txt","w+")
# for i in L:
#     f.write(str(i)+",")
# f.close()

# # READING BACK
# f=open("E:/pythoncourse2.py/Value.txt")
# data=f.read().split(",")
# data=[int(i) for i in data]
# print(data)
# f.close()
# FILE PRACTICE PROBLEM :
# QUESTION NO:1
# def crypto(file_name):
#     f=open(file_name)
#     text=f.read()
#     text=text.replace("umer","xxxx")
#     print(text)
#     f.close()
#     f=open(file_name,"w")
#     f.write(text)
# crypto("bc.txt")
# QUESTION NO:2
# def censor(file_name):
#     f=open(file_name)
#     text=f.read()
#     text=text.split()
#     l=[]
#     for word in text:
#       if len(word)==4:
#          word="xxxx"
#          l.append(word)
#       else:
#          l.append(word)
#     for j in l:
#        print(j,end=" ")
#     f.close()
#     f=open(file_name,"w")
#     for k in l:
#       f.write(k+" ")
#     f.close()
# censor("H.txt")
# QUESTION 3
def filecopy(file1,file2):
   f=open(str(file1))
   f.read()
   f.seek(0)
   lines=f.readlines()
   f.close()
   g=open(str(file2),"a")
   for i in lines:
      g.write(lines)
   g.close()
file1=input("Enter First file name: ")
file2=input("Enter second file name: ")
filecopy(file1,file2)
