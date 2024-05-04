# import csv
# class Item:
#     pay_rate=0.8
#     All=[]    #LIST IN WHICH ALL THE ELEMENTS RESIDE
#     def __init__(self,name:str,price:float,quantity=0):

#         self.name=name
#         self.price=price
#         self.quantity=quantity

#         Item.All.append(self) #APPEND ALL THE ELEMENTS IN THE ALL LIST

#     def calculate_price(self):
#         self.total_amount=self.quantity*self.price
#         print (f"Total price is of {self.name} is {self.total_amount}")

#     def apply_discount(self):
#         self.price=self.total_amount*self.pay_rate
#         print(f"After discount price is {self.price}")

#     @classmethod
#     def instantiate_from_csv(cls):

#         with open("oop.csv","r") as f:
#             #THIS WILL READ ALL THE CONTENT OF FILE AND RETURN IN THE FORM OF DICTIONARY
#             reader=csv.DictReader(f) 
#             items=list(reader)
        
#         for item in items:
#             print(item)
    
#     def __repr__(self):
#         return f"Item('{self.name}',{self.price},{self.quantity})"

# item1=Item("laptop",50,2)
# # item1.calculate_price()
# # item1.apply_discount()
# item2=Item("mobile",10,21)
# # item2.pay_rate=0.5
# # item2.calculate_price()
# # item2.apply_discount()
# item3=Item("mouse",60,2)
# item4=Item("charger",10,2)
# item5=Item("cable",80,2)
# # for instance in Item.All:
# #     print(instance.name)
# print(Item.All)

# print(Item.__dict__)   ALL ATTRIBUTE AT CLASS LEVEL
# print(item1.__dict__)  ALL ATTRIBUTE AT INSTANCE LEVEL
# print(item2.__dict__)  ALL ATTRIBUTE AT INSTANCE LEVEL

# Item.instantiate_from_csv()


# INHERITANCE 
# class Employee:
#     def __init__(self,Employee_ID,Employee_name,Employee_designation):
#         self.Employee_ID=Employee_ID
#         self.Employee_name=Employee_name
#         self.Employee_designation=Employee_designation

#     def display(self):
#         print(f"Employee name is {self.Employee_name} his ID is {self.Employee_ID} and he is {self.Employee_designation} in the company")

# class Manager(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)

# class Team_Lead(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)

# class clerk(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)

# E1=Team_Lead(98,"umer","Project manager")
# E1.display()





# class Employee:
#     def __init__(self, Employee_ID, Employee_name, Employee_designation):
#         self.Employee_ID = Employee_ID
#         self.Employee_name = Employee_name
#         self.Employee_designation = Employee_designation

#     def display(self):
#         print(f"Employee name is {self.Employee_name}, ID is {self.Employee_ID}, and designation is {self.Employee_designation}.")

# class Manager(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation, tasks_completed=0):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)
#         self.tasks_completed = tasks_completed

#     def display(self):
#         super().display()
#         print(f"Tasks Completed: {self.tasks_completed}")

# class Team_Lead(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation, team_size=0):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)
#         self.team_size = team_size

#     def display(self):
#         super().display()
#         print(f"Team Size: {self.team_size}")

# class Clerk(Employee):
#     def __init__(self, Employee_ID, Employee_name, Employee_designation):
#         super().__init__(Employee_ID, Employee_name, Employee_designation)

# E1 = Team_Lead(98, "Umer", "Project Manager", 10)
# E2 = Manager(99, "HASHIR", "Senior Manager", 20)
# E3 = Clerk(100,"HASSIN","clerk")

# E1.display()
# E2.display()
# E3.display()


# CREATE A STUDENT CLASS WHOSE CONSTRUCTOR TAKES MARKS OF 3 SUBJECTS AS AN ARGUMENT AND A METHOD WHICH PRINT AVERAGE OF IT
 
# class Student:

#     def __init__(self,marks):
#         self.marks=marks
    
#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         avg=round(sum/len(self.marks),2)
#         print("Average is ",avg)

# s1=Student([20,30,30,40])
# s1.average()


# Let's Practice
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

# class Account:

#     def __init__(self,Acc_No,Acc_Balance):
#         self.Acc_No=Acc_No
#         self.Acc_Balance=Acc_Balance

#     def Debit(self,Amount):
#         self.Amount=Amount
#         self.Acc_Balance-=Amount
#         print(f"{Amount}RS is debited from your account")

#     def Credit(self,Amount):
#         self.Amount=Amount
#         self.Acc_Balance+=Amount
#         print(f"{Amount}RS is credited on your account")

#     def get_balance(self):
#         print(f"Total amount in your account is {self.Acc_Balance}")
    
# c1=Account(1234,50000)
# c1.Debit(10000)
# c1.get_balance()
# c1.Credit(20000)
# c1.get_balance() 


# private method and their implementation

# class person:
#     __name="umer"

#     def __hello():
#         print("Hello")

#     def welcome(self):
#         self.__hello()
    
#     def update_name(self):
#         self.__name="ahmed"
#         print(self.__name)

# p1=person()
# print(person._person__hello()) #NAME MINGLING (classname._classname__attribute name)
# # print(p1.__name)
# p1.update_name()
# print(person._person__name)
# # print(p1.__name)
# # p1.welcome()
# # print(p1.__name)