import os
import requests
from helper import API_KEY, END_POINT, NAME as name

# Get city
city_name = input('Enter a city name: ')

# GET the weather data
response = requests.get(f'{END_POINT}/weather?q={city_name}&appid={API_KEY}')
weather_data = response.json()

# Check if raining or not
isRaining = weather_data['weather'][0]['main'] == 'Rain'

# Display the result
print(f'{name} its Raining' if isRaining else f'{name} its Not Raining')

