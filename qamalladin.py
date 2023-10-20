# n = int(input("Enter tge number:")) #10
# sum_number = 0
# for i in range(n): 
#     print(i)
#     sum_number += i
# print(sum_number)    

# n = int(input("Enter the number:"))
# for i in range(n+1):
#     if i % 2 == 0:
#         print(i)

# n = int(input("Enter the number:"))
# count = 1
# while count < 11: 
#     print(f"{n}*{count}={count*n}")
#     count +=1

# word = ("Python")
# for i in range(6):
#     print(word[i])

# # n = int(input("Enter the number:"))
# count = 1
# while count < 100:
#     if count % 2 == 1:
#         print(count)
#     count += 1

# # Task 8
# lenght = int(input())
# width = int(input())
# print(lenght * width ,2 *(lenght+width))

# Task 9 
# a = input()
# print(f"Вы вели число {a}")

# # Task 10
# first_str, second_str = input().split()
# print(first_str * 2, second_str * 3)
# print(first_str,first_str,second_str,second_str,second_str)

# Tasak 11
# a = input()
# b = input()
# print("Переменная a = {} , переменная b = {}".format(a,b))

# Task 12
# a = input()
# print(a[0],a[-1])
# new_str = "Hello - python"
# print(new_str.split())

# Task 1
# for i in range(1,6):
#   for i in range (i):
#     print("*", end="")
#   print()  

# Task 2 
# for i in range(1, 6):
#    for j in range(1, 11):
#       print(i, "x", i, "=", i * j) 

# Task 3
# number = int(input("Введите число:"))
# x = True 
# for i in range(2, number):
#   if number % i == 0:
#     is_prime = False 
#     break
# if is_prime:
#   print(number, "является простым числом")
# else:
#   print(number, "Не является простым числом")  

# Task 4
# for even_numbers in range(4,15,2):
#     print(even_numbers,end=' ')

# Task 5
# print('Hello, what is your name?')
# name = input()

# x = int(input())
# if 1<=3:
#     print("Плохо")
# if 4<=6:
#     print("Удовлетворительно")
# if 7<=9:
#     print("Хорошо")  
# if 10:
#     print("Отлично")         

# n = int(input("Время "))
# if n >= 0 and n<=6:
#     print("Споконой ночи")
# elif n >= 18 and n<= 24:
#     print("Добрый вечер")
# elif n >= 12 and n<= 18:
#     print("Добрый день")
# elif n >= 6 and n<= 12:
#     print("Доброе утро")

# x = int(input())n = int(input())
# lst = [9,3,5,-3,7,8,-4]
# sum_number = 0
# for i in lst:
#     if x>0:
#        sum_number += i
#     print(sum_number)

# num = float(input())  
# num = int(num)        
# print(num % 3 == 0) 

# Task 1
# n = int(input())
# m = int(input())
# for i in range(n,m+1):
#     print(i**2, end = " ")

# Task 2 
# price = float(input())
# for i in range (1,11):
#     print(f"{price * i:.2f}",end = " ")

# Task 3
# for i in range(11):
#     print(i,end = " ")

# Task 4 
# for i in range(10, -1, -1):
#     print(i,end = " ")

# Task 5 
# for i in range(-10, 0, 2):
#     print(i,end = " ")

# Task 6 
# for i in range(1, 20, 3):
#     print(i,end = " ")

# D/z
# Task 4

# n = int(input())                    
# total = 0                       
# for i in range(n):                  
#     if i % 3 == 0 or i % 5 == 0:    
#         total += i                  
# print(total)

# Task 2

# number = int(input())     
# list_num = []             
# for i in range(1, number+1):  
#     if number % i == 0:       
#         print(i)

# Task 1
# list_word = list(map(str, input().split()))
# list_num = []                  
# for i in list_word:                 
#     list_num.append(len(i))      
# print(*list_num)

# Task 3
# list_num = list(map(int, input().split()))
# result = 0             
# for i in list_num:     
#     if i % 2 != 0:     
#         result += i
#         print(result)
    
# age = int(input("Сколько вам лет? "))
# years_left = 100 - age
# print(f"Осталось {years_left} года/лет до сталетия.")

# name = "Разработчики"
# message = f"Привет, {name}! Как у вас дела?"
# print(message)

# radius = 10
# area = f"Площадь круга с радиусом {radius} равна {3.14 * radius ** 2}"
# print(area)

