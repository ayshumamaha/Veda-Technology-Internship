# Veda-Technology-Internship
# Simple Expense Tracker

## 1. Project Overview

The Simple Expense Tracker is a menu-driven Python application that allows users to record and manage daily expenses. It stores expense details, including date, category, description, and amount, in a CSV file.

The application also provides options to view expenses, calculate total spending, generate category-wise summaries, and filter expenses by month.

## 2. Objectives

* Develop a basic expense-tracking application.
* Understand CSV file handling in Python.
* Store and retrieve expense records.
* Calculate total and category-wise expenditure.
* Practise date validation and data processing.

## 3. Technologies Used

* Python 3
* csv module
* datetime module
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub for version control and project submission

## 4. Features

* Adds new expense records.
* Stores expense dates, categories, descriptions, and amounts.
* Saves records in a CSV file.
* Loads previously saved expenses.
* Displays all recorded expenses.
* Calculates overall expenditure.
* Generates category-wise expense summaries.
* Filters expenses by month using YYYY-MM format.

## 5. Project Structure

```text
simple-expense-tracker/
├── Task 18.py
├── expenses.csv
└── README.md
```

Note: The expenses.csv file is created automatically when the program saves the first expense.

## 6. Installation and Setup

1. Install Python 3.
2. Download or clone the repository.
3. Open the project folder in your code editor.
4. Open a terminal in the project directory.
5. Run the program.

```bash
python "Task 18.py"
```

## 7. Usage

1. Run the Python program.
2. Select an option from the expense-tracker menu.
3. Enter the expense date.
4. Enter the expense category and description.
5. Enter the expense amount.
6. Use the viewing option to display saved expenses.
7. Generate overall or category-wise summaries.
8. Use the monthly filter with YYYY-MM format.

## 8. Error Handling

The program validates expense dates and positive expense amounts. It also skips malformed CSV records while loading saved expenses so that individual invalid records do not interrupt the entire loading process.

## 9. Learning Outcomes

This project provides practical experience with CSV file handling, dictionaries, date parsing, data persistence, input validation, loops, and expense aggregation.

## 10. Conclusion

The Simple Expense Tracker demonstrates how Python can be used to build a practical financial record-management application. It strengthens understanding of file storage, data processing, and expense calculations.

## Author

M. Ayshwarya
