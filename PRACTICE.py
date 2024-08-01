# class A:
#     # def show(self):
#     #     print("in A")
#     pass

# class B:
#     def show(self):
#         print("in B")

# class C(A,B):
#     # def show(self):
#     #     print("in C")
#     pass

# class D(C,B):
#     # def show(self):
#     #     print("in D")
#     pass

# obj=D()
# obj.show()
# print(B.__mro__)

# class rectangle:
#     def __init__(self,w,h):
#         self.width=w
#         self.height=h
#         self.Area=w*h
#         return self.Area

# class square(rectangle):
#     def __init__(self,w,h):
#         super().__init__(w,h)
        
# sq=square(2,4)
# print(sq.Area)
# r1=rectangle(3,7)
# r2=rectangle(4,6)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_name(self):
#         return self.name
#     def show_age(self):
#         return self.age
    
# class student:
#     def __init__(self,student_id,student_rollno):
#         self.student_id=student_id
#         self.student_rollno=student_rollno

# class resident(student,person):
#     def __init__(self, name,age,student_id,student_rollno):
#         person.__init__(self,name,age)
#         student.__init__(self,student_id,student_rollno)

# p1=resident("haseeb","18","9686","95")
# print(p1.name)
# print(p1.age)
# print(p1.student_id)
# print(p1.student_rollno)

# class hospital:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
    
#     def show_info(self):
#         print(f"Name: {self.name}\nAddress: {self.address}")

# class doctor(hospital):
#     def __init__(self, name, address,specialization):
#         super().__init__(name, address)
#         self.specialization=specialization

#     def show_doctor_info(self):
#         print(f"Doctor Info")
#         super().show_info()
#         print(f"Specialization: {self.specialization}")

# class patient(hospital):
#     def __init__(self,name,address,disease):
#         super().__init__(name, address)
#         self.disease=disease

#     def show_patient_info(self):
#         print("Patient info: ")
#         super().show_info()
#         print(f"Disease: {self.disease}")


# class medical_test:
#     def __init__(self, doctor, patient):
#         self.doctor = doctor
#         self.patient = patient

#     def show_medical_repot(self):
#         print(f"This is the medical report of {self.patient} his checkup was done by the {self.doctor}")

# h1=hospital("saifi","KDA CHOWRANGI")
# h1.show_info()
# d1=doctor("DR MARIA","NEDUET","MBBS")
# p1=patient("Umer","Karachi","Fever")
# mr=medical_test(d1.name,p1.name)
# mr.show_medical_repot()

# -----------------------------------ABSTRACT-------------------------------------

# from abc import *

# class vehicle(ABC):   #ABSTRACT CLASS ATLEAST HAVE ONE ABSTRACT METHOD IT IS USED FOR STANDARIZATION

#     def __init__(self,n):
#         self.tyres=n

#     @abstractmethod
#     def start(self):
#         pass

#     def display(self):
#         print(f"display")

# class bike(vehicle):
#     def __init__(self, n):
#         super().__init__(n)
    
#     def start(self):
#         print("bike start with kick")

# class car(vehicle):
#     def __init__(self, n):
#         super().__init__(n)
    
#     def start(self):
#         print("car start with key")

# c1=car(4)
# c1.start()

# b1=bike(2)
# b1.start()

# from abc import ABCMeta,abstractmethod
# class super(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()

#     @abstractmethod
#     def action(self):
#         pass

# class sub(super):
#     def action(self):
#         print("action")

# x=sub()
# x.action()

# from abc import *
# class vehicle(ABC):

#     def __init__(self,make,model):
#         self.make=make
#         self.model=model

#     @abstractmethod
#     def show_details(self):
#         pass

# class car(vehicle):
#     def __init__(self, make, model,no_of_tyres,color):
#         super().__init__(make, model)
#         self.no_of_tyres=no_of_tyres
#         self.color=color

#     def show_details(self):
#         print(f"Car Make{self.make} model no: {self.model} &\nhas {self.no_of_tyres} & its color is {self.color}")

# class Truck(vehicle):
#     def __init__(self, make, model,load_capacity,milleage):
#         super().__init__(make, model)
#         self.load_capacity=load_capacity
#         self.milleage=milleage

#     def show_details(self):
#         print(f"Truck Make{self.make} model no: {self.model} &\nhas capacity of {self.load_capacity} & its milleage is {self.milleage}")

# class Motorcycle(vehicle):
#     def __init__(self, make, model,engine_no,speed):
#         super().__init__(make, model)
#         self.engine_no=engine_no
#         self.speed=speed
        
#     def show_details(self):
#         print(f"Car Made:{self.make}\nmodel no: {self.model}\nengine no:{self.engine_no}\nspeed is {self.speed}")

