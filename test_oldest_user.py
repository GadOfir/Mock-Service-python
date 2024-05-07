import pytest
import requests
from datetime import datetime

# Define the base URL of your Flask API
BASE_URL = "http://localhost:5000"  # Update the port if your Flask app is running on a different port


# Define a custom function to parse the date string and return a datetime object
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


# Define a pytest test function to check the oldest user via API
def test_oldest_user_api():
    # Make a GET request to fetch all users
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

    users = response.json()

    # Find the oldest user based on birthdate
    oldest_user = min(users, key=lambda user: parse_date(user["birthdate"]))

    print(f"The oldest user is: {oldest_user['name']}")  # Print the name of the oldest user

    # Make a GET request to get the oldest user's details by ID
    response_oldest_user = requests.get(f"{BASE_URL}/users/birthday/{oldest_user['id']}")
    assert response_oldest_user.status_code == 200

    oldest_user_api = response_oldest_user.json()

    # Assert that the oldest user's name matches the expected name
    assert oldest_user_api["name"] == oldest_user["name"]