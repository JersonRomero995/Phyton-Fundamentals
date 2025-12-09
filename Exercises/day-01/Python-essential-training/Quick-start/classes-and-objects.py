# Classes
class Dog: 
    def __init__(self, name):
        self.name = name 
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
another_dog =Dog('Fluffy')

my_dog.speak()

"""
Classes are blueprints for creating objects. Think of them like a cookie cutter - they define what shape the cookie will have, but they're not the cookie itself.
In your example, Dog is the class. It defines what every dog object will have:

A name attribute (unique to each dog)
A legs attribute (set to 4 for all dogs)
A speak() method (behavior all dogs can do)

Objects are actual instances created from a class. They're the real cookies made from the cookie cutter.
my_dog and another_dog are both objects created from the Dog class. They're separate entities with their own data.
Key pieces:
__init__ is the constructor - it runs automatically when you create a new object. It sets up the initial state. The name parameter lets you customize each dog when you create it.
self refers to the specific instance you're working with. When you call my_dog.speak(), inside that method self refers to my_dog, so self.name is "Rover".
When you do my_dog = Dog('Rover'), you're:

Creating a new Dog object
Passing "Rover" to __init__
Storing that object in the variable my_dog

So my_dog.speak() outputs: "Rover says: Bark!"

"""