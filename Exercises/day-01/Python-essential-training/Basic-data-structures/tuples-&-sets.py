# Sets
mySet = {'a','b','c'}
print(mySet)

mySet = set(('a','b','c'))
print(mySet)
print(type(mySet))

myList = ['a','b','c','d']
myList = list(set(myList))
print(myList)
print(type(myList))

# mySet[0] TypeError: 'set' object is not subscriptable
number = 1
# 1[0] TypeError: 'int' object is not subscriptable

mySet.add('d')
print(mySet)

print('a' in mySet)
print('z' in mySet)

print(len(mySet))

while len(mySet):
    print(mySet.pop())

print(mySet)

mySet = {'a','b','c'}
mySet.discard('a')

print(mySet)

#tuples

myTuple = ('a','b','c')
print(myTuple)
print(type(myTuple))


print(myTuple[0])
print(myTuple[1])

# myTuple[0] = 'd' TypeError: 'tuple' object does not support item assignment

def returnsMultipleValues():
    return 1,2,3
print(type(returnsMultipleValues))


myTuple = (1,2,3)
print(type(myTuple))

a, b, c = returnsMultipleValues()
print(a)
print(b)
print(c)