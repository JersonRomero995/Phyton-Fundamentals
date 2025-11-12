# Solution 1
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solution 2
def is_even(number):
    return number % 2 == 0

# Solution 3
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error: Division by zero"

# Solution 4
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Solution 5
def is_palindrome(word):
    return word.lower() == word.lower()[::-1]