# always add at the beginning when you need to import a already created fucntion
from decimal import Decimal, getcontext

# Integers 

int('100') # to convert string to int 

"""
int('100', 2) converts the string '100' from binary (base-2) to a regular decimal integer.
The second argument 2 tells Python "interpret this string as a binary number."

Breaking down '100' in binary:
In binary, each position represents a power of 2 (from right to left):

Position:  2²   2¹   2⁰
Binary:    1    0    0
Value:     4    0    0
So: (1 × 4) + (0 × 2) + (0 × 1) = 4

Result:
pythonint('100', 2)  # Returns 4

More examples:
python

int('101', 2)   # 5  (4 + 0 + 1)
int('1111', 2)  # 15 (8 + 4 + 2 + 1)
int('10', 2)    # 2  (2 + 0)
int('1', 2)     # 1  (just 1)

If you left out the 2, Python would interpret it as base-10:
python

int('100')      # 100 (one hundred in decimal)
int('100', 2)   # 4   (one-zero-zero in binary)

The int() function can actually convert from any base from 2 to 36 using that second parameter!
"""

#int(100, 2) #TypeError: int() can't convert non-string with explicit base
#correct

print(int("100", 2))

#Decimals
print(getcontext())
getcontext().prec=4
print(getcontext())

print(Decimal(1) / Decimal(3))

getcontext().prec=2
print(Decimal(1) / Decimal(3))

print(Decimal(3.14))
print(Decimal("3.14"))

"""
The results:
python

from decimal import Decimal

print(Decimal(3.14))      # 3.140000000000000124344978758017532527446746826171875
print(Decimal("3.14"))    # 3.14


Why the difference?

When you write 3.14 as a float in Python, it can't be represented exactly in binary floating-point format. Computers store floats in binary, and 3.14 in decimal doesn't have an exact binary representation (similar to how 1/3 = 0.333... goes on forever in decimal).
So 3.14 is actually stored as something like 3.140000000000000124344978758017532527446746826171875 internally.
What happens:

Decimal(3.14) - You pass the actual float value to Decimal, which reveals the true imprecise value that was stored in memory.
Decimal("3.14") - You pass a string, so Decimal interprets it exactly as written: "3.14" with no floating-point conversion involved.

Best practice:
Always use strings when creating Decimals if you want exact values:
python
Decimal("3.14")    # ✓ Correct
Decimal(3.14)      # ✗ Loses precision before Decimal even sees it
This is why financial calculations should use Decimal("0.01") instead of Decimal(0.01) - you want exact pennies, not approximate floating-point values!
"""
