import math

#Fuctions
def performOperation(num1,num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
print(performOperation(1,2, 'sum'))

# Named Parameters
def performOperation(num1,num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
print(performOperation(2,3, 'multiply'))

def performOperation(num1,num2, operation='sum', message= 'Default message'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
print(performOperation(2,3, message = 'A new message', operation = 'multiply'))


# *args
def performOperation(*args):
    print(args)

print(performOperation(1,2,3))

# **kwargs
def performOperations(*args, **kwargs):
    print(args)
    print(kwargs)
print(performOperations(1,2,3, operation= 'sum'))

def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)
    
print(performOperation(1,2,3,4,5,6,7,8, operation='sum'))