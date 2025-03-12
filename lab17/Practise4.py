# Examples in Python
# Example 1: Using an API to Fetch Data
# Imagine you want to get the current weather information for a city. Many weather services provide APIs for this purpose. Here’s a simplified examp

# explanation:The URL in api_url represents the endpoint where the weather data is available.The params dictionary includes parameters that the API needs (like the city name and API key).The requests.get() function sends a GET request to the API, and the response is parsed from JSON into a Python dictionary.
import requests, random

apiURL = "https://api.open-meteo.com/v1/forecast"

cities = [
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
]

randomCities = random.sample(cities, 5)

for city in randomCities:
    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "current_weather": "true"
    }

    response = requests.get(apiURL, params=params)

    if response.status_code == 200:
        data = response.json()
        if "current_weather" in data:
            weather = data["current_weather"]
            print(f"{city['name']}: {weather['temperature']}°C")
        else:
            print(f"Weather data not found for {city['name']}.")
    else:
        print("Status code: ", response.status_code)