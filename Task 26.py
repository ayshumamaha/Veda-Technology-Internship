# Basic Unit Testing Project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test cases
print("Running Unit Tests...\n")

assert add(5, 3) == 8
print("Test 1: Addition - PASS")

assert add(-5, -3) == -8
print("Test 2: Negative Addition - PASS")

assert subtract(10, 4) == 6
print("Test 3: Subtraction - PASS")

assert subtract(3, 8) == -5
print("Test 4: Negative Subtraction - PASS")

assert multiply(4, 3) == 12
print("Test 5: Multiplication - PASS")

assert multiply(7, 0) == 0
print("Test 6: Multiplication by Zero - PASS")

assert divide(12, 3) == 4
print("Test 7: Division - PASS")

assert divide(5, 2) == 2.5
print("Test 8: Decimal Division - PASS")

assert add(2.5, 1.5) == 4.0
print("Test 9: Decimal Addition - PASS")

try:
    divide(10, 0)
except ValueError:
    print("Test 10: Division by Zero - PASS")

print("\nAll 10 tests completed successfully!")
