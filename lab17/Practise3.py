# Example 2: API Endpoint Call

import requests

apiURL = "https://api.example.com/data?type=latest&limit=5"
response = requests.get(apiURL)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error occurred:",response.status_code)

# explanation:URL Structure: The URL defines the endpoint, and query parameters specify the type of data and how many items to retrieve.Result: The app receives and processes the data for display.