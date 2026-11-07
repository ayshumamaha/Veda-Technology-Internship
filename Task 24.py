"""
Simple Web Scraper
------------------
Extracts publicly available book information from the practice website
https://books.toscrape.com/ and saves it to a CSV file.
"""

import csv
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

START_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv"
REQUEST_DELAY = 2  # Be considerate; do not send rapid repeated requests.
USER_AGENT = "EducationalWebScraper/1.0"


def is_allowed_by_robots(url):
    """Return whether robots.txt allows this scraper to fetch the URL."""
    robots_url = urljoin(url, "/robots.txt")
    parser = RobotFileParser()
    parser.set_url(robots_url)

    try:
        parser.read()
        return parser.can_fetch(USER_AGENT, url)
    except Exception as error:
        print(f"Could not check robots.txt ({error}). Scraping stopped for safety.")
        return False


def scrape_books(page_url):
    """Fetch one catalogue page and extract its book details."""
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(page_url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for item in soup.select("article.product_pod"):
        title_element = item.select_one("h3 a")
        price_element = item.select_one(".price_color")
        availability_element = item.select_one(".availability")

        if not title_element:
            continue

        books.append(
            {
                "title": title_element.get("title", title_element.get_text(strip=True)),
                "price": price_element.get_text(strip=True) if price_element else "",
                "availability": (
                    availability_element.get_text(" ", strip=True)
                    if availability_element
                    else ""
                ),
                "product_url": urljoin(page_url, title_element.get("href", "")),
            }
        )

    return books


def save_to_csv(records, filename):
    """Write extracted records to a CSV file."""
    fieldnames = ["title", "price", "availability", "product_url"]

    with open(filename, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def main():
    print("Starting the web scraping program...")
    print(f"Target website: {START_URL}")

    if not is_allowed_by_robots(START_URL):
        print("Access is not permitted by robots.txt, or permission could not be verified.")
        return

    try:
        records = scrape_books(START_URL)

        if not records:
            print("No book records were found. The website structure may have changed.")
            return

        save_to_csv(records, OUTPUT_FILE)
        print(f"Successfully extracted {len(records)} book records.")
        print(f"CSV file saved as: {OUTPUT_FILE}")

        # A delay is included before any future additional requests.
        time.sleep(REQUEST_DELAY)

    except requests.RequestException as error:
        print(f"Network or HTTP error: {error}")
    except OSError as error:
        print(f"Could not save the CSV file: {error}")


if __name__ == "__main__":
    main()
