import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

data = requests.get(url).json()
print(json.dumps(data,indent=4))

# Loop through the users to check the address
# for username in data:
#     # Check if the street in the address matches "Kulas Light"
#     if username['company']['name'] == "Romaguera-Crona":
#         print(json.dumps(username, indent=4))
for username in data:
    if username['phone']=="024-648-3804":
        print(json.dumps(username,indent=4))