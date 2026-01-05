#Lists

my_list = [1,2,3,4,5]
print(my_list)

my_list1 = ['uno', '2', 'tres']
print(my_list1)

print(len(my_list1))

my_list.append(6)
print(my_list)

#sets

my_set= {1,2,3,4,5}
print(my_set)
print(type(my_set))

print(len(my_set))

print([1,2] == [2,1])

print({1,2,3} == {3,2,1})

# Tuples

my_tuple = (1,2,3)
print(len(my_tuple))

print((1,2) == (2,1)) 

# my_tuple.append(4)  AttributeError: 'tuple' object has no attribute 'append'

# Dictionaries 

my_dictionary = {
    'apple': 'A red fruit',
    'bear' : 'A scary animal'
}

print(my_dictionary['apple'])