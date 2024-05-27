# PRACTICE PROBLEMS Q1:
# MAKE A CLASS CIRCLE IN WHICH WE CAN SET COLOR RADIUS AND GET THE OUTPUT OF AREA AND CIRCUMFERENCE

# class Circle:

#     def set_color(self,color):
#         self.color=color

#     def get_color(self):
#         return self.color
    
#     def set_radius(self,radius):
#         self.radius=radius

#     def get_radius(self):
#         return self.radius
    
#     def get_circumference(self):
#         print(f"Circumference: {2*3.14*self.radius}")
    
#     def get_area(self):
#         print(f"Area: {3.14*(self.radius**2)}")
    
# c1=Circle()
# c1.set_radius(4)
# c1.get_circumference()
# c1.get_area()

# PRACTICE PROBLEMS Q2:
# MAKE A BANK CLASS AND DEFINE METHODS OF WITHDRAW DEPOSIT AND CHECK BALANCE 

# class Bank:
#     __Balance=0
#     def with_draw(self,Amount):
#         self.Amount=Amount
#         Bank.__Balance-=Amount
#         print(f"You have withdraw amount {self.Amount}RS")
#     def deposit(self,Amount):
#         self.Amount=Amount
#         Bank.__Balance+=Amount
#         print(f"You have deposited amount {self.Amount}RS")
#     def check_balance(self):
#         print(f"You have {Bank.__Balance}RS in your account")

# b1=Bank()
# b1.deposit(50000)
# b1.with_draw(30000)
# b1.check_balance()
# Bank._Bank__Balance=500000  #THROUGH THE NAME MINGLING WE CAN CHANGE THE ATTRIBUTE ON A CLASS LEVEL
# b1.check_balance()
# b1.with_draw(500000)
# b1.check_balance()

# PRACTICE PROBLEMS Q3:
# MAKE CLASS WORKER AND CALCULATE AND PRINT THE WAGE ACCORDING TO ITS HOURLY RATE

# class worker:
#     def __init__(self,hour_worked=0,rate=50):
#         self.hour_worked=hour_worked
#         self.rate=rate
#     def pay(self):
#         pay=self.hour_worked*self.rate
#         print(f"Total wage is {pay} RS")

# w1=worker(10,80)
# w1.pay()

# PRACTICE PROBLEMS Q4:
# DEVELOP CLASS TRACKER IN WHICH WE CAN TRACK THE CREATION OF OBJECT BY INCREASING THE COUNT

# class Tracker:
#     Counter=0

#     def __init__(self):
#         Tracker.Counter+=1

#     def report_serial(self):
#         print(f"I Am object number {self.Counter}")
# o1=Tracker()
# o1.report_serial()
# o2=Tracker()
# o2.report_serial()
# print(Tracker.Counter)
# o3=Tracker()
# o3.report_serial()
# # print(Tracker.Counter)

# class phonebook(list,file_saver,file_reader):

#     def __str__(self):
#         s="name,phone_no,email\n"
#         for item in self:
#             s+=f"{item[0]},{item[1]},{item[2]}\n"
#         return s
    
#     def search(self,n):
#         found=phonebook([])
#         for item in self:
#             if n in item[0]:
#                 found.append(item)
#         return found
    
# class file_saver:
#     def save_to_file(self,filename):
#         f=open(filename,"w")
#         for item in self:
#             f.write(str(item)+"\n")
#         f.close()

# class file_reader:
#     def read_from_file(self,filename):
#         f=open(filename,"r")
#         f.seek(0)
#         for item in f:
#             self.append()

# COMPOSITION CODE :BASICALLY TO DELEGATE SOME WORK TO OTHER CLASS
# EMPLOYEE CLASS USE SALARY CLASS TO PRINT THE TOTAL SALARY

# class salary:

#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
    
#     def annual_salary(self):
#         return (self.pay*12)+self.bonus

# class Employee:

#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary(pay,bonus)
    
#     def total_salary(self):
#         return self.obj_salary.annual_salary()

# E1=Employee("umer","18",50000,10000)
# print(E1.total_salary())

# AGGREGRATION: HAS-A RELAITONSHIP 
# class salary:

#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
    
#     def annual_salary(self):
#         return (self.pay*12)+self.bonus

# class Employee:

#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary
    
#     def total_salary(self):
#         return self.obj_salary.annual_salary()
    
# s1=salary(50000,10000)
# E1=Employee("umer","18",s1)
# print(E1.total_salary())