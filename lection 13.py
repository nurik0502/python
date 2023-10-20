# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def description(self):
#         print(self.brand, self.model, self.year)


# my_car = Car("Mersedes", "CLS 63", 2020)
# my_car.description()

# class Person:
#     def __init__(self, name , age, salary = 0):
#         self.name = name
#         self.age = age
# class Employee(Person):
#      def __init__(self,name , age, salary):
#          self.salary = salary
#          super().__init__(name,age)
#      def get_info(self):
#          print(f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}")
    
# emp = Employee("Rex", 2000, 10000)
# emp.get_info()

# class BankAccount:
#     def __init__(self, balance, account_numder):
#         self.balance = balance
#         self.account_number = account_numder
#     def deposit(self, amout):
#         self.balance += amout
#     def witndraw(self , amout):
#         self.balance -= amout
# class SavingAccount(BankAccount):
#     def __init__(self, balance, account_number, interest_rate):
#         super().__init__(balance, account_numder)
#         self.interest_rate = interest_rate
#     def add_interest(self,percent):
#         self.balance += (self.balance * percent) / 100
# account1 = SavingAccount(2000,1,20)
# print(account1.balance)

