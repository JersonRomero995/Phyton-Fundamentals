What is Programming?
Programming is the process of creating a set of instructions that tell a computer how to perform a task. These instructions are written in a programming language that both humans and computers can understand.
Why Python?

🐍 Easy to learn - Clean, readable syntax
🚀 Versatile - Web, data science, automation, AI
📚 Huge community - Extensive libraries and support
💼 Industry standard - Used by Google, NASA, Netflix
🔧 Great for automation - Perfect for your vSphere/AWS goals!

How Python Works
Source Code (.py file)
    ↓
Python Interpreter
    ↓
Machine Code
    ↓
Computer executes

Python Basics
Installing Python
Official Download: https://www.python.org/downloads/
bash# Verify installation
python --version
# or
python3 --version

# Open Python interactive shell
python
>>> print("Hello, World!")
Hello, World!
>>> exit()
Your First Program
python# hello.py
print("Hello, World!")
print("Welcome to Python programming!")

# Run with:
# python hello.py
Comments
python# This is a single-line comment
# Comments explain what your code does

"""
This is a multi-line comment
(also called a docstring)
Used for longer explanations
"""

print("Hello")  # You can add comments after code too

Variables and Data Types
What is a Variable?
A variable is a container for storing data values. Think of it as a labeled box where you can put information.
python

# Creating variables (assignment)
name = "John"
age = 25
height = 5.9
is_student = True

# Variables are case-sensitive
Name = "Jane"  # This is different from 'name'
Naming Rules
python# ✅ VALID variable names
user_name = "Alice"
user1 = "Bob"
_private = "secret"
userName = "Charlie"  # camelCase
USER_NAME = "Dave"    # UPPERCASE (usually constants)

# ❌ INVALID variable names
# 1user = "Invalid"      # Can't start with number
# user-name = "Invalid"  # No hyphens
# user name = "Invalid"  # No spaces
# class = "Invalid"      # Can't use Python keywords


Data Types
Python has several built-in data types:
python

# 1. INTEGER (int) - Whole numbers
age = 25
year = 2024
negative = -10

# 2. FLOAT (float) - Decimal numbers
price = 19.99
temperature = -5.5
pi = 3.14159

# 3. STRING (str) - Text
name = "Alice"
message = 'Hello, World!'
multiline = """This is
a multi-line
string"""

# 4. BOOLEAN (bool) - True or False
is_active = True
has_permission = False

# 5. NONE TYPE - Represents absence of value
result = None
Type Checking and Conversion
python

# Check type
x = 10
print(type(x))  # <class 'int'>

# Type conversion (casting)
# String to integer
age_str = "25"
age_int = int(age_str)  # 25

# Integer to string
num = 100
num_str = str(num)  # "100"

# String to float
price_str = "19.99"
price_float = float(price_str)  # 19.99

# Integer to float
x = 5
y = float(x)  # 5.0

# Float to integer (truncates decimal)
z = 3.9
z_int = int(z)  # 3 (not 4!)
String Operations
python

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"

# String formatting (f-strings - Python 3.6+)
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old"
print(message)  # My name is Alice and I am 30 years old

# String methods
text = "Hello, World!"
print(text.upper())      # "HELLO, WORLD!"
print(text.lower())      # "hello, world!"
print(text.replace("Hello", "Hi"))  # "Hi, World!"
print(len(text))         # 13 (length)
print(text.split(","))   # ['Hello', ' World!']

# String indexing
word = "Python"
print(word[0])    # 'P' (first character)
print(word[-1])   # 'n' (last character)
print(word[0:3])  # 'Pyt' (slice)

Operators
Arithmetic Operators
python
x = 10
y = 3

