# Lists
# List Slicing

myList = [1,2,3,4,5]
print(myList[3:])

print(myList[0:6:2]) # Here I'm telling to show from 0 to 6 every two values that is why result will be:

# [1, 3, 5]

print(myList[0:6:3])

print(myList[::2])

for i in range(100):
    print(i)

    
myList = list(range(100))
print(myList[::10])

# Modifying Lists
myList = [1,2,3,4]
myList.append(5)
print(myList)

myList.insert(3,'a new value')
print(myList)

myList.remove('a new value')
print(myList)

myList.pop()
print(myList)

while len(myList):
    print(myList.pop())

print(myList)

a = [1,2,3,4,5]
b=a

a.append(6)
print(b)

a = [1,2,3,4,5]
b=a.copy()
a.append(6)
print(a)
print(b)

for i in range(20):
    print(i)