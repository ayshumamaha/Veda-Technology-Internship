"""
Task 22 — Build a Simple API Client
A small Python client that calls the JSONPlaceholder public REST API,
retrieves JSON data, and displays selected fields in a readable format.

Install dependency:
    pip install requests

Run:
    python api_client.py
"""

"""
Task 22: Build a Simple API Client
Fetches an English quote from a public API
and displays it in a readable format.
"""

import requests

API_URL = "https://dummyjson.com/quotes/1"

def fetch_quote():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print("Error connecting to API:", error)
        return None


def display_quote(data):
    print("\n" + "=" * 45)
    print("          ENGLISH QUOTE DETAILS")
    print("=" * 45)

    print("Quote ID :", data.get("id"))
    print("Quote    :", data.get("quote"))
    print("Author   :", data.get("author"))

    print("=" * 45)


def main():
    print("Connecting to English Quote API...")

    data = fetch_quote()

    if data:
        print("Request successful!")
        display_quote(data)
    else:
        print("Unable to retrieve quote.")


if __name__ == "__main__":
    main()
