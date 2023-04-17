# This script performs CRUD operations on a RESTful API

import requests

api_url = "https://api.example.com/resources"

# CREATE
payload = {"key": "value"}
response = requests.post(api_url, json=payload)
print(response.json())

# READ
response = requests.get(api_url)
print(response.json())

# UPDATE
resource_id = 1
update_url = f"{api_url}/{resource_id}"
update_payload = {"key": "new_value"}
response = requests.put(update_url, json=update_payload)
print(response.json())

# DELETE
response = requests.delete(update_url)
print(response.status_code)
