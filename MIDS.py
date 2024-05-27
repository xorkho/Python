# IMPLEMENTATTION OF STR METHOD

# class student:
#     def __init__(self,name,grades):
#         self.name=name
#         self.grades=grades
    
#     def __str__(self):
#         return f"{self.name} got {self.grades}"
    
# S1=student("umer","A+")
# print(S1)

# class shape:

#     def __init__(self,sides):
#         self.sides=sides
    
# class Rectangle(shape):
#     def __init__(self,length=0,width=0):
#         self.length=length
#         self.width=width
#         super().__init__(4)
    
#     def Area(self):
#         return self.length*self.width
    
#     def perimeter(self):
#         return 2*(self.length+self.width)
    
#     def __str__(self):
#         s=f"Number of sides {self.sides}\n"
#         s+=f"length {self.length}\n"
#         s+=f"width {self.width}\n"
#         s+=f"Perimeter {self.perimeter()}\n"
#         s+=f"Area: {self.Area()}\n"
#         return s


# obj1=Rectangle(2,3)
# print(obj1)

# CREATE A CLASS STRING WHICH INHERITE FROM BUILTINS CLASS (STRING) AND CREATE A METHOD WORD COUNT:

# class String(str):

#     def word_count(self,word):
#         self.word=word
#         return len(self.word)

# obj1=String()
# print(obj1.word_count("UMER AHMED HASEEB"))

# CREATE A CLASS PHONE BOOK WHICH IMPLEMENTS THE FOLLOWING THINGS
# STORED NAME ,PHONE , EMAIL ,ADD ITEMS, SORT ITEMS ON NAME, SEARCH ITEM BY NAME
# PRINT IN READABALE WAY 

# class phonebook(list):
#     def __str__(self):
#         s=""
#         for item in self:
#             s+=f"{item[0]},{item[1]},{item[2]}\n"
#         return s
#     def search(self,n):
#         found=phonebook([])
#         for item in self:
#             if n in item[0]:
#                 found.append(item)
#         return found
    
# pb=phonebook([])
# pb.append(["Umer","03328264639","umer@gmail.com"])
# pb.append(["haseeb","03351205349","haseeb@gmail.com"])
# print(pb)
# pb.sort()
# print(pb)
# print(pb.search("e"))

# APPROACH 2:
# class phonebook:
#     def __init__(self):
#         self.contacts=[]

#     def append(self,item):
#         self.contacts.append(item)

#     def sort(self):
#         self.contacts.sort()
    
#     def __str__(self):
#         s=""
#         for item in self.contacts:
#             s+=f"{item[0]},{item[1]},{item[2]}\n"
#         return s
    
#     def search(self,n):
#         found=phonebook([])
#         for item in self:
#             if n in item[0]:
#                 found.append(item)
#         return found
# pb=phonebook()
# pb.contacts.append(["umer","03328264639","umer@gmail.com"])
# pb.contacts.append(["haseeb","03359224699","haseeb@gmail.com"])
# print(pb.contacts)
# pb.sort()
# # print(pb)
# pb.search("umer")

# -----------------------AGGREGATION-------------------------------------
# class address:

#     def __init__(self,city,state):
#         self.city=city
#         self.state=state

# class person:

#     def __init__(self,name,add):
#         self.name=name
#         self.add=add

    
#     def info(self):
#         return f"name {self.name} & address {self.add}"

# d1=address("karachi","Sindh")
# p1=person("umer",d1)
# print(p1.add.state)
# # print(p1.info())

# class car:
#     def __init__(self,model,engine_no):
#         self.model=model
#         self.engine_no=engine_no

# class engine:
#     def __init__(self,en):
#         self.en=en

# eng=engine("0114")
# my_car=car("2034",eng)
# del my_car
# # print(my_car.model)
# print(eng.en) 

# ------------------TYPES OF ASSOCIAITION--------------------------------------------

# -------------------ONE TO MANY TYPE--------------------------------------------------

# class library:

#     def __init__(self):
#         self.books=[]

#     def add_books(self,book_name):
#         self.books.append(book_name)
    
#     def show_books(self):
#         l=[]
#         for i in self.books:
#             l.append(i.name)
#         return l


# class book:

#     def __init__(self,name):
#         self.name=name

# b1=book("calculus")
# b2=book("Programming")
# lib=library()
# lib.add_books(b1)
# lib.add_books(b2)
# print(lib.show_books())

# -------------- MANY TO MANY -----------------------------------------------------------

# class book:

#     def __init__(self,book_name):
#         self.book_name=book_name
#         self.author=[]

#     def add_author(self,author_name):
#         self.author.append(author_name)
        
    

# class Author:

#     def __init__(self,author_name):
#         self.author_name=author_name
#         self.books=[]

#     def add_books(self,name):
#         self.books.append(name)
    
#     def show_books(self):
#         l=[]
#         for i in self.books:
#             l.append(i.book_name)
#         return l

# b1=book("python")
# b2=book("calculus")
# A1=Author("umer")
# A1.add_books(b1)
# A1.add_books(b2)
# print(A1.books)
# print(A1.show_books())



# class Book:

#     def __init__(self, book_name):
#         self.book_name = book_name
#         self.authors = []

#     def add_author(self, author_name):
#         self.authors.append(author_name)

# class Author:

#     def __init__(self, author_name):
#         self.author_name = author_name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def show_books(self):
#         return [book.book_name for book in self.books]

# # Creating book instances
# b1 = Book("Python")
# b2 = Book("Calculus")

# # Creating author instance
# A1 = Author("Umer")

# # Adding books to the author
# A1.add_book(b1)
# A1.add_book(b2)

# # Printing the list of book objects associated with the author
# print(A1.books)  # This will print the book objects

# # Printing the names of the books associated with the author
# print(A1.show_books())  # This will print the book names
