# Task 01

# ariphmetika = int(input())
# n = int(input())
# try:
#     print(ariphmetika / n)
# except ZeroDivisionError as e:
#     print(e)

# Task 02 

# class ContextManager:
#     def __ente__(self):
#         pass
#     def __exit__(self, *args):
#         pass

# Task 01

# from abc import ABC,abstractmethod
# class ShopInterface:
#     @abstractmethod
#     def get_it(self):
#         raise NotImplementedError("в классе не переопределен метод get_in")
# class ShopItem(ShopInterface):
#     _id = 0
#     def __init__(self, name, weidht, price):
#         self._id = ShopItem._id
#         self._name = name
#         self._weidht = weidht
#         self._price = price

# Task 02

# from abc import ABC, abstractmethod
# class Transprot(ABC):
#     @abstractmethod
#     def go(self):
#         """Метод для перемещения транспортного средства"""
# @classmethod
# @abstractmethod
# def abstract_class_method(cls):
#         """Абстрактный метод класса"""

# class Model:
#     @abstractmethod
#     def get_pk(self):
#          pass
#     def get_info(self):
#         return "Базовый класс Model"
    

# class ModelFrom(Model):
#      __id = 0
#      def __init__(self, login, password):
#         self._id = ModelFrom.__id
#         self.login = login
#         self.password = password
#         ModelFrom.__id +=1
#      def get_pk(self):
#         return self._id 
# login = ()
# password = ()
# form = ModelFrom(login, password)
# print(form.get_pk())

# Task 03
# from abc import abstractmethod

# class StackInterface:
#     @abstractmethod
#     def push_back(self):
#         pass
#     @abstractmethod
#     def pop_back(self):
#         pass
# class Stack(StackInterface):
#     def __init__(self):
#         self._id

