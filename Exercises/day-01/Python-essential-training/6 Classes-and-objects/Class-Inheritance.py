#Class Inheritance
class Dog:
    _legs = 4
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(self.name + 'says : bark!')

    def getLegs(self):
        return self._legs

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    def wagTail(self):
        print('Vigorous wagging!')

dog = Chihuahua('Roxy')
print(dog.speak())
print(dog.wagTail())  

# Extending built-in classes

myList = list()

class UniqueList(list):
    def append(self,item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)

class UniqueList(list):
    
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'
        

    def append(self, item):
        if item in self:
            return
        super().append(item)
        
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)

#Basic Inheritance
#pythonclass Chihuahua(Dog):
#The syntax class Chihuahua(Dog): means Chihuahua inherits from Dog. This means:

#Chihuahua is the child class (or subclass)
#Dog is the parent class (or superclass)
#Chihuahua automatically gets all of Dog's attributes and methods

#python

dog = Chihuahua('Roxy')
print(dog.getLegs())  # This works even though Chihuahua doesn't define getLegs()!
# Chihuahua inherited __init__, getLegs(), and _legs from Dog without writing any code.
#Method Overriding
#python

def speak(self):
    print(f'{self.name} says: Yap yap yap!')
#Chihuahua overrides the speak() method from Dog. When you call dog.speak() on a Chihuahua object, Python uses the Chihuahua version, not the Dog version. This is called polymorphism - same method name, different behavior.
#Adding New Methods
#python

def wagTail(self):
    print('Vigorous wagging!')
#Chihuahua adds its own method that Dog doesn't have. Child classes can extend functionality beyond what the parent provides.
#Inheriting from Built-in Classes
#python

class UniqueList(list):
#You can inherit from Python's built-in classes! UniqueList is now a list with custom behavior.
#The super() Function
#python

#super().append(item)
#super() lets you call methods from the parent class. Here's what happens:
#python

#def append(self, item):
#    if item in self:  # Custom logic
#        return
#    super().append(item)  # Call the parent's (list's) append method
#This means: "Check if the item already exists (our custom rule), and if not, use the normal list append behavior."
#Calling Parent's __init__
#python
# """""
def __init__(self):
    super().__init__()  # Call list's __init__
    self.someProperty = 'Unique List!'  # Then add our own stuff
#When you override __init__, you often want to call the parent's __init__ first using super().__init__() to make sure the parent class is properly initialized. Then you can add your own initialization.
#Why Use Inheritance?

#Code reuse: Don't repeat yourself - inherit common functionality
#Organization: Create hierarchies of related classes
#Extensibility: Add features to existing classes without modifying them
#Polymorphism: Different classes can share method names but behave differently

#Real-world example: You might have a Vehicle parent class, then Car, Truck, and Motorcycle child classes that inherit common vehicle properties but each have their own specific behaviors.

"""