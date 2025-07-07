import datetime

def greet_user():
    print("Hello! I am your Python assistant.")
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(f"The current time is {current_time}.")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")

greet_user()


### **Step 2: Add a Command Menu**

def display_menu():
    print("\nWhat would you like to do?")
    print("1. Manage To-Do List")
    print("2. Perform Calculations")
    print("3. Show Current Date and Time")
    print("4. Search Files in a Folder")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Goodbye! Have a great day!")
        break
    elif choice == '1':
        print("To-Do List Manager Coming Soon...")
    elif choice == '2':
        print("Calculator Coming Soon...")
    elif choice == '3':
        print("Date and Time Feature Coming Soon...")
    elif choice == '4':
        print("File Search Coming Soon...")
    else:
        print("Invalid choice. Please choose a number between 1-5.")


### **Step 3: Build a To-Do List Manager**

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    view_tasks()
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed = tasks.pop(task_number)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number!")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def to_do_list_manager():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose between 1-4.")

### **Step 4: Build a Simple Calculator**


def calculator():
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")


### **Step 5: Display Current Date and Time**



def show_date_time():
    now = datetime.datetime.now()
    print("\n--- Current Date and Time ---")
    print(now.strftime("Date: %Y-%m-%d"))
    print(now.strftime("Time: %H:%M:%S"))


### **Step 6: Search Files in a Folder**



import os

def search_files():
    folder_path = input("Enter the folder path: ")
    search_term = input("Enter the file name to search for: ")

    if os.path.exists(folder_path):
        print("\nSearching...")
        files = os.listdir(folder_path)
        found_files = [f for f in files if search_term in f]

        if found_files:
            print("Files found:")
            for file in found_files:
                print(file)
        else:
            print("No files found with that name.")
    else:
        print("The folder path does not exist.")



while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        to_do_list_manager()
    elif choice == '2':
        calculator()
    elif choice == '3':
        show_date_time()
    elif choice == '4':
        search_files()
    elif choice == '5':
        print("Goodbye! Have a great day!")
        break
    else:
        print("Invalid choice. Please choose a number between 1-5.")