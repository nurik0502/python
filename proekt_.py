# import random

# def hangman():
#     words = ['python', 'hangman', 'programming', 'code']
#     word = random.choice(words)
#     guesses = ''
#     attempts = 6

#     while attempts > 0:
#         for char in word:
#             if char in guesses:
#                 print(char, end=' ')
#             else:
#                 print('_', end=' ')
#         print()

#         guess = input("Guess a letter: ")
#         guesses += guess

#         if guess not in word:
#             attempts -= 1

#         if set(word) <= set(guesses):
#             print("Congratulations! You guessed the word.")
#             break
#         elif attempts == 0:
#             print("Sorry, you ran out of attempts. The word was", word)

# hangman()

# Task 02

# def calculator():
#     num1 = float(input("Enter the first number: "))
#     operator = input("Enter an operator (+, -, *, /): ")
#     num2 = float(input("Enter the second number: "))

#     if operator == '+':
#         print(num1 + num2)
#     elif operator == '-':
#         print(num1 - num2)
#     elif operator == '*':
#         print(num1 * num2)
#     elif operator == '/':
#         print(num1 / num2)
#     else:
#         print("Invalid operator")

# calculator()


# Task 03
# def todo_list():
#     tasks = []

#     while True:
#         print("1. Add a task")
#         print("2. View tasks")
#         print("3. Remove a task")
#         print("4. Quit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             task = input("Enter a task: ")
#             tasks.append(task)
#         elif choice == '2':
#             if tasks:
#                 print("Tasks:")
#                 for task in tasks:
#                     print(task)
#             else:
#                 print("No tasks.")
#         elif choice == '3':
#             if tasks:
#                 task = input("Enter the task to remove: ")
#                 if task in tasks:
#                     tasks.remove(task)
#                     print("Task removed.")
#                 else:
#                     print("Task not found.")
#             else:
#                 print("No tasks.")
#         elif choice == '4':
#             break
#         else:
#             print("Invalid choice. Try again.")

# todo_list()


# Proekt 01

# class Task:
#     def __init__(self, book, car, drink):
#         self.book = book
#         self.car = car
#         self.drink = drink


# Proekt 02

class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = False
 
    def complete(self):
        self.is_completed = True
 
    def __str__(self):
        return f"[{self.id}] {self.title} - {self.description} (Completed: {self.is_completed})"
    
# from task import Task
 
class ToDoList:
    def __init__(self):
        self.tasks = []
 
    def add_task(self, title, description):
        new_id = len(self.tasks) + 1
        new_task = Task(new_id, title, description)
        self.tasks.append(new_task)

    def show_task(self):
        for task in self.tasks:
            print(task)

    def update_task(self, id):
        for task in self.tasks:           
            print(task)
            
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
 
    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def save_task(self):
        with open ("task.txt", "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task.__str__(    ))
            

todo_list = ToDoList()
while True:
    print("To-Do List", end = " ")
    print("""
1) Добавить задачу
2) Просмотр задач
3) Редактировать задачу
4) Удалить задачу 
5) Сохранение задач  в файл
6) Выход из программы, Досвидания!""")
    n = input("Выбери действия: ")
    if n == "1":
        print("Add task")
        todo_list.add_task("Задача выполнена" , "task")
    elif n == "2":
        print("Show All Tasks")
        todo_list.show_task()
    elif n == "3":
        print("Поменять задачу")
        todo_list.update_task(1)
    elif n == "4":
        print("Delete zadacha")
        todo_list.remove_task(2)
    elif n == "5":
        print("Я сохраняю файл")
        todo_list.save_task()
    elif n == "6":
        print("Выхожу из программы, Досвидания!")
        break







# "a" = append
# "w" = write
# "r" read
# with open("task.txt", "r", encoding="uft-8") as file:
    # print(file.)



# todo_list = ToDoList()
# todo_list.add_task("task", "Задача выполнена")
# todo_list.display_tasks()
# todo_list.remove_task(1)

# from todolist import ToDoList
 
# Создаем ToDoList
# my_list = ToDoList()
 
# Добавляем задачи
# my_list.add_task("Выучить Python", "Изучить основы языка Python")
# my_list.add_task("Написать статью", "Написать статью на тему ToDoList с использованием Python")
 
# # Выводим все задачи
# my_list.display_tasks()
 
# # Завершаем первую задачу
# my_list.tasks[0].complete()
 
# # Выводим все задачи
# my_list.display_tasks()
 
# # Удаляем вторую задачу
# my_list.remove_task(2)
 
# # Выводим все задачи
# my_list.display_tasks()