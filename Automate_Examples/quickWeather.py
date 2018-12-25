#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
movie = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'http://www.omdbapi.com/?apikey=5d36aebf&s=%s&type&plot=full' % (movie)
response = requests.get(url)
response.raise_for_status()

# TODO Load JSON data into a Python variable.
movieData = json.loads(response.text)

# Print weather descriptions.
w = movieData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
