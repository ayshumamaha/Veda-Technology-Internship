"""
Task: Weather Data CLI
Fetches current weather information for a city.
"""

import requests

def get_weather():
    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()
        weather = data["current_condition"][0]

        print("\n====== WEATHER REPORT ======")
        print("City:", city.title())
        print("Temperature:", weather["temp_C"], "°C")
        print("Condition:", weather["weatherDesc"][0]["value"])
        print("Humidity:", weather["humidity"], "%")
        print("Wind Speed:", weather["windspeedKmph"], "km/h")
        print("============================")

    except requests.exceptions.RequestException:
        print("Unable to fetch weather. Check your internet connection.")
    except (KeyError, IndexError, ValueError):
        print("Unable to read weather information.")


get_weather()