# Basic operations
print(x + y)   # 13  Addition
print(x - y)   # 7   Subtraction
print(x * y)   # 30  Multiplication
print(x / y)   # 3.333... Division (always returns float)
print(x // y)  # 3   Floor division (integer result)
print(x % y)   # 1   Modulus (remainder)
print(x ** y)  # 1000 Exponentiation (10^3)

# Compound assignment
count = 5
count += 1   # Same as: count = count + 1  (now 6)
count -= 2   # Same as: count = count - 2  (now 4)
count *= 3   # Same as: count = count * 3  (now 12)
count /= 4   # Same as: count = count / 4  (now 3.0)
Comparison Operators
python

x = 10
y = 5

print(x == y)   # False  Equal to
print(x != y)   # True   Not equal to
print(x > y)    # True   Greater than
print(x < y)    # False  Less than
print(x >= y)   # True   Greater than or equal to
print(x <= y)   # False  Less than or equal to

# Comparing strings
print("apple" == "apple")   # True
print("apple" < "banana")   # True (alphabetical order)
Logical Operators
python

# AND - Both conditions must be True
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True

# OR - At least one condition must be True
is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday  # True

# NOT - Inverts the boolean value
is_raining = False
is_sunny = not is_raining  # True

# Complex conditions
age = 20
has_permission = True
is_valid = (age >= 18 and has_permission) or age >= 21

Control Flow
If Statements
python

# Basic if
age = 18
if age >= 18:
    print("You are an adult")

# if-else
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Nested if statements
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

For Loops
python

# Loop through a range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through a range with start and end
for i in range(1, 6):
    print(i)  # Prints 1, 2, 3, 4, 5

# Loop through a range with step
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Loop through a string
for letter in "Python":
    print(letter)  # Prints P, y, t, h, o, n
While Loops
python# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget to increment!

# While loop with condition
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Infinite loop (use CTRL+C to stop)
# while True:
#     print("This runs forever!")

# Break statement - exits loop
for i in range(10):
    if i == 5:
        break  # Stop when i equals 5
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue statement - skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)  # Prints 0, 1, 3, 4

Functions
What is a Function?
A function is a reusable block of code that performs a specific task.
Defining Functions
python

# Basic function
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8

# Function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20

# Function with default parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")          # Hello, Mr. Smith
greet_with_title("Johnson", "Dr.")  # Hello, Dr. Johnson

# Function with multiple return values
def get_name():
    first = "John"
    last = "Doe"
    return first, last

first_name, last_name = get_name()
print(first_name)  # John
print(last_name)   # Doe
Function Scope
python

# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

my_function()
print(global_var)  # Works
# print(local_var)  # ERROR! local_var doesn't exist here

# Modifying global variables
counter = 0

def increment():
    global counter  # Tell Python we want to modify global
    counter += 1

increment()
print(counter)  # 1
Docstrings
pythondef calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

Data Structures
Lists
python

# Create a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Access elements
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)

# Modify lists
fruits.append("orange")         # Add to end
fruits.insert(1, "mango")       # Insert at position
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last item
fruits[0] = "pear"             # Change item

# List operations
print(len(fruits))             # Length
print("apple" in fruits)       # Check if item exists
fruits.sort()                  # Sort in place
Dictionaries
python

# Create a dictionary (key-value pairs)
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Access values
print(student["name"])        # Alice
print(student.get("age"))     # 20

# Modify dictionaries
student["age"] = 21           # Update value
student["email"] = "alice@example.com"  # Add new key
del student["grade"]          # Delete key

# Dictionary operations
print(student.keys())         # All keys
print(student.values())       # All values
print(student.items())        # All key-value pairs

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
Tuples
python# Create a tuple (immutable)
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Access elements
x = coordinates[0]  # 10
y = coordinates[1]  # 20

# Tuple unpacking
x, y = coordinates
print(x)  # 10
print(y)  # 20

# Tuples are immutable
# coordinates[0] = 15  # ERROR! Can't modify
Sets
python# Create a set (unique items, unordered)
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 3, 4}  # Duplicates removed automatically

# Set operations
fruits.add("orange")
fruits.remove("banana")
print("apple" in fruits)  # True

# Set math
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}

Input/Output
User Input
python# Get input from user (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Convert input to number
age_str = input("Enter your age: ")
age = int(age_str)

# One-liner
age = int(input("Enter your age: "))

# Handle multiple inputs
full_name = input("Enter first and last name: ")
first, last = full_name.split()
File I/O
python# Write to file
file = open("output.txt", "w")
file.write("Hello, World!\n")
file.write("This is a new line.")
file.close()

# Better way - automatically closes file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!")

# Read from file
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Append to file
with open("output.txt", "a") as file:
    file.write("\nNew line added")

Error Handling
Try-Except Blocks
python# Basic error handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch any error
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")

# Try-except-else-finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully")
    print(content)
finally:
    print("This always executes")
    # file.close() if needed