# b=Motorcycle("japan","BM-762","EN-097","200")
# b.show_details()


# from abc import *

# class operations(ABC):
#     def __init__(self):
#         self.n1=int(input("Enter first number: "))
#         self.n2=int(input("Enter second number: "))
    
#     @abstractmethod
#     def mathematical_operation(self):
#         pass

# class Addition_operation(operations):
#     def mathematical_operation(self):
#         return f"sum is {self.n1+self.n2}"
    
# class subtraction_operation(operations):
#     def mathematical_operation(self):
#         return f"differnce is {self.n1-self.n2}"
    
# class Multiplication_operation(operations):  
#     def mathematical_operation(self):
#         return f"product is {self.n1*self.n2}"
    
# class Divison_operation(operations):   
#     def mathematical_operation(self):
#         if self.n2==0:
#             print("Error")
#         else:
#             return f"sum is {round((self.n1/self.n2),3)}"
        

# Add=Addition_operation()
# print(Add.mathematical_operation())

# sub=subtraction_operation()
# print(sub.mathematical_operation())

# mul=Multiplication_operation()
# print(mul.mathematical_operation())

# div=Divison_operation()
# print(div.mathematical_operation())

# -------------------------------OPERATOR OVERLOADING----------------------------------

# class mystring:
#     def __init__(self,s=""):
#         self.s=s

#     def __add__(self,obj):
#         return self.s+str(obj)
    
# s1=mystring("comp")
# print(s1+3)               #s1.__add__(3)

# class point:

#     def __init__(self,xcoord,ycoord):
#         self.xcoord=xcoord
#         self.ycoord=ycoord

#     def __str__(self):
#         return f"<{self.xcoord},{self.ycoord}>"
    
#     def __add__(self,p):
#         return point(self.xcoord+p.xcoord,self.ycoord+p.ycoord)
    
#     def __iadd__(self,p):
#         self.xcoord+=p.xcoord
#         self.ycoord+=p.ycoord
#         return self
    
#     def __neg__(self):
#         return -self.xcoord,-self.ycoord
    
# # p1=point(3,4)
# # print(p1)
# # p2=point(4,6)
# # print(-p2)
# # p1+=p2
# # print(p1)

# from math import sqrt
# class line:
#     def __init__(self,p1=None,p2=None):
#         if isinstance(p1,point):
#             self.p1=p1
#         else:
#             self.p1=point(0,0)
        
#         if isinstance(p2,point):
#             self.p2=p2
#         else:
#             self.p2=point(0,0)
    
#     def __invert__(self):
#         return sqrt((self.p2.xcoord-self.p1.xcoord)**2+(self.p2.ycoord-self.p1.ycoord)**2)
    
# p1=point(3,5)
# p2=point(9,11)
# l=line(p1,p2)
# l1=line(4,6)
# print(l.__invert__())


# ------------------------------- DECORATORS------------------------------------------

# def mydecorator(add):
#     def mywrapper(*args,**kwargs):   #*args take argument as a tuple **kwargs takes as a dictionary
#         print("before modification")
#         add(*args,**kwargs)
#         print("After Modification")
#     return mywrapper


# @mydecorator
# def func():
#     print("Hello")
 
# @mydecorator
# def add(a,b):
#     print(a+b)
# # myfunction=func()

# # mydecorator(func)()

# add(6,8)
# func()


# from time import *

# def mydecorator(long_loop):
#     def my_wrapper():
#         t1=time()
#         long_loop()
#         t2=time()
#         return t2-t1
#     return my_wrapper

# @mydecorator
# def long_loop():
#     user_input=input("Take your time: ")

# time=long_loop()
# print(round(time,2))

# def decorator(average):
#     def my_wrapper(v1,v2):
#         avg=average(v1,v2)
#         if avg>=6:
#             print("Congrats you passed the exam")
#         print("Your average is ",avg)
#     return my_wrapper

# @decorator
# def average(v1,v2):
#     return (v1+v2)/2

# average(3,8)


# ------------------------------------STATIC METHOD-------------------------------------
# class math:
#     def __init__(self,n):
#         self.n=n
#     def add_to_num(self,num):
#         self.num=num
#         self.num=self.num+self.n
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# m1=math(6)
# m1.add_to_num(4)
# print(m1.num)
# print(m1.add(6,3))


# ---------------------------------------CLASS METHOD-----------------------------------

# class Employee:
#     company_name="APPLE"

#     def show(self):
#         print(self.company_name)

#     @classmethod
#     def change_company(cls,new_company):  #CLASS METHOD CHANGE THE CLASS VAR
#         cls.company_name=new_company

# E1=Employee()
# E1.show()
# E1.change_company("TESLA")
# E1.show()

