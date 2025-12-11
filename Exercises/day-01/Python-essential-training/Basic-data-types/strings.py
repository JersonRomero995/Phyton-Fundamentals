import math

#Slicing

name = 'My name is Jerson Romero'

print(name[0])

print(name[1])

print(name[0:7])

print(name[:7])

print(name[7:])


my_list = [1,2,3,4,5]
print(my_list[2:4])

print(len(name))
print(len(my_list))

### Formating

print('My number is: ' + str(5))

print(f'My number is: {5}')

print(f'My number is: {5} and twice that is {5*2}')

print(f'Pi is: {math.pi:.2f}')

print('Pi is: {}'.format(math.pi))

# Multi-line Strings

myString = '''
Here is a long block of text
I can add newlines!
the text doesn't stop until it sees \'\'\'

'''

print(myString)