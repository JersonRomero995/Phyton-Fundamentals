

#The input() function
'''We're now going to introduce you to a completely new function, which seems to be a mirror reflection of the good old print() function.

Why? Well, print() sends data to the console.

The new function gets data from it.

print() has no usable result. The meaning of the new function is to return a very usable result.

The function is named input(). The name of the function says everything.

The input() function is able to read data entered by the user and to return the same data to the running program.

The program can manipulate the data, making the code truly interactive.

Virtually all programs read and process data. A program which doesn't get a user's input is a deaf program.'''





# input a float value for variable a here
varA = float(input("insert the number for a:"))
# input a float value for variable b here
varB =float(input("insert the number for b:"))
# output the result of addition here
print("the adittion is:", varA + varB )
# output the result of subtraction here
print("the substraction is:", varA - varB)
# output the result of multiplication here
print("the multiplication is:", varA * varB)
# output the result of division here
print('the division is:', varA / varB)
print("\nThat's all, folks!")


# solution

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")


x = float(input("Enter value for x: "))

# Write your code here.
y = (1 /(x + 1 /(x + 1 /(x + 1 / x))))
print("y =", y)


#solution
x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
