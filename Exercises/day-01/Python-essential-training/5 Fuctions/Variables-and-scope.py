#Fuction scope
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)

print(performOperation(1,2, operation='sum'))


#locals()

def perfromOperation(num1,num2, operation='sum'):
    print(locals())

print(performOperation(1,2, operation='multiply'))


#globals()

print(globals())

#Global and local scope

message = 'some global data'

def function1(varA, varB):
    print(message)
    print(locals())

def function2(varC, varD):
    print(message)
    print(locals())

function1(1,2)
function2(3,4)

message = 'some global data'
varA = 2
def function1(varA, varB):
    message = 'some local data'
    print(varA)
    print(message)
    print(locals())

def function2(varC, varD):
    print(varA)
    print(message)
    print(locals())

function1(1,2)
function2(3,4)

def function1(varA, varB):
    message = 'some local data'
    print(varA)
    def inner_function(varA, varB):
        print(f'inner_fuction local scope: {locals()}')
    inner_function(123,456)
print(function1(1,2))


def function1(varA, varB):
    message = 'some local data'
    print(varA)
    def inner_function(varA, varB):
        print(f'inner_fuction local scope: {locals()}')

    print(locals())
    inner_function(123,456)
    
print(function1(1,2))