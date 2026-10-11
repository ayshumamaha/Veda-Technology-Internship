
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


def main():
    print("=" * 35)
    print("       SIMPLE CALCULATOR")
    print("=" * 35)

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")

        choice = input("Enter your choice (1-5): ").strip()

        operations = {
            "1": ("Addition", add),
            "2": ("Subtraction", subtract),
            "3": ("Multiplication", multiply),
            "4": ("Division", divide),
            "5": ("Modulus", modulus)
        }

        if choice not in operations:
            print("Error: Invalid operation selected.")
            return

        operation_name, operation_function = operations[choice]
        result = operation_function(first, second)

        print(f"\nOperation: {operation_name}")
        print(f"First number: {first:g}")
        print(f"Second number: {second:g}")
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numerical inputs.")

    except OverflowError:
        print("Error: The result is too large to represent.")


if __name__ == "__main__":
    main()
