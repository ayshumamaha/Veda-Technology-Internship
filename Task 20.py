"""
utility_module.py
A reusable collection of common Python utility functions.

Includes:
- Validation helpers
- Text and number formatting
- Basic calculations
- File utilities

Run this file directly to see example usage:
    python utility_module.py

Import the functions into another Python program:
    from utility_module import is_valid_email, percentage, format_currency
"""

from pathlib import Path
import re
from typing import Union

Number = Union[int, float]


# ---------------------------------------------------------------------------
# VALIDATION FUNCTIONS
# ---------------------------------------------------------------------------

def is_valid_email(email: str) -> bool:
    """Return True if email has a basic valid email-address format."""
    if not isinstance(email, str):
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email.strip()) is not None


def is_positive_number(value: Number) -> bool:
    """Return True if value is a number greater than zero (excluding bool)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def is_valid_phone(phone: str) -> bool:
    """Return True if phone contains 7 to 15 digits, allowing common separators."""
    if not isinstance(phone, str):
        return False
    digits = re.sub(r"\D", "", phone)
    return 7 <= len(digits) <= 15


# ---------------------------------------------------------------------------
# FORMATTING FUNCTIONS
# ---------------------------------------------------------------------------

def format_currency(amount: Number, symbol: str = "₹") -> str:
    """Format a number as currency with two decimal places."""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("amount must be an integer or float")
    return f"{symbol}{amount:,.2f}"


def format_percentage(value: Number, decimal_places: int = 2) -> str:
    """Format a numeric value as a percentage (for example, 25 becomes 25.00%)."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("value must be an integer or float")
    if decimal_places < 0:
        raise ValueError("decimal_places cannot be negative")
    return f"{value:.{decimal_places}f}%"


def clean_text(text: str) -> str:
    """Remove extra whitespace and return a neatly spaced string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


# ---------------------------------------------------------------------------
# CALCULATION FUNCTIONS
# ---------------------------------------------------------------------------

def percentage(part: Number, whole: Number) -> float:
    """Return part as a percentage of whole; raise ValueError if whole is zero."""
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
               for x in (part, whole)):
        raise TypeError("part and whole must be numbers")
    if whole == 0:
        raise ValueError("whole cannot be zero")
    return (part / whole) * 100


def calculate_average(values: list[Number]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("values cannot be empty")
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
               for x in values):
        raise TypeError("all values must be numbers")
    return sum(values) / len(values)


def calculate_total(values: list[Number]) -> Number:
    """Return the sum of a list of numbers."""
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool)
               for x in values):
        raise TypeError("all values must be numbers")
    return sum(values)


# ---------------------------------------------------------------------------
# FILE UTILITY FUNCTIONS
# ---------------------------------------------------------------------------

def file_exists(file_path: Union[str, Path]) -> bool:
    """Return True if the given path points to an existing file."""
    return Path(file_path).is_file()


def read_text_file(file_path: Union[str, Path], encoding: str = "utf-8") -> str:
    """Read and return the complete contents of a text file."""
    return Path(file_path).read_text(encoding=encoding)


def write_text_file(
    file_path: Union[str, Path],
    content: str,
    encoding: str = "utf-8"
) -> None:
    """Write text to a file, creating parent folders when necessary."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)


# ---------------------------------------------------------------------------
# EXAMPLE PROGRAM
# ---------------------------------------------------------------------------

def main() -> None:
    """Demonstrate how the utility functions can be used."""
    print("PYTHON UTILITY MODULE - EXAMPLE")
    print("-" * 36)

    # Validation examples
    print("Valid email:", is_valid_email("student@example.com"))
    print("Positive number:", is_positive_number(25))
    print("Valid phone:", is_valid_phone("+91 98765 43210"))

    # Formatting examples
    print("Currency:", format_currency(12500.5))
    print("Percentage:", format_percentage(87.5))
    print("Clean text:", clean_text("  Python   utility   module  "))

    # Calculation examples
    print("Percentage:", round(percentage(45, 60), 2), "%")
    print("Average:", calculate_average([10, 20, 30, 40]))
    print("Total:", calculate_total([10, 20, 30, 40]))

    # File utility example (creates a small demonstration file)
    demo_path = Path("utility_demo.txt")
    write_text_file(demo_path, "This file was created using write_text_file().")
    print("File exists:", file_exists(demo_path))
    print("File contents:", read_text_file(demo_path))


if __name__ == "__main__":
    main()