# E2=Employee()
# E2.show()

# ----------------------------TYPES OF METHOD------------------------

# class method:
#     c_var="CLASS VARIABLE"
#     def __init__(self):
#         self.instancevar="INSTANCE VARIABLE"
#         self.instance_method()

#     def instance_method(self):
#         print(self.instancevar)
#         print(method.c_var)
#         print(self.c_var)

#     @classmethod
#     def class_method(cls):
#         print(cls.c_var)
#         print(method.c_var)
#         # print(self.instancevar)   in class method there is no NS Of inst. ERROR

#     @staticmethod
#     def s_method():
#         print(self.instancevar)
#         print(self.instance_method())
#         print(method.c_var)


# class child(method):
#     def __init__(self):
#         self.instance_method()
#         method.c_method()
#         method.s_method()

# m=method()
# # m.instance_method()
# # method.class_method()
# method.s_method()


# -------------------------------------------CLASS FRACTION OOP CLASS MISS MARIA-------------------------------------
# class Fraction:
#     def __init__(self,num=0,den=1):
#         self.num=num
#         if den!=0:
#             self.den=den
#         else:
#             self.den=1

#     def get_fraction(self):     #GET DECIMAL OF THE FRACTION
#         return self.num,self.den
    
#     def get_decimal(self): 
#         return self.num/self.den
    
#     def simplify(self):  #SIMPLIFIED THE GIVEN FRACTION
#         hcf=Fraction.find_hcf(self.num,self.den)
#         self.num=int(self.num/hcf)
#         self.den=int(self.den/hcf)

#     def find_hcf(a,b): #FIND HCF OF TWO NUMBERS
#         factor_a=Fraction.find_factor(a)
#         factor_b=Fraction.find_factor(b)
#         for i in range(len(factor_a)-1,-1,-1):
#             if factor_a[i] in factor_b:
#                 return factor_a[i]

#     def find_factor(x):  #FIND THE FACTOR
#         factors=[]
#         for i in range(1,x+1):
#             if x%i==0:
#                 factors.append(i)
#         return factors
    
#     def __gt__(self,f2):    #OVERLOAD THE GT OPER TO CHECK WHICH FRACTION IS GREATER
#         num1=f1.get_decimal()
#         num2=f2.get_decimal()
#         if num1>num2:
#             return True
#         elif num1<num2:
#             return False
    
#     def __add__(self,f2):    #OVERLOAD THE ADD OPER TO ADD THE FRACTION
#         num=(self.num*f2.den+f2.num*self.den)
#         den=self.den*f2.den
#         return "{}/{}".format(num,den)
    
#     def __str__(self,num,den):      #REPR HOW SHOULD O/P LOOK LIKE
#         return "{}/{}".format(num,den)
    
#     def __iadd__(self,f2):
#         num=(self.num*f2.den+f2.num*self.den)
#         den=self.den*self.num
#         f=num/den
#         return self
    
# f1=Fraction(50,2)
# # f1.simplify()
# f2=Fraction(75,2)
# # f2.simplify()
# print(f1+f2)
# f1+=f2
# print(f1)

# CLASS FRACTION USED TO CREATE FRACTION
# class FRACTION2:
#     def __init__ (self,n,d):
#         self.num=n
#         self.den=d
#     def __str__(self):
#         return '{}/{}'.format(self.num,self.den)
#     def __add__(self,other):
#         temp_num=self.num*other.den+other.num*self.den
#         temp_den=self.den*other.den
#         return'{}/{}'.format(temp_num,temp_den)
#     def __sub__(self,other):
#         temp_num=self.num*other.den-other.num*self.den
#         temp_den=self.den*other.den
#         return'{}/{}'.format(temp_num,temp_den)
#     def __mul__(self,other):
#         temp_num=self.num*other.num
#         temp_den=self.den*other.den
#         return'{}/{}'.format(temp_num,temp_den)
#     def __truediv__(self,other):
#         temp_num=self.num*other.den
#         temp_den=self.den*other.num
#         return'{}/{}'.format(temp_num,temp_den)

#-------------------------CLASS WORK OF ABSTRACT CLASS-------------------------------------

# from abc import ABC ,abstractmethod
# class polygon(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         print("I am type of polygon")

# class square(polygon):
#     def no_of_sides(self):
#         return super().no_of_sides()
# sq=square()
# sq.no_of_sides()

# -----------------------------CHAINING DECORATOR------------------------------------------
# def dec(fn):
#     def wrapper(name):
#         return f"Hi"+" "+fn(name)
#     return wrapper

# def dec2(fn):
#     def wrapper(name):
#         return fn(name)+" "+ "how are you"
#     return wrapper

