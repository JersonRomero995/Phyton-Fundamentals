import time

# Handling Exceptions
# Try / Except

def causeError():
    try:
        return 1/0
    except Exception as e:
        return e
    
print(causeError())

def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error!')
    
print(causeError())

#Finally

def causeError():
    try:
        return 1/1
    except Exception:
        print('There was some sort of error!')
    finally:
        print('This will always execute!')
    
print(causeError())

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some sort of error!')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')
    
print(causeError())

#Catching Exceptions by Type
def causeError():
    try:
        return 1 + 'a'

    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception:
        print('There was some sort of error!')

    
print(causeError())

#Custom Decorators

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sort of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

print(causeError())


# Raising Exceptions

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)
    
print(raiseError(1))