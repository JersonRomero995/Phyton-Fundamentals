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