# base = 2
# exponent = 3
# result = base ** exponent
# print(result) 

# x = 10
# if x > 15:
#  print("x больше 15")
# elif x > 10:
#  print("x больше 10, но не больше 15")
# else:
#  print("x не больше 10")

# x = 5
# y = 10
# if x > 0:
#  if y > 0:
#        print("Оба числа положительные")
# else:
#     print("x положительное, y отрицательное")
# else:  
# print("x отрицательное")

# flag = False
# if not flag:
#  print("Флаг ложный")
# else:
#  print("Флаг истинный")

# a = input()
# count = len(a)
# while a.count("--") !=0:
#     a = a.replace("--", "-")
#     print(a)

# n = int(input())
# ameba = 1
# for i in range(n//3):
#     ameba *=2
#     print(ameba)

# summa = 1000
# years = int(input())
# for i in range(years):
#     summa += summa*0.05
#     print()

# n = input().split()
# print(n)
# for i in range(len(n)):
#     n[i] = int(n[i])

# def sum_all_numbers(number):                    
#     sum = 0                       
#     for i in range(n):                  
#         if i % 3 == 0 or i % 5 == 0:    
#             sum += i                  
#     return sum
# n = int(input())
# summa =  sum_all_numbers(n)
# print(summa)

# l = input().split()
# for i in                

# n = int(input())
# def conv(c): 
#     f = 273+c
#     print(f)
# conv(n)

# n = int(input())
# def gcd(a,b):
#     while b !=0:
#         a, b = b, a % b
#     return a

# a = int(input())
# b = int(input())
# print(gcd(a, b))
# print((a*b)//gcd(a,b))

# Task 4  
# def fac(n):
#     if n == 1:
#         return 1
#     return fac(n - 1) * n
# print(fac(5))

# Task 11
# m = 4
# n = 2
# if m % n == 0:
#     print(int(m/n))
# else:
#     print("Не делится полностью")

# Task 21
# n = int(input())     
# print(f"{n:b}")
# print(f"{n:b}[:: -1]")

# Task 1
# n = [1,2,3,4,5,6,7,8,9,10,8,6]
# print(sum(n))
# print(sum(n)/len(n))

# Task 2
# lst_1 = ['Nurik', 'Baubek', 'Alikhan', 'Temirlan', 'Asel', 'Bota']
# for i in lst_1:
#     print(i)

# Task 3
# lst = ['Nurik', 'Baubek', 'Alikhan', 'Temirlan', 'Asel', 'Bota']
# lst.remove('Nurik')
# print(lst)

# Task 4 
# fruits = ['apple', 'banana', 'orange', 'lime', 'pineapple']
# for f in fruits:
#     if len(f) <5:
#         fruits.remove(f)
# print(fruits)

# Task 5
# students = (('Alisher',90), ('Nurbek',90) ,('Kairat',75))
# for i in students:
#     print(i)

# Task 6
# numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# numbers[1:21:2]
# print(numbers)

#  # Task 1

# lst = [int(i) for i in input().split(' ')]
# x = int(input())
# print(lst)

# Task 2
# cities = input().split()
# print(*sorted(list(map(int, input().split())), reverse=True))

# # Task 3
# lst = ['Astana', 'Aktobe', 'Taraz', 'Shymkent', 'Pavlodar']
# lst.remove('Pavlodar')
# print(lst)

# Task 4
# tom = ('Плаха', 'Чингиза', 'Айтматова', 233, 435.45) 
# for item in tom: 
#     print(item)

# Task 5
# v = [1205, 1101, 1434, 1320, 923, 874]
# print (f"{v:b}")

# Task 33
# x = int(input())
# lst = []
# for i in range(x):
#     tpl = tuple
#     for j in range(n):
#          if j == i:
#             tpl += (1,)
#          else:
#             tpl +=(0,)
#     lst.append(tpl)
# for i in tuple(lst):
#     print()
# print(tuple(lst))

# Task 32
# lst = input().split()[::-1]
# for l in lst:
#     if lst.count(l) == 1:
#         print(lst.index(l),end=" ")

# Task 31
# lst = input().split()[::-1]
# tpl = tuple()
# for l in lst:
#     if lst.count(l) != 1:
#         tpl += (l,)
#         lst.remove(l)
# print(tpl)

# Task 30
