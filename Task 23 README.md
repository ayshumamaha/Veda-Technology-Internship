Weather Data CLI Using Python
1. Project Overview
The Weather Data CLI is a command-line Python application developed as part of the Python Programming Internship at Veda Technology. It accepts a city name from the user and retrieves real-time weather information using the OpenWeatherMap API.

The project demonstrates the use of API requests, JSON processing, functions, user input handling, and error handling in Python.
2. Objectives
- Develop a weather application using Python.
- Retrieve weather information using an external API.
- Practise API requests and JSON data processing.
- Display temperature, humidity, pressure, and wind speed.
- Handle invalid city names and API errors.
- Manage API credentials securely.
3. Technologies Used
- Python 3
- Requests library
- OpenWeatherMap API
- Visual Studio Code or another Python-compatible editor
- Command Prompt or terminal
- Git and GitHub for version control and project submission
4. Features
- Accepts city names from the user.
- Retrieves real-time weather information.
- Displays temperature in Celsius.
- Shows feels-like temperature and weather conditions.
- Displays humidity, atmospheric pressure, and wind speed.
- Provides visibility information.
- Supports multiple city searches.
- Handles invalid city names and API errors.
- Handles network connection errors and request timeouts.
- Allows users to exit the application.
5. Project Structure
weather-data-cli-python/
├── weather_cli.py
└── README.md


6. Installation and Setup
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your preferred code editor.
4. Open a terminal in the project directory.
5. Obtain an API key from OpenWeatherMap.
6. Run the program using the command below.
python weather_cli.py


On some systems, you may need to use python3 weather_cli.py instead.

The program automatically installs the required Requests library if it is not already available.
7. Usage
1. Run the Python program.
2. Enter your OpenWeatherMap API key when prompted.
3. Enter the city name when requested.
4. Wait for the application to retrieve weather information.
5. View the formatted weather report.
6. Enter another city name to check its weather.
7. Type exit to close the application.
8. Error Handling
The program handles invalid city names, incorrect API keys, API rate limits, network connection failures, and request timeouts. It also validates empty city inputs and handles unexpected API responses to prevent the application from terminating unexpectedly.
9. Learning Outcomes
This project provides practical experience with Python API integration, HTTP requests, JSON processing, functions, external libraries, environment variables, and exception handling. It also improves understanding of retrieving and processing real-time information from external APIs.
10. Conclusion
The Weather Data CLI project demonstrates how Python can be used to develop a practical application that retrieves real-time weather information through an external API. It provides a foundation for understanding API integration, JSON processing, and error handling in Python application development.

Author

M. Ayshwarya
