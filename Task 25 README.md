# Veda-Technology-Internship

# Log File Analyzer Using Python

## 1. Project Overview

The Log File Analyzer is a Python application developed as part of the Python Programming Internship at Veda Technology. It reads a web server access log and analyzes request activity to identify the total number of requests, error responses, frequently occurring IP addresses, and commonly requested endpoints.

The project demonstrates the use of Python string processing, regular expressions, dictionaries, the collections.Counter class, file handling, and basic data analysis.

## 2. Objectives

* Develop a log file analyzer using Python.
* Read and process server log files.
* Count total valid requests and HTTP error responses.
* Identify the most frequent IP addresses.
* Find the most commonly requested endpoints.
* Handle malformed log lines without stopping the analysis.
* Generate a readable summary report.

## 3. Technologies Used

* Python 3
* re module for regular-expression-based log parsing
* collections.Counter for counting IP addresses, endpoints, and status codes
* argparse for command-line arguments
* pathlib for file handling
* CSV/Text logs or server access-log files
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub for version control and project submission

## 4. Features

* Reads server access logs in Common or Combined Log Format.
* Counts successfully parsed HTTP requests.
* Counts error responses with HTTP status codes 400 and above.
* Displays the most frequent IP addresses.
* Identifies the most requested endpoints.
* Summarizes the frequency of each HTTP status code.
* Skips malformed log lines and reports how many were skipped.
* Displays the analysis in the terminal.
* Saves the summary report to a text file.
* Allows the user to specify the input file, report filename, and number of top results.

## 5. Project Structure

```text
log-file-analyzer-python/
├── log_analyzer.py
├── server.log
├── analysis_report.txt
└── README.md
```

The server.log file is the input dataset. The analysis_report.txt file is generated automatically when the program runs successfully.

## 6. Installation and Setup

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your preferred code editor.
4. Place a server access-log file named server.log in the project directory. The file should use Common or Combined Log Format.
5. Open a terminal in the project directory.
6. Run the program using the command below.

```bash
python log_analyzer.py
```

On some systems, you may need to use `python3 log_analyzer.py` instead.

No external Python libraries are required.

## 7. Usage

1. Run the Python program.
2. The program reads the server.log file by default.
3. Each non-empty line is parsed to extract the IP address, requested endpoint, and HTTP status code.
4. Valid records are counted and grouped using Counter.
5. The program calculates the total request count, error count, top IP addresses, and most requested endpoints.
6. The summary is displayed in the terminal.
7. The report is saved as analysis_report.txt.

A different input file can be supplied:

```bash
python log_analyzer.py access.log
```

To display the top 10 IP addresses and endpoints:

```bash
python log_analyzer.py server.log --top 10
```

To specify a different report filename:

```bash
python log_analyzer.py server.log --output report.txt
```

## 8. Error Handling and Report Details

The program skips malformed or unsupported log lines and records their count in the report. It also checks whether the specified input file exists and handles file-reading or report-writing errors.

The report contains the following information:

* Total Requests: Number of valid log entries parsed.
* Error Responses: Number of responses with HTTP status codes 400–599.
* Malformed Lines: Number of non-empty lines that could not be parsed.
* Top IP Addresses: IP addresses with the highest request counts.
* Top Requested Endpoints: Endpoints accessed most frequently.
* HTTP Status-Code Counts: Number of occurrences of each status code.

The parser is designed for Common or Combined Log Format entries containing an IP address, timestamp, quoted request, status code, and response-size field.

## 9. Learning Outcomes

This project provides practical experience with Python file handling, string processing, regular expressions, dictionaries, the collections.Counter class, command-line arguments, and basic data analysis. It also demonstrates how raw server logs can be converted into a structured summary that helps identify request patterns and error activity.

## 10. Conclusion

The Log File Analyzer demonstrates how Python can be used to process server log files and extract useful information about web traffic. By identifying request counts, error responses, frequent IP addresses, and popular endpoints, the project provides a foundation for understanding log analysis and basic server monitoring.

**Author**

M. Ayshwarya
