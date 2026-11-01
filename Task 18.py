"""
Simple Expense Tracker
----------------------
A menu-driven expense tracker that stores records in expenses.csv.

Features:
- Add expenses with date, category, description, and amount
- Validate dates and positive expense amounts
- Keep records in a persistent CSV file
- View all expenses
- Generate total and category-wise spending summaries
- Filter expenses by month (YYYY-MM)
"""

import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDNAMES = ["date", "category", "description", "amount"]


def ensure_data_file():
    """Create the CSV file with headers if it does not already exist."""
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_expenses():
    """Load saved expense records from the CSV file."""
    ensure_data_file()
    expenses = []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "description": row["description"],
                    "amount": float(row["amount"]),
                })
            except (KeyError, TypeError, ValueError):
                # Skip any malformed row rather than stopping the program.
                continue
    return expenses


def save_expense(expense):
    """Append one expense to the persistent CSV file."""
    ensure_data_file()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(expense)


def get_valid_date():
    """Ask for a date in YYYY-MM-DD format."""
    while True:
        value = input("Expense date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD (example: 2026-11-01).")


def get_valid_amount():
    """Ask for a positive numeric amount."""
    while True:
        value = input("Amount: ").strip().replace(",", "")
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number, such as 250 or 250.50.")


def add_expense():
    """Collect and save a new expense."""
    print("\n--- Add Expense ---")
    date = get_valid_date()

    while True:
        category = input("Category (e.g. Food, Travel, Bills): ").strip()
        if category:
            break
        print("Category cannot be empty.")

    while True:
        description = input("Description: ").strip()
        if description:
            break
        print("Description cannot be empty.")

    amount = get_valid_amount()
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}",
    }
    save_expense(expense)
    print("Expense saved successfully.")


def display_expenses(expenses):
    """Display expense records in a readable table."""
    if not expenses:
        print("\nNo expense records found.")
        return

    print("\n{:<12} {:<18} {:<30} {:>12}".format(
        "Date", "Category", "Description", "Amount"
    ))
    print("-" * 76)
    for item in sorted(expenses, key=lambda x: x["date"]):
        print("{:<12} {:<18} {:<30} {:>12.2f}".format(
            item["date"],
            item["category"][:18],
            item["description"][:30],
            item["amount"],
        ))


def show_summary(expenses):
    """Print total spending and category-wise totals."""
    if not expenses:
        print("\nNo expenses available for the summary.")
        return

    total = sum(item["amount"] for item in expenses)
    category_totals = {}
    for item in expenses:
        category = item["category"].strip().title()
        category_totals[category] = (
            category_totals.get(category, 0) + item["amount"]
        )

    print("\n--- Spending Summary ---")
    print(f"Total spending: {total:.2f}")
    print("\nCategory-wise spending:")
    for category, amount in sorted(category_totals.items()):
        print(f"  {category:<20} {amount:>12.2f}")


def monthly_report(expenses):
    """Show expenses and totals for a selected month."""
    print("\n--- Monthly Report ---")
    while True:
        month = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(month, "%Y-%m")
            break
        except ValueError:
            print("Invalid month. Please use YYYY-MM (example: 2026-11).")

    selected = [item for item in expenses if item["date"].startswith(month)]
    if not selected:
        print(f"No expenses found for {month}.")
        return

    display_expenses(selected)
    print(f"\nTotal spending for {month}: "
          f"{sum(item['amount'] for item in selected):.2f}")
    show_summary(selected)


def main():
    ensure_data_file()
    print("================================")
    print("       SIMPLE EXPENSE TRACKER")
    print("================================")

    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Spending summary")
        print("4. Monthly report")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses(load_expenses())
        elif choice == "3":
            show_summary(load_expenses())
        elif choice == "4":
            monthly_report(load_expenses())
        elif choice == "5":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
