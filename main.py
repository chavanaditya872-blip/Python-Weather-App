import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    if not API_KEY:
        print("API key not found. Check your .env file.")
        return

    try:
        response = requests.get(
            URL,
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )

        if response.status_code == 404:
            print("City not found. Please enter a valid city.")
            return

        if response.status_code == 401:
            print("Invalid API key or key is not active yet.")
            return

        response.raise_for_status()

        data = response.json()

        print("\n========== WEATHER REPORT ==========")
        print("City:", data.get("name", "Unknown"))
        print("Temperature:", data.get("main", {}).get("temp", "N/A"), "°C")
        print("Humidity:", data.get("main", {}).get("humidity", "N/A"), "%")
        print("Weather:", data.get("weather", [{}])[0].get("description", "N/A"))
        print("Wind Speed:", data.get("wind", {}).get("speed", "N/A"), "m/s")
        print("====================================")

    except requests.exceptions.RequestException as error:
        print("Network or API error:", error)


def main():

    print("WELCOME TO PYTHON WEATHER APP")

    while True:

        city = input("\nEnter city name (or press Enter to exit): ").strip()

        if not city:
            print("Weather App closed.")
            break

        get_weather(city)


if __name__ == "__main__":
    main()