# Multiplication Table Generator
# Task 6 - Python Programming Track

number = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))

print(f"\nMultiplication Table of {number}")
print("-" * 30)

for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
