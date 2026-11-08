# Veda-Technology-Internship

# Web Scraping Program Using Python

## 1. Project Overview

The Web Scraping Program is a Python application developed as part of the Python Programming Internship at Veda Technology. It extracts publicly available book information from the practice website Books to Scrape and stores the collected data in a CSV file.

The program uses HTTP requests to retrieve webpage content, BeautifulSoup to parse HTML, and Python's CSV module to save the extracted information. The extracted fields include book title, price, availability, and product URL.

## 2. Objectives

* Build a simple web scraper using Python.
* Understand how HTTP requests retrieve webpage content.
* Practise parsing HTML using BeautifulSoup.
* Extract structured information from webpage elements.
* Store extracted data in a CSV file.
* Follow responsible scraping practices by checking website access rules and using a reasonable request delay.

## 3. Technologies Used

* Python 3
* requests
* BeautifulSoup (beautifulsoup4)
* CSV module
* Visual Studio Code or another Python-compatible editor
* Command Prompt or terminal
* Git and GitHub for version control and project submission

## 4. Features

* Retrieves webpage content using the requests library.
* Parses HTML content using BeautifulSoup.
* Extracts book titles, prices, availability, and product URLs.
* Checks the website's robots.txt before scraping.
* Uses a request timeout and a descriptive User-Agent.
* Saves the extracted dataset in CSV format.
* Handles common network and file-writing errors.

## 5. Project Structure

```text
web-scraping-python/
├── web_scraper.py
├── scraped_books.csv
└── README.md
```

The CSV file is generated automatically when the program runs successfully.

## 6. Installation and Setup

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in your preferred code editor.
4. Open a terminal in the project directory.
5. Install the required Python libraries using the command below.

```bash
pip install requests beautifulsoup4
```

6. Run the program.

```bash
python web_scraper.py
```

On some systems, you may need to use `python3 web_scraper.py` instead.

## 7. Usage

1. Run the Python program.
2. The program checks whether its User-Agent is allowed to access the target page according to the website's robots.txt.
3. If access is permitted, it sends an HTTP request to the Books to Scrape catalogue page.
4. BeautifulSoup parses the returned HTML.
5. The program extracts each book's title, price, availability, and product URL.
6. The extracted records are saved in scraped_books.csv in the project directory.
7. A message displays the number of records extracted and the output filename.

## 8. Extracted Data and Error Handling

The program extracts the following fields:

* Title: Name of the book.
* Price: Displayed price of the book.
* Availability: Availability text shown on the webpage.
* Product URL: Link to the individual book page.

The program uses a request timeout and handles network or HTTP errors. It also handles CSV file-writing errors and displays a message if no matching book records are found. If access is not permitted by robots.txt, or the permission check cannot be completed, the program stops rather than proceeding.

## 9. Learning Outcomes

This project provides practical experience with HTTP requests, HTML parsing, CSS selectors, data extraction, URL handling, and CSV file operations in Python. It also introduces responsible web scraping practices, including checking website policies, respecting robots.txt, identifying the scraper with a User-Agent, and avoiding unnecessary requests.

## 10. Conclusion

The Web Scraping Program demonstrates how Python can collect structured information from a webpage and store it in a reusable CSV dataset. It provides a foundation for learning web scraping, HTML parsing, and data handling while highlighting the importance of respecting website access policies.

**Author**

M. Ayshwarya
