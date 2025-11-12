Code Organization
python# File structure
"""
Module docstring explaining what this file does
"""

# 1. Imports
import math
from datetime import datetime

# 2. Constants
MAX_USERS = 100
DEFAULT_TIMEOUT = 30

# 3. Functions
def helper_function():
    """Function docstring"""
    pass

def main_function():
    """Main logic"""
    pass

# 4. Main execution
if __name__ == "__main__":
    main_function()

DRY Principle (Don't Repeat Yourself)
python# ❌ BAD: Repetitive code
def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

def calculate_circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

# ✅ GOOD: Use constants and reuse code
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius