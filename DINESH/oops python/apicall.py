import requests
import json

url = "https://api.sampleapis.com/coffee/hot"

response = requests.get(url).json()


for coffee in response:
    if 'ingredients' in coffee:  
        for ingredient in coffee['ingredients']:
            
            print(json.dumps(coffee, indent=4))  
            break  
