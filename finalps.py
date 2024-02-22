# COUNT NEG NO IN A LIST:

# def neg_count(lst):
#     count=0
#     for i in lst:
#         if i<0:
#             count+=1
#     return count
# lst=[2,3,4,6,8,7,5]
# x=neg_count(lst)
# print(x)

# GIVE THE INDEX OF FIRST OCCURENCE
# def index(lst,val):
#     for i in range(len(lst)):
#         if lst[i]==val:
#             return i


# lst=[2,3,4,5,6,7,-9]
# x=index(lst,-8)
# print(x) 

# MAKE A LIST OF A GIVEN NUMBER
# def lst(L):
#     L=L.split()
#     L=[int(i) for i in L]
#     return L
# L=input("Enter integer with spaces: ")
# L=lst(L)
# print(L)

# take input from user a value and file name to be appended

# def write_to_file(filename,values):
#     f=open(filename,"a")
#     for i in values:
#       f.write(str(i)+" ")
#     f.close()
# write_to_file("Haseeb.txt",[1,2,3,4,5])

# PRINT THE PRIME NO WHICH CONTAIN 2 OR 3 IN ITS:

# def is_prime(i):
#     count=0
#     for j in range(1,i+1):
#         if i % j==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False
# def is_23(i):
#     if "2" in str(i) or "3" in str(i):
#         return True
#     else:
#         return False
# def selection_prime():
#     for i in range(1,1001):
#         if is_prime(i) and is_23(i):
#             print(i)
# # num=int(input("enter Number: "))
# selection_prime()
# def power(x,y):
#     return x**y
# # FINDING 2**2**3:
# pow1=power(2,3)
# pow2=power(2,pow1)
# print(pow2)
# def count_down(n):
#     if n==0:
#         print("LAUNCH!")
#         return
#     print(n)
#     count_down(n-1)

# count_down(3)
# def count_down(n):
#     if n==0:
#         print("BLAST OFF!")
#         return
#     if n==2:
#         print("BOOM\nSCARE YOU..")
#         print(n)
#         count_down(n-1)
#     else:
#         print(n)
#         count_down(n-1)
# count_down(5)
# GENERATE A RECURSIVE FUNCTION FOR FACTORIAL:
# loop version:
# def fact(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial*=i
#     return factorial
# print(fact(5))

# RECURSIVE VERSION:
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(3))
# def sum1(n):
#     s = 0
#     while n > 0:
#         s += 1
#         n -= 1
#     return s
# def sum2():
#     global val
#     s = 0
#     while val > 0:
#         s += 1
#         val -= 1
#     return s
# def sum3():
#     s = 0
#     for i in range(val, 0, -1):
#         s += 1
#     return s
# def main():
#     global val
#     val = 5
#     print(sum2())
#     print(sum1(5))
#     print(sum3())
# print(main())

# PRACTICE PROBLEM FUNCTIONS
# QUESTION 12:
# def count_odd(list):
#     L=[i for i in list if i%2!=0]
#     return L
# x=[0,2,3,4,5,6,7,8,9,10]
# print(count_odd(x))

# QUESTION 8:
# def triangle(base,perp):
#     Hyp=((base**2)+(perp**2))**(1/2)
#     return Hyp
# print(triangle(3,4))

# QUESTION 14

# def index(l, val):
#     occ = []
#     for i in range(len(l)):
#         if l[i] == val:
#             occ.append(i)
#     if occ:
#         return tuple(occ)
#     else:
#         print("Value is not present")
#         return tuple(occ)

# result = index([2, 3, 4, 5, 3, 4, 6,3], 9)
# print(result)

# import math
# from random import randrange
# def fun1(n):
#     result=0
#     while n:
#         result+=n
#         n-=1
#     return result
# def fun2(n):
#     fun1(n)
#     return(math.log(n,10))
# print(fun2(randrange(0,20)))

# def sum_of_series(n):
#     return n+sum_of_series(n-1)
# n=int(input("Enter n: "))
# print(sum_of_series(n))

# n=int(input("Enter N: "))
# if abs(n)>=0:
#     print("Inside If")
# else:
#     print("Inside else")

# def sum_of_series(n):
#     total=0
#     for i in range(1,n+1):
#         if i==0:
#             return total
#         total+=i
#     return total
# n=int(input("Enter n: "))
# print(sum_of_series(n))

# n=int(input("Enter n: "))
# while True:
#     if n>=0:
#         break
#     else:
#         print("Inside else")
# statement=["I","can","not","do","it","!"]
# statement[2:3]=["atleast","try","to"]
# print(statement)

# def proc(n):
#     return 2*n+1
# def proc(x):
#     return x+2
# x=proc(5)
# print(x)

# def add_math():
#     print("ADD TWO MATRICES")
# def sub_math():
#     print("SUB TWO MATRICES")
# def mul_math():
#     print("MULTIPLY TWO MATRICES")
# def Exit():
#     print("Thank you for using my app")
# menu={1:add_math,2:sub_math,3:mul_math,4:Exit}
# print(''' 1. Add Matrices
#           2. Subtract Matrices
#           3. Multiply Matrices
#           4. Exit ''')
# choice=int(input("Enter Choice"))
# print(menu)
# print(menu[choice])
# print(menu[choice]())

# SEPARATOR FUNCTION

# def fun(st,sepa):
#     L=[]
#     chunk=""
#     for i in st:
#         if i!=sepa:
#             chunk+=i
#         else:
#             L+=[chunk]
#             chunk=""
#     if chunk!="":
#         L+=[chunk]
#     return L
# st=input("Enter N: ")
# sepa=input("Enter sepa: ")
# print(fun(st,sepa))


# MATRICES
# m2=[]
# def be_positive(m):
#     for i in m:
#         new=[]
#         for j in i:
#             new.append(0 if j<0 else j)
#         m2.append(new)
#     return m2
# m=[]
# for r in range(3):
#     row=[]
#     for c in range(3):
#         val=int(input(f"Enter Value for row{r} and coloumn {c}:  "))
#         row.append(val)
#     m.append(row)
# print(be_positive(m))
# def index(l, val):
#     for i in range(len(l)):
#         if l[i] == val:
#             return i
#     else:
#         print("Value is not present")

# result = index([2, 3, 4, 5, 3, 4, 6,3], 9)
# print(result)
from tkinter import Tk,Label
r=Tk()
r.title("My Window")
r.geometry('200x200+400+400')
lab1=Label(r,text="Hello World",fg="red",bg="#AFB42B",)
r.mainloop()