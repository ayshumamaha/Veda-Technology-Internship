"""
Task 27 — Build a Simple API Client
A small Python client that calls the JSONPlaceholder public REST API,
retrieves JSON data, and displays selected fields in a readable format.

Install dependency:
    pip install requests

Run:
    python api_client.py
"""

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"
TIMEOUT_SECONDS = 10


def fetch_post(url: str = API_URL) -> dict | None:
    """Fetch one post from the public API and return its JSON data."""
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)

        # Raise an exception for HTTP errors (4xx or 5xx).
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, dict):
            print("Error: The API returned an unexpected JSON format.")
            return None

        return data

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        status = error.response.status_code if error.response is not None else "unknown"
        print(f"Error: The API returned HTTP status {status}.")
    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
    except ValueError:
        print("Error: The response was not valid JSON.")

    return None


def display_post(post: dict) -> None:
    """Print selected post information in a clean format."""
    print("\n" + "=" * 45)
    print("           API RESPONSE — POST DETAILS")
    print("=" * 45)
    print(f"Post ID : {post.get('id', 'Not available')}")
    print(f"User ID : {post.get('userId', 'Not available')}")
    print(f"Title   : {post.get('title', 'Not available')}")
    print("-" * 45)
    print("Body:")
    print(post.get("body", "Not available"))
    print("=" * 45)


def main() -> None:
    print("Connecting to JSONPlaceholder API...")
    post = fetch_post()

    if post is not None:
        print("Request successful (HTTP 200).")
        display_post(post)
    else:
        print("Unable to retrieve post data.")


if __name__ == "__main__":
    main()
