Veda-Technology-Internship
Weather Data CLI Using Python
1. Project Overview
The Weather Data CLI is a command-line Python application developed as part of the Python Programming Internship at Veda Technology. It retrieves real-time weather information for a user-provided city using the OpenWeatherMap API.
The application displays important weather details, including temperature, feels-like temperature, weather conditions, humidity, atmospheric pressure, wind speed, and visibility.
The project demonstrates the use of API integration, HTTP requests, JSON data processing, functions, environment variables, user input handling, and exception handling in Python.
2. Objectives
- Develop a command-line weather application using Python.
- Retrieve real-time weather information using the OpenWeatherMap API.
- Practise sending HTTP requests and processing JSON responses.
- Display weather information in a structured format.
- Handle invalid city names and API errors.
- Manage API credentials securely.
- Implement error handling for network and request failures.
3. Technologies Used
- Python 3
- Requests library
- OpenWeatherMap API
- Visual Studio Code or another Python-compatible editor
- Command Prompt or terminal
- Git and GitHub for version control and project submission
4. Features
- Accepts a city name from the user.
- Retrieves current weather information through an API.
- Displays city name and country.
- Shows temperature in Celsius.
- Displays feels-like temperature and weather conditions.
- Provides humidity and atmospheric pressure information.
- Displays wind speed and visibility.
- Automatically installs the required Requests library if unavailable.
- Handles invalid city names and incorrect API keys.
- Handles connection errors, request timeouts, and API failures.
- Allows users to search for multiple cities until they choose to exit.
5. Project Structure
weather-data-cli-python/
├── weather_cli.py
└── README.md


6. Installation and Setup
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your preferred code editor.
4. Register for an API key on the OpenWeatherMap website.
5. Open a terminal in the project directory.
6. Run the program using the command below.
python weather_cli.py


On some systems, you may need to use python3 weather_cli.py instead.

The program automatically checks for and installs the required Requests library.

API key registration: https://openweathermap.org/api
7. Usage
1. Run the Python program.
2. Enter your OpenWeatherMap API key when prompted, unless it is already configured as an environment variable.
3. Enter the name of the city for which you want weather information.
4. Wait for the application to retrieve the weather data.
5. View the formatted weather report.
6. Enter another city name to check additional weather information.
7. Type exit to close the application.
8. Error Handling
The application includes exception handling to manage common errors during API communication.
- Displays an error message when an invalid city name is entered.
- Handles invalid API keys.
- Handles API rate-limit errors.
- Detects request timeouts.
- Handles internet connection failures.
- Handles HTTP request errors.
- Handles unexpected or incomplete JSON responses.
- Checks for empty city-name inputs.
The API key is requested at runtime or read from an environment variable instead of being directly stored in the source code.
9. Learning Outcomes
This project provides practical experience with Python API integration, HTTP requests, JSON processing, external libraries, functions, environment variables, and exception handling.
It also improves understanding of how external APIs communicate with Python applications, how to extract useful information from JSON responses, and how to handle network-related errors while developing command-line applications.

10. Conclusion
The Weather Data CLI project demonstrates how Python can be integrated with an external weather API to develop a practical command-line application. It combines API communication, JSON data processing, formatted output, and error handling into a single program.
The project provides a foundation for understanding API-based application development and strengthens practical Python programming skills.

Author
M. Ayshwarya
