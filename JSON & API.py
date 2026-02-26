
import requests
import json

print("===== WEATHER INFO FETCHER =====")

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

try:
    city = input("Enter city name: ").strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Write JSON to file
        with open("weather.json", "w") as f:
            json.dump(data, f, indent=4)

        # Extract information
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"\nCity: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")

    else:
        print("City not found or API error.")

except Exception as e:
    print("Error:", e)

