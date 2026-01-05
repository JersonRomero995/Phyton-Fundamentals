"""
Docstring para Exercises.day-01.Python-essential-training.Quick-start.challenge1
Factorial Challenge
The factorial function gives the number of possible arrangements of a set of items of length "n"

For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1

5! = 5 * 4 * 3 * 2 * 1 = 120

6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

etc.

In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1

For the purposes of this exercise, factorials are only defined for positive integers (including 0)
"""



def addNumbers(i):
    if i == 0:
        return 0
    return i + addNumbers(i - 1)
    
print(addNumbers(2))

#  Recursive approach:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# resolution from course:

def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    
    fact = 1 
    counter = 1
    while counter <= num:
        fact = fact * counter 
        counter = counter + 1 
    return fact

print(factorial(3))

print(10*9*8*7*6*5*4*3*2*1)

print(456 % 10)
"""
Input validation:

pythonif type(num) != int:
    return None
if num < 0:
    return None

These check if the input is valid. Factorials only work with non-negative integers, so if you pass in a float (like 3.5) or a negative number, it returns None instead of trying to calculate.

Setup:
pythonfact = 1 
counter = 1

fact accumulates the result (starts at 1 because multiplying by 1 doesn't change anything)
counter tracks which number we're multiplying by (starts at 1)

The while loop:
python
while counter <= num:
    fact = fact * counter 
    counter = counter + 1

This multiplies all numbers from 1 up to num.
For factorial(3), here's what happens:

Loop iteration      counter     fact (before)       fact (after)
1st                 1           1                   1 × 1 = 1
2nd                 2           1                   1 × 2 = 2
3rd                 3           2                   2 × 3 = 6
(loop ends)         4           6                   —

The loop stops when counter becomes 4 (which is > 3), and it returns fact = 6.
So print(factorial(3)) outputs 6.
It's essentially doing: 1 × 1 × 2 × 3 = 6, which is 3!
"""