# @dec
# @dec2
# def name(name):
#     return name

# print(name("umer"))

# ----------------------------------------------LAB NO 9----------------------------------------------------------------------
# -----------------------------TASK 1----------------------------------------------------------
# def divide(n1,n2):
#     return n1/n2
# print(divide(5,5))

#-----------------------------------TASK 2--------------------------------------------------


# def decorator1(fn):
#     def my_wrapper():
#         print_x()
#         print()
#         print_y()
#         print("Hello")
#     return my_wrapper

# def decorator2(fn):
#     def my_wrapper():
#         print_y()
#         print()
#         print_x()
#     return my_wrapper


# def print_x():
#     for _ in range(5):
#         print("X",end="")

# def print_y():
#     for _ in range(5):
#         print("Y",end="")

# def decorator1(fn):
#     def my_wrapper():
#         print_x()
#         print()
#         print_y()
#         print()
#         print("HELLO")
#         fn()
#     return my_wrapper

# def decorator2(fn):
#     def my_wrapper():
#         fn()
#         print_y()
#         print()
#         print_x()
#     return my_wrapper

# def print_x():
#     for _ in range(5):
#         print("X", end="")

# def print_y():
#     for _ in range(5):
#         print("Y", end="")

# @decorator1
# @decorator2
# def my_function():
#     pass

# my_function()

# --------------------------------------- LAB NO 12--------------------------------------------------#
# -------------------------------------------TASK 1--------------------------------------------------
# class vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __str__(self):
#         return f"{self.x}i+{self.y}j"
    
# v=vector(6,9)
# print(v)


# ------------------------------------------------TASK 2------------------------------------------------

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __str__(self):
#         return f"({self.x},{self.y})"

# p1=point(2,3)
# print(p1)
    
# --------------------------------LAB NO 13------------------------------------------------
# import math

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
#     def __add__(self,p):
#         return self.x+p.x,self.y+p.y
    
#     def __lt__ (self,p):
#         first=math.sqrt(self.x**2+self.y**2)
#         second=math.sqrt(p.x**2+p.y**2)
#         return first<second
    
#     def __gt__(self,p):
#         first=math.sqrt(self.x**2+self.y**2)
#         second=math.sqrt(p.x**2+p.y**2)
#         return first>second

    

# p1=point(5,5)
# p2=point(3,5)
# print(p1>p2)  #-----> TRUE
# print(p1<p2)  #-----> FALSE


# --------------------------------------LAB NO 13-------------------------------------------
# ----------------------------------------TASK 3----------------------------------------------

# class circle:

#     def __init__(self):
#         self.r=int(input("Input for radius"))
    
#     def __lt__(self,c):
#         if self.r<c.r:
#             return True
#         else:
#             return False
#     def __gt__(self,c):
#         if self.r>c.r:
#             return True
#         else:
#             return False

# c1=circle()  #USER_INPUT IS 4
# c2=circle()  #USER INPUT IS 9
# print(c1>c2) #-----> FALSE


# -------------------------------10 JUN 2024---------------------------------------------------
# from _collections_abc import Container
# class Employee:   #CONTAINER SE INHERIT KREGY TO BHI CHALEGA NAHI KRYGY TO BHI CHAL JYEGA
#     def __init__(self,n,id):
#         self.name=n
#         self.id=id
#     def __contains__(self,n):
#         return n in self.name
# E=Employee("BooAli",1001)
# # print("Ali" in E)
# print(isinstance(E,Employee))
# print(isinstance(E,Container))
# print(issubclass(Employee,Container))
# print(Employee.__mro__)

# class odd_int:
#     def __contains__(self,x):
#         return isinstance(x,int) and x%2!=0
    
# n=odd_int()
# print(0 in n)
    

# -----------------------PROPERTY IN PYTHON-----------------------------------------------------

# class Pencil:
#     def __init__(self,c=None):
#         self.set_color(c)
    

#     def get_color(self):
#         if self.__color!=None:
#             return self.__color
#         else:
#             print("color is not set")

#     def set_color(self,c):
#         color=["red","blue","green"]
#         if c in color or c==None:
#             self.__color=c
#         else:
#             print("INVALID COLOR CHOICE")
    

# p=Pencil()
# print(p.get_color())

# --------------------------------11 JUN 2024---------------------------------------

# IMPLEMENT PROPERTY USING FUNCTION

# class Pencil:
#     def __init__(self,c=None):
#         self.set_color(c)
    

#     def get_color(self):
#         if self.__color!=None:
#             return self.__color
#         else:
#             print("color is not set")

#     def set_color(self,c):
#         color=["red","blue","green"]
#         if c in color or c==None:
#             self.__color=c
#         else:
#             print("INVALID COLOR CHOICE")

