from datetime import datetime

import requests as requests

print("Imported Successfully")

my_apiKey = "533c9d81555477636864800774e8eb86"
location = input("Enter your current city")

api_request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={my_apiKey}")

api_data = api_request.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# for printing in the console
print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  : {}".format(weather_desc))
print("Current Humidity      : {} %".format(humidity))
print("Current wind speed    : {} kmph".format(wind_speed))

# logging the output in the weather.txt file
with open('weather.txt', 'w') as f:
    f.write("-------------------------------------------------------------\n")
    f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
    f.write("-------------------------------------------------------------\n")

    f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
    f.write("Current weather desc  : {}\n".format(weather_desc))
    f.write("Current Humidity      : {} %\n".format(humidity))
    f.write("Current wind speed    : {} kmph\n".format(wind_speed))
