import requests
import json

endpoint = "https://api.sampleapis.com/coffee/hot"
data = requests.get(endpoint)
data=data.json()
ingredient = "Espresso"
flag = 0

tosearch='ingredients'
for coffeetype in data:
    if tosearch in coffeetype: 
        if ingredient not in coffeetype['ingredients']:
            print("next coffe is :")
            print("               ",json.dumps(coffeetype))
            print("#"*100)
            print("")
            print("")
            
            flag = 1

if flag==0:
    print(f"in the api present the every coffe type :{ingredient}")
