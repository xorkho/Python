# Q1: Print the first 20 numbers of a Fibonacci series
# no_of_term=int(input("Enter number of terms: "))
# a,b=0,1
# print(a,end=",")
# print(b,end=",")
# for i in range(no_of_term):
#     c=a+b
#     print(c,end=",")
#     a=b
#     b=c

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# num=int(input("Enter number: "))
# total=0
# for i in range(1,num+1):
#     calc=str(num)*i
#     total+=int(calc)
#     if i==num:
#         # calc=str(num)*i
#         print(calc)
#     else:
#         print(calc,end="+")
# print("total is",total)

# Take a number from the user and find the number of digits in it. 
# num=input("Enter Number: ")
# dig=len(num)
# print("Total Number of digit is",dig)

# Find the reverse of a number provided by the user(any number of digit) 
# num=input("Enter number: ")
# rev=num[::-1]
# print("Reverse of a given digit is",rev)

# Write a program to print the following pattern
# *
# **
# ***
# ****
# *****

# num=int(input("Enter number of terms: "))
# for i in range(1,num+1):
#     print("*"*i)

# Write a program to print the following pattern
# *
# **
# ***
# **
# *

# num=int(input("Enter number of terms: "))
# for i in range(1,num+1):
#     print("*"*i)
# for j in range(num+1,0,-1):
#     print("*"*j)

# Write a program to print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# num=int(input("Enter number of terms: "))
# n=1
# for i in range(1,num+1):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

