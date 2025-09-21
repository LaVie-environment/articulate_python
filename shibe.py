#!/usr/bin/env python3

# First thing we will do is import the requests library
import requests

# Define a variable with the URL of the API endpoint
api_url = "https://shibe.online/api/shibes?count=1"

# Call the root of the api with GET, store the answer in a response variable
# THia call will return a list of URLs that represent dog pictures
response = requests.get(api_url, timeout=10)

# Get the status code for the response. Should be 200 OK
# Which means everything worked as expected
print(f"Response status code is: {response.status_code}")

# Get the result as JSON
response_json = response.json()

# Print it. We should see a list of one image URL.
print(response_json)