#     def deleter(self):
#         del self.__color

#     color=property(get_color,set_color,deleter,"THE COLOR PROPERTY")

# p=Pencil("red")
# print(p.color)     #CALL THE GETTER METHOD
# p.color="blue"    #CALL THE SETTER METHOD
# print(p.color)
# del p.color
# # print(p.color)
# p.color="red"
# print(p.color)
# print(p.__dict__)
# print(type(Pencil.color))
# print(p.set_color("green"))
# print(p.get_color())   #IN THIS METHOD SET & GET COLOR IS ACCESSABLE 
# print(p.color)

# -------------------IMPLEMENT USING PROPERTY DECORATOR------------------------------------

# class Pencil:
#     def __init__(self,c=None):
#         self.color=c
    
#     @property
#     def color(self):
#         if self.__color!=None:
#             return self.__color
#         else:
#             print("color is not set")

#     @color.setter
#     def color(self,c):
#         color=["red","blue","green"]
#         if c in color or c==None:
#             self.__color=c
#         else:
#             print("INVALID COLOR CHOICE")

#     @color.deleter
#     def color(self):
#         del self.__color

# p=Pencil("red")
# print(p.color)     #CALL THE GETTER METHOD
# p.color="blue"    #CALL THE SETTER METHOD
# print(p.color)
# del p.color
# # print(p.color)
# p.color="red"
# print(p.color)
# print(p.__dict__)
# print(type(Pencil.color))
# help(Pencil)


# ----------------------------------------------------OOP LAB 10 (CODE)-------------------------------------------
# Q1:
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def talk(self):
#         pass

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def talk(self):
#         print(f'I am {self.name} and I meow!!')

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)


#     def talk(self):
#         print(f'I am {self.name} and I bark!!')



# c = Cat('Cat')
# c.talk()
# d = Dog('Dog')
# d.talk()


# from abc import ABC, abstractmethod
# class Person(ABC):
#     @abstractmethod
#     def ticket_price(self):
#         pass

# class Employee(Person):
#     def ticket_price(self):
#         return print('Sorry! we have no concession for Employees.')

# class Student(Person):
#     def ticket_price(self):
#         return print('Concession granted successfully!')

# e = Employee()
# e.ticket_price()
# s = Student()
# s.ticket_price()

# -------------------------------------------14 JUN 24-----------------------------------------------------------------------
# -------------------------------------------PROPERTY IN PYTHON-------------------------------------------------------
# EXAMPLE 2:
# CREATING A CIRCLE CLASS HAVING ONE ATTRIBUTE RADIUS

# -------------------------------------CASE ONE :----------------------------------------------------------
# DEFINING RADIUS AS A READ_WRITE PROPERTY 

# class circle:
#     def __init__(self,r=1):
#         self.radius=r    #CLASSS ATTRI   
#     #BASICALLY THIS STATEMENT CALLS THE SETTER
    
#     @property
#     def radius (self):
#         "The radius property"
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r>0:
#             self.__radius=int(r)
#         else:
#             self.__radius=1

# c1=circle(6.7)
# print(c1.radius)
# # print(c1.__dict__)


# -------------------------------------CASE TWO ----------------------------------------------------------
# DEFINING RADIUS AS A READ ONLY  PROPERTY 

# class circle:
#     def __init__(self,r=1):
#         if r>0:
#             self.__radius=int(r)
#         else:
#             self.__radius=1
    
#     @property
#     def radius (self):
#         "The radius property"
#         return self.__radius

# c1=circle(6.7)
# print(c1.radius)
# c1.radius=8    #IT WILL RAISE ERROR BCOZ IT HAS NO SETTER METHOD


# -------------------------------------CASE THREE -----------------------------------------------------------
# DEFINING RADIUS AS A WRITE ONLY PROPERTY 

# class circle:
#     def __init__(self,r=1):
#         self.radius=r    #CLASSS ATTRI   
#     #BASICALLY THIS STATEMENT CALLS THE SETTER
    
#     @property
#     def radius (self):
#         return "YOU CANT READ THE WRITE ONLY PROPERTY"
    
#     @radius.setter
#     def radius(self,r):
#         if r>0:
#             self.__radius=int(r)
#         else:
#             self.__radius=1

# c1=circle(6.7)
# print(c1.radius)
# c1.radius=9
# print(c1.radius)  


# -------------------------------------CASE FOUR -----------------------------------------------------------
# ADDING ANOTHER COMPUTED PROPERTY DIAMETER

# class circle:
#     def __init__(self,r=1):
#         self.radius=r    #CLASSS ATTRI   
#     #BASICALLY THIS STATEMENT CALLS THE SETTER
    
