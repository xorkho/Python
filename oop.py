# CODE WITH HARRY VIDEO 57
# class person:
#     name="umer"
#     Age=20
#     Occupation="Software Developer"
#     Networth=20
#     def info(self):
#         print(f"{self.name} is a {self.Occupation} ")
# a=person()
# a.name="Raza"
# a.Occupation="Programmer"
# a.info()

# b=person()
# b.name="Yousuf"
# b.Occupation="Data scientist"
# b.info()

# CODE WITH HARRY VIDEO 59
# def greet(fx):
#     def mfx(*args,**kwargs):
#         fx(*args,**kwargs)
#         # add(*args,**kwargs)
#         print("Thanks for using it ")
#     return mfx
# @greet
# def hello():
#     print("Welcome to our store")
# # hello()
# def add(a,b):
#     print(a+b)
# hello()
# greet(add)(1,2)
# CODE WITH HARRY VIDEO 60
# class tution:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def detail(self):
#         return f"This is {self.fname} {self.lname}"
# Rohan=tution("Rohan","Ali")
# Ashas=tution("Ashas","Owais")
# print(Rohan.detail())
# class student:
#     def set_name(self,name):
#         self.name=name #class attribute
#     def get_name(self):
#         return self.name
# student1=student()
# student1.set_name("Umer")
# print(student1.get_name())
# student1.engmarks=45
# print(student1.engmarks) #instance attribute use for a instance
# student2=student()
# student2.set_name("Ali")
# print(student2.get_name())
# WRITE A CLASS WHICH CALCULATE AREA AND PERIMETER OF A RECTANGLE:
# class rectangle:
#     def __init__ (self,length,width):
#         self.length=length
#         self.width=width
        
    # def set_dimension(self,length,width):  BECAUSE OF CONSTRUCTOR WE DON'T NEED IT
    #     self.length=length
    #     self.width=width      
#     def area(self):
#         return f"Area is {self.width*self.length}"
#     def parameter(self):
#         peri=(self.length+self.width)*2
#         return f"Perimeter is {peri}"
# rectangle1=rectangle(12,15)
# # rectangle1(12,15)
# print(rectangle1.area())
# print(rectangle1.parameter())
# rectangle2=rectangle(115,15)
# # rectangle1(12,15)
# print(rectangle2.area())
# print(rectangle2.parameter())


# CAMPUS X
# class ATM:
#     def __init__(self):
#         self.__pin=""
#         self.__balance=0
#         self.menu()
#     def get_pin(self):
#         return self.__pin
#     def set_pin(self,new_pin):
#         if type(new_pin)==str:
#             self.__pin=new_pin
#             print("Pin Changes successfully")
#         else:
#             print("Not Allowed")
#     def menu(self):
#         print('''What You Want to do?
#                           1: CREATE PIN
#                           2: DEPOSIT
#                           3: WITHDRAW
#                           4: CHECK BALANCE
#                           5: EXIT''')
#         user_input=input("Enter What You Want To Do: ")
#         if user_input=="1":
#             self.create_pin()
#         elif user_input=="2":
#             self.deposit_amount()
#         elif user_input=="3":
#             self.withdraw_amount()
#         elif user_input=="4":
#             self.check_balance()
#         else:
#             print("bye")
#     def create_pin(self):
#         self.__pin=input("Enter Pin")
#         print("PIN SET SUCCESSFULLY")
#     def deposit_amount(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             amount=int(input("Enter Amount"))
#             self.__balance=self.__balance+amount
#             print("Deposited successfully")
#         else:
#             print("Invalid pin")
#     def withdraw_amount(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             amount=int(input("Enter Amount For Withdraw"))
#             if amount<=self.__balance:
#                 self.__balance=self.__balance-amount
#                 print("Deposit sucessfully")
#             else:
#                 print("You dont have much amount")
#         else:
#             print("Invalid pin")
#     def check_balance(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             print(self.__balance)
#         else:
#             print("Invalid pin")


# CLASS FRACTION USED TO CREATE FRACTION
# class FRACTION:
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

