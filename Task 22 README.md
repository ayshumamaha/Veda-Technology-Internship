# Veda-Technology-Internship
# Build a Simple API Client

## 1. Project Overview

The Simple API Client is a Python application that connects to a public REST API, retrieves JSON data, and displays selected information in a clean and readable format.

The project uses the requests library to send an HTTP GET request to the JSONPlaceholder public API. It demonstrates basic API consumption, JSON response handling, HTTP status checking, and error handling.

## 2. Objectives

* Develop a simple API client using Python.
* Understand basic REST API communication.
* Send HTTP requests using the requests library.
* Retrieve and process JSON responses.
* Check HTTP status codes.
* Handle connection failures and request errors.

## 3. Technologies Used

* Python 3
* requests library
* JSONPlaceholder public REST API
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub for version control and project submission

## 4. Features

* Sends an HTTP GET request to a public REST API.
* Retrieves JSON response data.
* Checks HTTP response status using raise_for_status().
* Uses a request timeout of 10 seconds.
* Extracts post ID, user ID, title, and body.
* Displays selected information in a formatted output.
* Handles connection failures and timeout errors.
* Handles HTTP errors and invalid JSON responses.

## 5. Project Structure

```text
simple-api-client/
├── Task 22.py
└── README.md
```

## 6. Installation and Setup

1. Install Python 3 on your computer.
2. Download or clone the repository.
3. Open the project folder in your preferred code editor.
4. Open a terminal in the project directory.
5. Install the required requests library.

```bash
pip install requests
```

6. Run the program.

```bash
python "Task 22.py"
```

On some systems, you may need to use python3 instead of python.

## 7. Usage

1. Run the Python program.
2. Ensure that an internet connection is available.
3. The application sends a GET request to the JSONPlaceholder API.
4. The API returns a JSON response containing post information.
5. The program extracts selected fields.
6. View the formatted API response in the terminal.

## 8. Error Handling

The program handles connection failures, request timeouts, HTTP errors, general request exceptions, and invalid JSON responses.

It also verifies that the returned JSON data is in the expected dictionary format. The selected public API endpoint does not require an API key.

## 9. Learning Outcomes

This project provides practical experience with REST APIs, HTTP GET requests, JSON parsing, HTTP status codes, third-party Python libraries, formatted output, and exception handling.

## 10. Conclusion

The Simple API Client demonstrates how Python can interact with external web services and retrieve structured data. It provides a foundation for understanding API integration, JSON processing, and building applications that communicate with online services.

## Author

M. Ayshwarya
