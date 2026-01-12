# Variables as functions
x = 5
def x():
    return 5

# Viewing function data with __code__

print(x.__code__.co_varnames)
print(x.__code__.co_code)

# Text processing in Python

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def lowerCase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.','-',',','*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewLines(text):
    text = text.replace('\n', ' ')
    return text 

def removeShortWords(text):
    return ' '.join([word for word in text.split()if len (word) > 3])

def removeLongWords(text):
    return ' '.join([word for word in text.split()if len (word) < 6])

processingFunctions = [lowerCase, removePunctuation, removeNewLines, removeShortWords, removeLongWords]

for func in processingFunctions:
    text = func(text)

print(text)


#lambda fuctions

print (2+3)

print((lambda x: x + 3)(5))

myList = [5,4,3,2,1]
print(sorted(myList))

myList = [{'num': 3}, {'num': 2}, {'num': 1}]
print(sorted(myList, key= lambda x: x['num']))

"""

The sorted() function is sorting your list of dictionaries based on the 'num' value in each dictionary.
Here's what's happening:
The lambda x: x['num'] is an anonymous function that takes one argument (x) and returns x['num'].
When sorted() runs, it goes through each dictionary in myList one at a time:

First dictionary: x = {'num': 3}, the lambda returns 3
Second dictionary: x = {'num': 2}, the lambda returns 2
Third dictionary: x = {'num': 1}, the lambda returns 1

The key parameter tells sorted() to use these returned values (3, 2, 1) to determine the sort order. Since sorted() sorts in ascending order by default, it arranges the dictionaries so their 'num' values go from smallest to largest.
So the output is:
python[{'num': 1}, {'num': 2}, {'num': 3}]
Without the key parameter, sorted() wouldn't know how to compare dictionaries. The lambda function essentially says "compare these dictionaries by looking at their 'num' values."

"""


"""Basic syntax:
python

lambda arguments: expression

lambda is the keyword that starts the function
arguments are the inputs (like parameters in a regular function)
expression is what gets returned (no return keyword needed)

In your example:
python

lambda x: x['num']

x is the argument (the input)
x['num'] is the expression that gets returned

It's equivalent to writing a regular function like this:
python

def get_num(x):
    return x['num']

Then you could use it as: sorted(myList, key=get_num)
Key characteristics of lambda functions:

Anonymous - They don't need a name (though you can assign them to a variable)
Single expression - They can only contain one expression, not multiple statements
Automatic return - Whatever the expression evaluates to is automatically returned

More examples:
python

# Takes two arguments, returns their sum
lambda a, b: a + b

# Takes one argument, returns it doubled
lambda n: n * 2

# Takes a string, returns its length
lambda s: len(s)

# No arguments, always returns 5
lambda: 5
Lambdas are useful when you need a simple function for a short period (like as a sorting key) and don't want to define a full function with def."""


#Examples

# You have a list of tuples where each tuple contains a name and an age:

people = [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('Diana', 28)]

print(sorted(people, key = lambda x: x[1] ))


"""Explanation:

x represents each tuple as sorted() processes them
x[1] accesses the second element of the tuple (the age), since tuples use 0-based indexing
So for ('Alice', 30), x[1] returns 30
sorted() then uses these age values to sort the list"""


words = ['apple', 'pie', 'banana', 'cat', 'elephant']

"""Task: Use sorted() with a lambda function to sort this list by the length of each word, from shortest to longest."""

print(sorted(words, key=lambda x: len(x)))


products = [
    {'name': 'laptop', 'price': 1000},
    {'name': 'mouse', 'price': 25},
    {'name': 'keyboard', 'price': 75},
    {'name': 'monitor', 'price': 300}
]

# Task: Use sorted() with a lambda function to sort this list by price, from most expensive to least expensive.

print(sorted(products, key=lambda x : x['price'], reverse=True))


def someFunc(var1, var2, var3, var4):
print(someFunc(1,2,3,4))