# Veda-Technology-Internship
# Reusable Python Utility Module

## 1. Project Overview

The Reusable Python Utility Module is a collection of commonly used helper functions for validation, formatting, calculations, and file operations. It is designed to make frequently required operations easier to reuse across different Python programs.

The module can be executed directly to demonstrate its functions or imported into another Python application.

## 2. Objectives

* Develop a reusable Python utility module.
* Understand modular programming.
* Create validation and formatting functions.
* Perform basic mathematical calculations.
* Implement file-reading and file-writing utilities.

## 3. Technologies Used

* Python 3
* re module
* pathlib module
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub for version control and project submission

## 4. Features

* Validates basic email-address formats.
* Validates positive numerical values.
* Checks phone-number digit counts.
* Formats currency and percentages.
* Removes unnecessary whitespace from text.
* Calculates percentages, averages, and totals.
* Checks whether a file exists.
* Reads and writes UTF-8 text files.
* Creates parent directories when writing files.
* Includes built-in demonstrations of utility functions.

## 5. Project Structure

```text
python-utility-module/
├── Task 20.py
└── README.md
```

## 6. Installation and Setup

1. Install Python 3.
2. Download or clone the repository.
3. Open the project folder in your preferred code editor.
4. Open the terminal.
5. Run the module.

```bash
python "Task 20.py"
```

## 7. Usage

1. Run the Python file to view the built-in demonstrations.
2. To reuse its functions, place the module in your project directory or Python import path.
3. Import the required functions into another Python program.
4. Call the functions with appropriate arguments.

Example:

```python
from utility_module import (
    is_valid_email,
    percentage,
    format_currency
)
```

Note: Use the actual Python module filename when importing it.

## 8. Error Handling

The utility functions validate input types and values. Invalid arguments may raise TypeError or ValueError. File operations may also raise standard file-system exceptions, which can be handled by the calling application.

## 9. Learning Outcomes

This project provides practical experience with modular programming, imports, functions, type hints, regular expressions, validation, formatting, mathematical calculations, and file operations.

## 10. Conclusion

The Reusable Python Utility Module demonstrates the importance of modular programming and code reusability. It provides a foundation for creating organised Python projects with reusable functions.

## Author

M. Ayshwarya
