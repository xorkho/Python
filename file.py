# QUESTION 2:
f=open("My File.txt")
text=f.read()
print("Number Of Character:",len(text))
word=text.split()
print("Number Of Words:",len(word))
f.seek(0)
lines = f.readlines()
print("Number Of Lines: ",len(lines))
alphabets=0
for i in text:
    if i.isalpha():
        alphabets+=1
print("Number of Alphabets:",alphabets)
f.close()
# QUESTION 4:
# values=(input("Enter Integer: "))
# values=values.split()
# f=open("Values.txt","w+")
# for val in values:
#     if val.isdigit():
#         f.write(val+" ")
# choice=input("Press Y to verify the content")
# if choice=="y" or "Y":
#     f.seek(0)
#     print(f.read())
# f.close()
# QUESTION 5:
# f=open("Values.txt")
# num=f.read()
# num=num.split()
# total=0
# for i in num:
#     total+=int(i)
# print("Average",round(total/len(num),3))
# f.close()
# QUESTION 3:
# f=open("H.txt")
# for line in f:
#     print(line.strip())
# print(f)
# QUESTIN 6:PART 2:
# L=[1,2,3,4,5]
# f=open("E:/pythoncourse2.py/bk.txt","w")
# for i in L:
#     f.write(str(i)+",")
# f.close()
# ps:
# L=[2,3,4,5,6]
# f=open("bk.txt","w")
# f.write(str(L))
# f.close()