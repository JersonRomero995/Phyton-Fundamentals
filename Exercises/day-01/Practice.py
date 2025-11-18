#Practice hello world first baby steps 

print("Hello, World!")

"""this is a simple Python program that prints 'Hello, World!' to the console. 
"""

# Variables is the next step

name = "Jerson"
last_name = "Romero"
Full_name = name + " " + last_name
age = 30
weight = 85.5
Is_student = True

print("name", name)
print("Full_name", Full_name)
print("age", age)
print("weight", weight)
print("Is_student", Is_student)

print(type(name))
print(type(age))
print(type(weight))
print(type(Is_student))


name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old"
print(message)  # My name is Alice and I am 30 years old


x = 10
y = 5

print(x == y)

age = 25
has_license = True
can_drive = age >= 18 and has_license

print(can_drive)  # True


# line 311 

for i in range(10):
    if i == 5:
        break  # Stop when i equals 5
    print(i)  # Prints 0, 1, 2, 3, 4