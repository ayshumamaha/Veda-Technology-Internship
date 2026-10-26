"""
Employee Salary Calculator
Task 16 — Python Programming Track

Calculates gross salary, deductions, and net salary using configurable rules.
Includes sample employee records and a salary calculation breakdown.
"""

# Configure salary rules here.
# Allowances and deductions are percentages of basic salary / gross salary as noted.
SALARY_RULES = {
    "hra_rate": 0.20,                 # House Rent Allowance: 20% of basic salary
    "transport_allowance": 1500.00,   # Fixed monthly allowance
    "medical_allowance": 1000.00,     # Fixed monthly allowance
    "provident_fund_rate": 0.12,      # PF: 12% of basic salary
    "professional_tax": 200.00,       # Fixed monthly deduction
    "income_tax_rate": 0.10,          # Income tax: 10% of gross salary
}


def get_non_negative_number(prompt):
    """Read and validate a non-negative numeric input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
            if value < 0:
                print("Please enter a number greater than or equal to zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_salary(basic_salary, rules=SALARY_RULES):
    """Return a dictionary containing salary components and totals."""
    hra = basic_salary * rules["hra_rate"]
    transport = rules["transport_allowance"]
    medical = rules["medical_allowance"]

    gross_salary = basic_salary + hra + transport + medical

    provident_fund = basic_salary * rules["provident_fund_rate"]
    professional_tax = rules["professional_tax"]
    income_tax = gross_salary * rules["income_tax_rate"]

    total_deductions = provident_fund + professional_tax + income_tax
    net_salary = gross_salary - total_deductions

    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "transport_allowance": transport,
        "medical_allowance": medical,
        "gross_salary": gross_salary,
        "provident_fund": provident_fund,
        "professional_tax": professional_tax,
        "income_tax": income_tax,
        "total_deductions": total_deductions,
        "net_salary": net_salary,
    }


def print_salary_breakdown(employee, salary):
    """Display an employee's salary calculation in a readable format."""
    print("\n" + "=" * 48)
    print(f"Salary Breakdown — {employee['name']}")
    print(f"Employee ID: {employee['employee_id']}")
    print("-" * 48)
    print(f"{'Basic salary':28s} ₹{salary['basic_salary']:>12,.2f}")
    print(f"{'HRA':28s} ₹{salary['hra']:>12,.2f}")
    print(f"{'Transport allowance':28s} ₹{salary['transport_allowance']:>12,.2f}")
    print(f"{'Medical allowance':28s} ₹{salary['medical_allowance']:>12,.2f}")
    print("-" * 48)
    print(f"{'Gross salary':28s} ₹{salary['gross_salary']:>12,.2f}")
    print("\nDeductions")
    print(f"{'Provident fund':28s} ₹{salary['provident_fund']:>12,.2f}")
    print(f"{'Professional tax':28s} ₹{salary['professional_tax']:>12,.2f}")
    print(f"{'Income tax':28s} ₹{salary['income_tax']:>12,.2f}")
    print("-" * 48)
    print(f"{'Total deductions':28s} ₹{salary['total_deductions']:>12,.2f}")
    print(f"{'NET SALARY':28s} ₹{salary['net_salary']:>12,.2f}")
    print("=" * 48)


def main():
    """Run the calculator for sample employees or a new employee."""
    employees = [
        {"employee_id": "E001", "name": "Aarav Sharma", "basic_salary": 30000.00},
        {"employee_id": "E002", "name": "Diya Kumar", "basic_salary": 45000.00},
        {"employee_id": "E003", "name": "Rohan Das", "basic_salary": 60000.00},
    ]

    print("EMPLOYEE SALARY CALCULATOR")
    print("-" * 30)
    print("1. Calculate salary for a sample employee")
    print("2. Enter a new employee")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        print("\nSample employees:")
        for index, employee in enumerate(employees, start=1):
            print(
                f"{index}. {employee['name']} "
                f"(ID: {employee['employee_id']}, "
                f"basic salary: ₹{employee['basic_salary']:,.2f})"
            )

        while True:
            selection = input("Select employee (1-3): ").strip()
            if selection in {"1", "2", "3"}:
                employee = employees[int(selection) - 1]
                break
            print("Invalid selection. Please choose 1, 2, or 3.")

    elif choice == "2":
        employee_id = input("Enter employee ID: ").strip()
        while not employee_id:
            print("Employee ID cannot be empty.")
            employee_id = input("Enter employee ID: ").strip()

        name = input("Enter employee name: ").strip()
        while not name:
            print("Employee name cannot be empty.")
            name = input("Enter employee name: ").strip()

        basic_salary = get_non_negative_number("Enter monthly basic salary (₹): ")
        employee = {
            "employee_id": employee_id,
            "name": name,
            "basic_salary": basic_salary,
        }
    else:
        print("Invalid option. Please run the program again and choose 1 or 2.")
        return

    salary = calculate_salary(employee["basic_salary"])
    print_salary_breakdown(employee, salary)


if __name__ == "__main__":
    main()