# REFERENCE VARIABLE CONCEPT:
# class Customer:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# def greet(Customer):
#     if Customer.gender=='Male':
#         print('Hello',Customer.name,'sir')
#     else:
#         print('Hello',Customer.name,'Mam')
# cust=Customer('Umer','Male')
# print(greet(cust))

# COLLECTION OF OBJECTS TOPIC:


# class Customer:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def intro(self):
#         print('I am',self.name,'and I am', self.age)
# c1=Customer('Umer',18)
# c2=Customer('Ahmed',19)
# c3=Customer('Yousuf',17)
# l=[c1,c2,c3]
# for i in l:
#     i.intro()

# STATIC VARIABLE AND METHODD:
# class ATM:
#     __counter=1       
#     def __init__(self):
#         self.__pin=""
#         self.__balance=0
#         self.sno=ATM.__counter
#         ATM.__counter=ATM.__counter+1
#         # self.menu()
#     @staticmethod
#     def get_counter():
#         return ATM.__counter
#     @staticmethod
#     def set_counter(new):
#         if type(new)==int:
#             ATM.__counter=new
#         else:
#             print("INVALID")
#     def get_pin(self):
#         return self.__pin
#     def set_pin(self,new_pin):
#         if type(new_pin)==str:
#             self.__pin=new_pin
#             print("Pin Changes successfully")
#         else:
#             print("Not Allowed")
#     def menu(self):
#         print('''What You Want to do?
#                           1: CREATE PIN
#                           2: DEPOSIT
#                           3: WITHDRAW
#                           4: CHECK BALANCE
#                           5: EXIT''')
#         user_input=input("Enter What You Want To Do: ")
#         if user_input=="1":
#             self.create_pin()
#         elif user_input=="2":
#             self.deposit_amount()
#         elif user_input=="3":
#             self.withdraw_amount()
#         elif user_input=="4":
#             self.check_balance()
#         else:
#             print("bye")
#     def create_pin(self):
#         self.__pin=input("Enter Pin")
#         print("PIN SET SUCCESSFULLY")
#     def deposit_amount(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             amount=int(input("Enter Amount"))
#             self.__balance=self.__balance+amount
#             print("Deposited successfully")
#         else:
#             print("Invalid pin")
#     def withdraw_amount(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             amount=int(input("Enter Amount For Withdraw"))
#             if amount<=self.__balance:
#                 self.__balance=self.__balance-amount
#                 print("Deposit sucessfully")
#             else:
#                 print("You dont have much amount")
#         else:
#             print("Invalid pin")
#     def check_balance(self):
#         temp=input("Enter Pin")
#         if temp==self.__pin:
#             print(self.__balance)
#         else:
#             print("Invalid pin")

# RELATIONSHIP AGGREGATION:

# class customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
#     def edit_profile(self,new_name,new_city,new_pincode,new_state):
#         self.name=new_name
#         self.address.change_address(new_city,new_pincode,new_state)
# class address:
#     def __init__(self,city,pincode,state):
#         self.city=city
#         self.pincode=pincode
#         self.state=state
#     def change_address(self,new_city,new_pincode,new_state):
#         self.city=new_city
#         self.pincode=new_pincode
#         self.state=new_state
        
# add=address("Karachi",8988,"Sindh")
# cust1=customer("umer",'male',add)
# cust1.edit_profile('haseeb','Lahore',4566,'punjab')
# print(cust1.address.city)
# in aggregration u can call another class method to do task just like edit profile use change adress method to change 
# the address this is called aggregation



# RELATION INHERITANCE IN OOP:

# class user:     #PARENT CLASS
#     def login(self):
#         print('Login')   
#     def register(self):
#         print('Register')

# class student(user):        # CHILD CLASS   
#     def enroll(self):
#         print('Enroll')
#     def review(self):
#         print('Reviewed')
# stu1=student()
# stu1.login
# stu1.register
# stu1.enroll
# stu1.review

# OPERATOR OVERLOADING:
 