#     @property
#     def radius (self):
#         "The radius property"
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r>0:
#             self.__radius=int(r)
#         else:
#             self.__radius=1


#     @property
#     def diameter(self):
#         "The diameter property"
#         return self.__radius*2
    
#     @diameter.setter
#     def diameter(self,d):
#         self.__radius=d/2

# c1=circle(6.7)
# print(c1.radius)
# print(c1.__dict__)
# c1.diameter=15.4
# print(c1.diameter)
# print(circle.radius)  #PROPERTY OBJ RETURNS


# ---------------------------ABSTRACT PROPERTY--------------------------------------------------
# from abc import ABC,abstractproperty
# class circle(ABC):
#     def __init__(self,r=1):
#         self.radius=r    #CLASSS ATTRI   
#     #BASICALLY THIS STATEMENT CALLS THE SETTER
    
#     @abstractproperty
#     def radius (self):
#         pass
    
#     @radius.setter
#     def radius(self,r):
#         pass

# class precise_circle(circle):

#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r>0:
#             self.__radius=r
#         else:
#             self.__radius=1

# c1=precise_circle(6.7)
# print(c1.radius)
# print(c1.__dict__)


# --------------------------------------21 JUNE 2024-----------------------------------------------------------
# ------------------------------------EXCEPTION HANDLING------------------------------------------------------------------
# try:
#     money=int(input("ENTER AMOUNT: "))
#     sharers=int(input("ENTER SHARERS: "))
#     total=money/sharers
#     print("Amount for one sharers is : ",total)

# except ValueError as ve:
#     print(f"{type(ve)}; {ve}")

# except ZeroDivisionError as zed:
#     print(f"{type(zed)}; {zed}")

# except Exception as e:
#     print(f"{type(e)}; {e}")
# print("Have a nice day ")

# ---------------------------------------------24 JUNE 2024-----------------------------------------
# while True:
#     try:
#         money=int(input("ENTER AMOUNT: "))
#         sharers=int(input("ENTER SHARERS: "))
#         if sharers==1:
#             raise ValueError("No Of sharer must be greater than 1")
#         total=money/sharers
#         print("Amount for one sharers is : ",total)
#         break     #Break can be placed here 

#     # except ValueError as ve:
#     #     print(f"{type(ve)}; {ve}")

#     # except ZeroDivisionError as zed:
#     #     print(f"{type(zed)}; {zed}")
    

#     except Exception as e:      #THIS STATEMENT HANDLES ALL THE ERRORS 
#         print(f"{type(e)}; {e}")

#     finally:   #ALWAYS THE LAST BLOCK
#         print("Have a nice day ")


# --------------------PRACTICE PROBLEM SET-------------------------------------
# --------------------------------QUES1-----------------------------------------

# from math import sqrt
# from abc import ABC ,abstractmethod

# class polygon(ABC):
#     def __init__(self): #where n= no of sides & l= length stored in list
#         self.n=3
#         self.l=[]
    
#     def set_sides(self,ns):
#         if isinstance(self.n,int) and (self.n==3 or self.n>3):
#             self.n=ns
#         else:
#             print("INVALID CHOICE")

#     def set_length(self,l):
#         if len(l)==self.n:
#             for i in l:
#                 if isinstance(i,int) or isinstance(i,float):
#                     self.l.append(i)
    
#     def perimeter(self):
#         sum=0
#         for i in range(len(self.l)):
#             sum+=self.l[i]
#         return f"perimeter is {round(sum,2)}"
    
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(polygon):

#     def set_length(self, l):
#         for i in l:
#             if isinstance(i,int) or isinstance(i,float):
#                 self.l.append(i)
        
#     def perimeter(self):
#         sum=0
#         for i in range(len(self.l)):
#             sum+=self.l[i]
#         sum*=2
#         return f"perimeter is {sum}"
    
#     def area(self):
#         total=1
#         for i in range(len(self.l)):
#             total*=self.l[i]
#         return f"Area is {total}"
    
# class RightTriangle(polygon):

#     def set_length(self, l):
#         for i in l:
#             if isinstance(i,int) or isinstance(i,float):
#                 self.l.append(i)

#         hyp=sqrt((self.l[0])**2+(self.l[1])**2)
#         self.l.append(hyp)

#     def area(self):
#         total=1
#         for i in range(2):
#             total*=self.l[i]
#         total/=2
#         return f"Area is {total}"

# p=RightTriangle()
# p.set_length([2,4])
# print(p.perimeter())
# print(p.area())

# -----------------------------------QUES 2--------------------------------------------
# Repeat problem 1, converting both the attributes no_of_sides and lengths to non-public / private attributes.
# Define properties for both these attributes without the delete method.


# from math import sqrt
# from abc import ABC, abstractmethod

