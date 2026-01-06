# List Comprehensions
myList = [1,2,3,4,5]
print([2*item for item in myList])
# print([4*item(3) for item(3) in myList]) # this does not work, The parentheses after a variable name means "call this as a function," which only works if the variable actually contains a function.


# if you want to multiply only specific values, you have a few options:

# 1. Use a conditional in the list comprehension:
# Multiply only the value 3 by 4, keep others as-is
[4*item if item == 3 else item for item in myList]
# Result: [1, 2, 12, 4, 5]

# Multiply only values greater than 3
[4*item if item > 3 else item for item in myList]
# Result: [1, 2, 3, 16, 20]

# 2. Multiply specific positions/indices:
# Multiply only the item at index 2 (which is 3)

[4*item if i == 2 else item for i, item in enumerate(myList)]
# Result: [1, 2, 12, 4, 5]

# Multiply items at indices 1 and 3
[4*item if i in [1, 3] else item for i, item in enumerate(myList)]
# Result: [1, 8, 3, 16, 5]

# 3. Filter and multiply only certain values:
# Only include items greater than 3, multiplied by 4
[4*item for item in myList if item > 3]
# Result: [16, 20]
#The key is using if conditions inside the comprehension to decide when to apply the multiplication. Which approach you use depends on whether you're targeting specific values, positions, or conditions.

#List comprehensions with filters
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
print(filteredList)

filteredList = [item for item in myList if item % 10 < 3]
print(filteredList)

# List comprehensions with functions
myString = 'My name is Ryan Mitchell. I live in Boston'
print(myString.split('.'))
print(myString.split())

def cleanWord(word):
    return word.replace('.','').lower()
print([cleanWord(word) for word in myString.split() if len(cleanWord(word)) > 3 ])
# ['name', 'ryan', 'mitchell', 'live', 'boston']

# Nested list comprehensions
print([[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')])
