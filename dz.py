# Task 1

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 & set2)
# print(set1.difference(set2))
# print(set1 ^ set2)
# print(set.intersection(set2))

# Task 2
# d = {}
# key_pairs = input().split()
# for i in key_pairs:
#     key, value =i.split("=")
#     d[key] = value
# print(*sorted(d.items()))

# Task 3
# key_pairs = input().split()
# d = {}
# for i in key_pairs:
#     key,value = i.split("=")
#     d[key] = value
# if "house" in d and "True" in d and "5" in d:
#     print("Да")
# else:
#     print("Нет")

# Task 4
# key_pairs = input().split()
# d = {}
# for i in key_pairs:
#     key,value = i.split("=")
#     d[key] = value
# del d["False"]
# del d["3"]
# print(*sorted(d.items()))

# Task 5
# x = input().split()
# d = {}
# keys = []
# for i in x:
#     keys.append(i[:2])
# for i in keys:
#     d[i] = []
# for i in x:
#     d[i[:2]].append(i)
# print(list(set(keys)))
# print(d)

# Task 6
# morze = {
# 'А': '.-', 'Б': '-...', 'В': '.--',
# 'Г': '--.', 'Д': '-..', 'Е': '.',
# 'Ж': '...-', 'З': '--..', 'И': '..',
# 'Й': '.---', 'К': '-.-', 'Л': '.-..',
# 'М': '--', 'Н': '-.', 'О': '---',
# 'П': '.--.', 'Р': '.-.', 'С': '...',
# 'Т': '-', 'У': '..-', 'Ф': '..-.',
# 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
# 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--',
# 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
# 'Ю': '..--', 'Я': '.-.-', ' ': '-...-'
# }
# x = input().split()
# counter = 0
# for i in x:
#     for key,value in morze.items():
#         counter += 1
#         if value == i:
#             print(counter)

# Task 7
# print(len(set(input().split())))

# 10 Лекция

# Task 3
# a = []
# k = 10  
# for r in range(6):  
#     a.append([])  
#     for c in range(6):  
#         a[r].append(k)  
#         k += 1  
# for r in a:
#     print(r)

# Task 4
# books = {
#     "Abay Zholy":{
#         "author":"Mukhtar Auezov",
#         "desription":"dsagdfdsa",
#         "price":1000
#     }   
# }
# def find_book_info_author(author):
#     for k,v in books.items():
#         if v['author'] == author:
#             return v
# print(find_book_info_author("Mukhtar Auezov"))

# Task 5
# coordinates = (4,5,9)
# def return_sum(coordinates):
#     return sum(coordinates)
# print(return_sum(coordinates))

# Task 1
# from math import ceil
# n = float(input())
# print(ceil(n))

# Task 2

# from math import floor
# n = float(input())
# print(floor(n))

# Task 3

# from math import factorial as fact
# def factorial(n):
#     p = 1
#     for i in range(2, n+1):
#         p *= i
#     print("my factorial")
#     return f"My fact"

# Task 4

# from random import seed, randint
# seed(50)
# print(randint(10,50))

# Task 5

# from random import seed as s,random as rnd
# s(10)
# print(round(10.4567, 2)

# Task 1

# class Notes:
#     def __init__(self, uid, title, author, pages):
#             self.uid = uid
#             self.title = title
#             self.author = author
#             self.pages = pages
#     def print_notes1(self):
#         print(f"uid:{self.uid}\ntitle:{self.title}\nauthor:{self.author}\npages:{self.pages}")
# notes = Notes(1005435, "Шутка","И.С. Бах", 2 )
# notes.print_notes1()

# Task 3

# class Translator:
#     def __init__(self):
#         self.dictionary = {}
        
#     def add(self, eng, rus):
#         self.dictionary[eng] = []
#         self.dictionary[eng].remove(eng)
#     def translate(self,eng):
#         self

# Task 4

# class Money:
#     def __init__(self, money):
#         self.money = money
# my_money = Money(100)
# your_money = Money(1000)



# Task 5
# class Point:
#     def __init__(self, x, y, color ="black"):
#         self.x = x
#         self.y = y
#         self.color = color
# p1 = Point(10, 20)
# print(p1.color)
# p2 = Point(10, 5, "red")
# print(p2.color)

# Task 6

# class TriangChecker:
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if self.a <= 0 or self.b <= 0 or self.c <= and type(self.a) in [int,float]:
#             print(1)
#         elif: 

# 14
# Task 1

# class GamePole:
#     def __init__(self, n, m):
#         self.pole = []
#         for i in range(n):
#             lst = []
#             for i in range(n):
#                 lst

# Task 1

# class Graph:
#     LIMIT_Y = [0,10]
#     def set_data(self, data):
#         self.data = data
#     def draw(self):
#         for i in self.data:
#             if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
#                 print(i)
# graph_1 = Graph()
# lst = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

# graph_1()

# Task 5

# class Book:
#     def __init__(self, book, title, author, price):
#         self.__book = book
#     def set_title(self, title):
#         self.__title = title
#     def set_author(self, author):
#         self.__author = author
#     def set_price(self, price):
#         self.__price = price
#     def get_title(self):
#         return self.__title
#     def get_author(self):
#         return self.__author
#     def get_price(self):
#         return self.__price
# author = "Red Shapochka"
# book = Book(author, "Book2005", 10000)
# print(book.get_book)

# Task 6 

# class ShopItem:
#     ID_SHOP_ITEM = 0
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#     def get_pk(self):
#         return self._id
# class Book(ShopItem):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
# book = Book("Python OOП", "Балакирев", 2022)



