# -------------------------2023 PAST PAPER----------------------------
# from collections.abc import Container
# class odd_container:
#     def __contains__(self,x):
#         if not isinstance(x,int) or x %2:
#             return False
#         return True
# print(issubclass(odd_container,Container))


# try:
#     raise Exception ("This is always executed")
#     print("Never Executed")
    
# except Exception as E:
#     print(f"i caught an exception {E!r}")
# print("Executed after exception")


# animal="cat"
# family="persian"

# class pranthera:
#     animal="lion"
#     family="cheetah"
#     def __init__(self):
#         self.family="dog"
#         animal="german"
#         def display():
#             print(self.family)
#             print(self.animal)
#             print(family)
#             print(animal)
#         display()
# f=pranthera()


# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def do_action(self):
#         pass

# a=Animal()
# from math import sqrt
# class point:
#     def __init__(self,x,y):
#         self.setter(x,y)
    
#     def setter(self,x,y):
#             self.x=x
#             self.y=y
    
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
# class line_segment:

#     def __init__(self,x1,y1,x2,y2):
#         self.p1=point(x1,y1)
#         self.p2=point(x2,y2)

#     def line_distance(self):
#         self.tot=round(sqrt((self.p2.x-self.p1.x)**2 + (self.p2.y-self.p1.y)**2),3)
#         return self.tot
#     def __gt__(l1,l2):
#         return l1.tot>l2.tot
         
         
# l=line_segment(3,4,5,7)
# print(l.line_distance())

# l1=line_segment(10,5,6,8)
# print(l1.line_distance())

# print(l1>l)


# class exponential:
#     try:
#         def __init__(self,b=1,e=1):
#             if b==0 or e==0:
#                 raise Exception ("Invalid 0 Input")
#             else:
#                 self.base=b
#                 self.exp=e
            
#         def __str__(self):
#             return f"{self.base}^{self.exp}"
        
#         def __mul__(self,p):
#             if self.base==p.base:
#                 return f"{self.base}^{self.exp+p.exp}"
#             else:
#                 raise Exception("BASES NOT SAME")
        
#     except Exception as E:
#         print(E)
# e1=exponential()
# e2=exponential(2)
# print(e1*e2)
# from abc import ABC ,abstractmethod
# class shape(ABC):
#     def __init__(self,name,dimension=[0,0]) :
#         self.name=name
#         self.dimension=dimension

#     @abstractmethod
#     def area(self):
#         pass
    
#     def perimeter(self):
#         return sum(self.dimension)
    
# # sq=shape("rectangle",[6,3])
# # print(sq.area())
# # print(sq.perimeter())

# class rightTriangle(shape):
#     def area(self):
#         return round((self.dimension[0]*self.dimension[1])/2,2)

# r=rightTriangle("right",[3,4,5])
# print(r.area())
# print(r.perimeter())


# try:
#     x=int(input('Enter a value'))
#     print (x)

# except ValueError:
#     print ( 'Wrong value entered')

# except Exception:
#     print('Something went wrong!')
# def cheers(fn):
#     def inner(winner):
#         fn(winner)
#         print("How do u spell winner")
#         print("i know i know")
#         print(winner)

#     return inner


# @cheers
# def print_name(winner):
#     print(f"winner is {winner}")

# print_name("umer")

# class Goat:
#     def __init__(self,name,sport,age,gender):
#         self.name=name
#         self.sport=sport
#         self.age=age
#         self.gender=gender
     
#     def __str__(self):
#         return f"Goat(name={self.name}, sport={self.sport}, age={self.age}, gender={self.gender})"
    
# class display:
#     def display(self,max_age,min_age,gender):
#         # self.gender=gender
#         for member in self.all_goat:
#             if min_age<=member.age<=max_age:
#                 if member.gender=="M" and gender!="F":
#                     print(f"Mr.{member.name} He is {member.age} years old & he plays {member.sport}")
#                 if member.gender=="F" and gender!="M":
#                     print(f"Ms.{member.name} she is {member.age} years old & she plays {member.sport}")

# class sport(display):
#     def __init__(self):
#         self.all_goat=[]
    
#     def add_member(self,name,sport,age,gender):
#         new_goat=Goat(name,sport,age,gender)
#         self.all_goat.append(new_goat)
    

# all_times=sport()
# all_times.add_member("BABAR","CRICKET",28,"M")
# all_times.add_member("RONALDO","FOOTBALL",38,"M")
# all_times.add_member("SANIA","TENNIS",35,"F")
# all_times.add_member("ASH","GAMER",20,"M")
# all_times.display(50,0,0)

# class ingridient:
#     def __init__(self,name=None,quantity=None,units=None):
#         self.name=name
#         self.quantity=quantity
#         self.units=units
#     def print(self):
#         print(f"<{self.name}>:<{self.quantity}> <{self.units}>")

# ing=ingridient("BUTTER",1,"KG")
# ing.print()

# class Recipe:
#     def __init__(self, recipe_name):
#         self.recipe_name=recipe_name
#         self.ingridient_list=[]
#         self.procedure=""
#         self.carbohydrate=""
#         self.protein=""
#         self.fats=""
#     def add_ingridient(self,q,i,u):
#         self.quantity=q
#         self.ingridient=i
#         self.unit=u
#         l=[self.ingridient,self.quantity,self.unit]
#         self.ingridient_list.append(l)

#     def set_procedur(self,p):
#         self.procedure=p

#     def set_portion(self,c,p,f):
#         self.protein=p
#         self.carbohydrate=c
#         self.fats=f

#     def calculate_calories(self):
#         return self.carbohydrtae*4+self.protein*4+self.fats*9

#     def print(self):
#         print(f'''{self.recipe_name}\nINGRIDIENTS:\n
#               ''')


# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner

# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner

# @decor1
# @decor
# def func():
#     return 5

# @decor
# @decor1
# def func2():
#     return 3

# print(func())
# print(func2())


class car:
    __color=5
    _wheel=4
    def __init__(self):
        self.__a=2
        self._b=3
        
    @staticmethod
    def cal_mile(a,b):
        return a+b
# c1=car()
print(car._car__color)
# print(c1._car__color)
# print(c1._wheel)

