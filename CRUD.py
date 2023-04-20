# This script performs CRUD operations on a RESTful API

import requests

# Constants
API_URL = "https://api.example.com/resources"

def create_resource(payload):
    response = requests.post(API_URL, json=payload)
    if response.status_code == 201:
        print("Resource created successfully.")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def read_resources():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Resources retrieved successfully.")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def update_resource(resource_id, payload):
    update_url = f"{API_URL}/{resource_id}"
    response = requests.put(update_url, json=payload)
    if response.status_code == 200:
        print("Resource updated successfully.")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def delete_resource(resource_id):
    delete_url = f"{API_URL}/{resource_id}"
    response = requests.delete(delete_url)
    if response.status_code == 204:
        print("Resource deleted successfully.")
    else:
        print(f"Error: {response.status_code}")

# Usage examples:

# CREATE
new_payload = {"key": "value"}
new_resource = create_resource(new_payload)

# READ
resources = read_resources()

# UPDATE
resource_id_to_update = 1
update_payload = {"key": "new_value"}
updated_resource = update_resource(resource_id_to_update, update_payload)

# DELETE
resource_id_to_delete = 1
delete_resource(resource_id_to_delete)
