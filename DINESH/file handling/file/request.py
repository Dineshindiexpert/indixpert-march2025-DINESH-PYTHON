import requests
import json

endpoint = "http://universities.hipolabs.com/search?country=India"

response = requests.get(endpoint)
data = response.json()

state = "Haryana"
flag = 0
i = 1

for university in data:
    if university.get('state-province'):
        if university['state-province'] == state:
            print(f"University {i} = {university['name']}")
            webpageno=1
            for j in university['web_pages']:
                print(f"Web Pages{webpageno} : {j}")
                flag = 1
                i += 1
            print(f"{webpageno} url  is present of  this university.")
            webpageno+=1
            print("#"*100)
if flag == 0:
    print("Not found")
else:
    print("Data found successfully.")
    print("thanks.")