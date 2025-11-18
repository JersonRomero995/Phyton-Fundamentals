Python Array Data Structures
📚 Table of Contents

-What are Arrays?
-Lists (Python's Dynamic Arrays)
-Tuples (Immutable Arrays)
-Array Module
-NumPy Arrays
-Common Operations
-Performance Comparison
-Best Practices


What are Arrays?
An array is a data structure that stores a collection of elements (values or variables), each identified by an index or key.
Key Characteristics:

📦 Store multiple items in a single variable
🔢 Elements are ordered and indexed (starting at 0)
🎯 Allow direct access to elements via index
📊 Typically store elements of the same type (in some languages)

Visual Representation:
Index:    0      1      2      3      4
         ┌──────┬──────┬──────┬──────┬──────┐
Array:   │  10  │  20  │  30  │  40  │  50  │
         └──────┴──────┴──────┴──────┴──────┘

Lists (Python's Dynamic Arrays)
Lists are Python's built-in dynamic arrays. They're the most commonly used array-like structure.
Creating Lists
python# Empty list
empty_list = []

# List with initial values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Mixed data types (Python allows this!)
mixed = [1, "hello", 3.14, True]

# Nested lists (2D array)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using list() constructor
letters = list("abc")  # ['a', 'b', 'c']
range_list = list(range(5))  # [0, 1, 2, 3, 4]
Accessing Elements
pythonfruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (from start)
print(fruits[0])   # "apple"
print(fruits[2])   # "cherry"

# Negative indexing (from end)
print(fruits[-1])  # "date" (last item)
print(fruits[-2])  # "cherry" (second to last)

# Slicing [start:end:step]
print(fruits[1:3])    # ["banana", "cherry"]
print(fruits[:2])     # ["apple", "banana"]
print(fruits[2:])     # ["cherry", "date"]
print(fruits[::2])    # ["apple", "cherry"] (every 2nd item)
print(fruits[::-1])   # ["date", "cherry", "banana", "apple"] (reversed)
Modifying Lists
pythonnumbers = [1, 2, 3, 4, 5]

# Change a single element
numbers[0] = 10  # [10, 2, 3, 4, 5]

# Change multiple elements
numbers[1:3] = [20, 30]  # [10, 20, 30, 4, 5]

# Append (add to end)
numbers.append(6)  # [10, 20, 30, 4, 5, 6]

# Insert at specific position
numbers.insert(1, 15)  # [10, 15, 20, 30, 4, 5, 6]

# Extend (add multiple items)
numbers.extend([7, 8, 9])  # [10, 15, 20, 30, 4, 5, 6, 7, 8, 9]

# Remove by value
numbers.remove(30)  # Removes first occurrence of 30

# Remove by index
deleted = numbers.pop(2)  # Removes and returns item at index 2

# Remove last item
last = numbers.pop()  # Removes and returns last item

# Clear all items
numbers.clear()  # []
List Methods Cheat Sheet
pythonfruits = ["apple", "banana", "cherry", "banana"]

# Length
len(fruits)  # 4

# Count occurrences
fruits.count("banana")  # 2

# Find index of first occurrence
fruits.index("cherry")  # 2

# Sort (modifies original)
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # [1, 1, 3, 4, 5]
numbers.sort(reverse=True)  # [5, 4, 3, 1, 1]

# Sorted (returns new list)
sorted_nums = sorted(numbers)  # Original unchanged

# Reverse (modifies original)
numbers.reverse()  # Reverses in place

# Copy
fruits_copy = fruits.copy()  # Shallow copy
fruits_copy2 = fruits[:]     # Another way to copy

Tuples (Immutable Arrays)
Tuples are like lists but immutable (cannot be changed after creation).
Why Use Tuples?

✅ Faster than lists
✅ Protect data from accidental modification
✅ Can be used as dictionary keys
✅ Perfect for fixed data (coordinates, RGB colors, etc.)

Creating Tuples
python
# Empty tuple
empty_tuple = ()

# Single item tuple (note the comma!)
single = (5,)  # Without comma, it's just 5
wrong = (5)    # This is just an integer

# Multiple items
coordinates = (10, 20)
rgb = (255, 128, 0)

# Without parentheses (tuple packing)
point = 10, 20, 30

# Using tuple() constructor
tuple_from_list = tuple([1, 2, 3])
Accessing Tuples
pythonpoint = (10, 20, 30)

# Indexing (same as lists)
x = point[0]  # 10
z = point[-1]  # 30

# Slicing (same as lists)
first_two = point[:2]  # (10, 20)

# Unpacking
x, y, z = point
print(x)  # 10
print(y)  # 20
print(z)  # 30

# Unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
Tuple Methods
pythonnumbers = (1, 2, 3, 2, 2, 4)

# Count occurrences
numbers.count(2)  # 3

# Find index
numbers.index(3)  # 2

# Length
len(numbers)  # 6

# Note: No append, remove, or other modification methods!
When to Use Tuples vs Lists
python# Use TUPLES for:
# - Fixed data that shouldn't change
coordinates = (40.7128, -74.0060)  # NYC coordinates
rgb_color = (255, 0, 0)  # Red color
config = ("localhost", 8080)  # Server config

# Use LISTS for:
# - Data that needs to change
shopping_cart = ["milk", "eggs"]
shopping_cart.append("bread")  # Can modify

to_do_list = ["email", "call", "meeting"]
to_do_list.remove("email")  # Can remove

Array Module
Python's array module provides space-efficient arrays of basic values (numbers).
When to Use?

Need to store large amounts of numeric data
Want better memory efficiency than lists
All elements must be the same type

Creating Arrays
pythonimport array

# Type code 'i' = signed integer
numbers = array.array('i', [1, 2, 3, 4, 5])

# Type code 'd' = double (float)
floats = array.array('d', [1.1, 2.2, 3.3])

# Common type codes:
# 'b' = signed char (1 byte)
# 'i' = signed int (2 bytes)
# 'f' = float (4 bytes)
# 'd' = double (8 bytes)
Array Operations
pythonimport array

arr = array.array('i', [1, 2, 3])

# Append
arr.append(4)  # array('i', [1, 2, 3, 4])

# Extend
arr.extend([5, 6])  # array('i', [1, 2, 3, 4, 5, 6])

# Insert
arr.insert(0, 0)  # Insert 0 at index 0

# Remove
arr.remove(3)  # Remove first occurrence of 3

# Pop
last = arr.pop()  # Remove and return last item

# Access by index (same as lists)
print(arr[0])  # First element

NumPy Arrays
NumPy is the most powerful array library for numerical computing.
Installation
bashpip install numpy
Creating NumPy Arrays
pythonimport numpy as np

# From list
arr = np.array([1, 2, 3, 4, 5])

# Zeros
zeros = np.zeros(5)  # [0. 0. 0. 0. 0.]

# Ones
ones = np.ones(5)  # [1. 1. 1. 1. 1.]

# Range
range_arr = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

# Evenly spaced
linspace = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Random numbers
random = np.random.rand(5)  # 5 random floats between 0 and 1
NumPy Operations (Vectorized!)
pythonimport numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Mathematical operations (element-wise)
print(arr + 10)  # [11 12 13 14 15]
print(arr * 2)   # [2 4 6 8 10]
print(arr ** 2)  # [1 4 9 16 25]

# Array operations
print(arr.sum())   # 15
print(arr.mean())  # 3.0
print(arr.max())   # 5
print(arr.min())   # 1

# Boolean indexing
print(arr > 3)  # [False False False True True]
print(arr[arr > 3])  # [4 5]

Common Operations
Iteration
python# List
fruits = ["apple", "banana", "cherry"]

# Simple iteration
for fruit in fruits:
    print(fruit)

# With index
for i in range(len(fruits)):
    print(i, fruits[i])

# Using enumerate (BETTER)
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)
Searching
pythonnumbers = [10, 20, 30, 40, 50]

# Check if item exists
if 30 in numbers:
    print("Found!")

# Get index
index = numbers.index(30)  # 2

# Count occurrences
count = numbers.count(20)  # 1

# Find with condition
found = [x for x in numbers if x > 25]
print(found)  # [30, 40, 50]
List Comprehensions
python# Create new list from existing
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squares = [x**2 for x in numbers]
# [1, 4, 9, 16, 25]

# Filter and transform
evens = [x for x in numbers if x % 2 == 0]
# [2, 4]

# With condition
results = [x*2 if x > 2 else x for x in numbers]
# [1, 2, 6, 8, 10]

Performance Comparison
python# Time complexity for common operations

# LIST
# Access by index: O(1)
# Append: O(1)
# Insert at beginning: O(n)
# Delete: O(n)
# Search: O(n)

# TUPLE
# Access by index: O(1)
# All modifications: Not allowed!
# Search: O(n)

# ARRAY (array module)
# Access by index: O(1)
# Append: O(1)
# Insert: O(n)
# More memory efficient than list

# NUMPY ARRAY
# Access by index: O(1)
# Vectorized operations: Much faster!
# Best for mathematical operations

Best Practices
✅ DO
python# Use list comprehensions for transformations
squares = [x**2 for x in range(10)]

# Use tuples for fixed data
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Use meaningful names
student_names = ["Alice", "Bob", "Charlie"]

# Check before accessing
if index < len(my_list):
    item = my_list[index]

# Use enumerate when you need index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")
❌ DON'T
python# Don't modify list while iterating
for item in my_list:
    my_list.remove(item)  # BAD!

# Don't use list for fixed data
weekdays = ["Mon", "Tue", "Wed"]  # Should be tuple

# Don't compare with ==
if type(my_var) == list:  # BAD!
    pass
# Use isinstance instead
if isinstance(my_var, list):  # GOOD!
    pass

# Don't forget the comma in single-item tuple
single = (5)   # This is int, not tuple!
single = (5,)  # Correct tuple

Real-World Examples
Example 1: Server Inventory (Your vSphere Project!)
python# Store server information
servers = [
    ("web-01", "192.168.1.10", "Ubuntu 22.04", 16),
    ("db-01", "192.168.1.20", "RedHat 8", 32),
    ("app-01", "192.168.1.30", "Ubuntu 22.04", 8)
]

# Find servers with low RAM
low_ram_servers = [s for s in servers if s[3] < 16]

# Get all IPs
ips = [server[1] for server in servers]
Example 2: AWS Resource List
python# List of EC2 instances
ec2_instances = [
    {"id": "i-123", "type": "t2.micro", "state": "running"},
    {"id": "i-456", "type": "t2.small", "state": "stopped"},
    {"id": "i-789", "type": "t2.medium", "state": "running"}
]

# Find running instances
running = [i for i in ec2_instances if i["state"] == "running"]
Example 3: VM Snapshot Management
python# Snapshot data
snapshots = [
    ("snap-001", "vm-web-01", "2024-01-15"),
    ("snap-002", "vm-db-01", "2024-02-01"),
    ("snap-003", "vm-web-01", "2024-03-10")
]

# Find snapshots for specific VM
vm_snapshots = [s for s in snapshots if s[1] == "vm-web-01"]

Quick Reference Card
python

# CREATING
list_a = [1, 2, 3]
tuple_a = (1, 2, 3)
array_a = array.array('i', [1, 2, 3])

# ACCESSING
item = list_a[0]
slice_a = list_a[1:3]

# MODIFYING (lists only)
list_a.append(4)
list_a.insert(0, 0)
list_a.remove(2)
list_a.pop()

# SEARCHING
if item in list_a:
    index = list_a.index(item)

# ITERATING
for item in list_a:
    print(item)

# COMPREHENSIONS
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]

Summary
TypeMutableUse CaseList✅ YesGeneral purpose, dynamic dataTuple❌ NoFixed data, coordinates, configsarray✅ YesNumeric data, memory efficiencyNumPy✅ YesMathematical operations, data science
Remember: Start with lists for most cases. Use tuples when data shouldn't change. Consider array/NumPy for numerical work.

## References

1. Python Software Foundation. (2024). *Data Structures - Lists*. 
   Retrieved from https://docs.python.org/3/tutorial/datastructures.html

2. Python Software Foundation. (2024). *array - Efficient arrays of numeric values*. 
   Retrieved from https://docs.python.org/3/library/array.html

3. NumPy Developers. (2024). *NumPy Documentation*. 
   Retrieved from https://numpy.org/doc/stable/

Date Accessed: [November 12, 2025]
