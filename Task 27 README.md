# Veda-Technology-Internship

# TASK 27 Python Configuration Management System

## 1. Project Overview

The Python Configuration Management System is a simple Python application that reads configuration values from external files and environment variables instead of hardcoding them into the program.

It allows users to manage application settings using a JSON configuration file (`config.json`), environment variables, and an optional `.env` file.

The project demonstrates file handling, JSON operations, environment variable management, functions, conditional statements, and error handling in Python.

## 2. Objectives

- Develop a Python application that manages configuration settings.
- Learn how to read and process JSON configuration files.
- Understand the use of environment variables.
- Separate application configuration from source code.
- Implement default values when configuration settings are missing.
- Follow basic security practices for handling sensitive information.

## 3. Features

- Automatically creates a `config.json` file if it does not exist.
- Reads configuration values from JSON files.
- Supports environment variables and optional `.env` files.
- Allows environment variables to override JSON configuration values.
- Provides default configuration settings.
- Converts configuration values into appropriate data types.
- Handles invalid JSON and configuration errors.
- Avoids displaying sensitive database information.

## 4. Technologies Used

- **Programming Language:** Python 3
- **Libraries:** `json`, `os`, `pathlib`
- **Configuration Formats:** JSON, `.env`
- **IDE:** VS Code / Jupyter Notebook / Google Colab

## 5. Project Structure

```text
Python-Configuration-Management/
│
├── config_manager.py
├── config.json
├── .env
└── README.md
```

*Note: The `config.json` file is generated automatically when the program runs for the first time. The `.env` file is optional.*

## 6. How to Run the Project

1. Download or clone the project repository.
2. Open the project in VS Code or any Python environment.
3. Run the Python file:

```bash
python config_manager.py
```

4. The application automatically creates the configuration file if it is missing.
5. The configuration values are loaded and displayed in the terminal.

## 7. Sample Configuration

Example `config.json`:

```json
{
    "APP_NAME": "My Python Application",
    "DEBUG": true,
    "PORT": 5000,
    "ENVIRONMENT": "development",
    "DATABASE_URL": ""
}
```

Example `.env` file:

```text
APP_PORT=8000
APP_DEBUG=false
```

Environment variables take priority over values stored in the JSON configuration file.

## 8. Expected Output

```text
=============================================
PYTHON CONFIGURATION MANAGEMENT SYSTEM
=============================================
Application : My Python Application
Environment : development
Debug Mode  : True
Port        : 5000
Database URL: Not configured
---------------------------------------------
Configuration loaded successfully!
=============================================
```

## 9. Security Practices

- Avoid hardcoding sensitive configuration values.
- Do not store passwords or API keys directly in source code.
- Do not commit `.env` files containing real secrets to GitHub.
- Use environment variables to manage sensitive information.
- Keep configuration files separate from application logic.

## 10. Conclusion

This project provides a basic understanding of configuration management in Python. It demonstrates how applications can load settings from external sources, use environment variables, and maintain default configurations.
It also introduces good software development practices by separating configuration data from application code.

## Author
M. Ayshwarya
