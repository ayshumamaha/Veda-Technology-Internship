import csv
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")
DATE_FORMAT = "%Y-%m-%d"

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Health",
    "Entertainment",
    "Education",
    "Other",
]


def load_data():
    """Load expenses and monthly budgets from the JSON file."""
    if not DATA_FILE.exists():
        return {"expenses": [], "budgets": {}}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            raise ValueError("Invalid data format")
        data.setdefault("expenses", [])
        data.setdefault("budgets", {})
        return data
    except (json.JSONDecodeError, OSError, ValueError):
        print("Warning: Could not read expenses.json. Starting with empty data.")
        return {"expenses": [], "budgets": {}}


def save_data(data):
    """Save all expenses and budgets to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_amount(prompt):
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Please enter a number.")


def read_date(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()
        if allow_blank and not value:
            return datetime.today().strftime(DATE_FORMAT)
        try:
            return datetime.strptime(value, DATE_FORMAT).strftime(DATE_FORMAT)
        except ValueError:
            print("Enter the date in YYYY-MM-DD format (for example, 2026-11-19).")


def choose_category():
    print("\nCategories:")
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}. {category}")

    while True:
        choice = input("Choose a category number: ").strip()
        try:
            index = int(choice) - 1
            if 0 <= index < len(CATEGORIES):
                return CATEGORIES[index]
        except ValueError:
            pass
        print("Please choose a valid category number.")


def add_expense(data):
    print("\n--- Add Expense ---")
    title = input("Expense description: ").strip()
    while not title:
        print("Description cannot be empty.")
        title = input("Expense description: ").strip()

    amount = read_amount("Amount: Rs. ")
    category = choose_category()
    date = read_date("Date (YYYY-MM-DD, press Enter for today): ", allow_blank=True)

    expense = {
        "id": int(datetime.now().timestamp() * 1000000),
        "title": title,
        "amount": amount,
        "category": category,
        "date": date,
    }
    data["expenses"].append(expense)
    save_data(data)
    print("Expense saved successfully.")


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n{:<4} {:<12} {:<22} {:<16} {:>12}".format(
        "No.", "Date", "Description", "Category", "Amount (Rs.)"
    ))
    print("-" * 72)
    for number, expense in enumerate(
        sorted(expenses, key=lambda item: item.get("date", "")), start=1
    ):
        print("{:<4} {:<12} {:<22} {:<16} {:>12.2f}".format(
            number,
            expense.get("date", ""),
            expense.get("title", "")[:21],
            expense.get("category", ""),
            float(expense.get("amount", 0)),
        ))
    total = sum(float(item.get("amount", 0)) for item in expenses)
    print("-" * 72)
    print(f"Total: Rs. {total:.2f}")


def view_expenses(data):
    print("\n--- All Expenses ---")
    display_expenses(data["expenses"])


def category_summary(data):
    print("\n--- Category-wise Summary ---")
    totals = {}
    for expense in data["expenses"]:
        category = expense.get("category", "Other")
        totals[category] = totals.get(category, 0) + float(expense.get("amount", 0))

    if not totals:
        print("No expenses available for summary.")
        return

    for category, total in sorted(totals.items()):
        print(f"{category:<18} Rs. {total:>10.2f}")
    print("-" * 32)
    print(f"{'Total':<18} Rs. {sum(totals.values()):>10.2f}")


def set_monthly_budget(data):
    print("\n--- Set Monthly Budget ---")
    month = input("Enter month (YYYY-MM): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM format.")
        return

    budget = read_amount("Monthly budget (Rs.): ")
    data["budgets"][month] = budget
    save_data(data)
    print(f"Budget for {month} saved: Rs. {budget:.2f}")


def monthly_summary(data):
    print("\n--- Monthly Spending Summary ---")
    month = input("Enter month (YYYY-MM): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM format.")
        return

    month_expenses = [
        item for item in data["expenses"]
        if item.get("date", "").startswith(month)
    ]
    total = sum(float(item.get("amount", 0)) for item in month_expenses)
    budget = data["budgets"].get(month)

    print(f"\nMonth: {month}")
    print(f"Total spent: Rs. {total:.2f}")
    if budget is None:
        print("No budget has been set for this month.")
    else:
        remaining = float(budget) - total
        print(f"Monthly budget: Rs. {float(budget):.2f}")
        print(f"Remaining: Rs. {remaining:.2f}")
        if remaining < 0:
            print(f"Budget exceeded by Rs. {abs(remaining):.2f}!")
        else:
            print("You are within your monthly budget.")

    if month_expenses:
        print("\nCategory breakdown:")
        totals = {}
        for item in month_expenses:
            category = item.get("category", "Other")
            totals[category] = totals.get(category, 0) + float(item.get("amount", 0))
        for category, amount in sorted(totals.items()):
            print(f"  {category}: Rs. {amount:.2f}")
    else:
        print("No expenses recorded for this month.")


def search_expenses(data):
    print("\n--- Search and Filter ---")
    keyword = input("Description keyword (press Enter to skip): ").strip().lower()
    category = input("Category (press Enter to skip): ").strip().lower()
    month = input("Month YYYY-MM (press Enter to skip): ").strip()

    if month:
        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month. Use YYYY-MM format.")
            return

    matches = []
    for item in data["expenses"]:
        if keyword and keyword not in item.get("title", "").lower():
            continue
        if category and category != item.get("category", "").lower():
            continue
        if month and not item.get("date", "").startswith(month):
            continue
        matches.append(item)

    print(f"\nFound {len(matches)} matching expense(s).")
    display_expenses(matches)


def export_csv(data):
    filename = "expenses_export.csv"
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["date", "title", "category", "amount"]
            )
            writer.writeheader()
            for item in data["expenses"]:
                writer.writerow({
                    "date": item.get("date", ""),
                    "title": item.get("title", ""),
                    "category": item.get("category", ""),
                    "amount": item.get("amount", 0),
                })
        print(f"Expenses exported successfully to {filename}.")
    except OSError as error:
        print(f"Could not export expenses: {error}")


def main():
    data = load_data()

    while True:
        print("\n" + "=" * 42)
        print("       PERSONAL EXPENSE & BUDGET TRACKER")
        print("=" * 42)
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Category-wise expense summary")
        print("4. Set monthly budget")
        print("5. View monthly spending summary")
        print("6. Search and filter expenses")
        print("7. Export expenses to CSV")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            category_summary(data)
        elif choice == "4":
            set_monthly_budget(data)
        elif choice == "5":
            monthly_summary(data)
        elif choice == "6":
            search_expenses(data)
        elif choice == "7":
            export_csv(data)
        elif choice == "8":
            print("Thank you for using Personal Expense & Budget Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
