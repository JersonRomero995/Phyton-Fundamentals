from collections import defaultdict

# Dictionaries
animals = {
    'a' : 'aardvark',
    'b' : 'bear',
    'c' : 'cat' ,
}
print(animals)

print(animals['a'])

animals['d'] = 'dog'

print(animals)
animals['a'] = 'antelope' # this replace the current value 
print(animals)

print(animals.keys())
# dict_keys(['a', 'b', 'c', 'd'])

print(animals.values())
# dict_keys(['a', 'b', 'c', 'd'])

print(list(animals.keys()))
# ['a', 'b', 'c', 'd']

# print(animals['e'])
# KeyError: 'e'

print(animals.get('a'))

print(len(animals))

animals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
}

animals['b'].append('bison')
print(animals)

animals['c'] = 'cat'
print(animals)

#if 'c' not in animals:
 #   animals['c'] = []

#animals['c'].append('cat')

#print(animals)

#if 'c' not in animals:
#    animals['c'] = []
    
#animals['c'].append('cat')

#print(animals)


# The Default Dict

animals = defaultdict(list)
print(animals)

animals['e'].append('elephant')

print(animals)

animals['e'].append('emu')

print(animals)

print(animals['f'])