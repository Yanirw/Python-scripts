# This script fetches data from a JSON API, parses it, and displays each item in the JSON object

import json
import requests

def fetch_and_parse_json_api(url):
    response = requests.get(url)
    data = json.loads(response.text)

    for item in data:
        print(item)

url = "https://jsonplaceholder.typicode.com/todos"
fetch_and_parse_json_api(url)

