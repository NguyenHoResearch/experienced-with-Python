"""-----What will I learn in this project-----
- 1. What is Inheritance?
- 2. Types of Inheritance
- 3. Using the super() Function
- 4. Method Overriding
- 5. Project 24: Employee Management System
"""
# %% 1. What is Inheritance?
# Inheritance allows a class to inherit properties and methods from another class.
# It promotes code reusability and reduces redundancy.
# 
# Some key terms in inheritance include:
# - The **parent class**, also called the **base class**, is the class whose properties and methods are inherited.
# - The **child class**, also called the **derived class**, is the class that inherits from the parent class.

#Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

#Child class
class Dog(Animal):
    def barks(self):
        print("Dog barks")

#Child class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
dog.sound()

# %% 2. Types of Inheritance
# The Frist Types
class Parent:
    def display(self):
        print("I am a Parent class")

class Child(Parent):
    pass

child = Child()
child.display()

# The Second Type
class A:
    def method_a(self):
        print("I am method A")

class B:
    def method_b(self):
        print("I am method B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()

# The Third Type
class GrandParent:
    def display(self):
        print("I am a Grand Parent class")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

child = Child()
child.display()

# %% 3. Using the super() Function
# The super() function allows you to call methods from the parent class.
class Animal:
  def __init__(self):
    print("Animal Created")

class Dog(Animal):
  def __init__(self):
    super().__init__()
    print("Dog Created")

dog = Dog()

# %% 4. Method Overriding
# A child class can override methods from the parent class  
# to provide specific behavior.
class Vehicle:
  def fuel_type(self):
    print("Fuel type: Petrol/Diesel")

class ElectricCar(Vehicle):
  def fuel_type(self):
    print("Fuel type: Electric")

car = ElectricCar()
car.fuel_type()

# %% 5. Project 24: Employee Management System
# Base Class: Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.1

#Derived Class: Manager
class Manager(Employee):
  def __init__(self, name, emp_id, salary, department):
    super().__init__(name, emp_id, salary)
    self.department = department

  def display_info(self):
    super().display_info()
    print(f"Department: {self.department}")

  def calculate_bonus(self):
    return self.salary * 0.2

#Derived Class: Developer
class Developer(Employee):
  def __init__(self, name, emp_id, salary, programming_language):
    super().__init__(name, emp_id, salary)
    self.programming_language = programming_language

  def display_info(self):
    return super().display_info()
    print(f"Programming Language: {self.programming_language}")

  def calculate_bonus(self):
    return self.salary * 0.5

# Main Program
employees = []

def add_employee():
  print("\n--- Choose Employee Type ---")
  print("1. Regular Employee")
  print("2. Manager")
  print("3. Developer")
  choice = int(input("Enter your choice: ").strip())

  name = input("Enter Employee Name: ").strip()
  emp_id = input("Enter Employee ID: ").strip()
  salary = float(input("Enter Employee Salary: ").strip())

  if choice == 1:
    employees.append(Employee(name, emp_id, salary))
  elif choice == 2:
    department = input("Enter Department: ").strip()
    employees.append(Manager(name, emp_id, salary, department))
  elif choice == 3:
    programming_language = input("Enter Programming Language: ").strip()
    employees.append(Developer(name, emp_id, salary, programming_language))
  else:
    print("Invalid choice")

def display_all_employees():
  print("\n--- All Employees ---")
  for employee in employees:
    employee.display_info()
    print(f"Bonus: {employee.calculate_bonus()}")

# Menu
while True:
  print("\n--- Employee Management System ---")
  print("1. Add Employee")
  print("2. Display All Employees")
  print("3. Exit")
  choice = int(input("Enter your choice(1-3): ").strip())

  if choice == 1:
    add_employee()
  elif choice == 2:
    display_all_employees()
  elif choice == 3:
    print("Exiting the program.")
    break
  else:
    print("Invalid choice")
# %%
