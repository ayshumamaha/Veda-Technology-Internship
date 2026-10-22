# Prime Number Analyzer
# VEDA Technology - Python Programming Track, Level 1, Task 13

def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def primes_in_range(start, end):
    """Return all prime numbers from start to end, inclusive."""
    return [n for n in range(start, end + 1) if is_prime(n)]


def main():
    print("=== Prime Number Analyzer ===")
    try:
        number = int(input("Enter a number to check: "))
        print(f"{number} is " + ("a prime number." if is_prime(number) else "not a prime number."))

        start = int(input("\nEnter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        if start > end:
            start, end = end, start

        primes = primes_in_range(start, end)
        print(f"Prime numbers between {start} and {end}:")
        print(", ".join(map(str, primes)) if primes else "No prime numbers found in this range.")
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")


if __name__ == "__main__":
    main()
