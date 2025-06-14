import datetime as dt
import requests

# This script fetches the current weather data for Waterford, IE from the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "Waterford, IE"

# Converts temperature from Kelvin to Celsius
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Fetching weather data from OpenWeatherMap API
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY 
response = requests.get(url).json()
# print(response)

# Check if the response is valid
if response['cod'] != 200:
    print(f"Error fetching data for {CITY}: {response['message']}")
    exit()

# Extracting relevant data from the response
temp = kelvin_to_celsius(response['main']['temp'])
feels_like = kelvin_to_celsius(response['main']['feels_like'])
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

# Displaying the weather information
print(f"\nTemperature in {CITY} is {temp:.2f}°C")
print(f"Temperature in {CITY} feels like {feels_like:.2f}°C")
print(f"Wind speed in {CITY} is {wind_speed} m/s")
print(f"Humidity in {CITY} is {humidity}%")
print(f"Weather description in {CITY} is {description}")
print(f"Sunrise in {CITY} is at {sunrise_time} local time")
print(f"Sunset in {CITY} is at {sunset_time} local time\n")