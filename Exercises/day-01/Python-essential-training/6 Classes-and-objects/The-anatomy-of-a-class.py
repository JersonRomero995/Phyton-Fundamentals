# Instance Attributes
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + 'says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

#Static attribute 

class Dog:
    legs = 4
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)


print(Dog.legs)


class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
        
    def getLegs(self):
        return self._legs
    
    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())

myDog = Dog('Rover')
myDog._legs = 3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)

# 1. Instance Attributes
python

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

# Here, both name and legs are instance attributes - they're created inside __init__ using self. Each Dog object gets its own copy of these attributes. If you create two dogs and change one dog's legs, it won't affect the other dog's legs.

#2. Static (Class) Attributes
python

class Dog:
    legs = 4  # Defined at class level
    def __init__(self, name):
        self.name = name
# legs is now a class attribute (also called static attribute). It's defined outside any method, directly in the class body. This means:

#All instances share this single attribute
#You can access it via the class itself: Dog.legs
#You can also access it through instances: myDog.legs

#This is more memory-efficient when all dogs should have the same value.
# 3. Protected Attributes with Getter Methods
python

class Dog:
    _legs = 4  # The underscore suggests "protected"
    
    def getLegs(self):
        return self._legs
# The underscore prefix (_legs) is a Python convention meaning "this is internal, don't access directly." The getLegs() method provides controlled access to this attribute.
#Important behavior shown in your code:
python

myDog._legs = 3  # This creates a NEW instance attribute
print(myDog.getLegs())  # Prints 3 (instance attribute)
print(Dog._legs)  # Prints 4 (class attribute unchanged)

#When you assign myDog._legs = 3, you're not changing the class attribute - you're creating a new instance attribute that shadows the class attribute. The getLegs() method now finds the instance attribute first.
#Key takeaway: Instance attributes (created with self.) are unique to each object, while class attributes are shared across all instances unless you shadow them by creating an instance attribute with the same name.