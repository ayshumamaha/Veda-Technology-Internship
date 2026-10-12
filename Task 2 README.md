# Even and Odd Number Checker Using Python

## 1. Project Overview

The Even and Odd Number Checker is a simple console-based Python application developed as part of the Python Programming Internship at Veda Technology. The program accepts an integer from the user and determines whether it is even or odd using the modulus operator and conditional statements.

The application uses a separate function to perform the classification, validates user input, and displays the result clearly. It supports positive integers, negative integers, and zero, while handling invalid inputs through exception handling.

## 2. Objectives

* Develop a Python program to identify even and odd numbers.
* Understand the use of the modulus operator (`%`).
* Practise conditional statements and functions.
* Handle positive and negative integers correctly.
* Validate user input and handle invalid entries.
* Display results through a simple console interface.

## 3. Technologies Used

* Python 3
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub

## 4. Features

* Accepts an integer from the user.
* Identifies whether the number is even or odd.
* Uses a separate function for number classification.
* Supports negative integers and zero.
* Handles invalid inputs such as text and decimal values.
* Displays the entered number and its classification.
* Provides clear error messages for invalid input.

## 5. Project Structure

```text
even-odd-number-checker/
├── even_odd_checker.py
└── README.md
```

## 6. Installation and Setup

1. Install Python 3 on your computer.
2. Create or download the project repository.
3. Save the Python source code as `even_odd_checker.py`.
4. Open the project folder in a terminal or code editor.
5. Execute the following command:

```bash
python even_odd_checker.py
```

If your system uses the `python3` command, run:

```bash
python3 even_odd_checker.py
```

## 7. Usage

1. Run the Python program.
2. Enter an integer when prompted.
3. The program checks whether the number is divisible by two without a remainder.
4. The classification and a brief explanation are displayed.
5. If the input is invalid, the program displays an error message.

## 8. Sample Results

| Input   | Expected Result       |
| ------- | --------------------- |
| `8`     | Even                  |
| `7`     | Odd                   |
| `-4`    | Even                  |
| `-5`    | Odd                   |
| `0`     | Even                  |
| `hello` | Invalid input message |
| `4.5`   | Invalid input message |

## 9. Concepts Demonstrated

* **Modulus operator:** Calculates the remainder after division by two.
* **Conditional statements:** Uses `if` and `else` to classify the number.
* **Functions:** Separates the classification logic into a reusable function.
* **Input handling:** Accepts user input and converts it into an integer.
* **Exception handling:** Uses `try-except` to handle invalid integer input.
* **Program structure:** Uses a `main()` function and the standard execution guard.

## 10. Learning Outcomes

This project provides practical experience in Python functions, arithmetic operators, conditional statements, integer conversion, and exception handling. It also improves logical reasoning and demonstrates how a simple mathematical rule can be implemented as a working program.

## 11. Conclusion

The Even and Odd Number Checker demonstrates the use of Python to solve a basic number-classification problem. By combining the modulus operator, conditional statements, functions, and input validation, the application provides a simple and understandable example of foundational programming. The project establishes a basis for further learning in Python programming and software development.

Author
M. Ayshwarya
