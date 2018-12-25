#! python3
# movieData.py - Prints the requested title from the command line.

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
movie = json.loads(response.text)