# class Polygon(ABC):
#     def __init__(self,n=3): 
#         self.no_of_sides = n

#     @property
#     def no_of_sides(self):
#         return self.__no_of_sides
    
#     @no_of_sides.setter
#     def no_of_sides(self, ns):
#         if isinstance(ns, int) and (ns == 3 or ns > 3):
#             self.__no_of_sides = ns
#         else:
#             print("INVALID CHOICE")
    
#     @property
#     def lengths(self):
#         return self.__lengths
    
#     @lengths.setter
#     def lengths(self, l):
#         self.__lengths=[]
#         if len(l) == self.__no_of_sides:
#             for i in l:
#                 if isinstance(i, int) or isinstance(i, float):
#                     self.__lengths.append(i)

#     def perimeter(self):
#         return f"perimeter is {round(sum(self.__lengths), 2)}"
    
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Polygon):

#     @property
#     def lengths(self):
#         return self.__lengths

#     @lengths.setter
#     def lengths(self, l):
#         self.__lengths=[]
#         for i in l:
#             if isinstance(i, int) or isinstance(i, float):
#                 self.__lengths.append(i)
        
#     def perimeter(self):
#         return f"perimeter is {2 * sum(self.__lengths)}"
    
#     def area(self):
#         total = 1
#         for i in range(len(self.__lengths)):
#             total *= self.__lengths[i]
#         return f"Area is {total}"
    
# class RightTriangle(Polygon):

#     @property
#     def lengths(self):
#         return self.__lengths
    
#     @lengths.setter
#     def lengths(self, l):
#         self.__lengths=[]
#         for i in l:
#             if isinstance(i, int) or isinstance(i, float):
#                 self.__lengths.append(i)
#         hyp = sqrt((self.__lengths[0])**2 + (self.__lengths[1])**2)
#         self.__lengths.append(hyp)

#     def area(self):
#         return f"Area is {0.5 * self.__lengths[0] * self.__lengths[1]}"

# p = Rectangle(9)
# p.lengths = [2, 4]
# print(p.area())
# p.lengths=[3,4]
# print(p.no_of_sides)
# print(p.area())
# print(p.perimeter())
    
# ----------------------------------LAB:EXCEPTION---------------------------------------------------------------------------------
# ---------------------------------------QUES 1------------------------------------------------
# try:
#     edu=int(input("Enter your year of education: "))
#     assert edu>16
        
# except ValueError as E:
#     print(f"{type(E)} ; {E}")

# except:
#     print("You Are not Elgible")

# else:
#     print("You are not eligible")


# try:
#     years = int(input('Enter years of education: '))
#     assert years > 16
# except ValueError:
#     print('Invalid Input')
# except:
#     print('You are not eligible :(( ')
# else:
#     print('You are eligible :))')





# --------------------------------QUES 2---------------------------------------------------

# def smart_division():
#     try:
#         n1=int(input("Enter first number : "))
#         n2=int(input("Enter second number : "))
#         print(f"Division of {n1} & {n2} is {n1/n2}")

#     except Exception as E:
#         print(F"{type(E)} ; {E}")

# smart_division()







# --------------------------------------QUES 3-------------------------------------------
# def factorial():
#     try:
#         n=int(input("Enter Number for the factorial: "))
#         if n<=0:
#             raise ValueError("Plz Enter a positive number")
#         fact=1
#         for i in range(1,n+1):
#             fact*=i
#         print(f"Factorial of {n} is {fact}")

#     # except Exception as E:
#     #     print(f"{type(E)} ; {E}")

# factorial()


# ---------------------------QUES 4--------------------------------------------------

# class EligibilityError(Exception):
#     pass
# try:
#     years = int(input('Enter years of education: '))
#     if years <= 16:
#         raise EligibilityError
    
# except ValueError:
#     print('Invalid Input')

# except EligibilityError as E:
#     print('You are not eligible :(( ')
 
# else:
#     print('You are eligible :))')


# --------------------TRY EXCEPT CLASS WORK-----------------------------
# def input_in_range(min,max):
#     while True:
#         try:
#             inp=int(input(f"Enter integr in between {min} & {max}: "))
#             if min<=inp<=max:
#                 return inp
#             raise ValueError("Value out of range")
#         except Exception as e:
#             print(f"{type(e)} ; {e}")

# def create_list(n,min,max):
#     l=[]
#     for _ in range(n):
#             val=int(input(f"Enter integr in between {min} & {max}: "))
#             l.append(val)
#     return l

# try:
#     print("opening file..........")
#     f=open("mylist.txt","w")
#     l=create_list(5,1,100)   #TAKING 5 INPUT 

# except Exception as e:
#     print(f"{type(e)} ; {e}")

