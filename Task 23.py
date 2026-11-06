import sys
import subprocess
import os


def install_requests():
    """Install requests automatically if it is not already installed."""
    try:
        import requests
        return requests
    except ImportError:
        print("Installing required package: requests...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "requests"]
        )
        import requests
        return requests


def get_weather(city, api_key, requests):
    """Fetch and display current weather for the selected city."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    print("\nFetching weather information...")

    try:
        response = requests.get(url, params=params, timeout=15)

        if response.status_code == 404:
            print("Error: City not found. Please check the city name.")
            return
        if response.status_code == 401:
            print("Error: Invalid API key. Check your OpenWeatherMap API key.")
            return
        if response.status_code == 429:
            print("Error: API rate limit exceeded. Try again later.")

        response.raise_for_status()
        data = response.json()

        print("\n" + "=" * 45)
        print("                 WEATHER REPORT")
        print("=" * 45)
        print(f"City          : {data['name']}")
        print(f"Country       : {data['sys']['country']}")
        print(f"Temperature   : {data['main']['temp']} °C")
        print(f"Feels Like    : {data['main']['feels_like']} °C")
        print(f"Condition     : {data['weather'][0]['description'].title()}")
        print(f"Humidity      : {data['main']['humidity']}%")
        print(f"Pressure      : {data['main']['pressure']} hPa")
        print(f"Wind Speed    : {data.get('wind', {}).get('speed', 'N/A')} m/s")
        print(f"Visibility    : {data.get('visibility', 'N/A')} metres")
        print("=" * 45)

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"API error: {error}")
    except (KeyError, IndexError, ValueError):
        print("Error: The API returned unexpected weather data.")
    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")


def main():
    requests = install_requests()

    print("=" * 45)
    print("              WEATHER DATA CLI")
    print("=" * 45)
    print("Get current weather information for any city.")

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        api_key = input("\nEnter your OpenWeatherMap API key: ").strip()

    if not api_key:
        print("An API key is required. Exiting.")
        return

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Data CLI!")
            break
        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city, api_key, requests)


if __name__ == "__main__":
    main()
