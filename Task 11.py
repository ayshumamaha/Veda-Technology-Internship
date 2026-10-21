# Palindrome Checker
# VEDA Technology - Python Programming Track, Level 1, Task 12

def is_palindrome(text):
    """Check whether text is a palindrome, ignoring case and non-alphanumeric characters."""
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def main():
    print("=== Palindrome Checker ===")
    text = input("Enter a word or sentence: ")

    if not text.strip():
        print("Please enter a non-empty word or sentence.")
        return

    if is_palindrome(text):
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")

    print("\nExamples:")
    for example in ["madam", "Race car", "A man, a plan, a canal: Panama", "hello"]:
        result = "Palindrome" if is_palindrome(example) else "Not a palindrome"
        print(f"{example!r}: {result}")


if __name__ == "__main__":
    main()
