# Exercise 1: Temperature Converter
# Write a function that converts Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32

#Resolution 1

input_celsius = float(input("Enter temperature in celsius: ")) #create variable to take input from user, it print a message to the user and convert the input to float
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32   #define function to convert celsius to fahrenheit using formula with input parameter celsius

print(f"{input_celsius}°C is equal to {celsius_to_fahrenheit(input_celsius)}°F")

# Explanation:

""" The function DOESN'T know that input_celsius exists
The function is separate from the rest of the code. Look:
pythondef celsius_to_fahrenheit(celsius):  # "celsius" is just a generic name
    return (celsius * 9/5) + 32
The function only knows that:

It will receive some value
That value will be called celsius inside the function
It doesn't care where that value comes from

So how do they connect?
They connect when you call it and pass the value:
pythoncelsius_to_fahrenheit(input_celsius)
#                     ↑
#                     Here you pass the value
Step-by-step example:
pythoninput_celsius = 25.0  # Variable in the main code

# When you call the function:
result = celsius_to_fahrenheit(input_celsius)
#                              ↑
#                   You pass the value 25.0

# Inside the function, temporarily:
# celsius = 25.0  (copies the value)
# return (25.0 * 9/5) + 32
```

## Analogy:

Think of the function as a machine:
```
📦 Function: celsius_to_fahrenheit
   Input:  [____]  ← You put any number here
   Output: result

# You can use it with ANY variable:
celsius_to_fahrenheit(input_celsius)  ✅
celsius_to_fahrenheit(30)             ✅
celsius_to_fahrenheit(temperature)    ✅
celsius_to_fahrenheit(x)              ✅
Another example to clarify:
pythonhouse_temp = 22.0
street_temp = 15.0

# The same function works for both:
print(celsius_to_fahrenheit(house_temp))   # 71.6°F
print(celsius_to_fahrenheit(street_temp))  # 59.0°F
The function doesn't "know" the variables from the main code. It only receives the value that you pass to it when you call it."""

