def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    print("=" * 40)
    print("       EVEN AND ODD NUMBER CHECKER")
    print("=" * 40)

    try:
        user_input = input("Enter an integer: ").strip()
        number = int(user_input)

        result = check_even_odd(number)

        print("\n" + "-" * 40)
        print(f"Entered Number : {number}")
        print(f"Classification : {result}")
        print("-" * 40)

        if result == "Even":
            print(f"{number} is divisible by 2 without a remainder.")
        else:
            print(f"{number} is not divisible by 2 without a remainder.")

    except ValueError:
        print("\nError: Invalid input.")
        print("Please enter a whole number, such as 8, -5, or 0.")

    except OverflowError:
        print("\nError: The entered number is too large to process.")


if __name__ == "__main__":
    main()
