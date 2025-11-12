Best Practices
Code Style (PEP 8)
python# ✅ GOOD: Clear variable names
user_name = "Alice"
total_price = 99.99

# ❌ BAD: Unclear names
x = "Alice"
tp = 99.99

# ✅ GOOD: Proper spacing
result = (10 + 5) * 2

# ❌ BAD: No spacing
result=(10+5)*2

# ✅ GOOD: One statement per line
x = 5
y = 10

# ❌ BAD: Multiple statements
x = 5; y = 10

# ✅ GOOD: Use comments
# Calculate total price with tax
total = price * 1.08

# ✅ GOOD: Consistent naming
def calculate_total():  # snake_case for functions
    pass

class UserAccount:      # PascalCase for classes
    pass

CONSTANT_VALUE = 100    # UPPERCASE for constants