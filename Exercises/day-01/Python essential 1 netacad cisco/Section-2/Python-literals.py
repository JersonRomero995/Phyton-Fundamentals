# 2.2.2 Integers
'''
You may already know a little about how computers perform calculations on numbers. Perhaps you've heard of the binary system, and know that it's the system computers use for storing numbers, and that those computers can perform any operation upon them.

We won't explore the intricacies of positional numeric systems here, but we will say that the numbers handled by modern computers are of two types:

integers, that is, those which are devoid of the fractional part;
and floating-point numbers (or simply floats), that contain (or are able to contain) the fractional part.
This definition is not entirely accurate, but quite sufficient for now. The distinction is very important, and the boundary between these two types of numbers is very strict. Both of these kinds of numbers differ significantly in how they're stored in a computer memory and in the range of acceptable values.

The characteristic of the numeric value which determines its kind, range, and application, is called the type.

If you encode a literal and place it inside Python code, the form of the literal determines the representation (type) Python will use to store it in the memory.

For now, let's leave the floating-point numbers aside (we'll come back to them soon) and consider the question of how Python recognizes integers.

The process is almost like how you would write them with a pencil on paper - it's simply a string of digits that make up the number. But there's a reservation ‒ you must not interject any characters that are not digits inside the number.

Take, for example, the number eleven million one hundred eleven thousand one hundred eleven. If you took a pencil in your hand right now, you would write the number like this: 11,111,111, or like this: 11.111.111, or even like this: 11 111 111.

It's clear that this provision makes it easier to read, especially when the number consists of many digits. However, Python doesn't accept things like these. It's prohibited. What Python does allow, though, is the use of underscores in numeric literals.*

Therefore, you can write this number either like this: 11111111, or like this: 11_111_111.

Note *Python 3.6 has introduced underscores in numeric literals, allowing for the placement of single underscores between digits and after base specifiers for improved readability. This feature is not available in older versions of Python.

And how do we code negative numbers in Python? As usual ‒ by adding a minus. You can write: -11111111, or -11_111_111.

Positive numbers do not need to be preceded by the plus sign, but it's permissible, if you wish to do it. The following lines describe the same number: +11111111 and 11111111.'''


#Octal and hexadecimal numbers
'''There are two additional conventions in Python that are unknown to the world of mathematics. The first allows us to use numbers in an octal representation.

If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

0o123 is an octal number with a (decimal) value equal to 83.

The print() function does the conversion automatically. Try this:'''

print(0o123) #Result 83

'''The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. Try this:'''

print(0x123) #Result 291

#2.2.3 Floats

'''Now it's time to talk about another type, which is designed to represent and to store the numbers that (as a mathematician would say) have a non-empty decimal fraction.

They are the numbers that have (or may have) a fractional part after the decimal point, and although such a definition is very poor, it's certainly sufficient for what we wish to discuss.

Whenever we use a term like two and a half or minus zero point four, we think of numbers which the computer considers floating-point numbers:

2.5
-0.4
Note: two and a half looks normal when you write it in a program, although if your native language prefers to use a comma instead of a point in the number, you should ensure that your number doesn't contain any commas at all.

Python will not accept that, or (in very rare but possible cases) may misunderstand your intentions, as the comma itself has its own reserved meaning in Python.

If you want to use just a value of two and a half, you should write it as shown above. Note once again: there is a point between 2 and 5, not a comma.

As you can probably imagine, the value of zero point four could be written in Python as:

0.4
But don't forget this simple rule ‒ you can omit zero when it is the only digit in front of or after the decimal point.

In essence, you can write the value 0.4 as:

.4

For example: the value of 4.0 could be written as:

4.

This will change neither its type nor its value.'''

#Ints vs. floats

'''The decimal point is essential for recognizing floating-point numbers in Python.

Look at these two numbers:

4
4.0
You may think that they are exactly the same, but Python sees them in a completely different way.

4 is an integer number, whereas 4.0 is a floating-point number.

The point is what makes a float.

On the other hand, it's not only points that make a float. You can also use the letter e.

When you want to use any numbers that are very large or very small, you can use scientific notation.

Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000.

To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.

It reads: three times ten to the power of eight.

In Python, the same effect is achieved in a slightly different way ‒ take a look:

3E8

The letter E (you can also use the lower-case letter e ‒ it comes from the word exponent) is a concise record of the phrase times ten to the power of.

Note:

the exponent (the value after the E) has to be an integer;
the base (the value in front of the E) may be either an integer or a float.'''

#Coding floats

"""Let's see how this convention is used to record numbers that are very small (in the sense of their absolute value, which is close to zero).

A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.

If you would like to use it in a program, you should write it this way:

6.62607E-34

Note: the fact that you've chosen one of the possible forms of coding float values doesn't mean that Python will present it the same way.

Python may sometimes choose different notation than you.

For example, let's say you've decided to use the following float literal:

0.0000000000000000000001

When you run this literal through Python:

Output
print(0.0000000000000000000001)
 
this is the result:
Output
1e-22
Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals."""

#Strings

'''Strings are used when you need to process text (like names of all kinds, addresses, novels, etc.), not numbers.

You already know a bit about them, e.g., that strings need quotes the way floats need points.

This is a very typical string: "I am a string."

However, there is a catch. The catch is how to encode a quote inside a string which is already delimited by quotes.

Let's assume that we want to print a very simple message saying:

I like "Monty Python"
How do we do it without generating an error? There are two possible solutions.

The first is based on the concept we already know of the escape character, which you should remember is played by the backslash. The backslash can escape quotes too. A quote preceded by a backslash changes its meaning ‒ it's not a delimiter, but just a quote. This will work as intended:'''

print("I like \"Monty Python\"")

"""Note: there are two escaped quotes inside the string ‒ can you see them both?

The second solution may be a bit surprising. Python can use an apostrophe instead of a quote. Either of these characters may delimit strings, but you must be consistent.

If you open a string with a quote, you have to close it with a quote.

If you start a string with an apostrophe, you have to end it with an apostrophe.

This example will work too:"""

print('I like "Monty Python"')

