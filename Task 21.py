from datetime import date, datetime, timedelta


def get_date(prompt):
    """Get and validate date input."""
    while True:
        try:
            value = input(prompt)
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date! Enter in YYYY-MM-DD format.")


def calculate_age(birth_date):
    """Calculate age in completed years."""
    today = date.today()

    if birth_date > today:
        raise ValueError("Birth date cannot be in the future.")

    age = today.year - birth_date.year

    try:
        birthday = birth_date.replace(year=today.year)
    except ValueError:
        birthday = date(today.year, 2, 28)

    if today < birthday:
        age -= 1

    return age


def days_between(date1, date2):
    """Calculate difference between two dates."""
    return abs((date2 - date1).days)


def working_days(date1, date2):
    """Count weekdays between two dates."""
    if date1 > date2:
        date1, date2 = date2, date1

    count = 0
    current = date1 + timedelta(days=1)

    while current <= date2:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)

    return count


def formatted_datetime():
    """Display formatted current date and time."""
    now = datetime.now()

    print("\nCurrent Date and Time")
    print("---------------------")
    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%I:%M:%S %p"))
    print("24-Hour Time:", now.strftime("%H:%M:%S"))
    print("Day:", now.strftime("%A"))
    print("Full Format:", now.strftime("%A, %d %B %Y"))


def sample_calculations():
    """Display sample calculations."""
    birth = date(2000, 2, 29)
    today = date.today()

    start = date(2026, 11, 1)
    end = date(2026, 11, 10)

    print("\nSample Calculations")
    print("-------------------")
    print("Age:", calculate_age(birth), "years")
    print("Days Between:", days_between(start, end))
    print("Working Days:", working_days(start, end))


def main():
    while True:
        print("\n====== DATE AND TIME UTILITY ======")
        print("1. Calculate Age")
        print("2. Calculate Days Between Dates")
        print("3. Calculate Working Days")
        print("4. Display Formatted Date and Time")
        print("5. Sample Calculations")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            birth = get_date("Enter date of birth (YYYY-MM-DD): ")

            try:
                print("Your Age:", calculate_age(birth), "years")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            date1 = get_date("Enter first date (YYYY-MM-DD): ")
            date2 = get_date("Enter second date (YYYY-MM-DD): ")

            print("Days Between:", days_between(date1, date2))

        elif choice == "3":
            date1 = get_date("Enter start date (YYYY-MM-DD): ")
            date2 = get_date("Enter end date (YYYY-MM-DD): ")

            print("Working Days:", working_days(date1, date2))

        elif choice == "4":
            formatted_datetime()

        elif choice == "5":
            sample_calculations()

        elif choice == "0":
            print("Thank you for using the utility!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
