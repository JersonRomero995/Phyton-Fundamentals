#Python escape and newline characters

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

'''
Interestingly, while you can see two characters, Python sees one.

The backslash (\) has a very special meaning when used inside strings ‒ this is called the escape character.

The word escape should be understood specifically ‒ it means that the series of characters in the string escapes for the moment (a very short moment) to introduce a special inclusion.

In other words, the backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.

The letter n placed after the backslash comes from the word newline.

Both the backslash and the n form a special symbol named a newline character, which urges the console to start a new output line.
'''

'''
This convention has two important consequences:

1. If you want to put just one backslash inside a string, don't forget its escaping nature ‒ you have to double it. For example, an invocation like this will cause an error:

print("\")

while this one won't:

print("\\")

'''

#Key words arguments
'''
Python offers another mechanism for the passing of arguments, which can be helpful when you want to convince the print() function to change its behavior a bit.

We aren't going to explain it in depth right now. We plan to do this when we talk about functions. For now, we simply want to show you how it works. Feel free to use it in your own programs.

The mechanism is called keyword arguments. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The print() function has two keyword arguments that you can use for your purposes. The first is called end.

In the editor window you can see a very simple example how to use a keyword argument.
'''
print("My name is", "Python.", end=" ")
print("Monty Python.")

'''
In order to use it, it is necessary to know some rules:

a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
any keyword arguments have to be put after the last positional argument (this is very important)
In our example, we have made use of the end keyword argument, and set it to a string containing one space.

Run the code to see how it works.

The console should now be showing the following text:

'''

#My name is Python. Monty Python.

#Keyword arguments

'''
Python offers another mechanism for the passing of arguments, which can be helpful when you want to convince the print() function to change its behavior a bit.

We aren't going to explain it in depth right now. We plan to do this when we talk about functions. For now, we simply want to show you how it works. Feel free to use it in your own programs.

The mechanism is called keyword arguments. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The print() function has two keyword arguments that you can use for your purposes. The first is called end.

In the editor window you can see a very simple example how to use a keyword argument.

'''

print("My name is", "Python.", end=" ")
print("Monty Python.")

#My name is Python. Monty Python.
'''
In order to use it, it is necessary to know some rules:

a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
any keyword arguments have to be put after the last positional argument (this is very important)
In our example, we have made use of the end keyword argument, and set it to a string containing one space.
'''

'''As you can see, the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.

The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".

And now it's time to try something more difficult.

If you look carefully, you'll see that we've used the end argument, but the string assigned to it is empty (it contains no characters at all).

What will happen now? Run the program in the editor to find out.'''

print("My name is ", end="")
print("Monty Python.")

#My name is Monty Python.

'''Note: no newlines have been sent to the output.

The string assigned to the end keyword argument can be of any length. Experiment with it if you want.

We said previously that the print() function separates its outputted arguments with spaces. This behavior can be changed, too.

The keyword argument that can do this is named sep (as in separator).

Look at the code in the editor, and run it.'''

print("My", "name", "is", "Monty", "Python.", sep="-")

#My-name-is-Monty-Python.

'''The print() function now uses a dash, instead of a space, to separate the outputted arguments.

Note: the sep argument's value may be an empty string, too. Try it for yourself.

Both keyword arguments may be mixed in one invocation, just like here in the editor window.'''

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#My_name_is*Monty*Python.*


print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print("          *\n         * *\n        *   *\n       *     *\n      *       *\n     *         *")
print("    ****     ****")
print("       *     *\n       *     *\n       *     *\n       *     *")
print("       *******")

print("          *\n         * *\n        *   *\n       *     *\n      *       *\n     *         *" * 2)
print("    ****     ****" * 2)
print("       *     *\n       *     *\n       *     *\n       *     *" * 2)
print("       *******" *2 )


# SECTION SUMMARY

'''1. The print() function is a built-in function. It prints/outputs a specified message to the screen/console window.

2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.8 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library https://docs.python.org/3/library/functions.html.

3. To call a function (this process is known as function invocation or function call), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

4. Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).

5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.

6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.

9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments, e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.
'''
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('Greg's book."')