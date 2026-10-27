
def safe_division():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation completed.")


def safe_list_access():
    values = [10, 20, 30]

    try:
        index = int(input("Enter a list index (0-2): "))
        print("Value:", values[index])

    except ValueError:
        print("Error: Index must be an integer.")

    except IndexError:
        print("Error: Index is outside the list range.")


def safe_dictionary_access():
    employee = {"name": "Asha", "salary": 30000}

    try:
        key = input("Enter a key (name or salary): ")
        print("Value:", employee[key])

    except KeyError:
        print("Error: The requested key does not exist.")


def main():
    print("EXCEPTION HANDLING DEMONSTRATION")

    safe_division()
    safe_list_access()
    safe_dictionary_access()

    print("\nHandled exceptions:")
    print("1. ValueError")
    print("2. ZeroDivisionError")
    print("3. IndexError")
    print("4. KeyError")
    print("5. Invalid numeric input")


if __name__ == "__main__":
    main()