# else:
#     f.write(str(l))     #STORED THOSE ELEMENTS IN FILE
#     print("List saved......")

# finally:
#     f.close()
#     print("file closedd.....")

# input_in_range(6,20)

# ------------------------CLASS WORK EVENT LOGGING---------------------------------
# import logging
# logging.debug("A simple msg")
# logging.info("This is a low severity msg")
# logging.warning("Very low file name")
# logging.error("Value error")
# logging.critical("Shutting down")

# -------------------LOGGING FROM YT-------------------------------
# import logging

# logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w"
#                     ,format="%(asctime)s-%(levelname)s-%(message)s")

# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.exception("zero division error")
# logger=logging.getLogger(__name__)
# handler=logging.FileHandler("log.log")
# formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
# logger.info("Test the custom logger")


# ----------------CLASS WORK OF LOGGING-----------------
# import logging
# logging.basicConfig(filename="log.log",filemode="w",level=logging.INFO,format='%(asctime)s - %(message)s')

# logging.debug('Admin logged out')
# logging.info('Admin logged out')
# logging.warning('Admin logged out')

# A small code to input an integer from user. Each time the code is run, the input is logged into a file
# called 'value.log'. Exceptions if any are also logged.#
# import logging
# logging.basicConfig(level=logging.INFO,filename='log.log',\
#                     format='%(asctime)s - %(message)s')

# try:
#     value=int(input('Enter an integer: '))
#     logging.info(value)
# except:
#     # # Case 1:
#     # logging.error('Error')
#     # Case 2
#     logging.exception('Error')


# Using a user-defined logger with custom settings via basicConfig function
# import logging
# logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
# logging.critical('This is a critical message')
# l=logging.getLogger('myLogger')
# l.critical('This is my logger critical message')


#Using a user-defined logger with custom settings via console handler and formatter

# import logging
# l=logging.getLogger('my_logger')
# l.setLevel(logging.DEBUG)
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# # create formatter
# formatter = logging.Formatter('%(name)s - %(levelname)s –%(message)s')

# # add formatter to ch
# ch.setFormatter(formatter)
# # add ch to logger
# l.addHandler(ch)
# # log message
# l.critical('This is a debug message')

# Using a user-defined logger with custom settings via file handler and formatter

# import logging
# l=logging.getLogger('my_logger')
# l.setLevel(logging.INFO)

# # create file handler and set level to debug
# fh = logging.FileHandler('my_log.log','w')

# # create formatter
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# # add formatter to ch
# fh.setFormatter(formatter)

# # add ch to logger
# l.addHandler(fh)

# # log message
# l.info('This is a INFO message')


# -------------------------------8 JUL 24------------------------------------------
# ----------------------IN CLASS EXERCISE--------------------
# --------------------------QUES 1 and Q2-------------------------

# def find_avg(lst):
#     try:
#         assert len(lst)!=0,"Plz enter non empty list"
#         return sum(lst)/len(lst)
#     except Exception as E:
#         print(f"{type(E)} ; {E}")

# a=find_avg([])
# # print(a)

# -----------------------------QUES NO 3------------------------------
# class circle:
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         assert self.radius!=0
#         return 3.14*self.radius**2
    
# c1=circle(0)
# print(c1.area())

# -----------------------------QUES 4---------------------------------

# def print_lst(lst):
#     try:
#         assert type(lst)==list,"No list" 
#         assert len(lst)!=0 ,"len shouldnt be zero"
#         serial=1
#         for i in lst:
#             print(f"{serial}: {i}")
#             serial+=1
    
#     except Exception as E:
#         print(f"{type(E)} ; {E}")

# # print_lst([])

# -----------------------QUES 5-------------------------------------------
# try:
#     f=open("myfile.txt","r")
#     content=f.read()
#     assert content!=" ","CONTENT NOT FOUND"
#     # content=eval(content)
#     assert isinstance(content,list),"NO LIST FOUND"
#     print(content)
#     print(f"Total numbers are {len(content)}")

# except Exception as E:
#     print(f"{type(E)} ; {E}")

# f.close()

# -------------------------10 JUL 2024------------------
# import unittest 
# def find_avg(lst):
#     try:
#         assert len(lst)!=0,"Plz enter non empty list"
#         return sum(lst)/len(lst)
#     except Exception as E:
#         print(f"{type(E)} ; {E}")

# # a=find_avg([])
# # print(a)

# class test_avg(unittest.TestCase):
#     def test_case1(self):
#         self.assertEqual(find_avg([2,3,4]),6.0)
#     def test_case2(self):
#         self.assertEqual(find_avg([2,4]),0)
#     def test_case3(self):
#         self.assertEqual(find_avg([]),1)

# unittest.main()


