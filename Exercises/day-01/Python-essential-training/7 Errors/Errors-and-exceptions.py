# Errors and Exceptions

def causeError():
    return 1/0

causeError()

def causeError():
    return 1/0

def callCauseError():
    return causeError()

callCauseError()

#try / Except

try:
    1/0
except Exception as e:
    print(type(e))

#python
# This will raise ZeroDivisionError
def causeError():
    return 1/0

causeError()  # Program crashes here with ZeroDivisionError
#What happens: The program terminates immediately with an unhandled ZeroDivisionError.
#python
# # This shows the traceback chain
def causeError():
    return 1/0

def callCauseError():
    return causeError()

callCauseError()  # Shows error originated in causeError() called by callCauseError()
#What happens: Python shows the full call stack, tracing the error from callCauseError() → causeError() → line with 1/0.
#python
# # This catches the error
try:
    1/0
except Exception as e:
    print(type(e))  # Prints: <class 'ZeroDivisionError'>
#What happens: The exception is caught and handled, printing the exception type instead of crashing.
#More Exception Handling Techniques
#python
# # Catching specific exceptions
try:
    1/0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
except Exception as e:
    print(f"Other error: {e}")

# Getting exception details
try:
    1/0
except ZeroDivisionError as e:
    print(f"Type: {type(e)}")           # <class 'ZeroDivisionError'>
    print(f"Message: {e}")              # division by zero
    print(f"Args: {e.args}")            # ('division by zero',)

# Multiple exception types
try:
    result = int("not a number")
except (ValueError, TypeError, ZeroDivisionError) as e:
    print(f"Caught: {type(e).__name__}")

# Try/Except/Else/Finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Success! Result: {result}")  # Runs if no exception
finally:
    print("Always executes")             # Runs no matter what

# Re-raising exceptions
try:
    1/0
except ZeroDivisionError as e:
    print("Logging error...")
    raise  # Re-raises the same exception

# Raising custom exceptions
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems invalid: {age}")
    return age

# Exception chaining
try:
    1/0
except ZeroDivisionError as e:
    raise RuntimeError("Failed to calculate") from e
#Best Practices
#python
# # ❌ Too broad - catches everything
try:
    do_something()
except:
    pass

# ✅ Specific exceptions
try:
    do_something()
except FileNotFoundError:
    handle_missing_file()
except PermissionError:
    handle_permission_issue()

# ✅ Don't silently ignore errors
try:
    risky_operation()
except Exception as e:
    logger.error(f"Operation failed: {e}")
    raise  # Re-raise if you can't handle it

# ✅ Use finally for cleanup
file = None
try:
    file = open('data.txt')
    process(file)
except IOError as e:
    print(f"Error reading file: {e}")
finally:
    if file:
        file.close()  # Always closes, even if exception occurs