import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import matplotlib.pyplot as plt


# Weather App using OpenWeatherMap API

load_dotenv()  # Load the .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("Error: API key not found.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    
    # Step 2: Check status code
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message')}")
        return

    data = response.json()

    # Step 3: Validate required fields
    try:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print(f"\nWeather in {city.title()}:")
        print(f"🌡️  Temperature: {temp}°C")
        print(f"☁️  Description: {description}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️  Wind Speed: {wind} m/s")
        visualize_weather(city, temp, humidity, wind)
        print("\nWeather data retrieved successfully!")

        # Optional: Log raw response
        weather_log_path = os.path.join(os.path.dirname(__file__), "weather_log.json")
        with open(weather_log_path, "w", encoding="utf-8") as f:
            f.write(response.text)

    except KeyError as e:
        print(f"Missing expected field: {e}")



def visualize_weather(city, temp, humidity, wind_speed):
    metrics = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [temp, humidity, wind_speed]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(metrics, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title(f"Weather Summary: {city.title()}")
    plt.ylim(0, max(values) + 10)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + 1, f'{yval:.1f}', fontsize=10)

    plt.tight_layout()
    # Save the image in the same folder as the script
    output_path = os.path.join(os.path.dirname(__file__), "weather_visual.png")
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
