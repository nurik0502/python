# Task 01

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print("Петствривую",self.get_name(), "Ваш возраст =",self.get_age())
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age    
#     def set_name(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age

# person = Person("Rex", 15)
# person.set_age(17)
# person.set_name("Beka")
# person.introduce()
# print(person.get_age())

# Task 03

# class Book:
#     def __init__(self, title, author, publication_year, is_available):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.is_available = is_available
#     def checkout(self):
#         self.is_available = False
#     def checkin(self):
#         self.is_available = True
#     def display_info(self):
#         print(f"{self.title}, {self.author}, {self.publication_year}, {self.is_available}")
# book = Book("biologi", "dmfvofdn", 1998, 5446)
# print(book)
