#Lab Exercise 1: Converting a Python Dictionary to a JSON String (Serialization)
import json

from lab15.Practise import fileName

data = {
    "name": "Adilet",
    "age": 21,
    "courses": ["Intro to Web Programming", "German Language", "Algorithms"]
}

json_data = json.dumps(data, indent=4)
print(json_data)

#Lab Exercise 2: Converting a JSON String Back to a Python Object (Deserialization)
import json

jsonData = '''
    {    
    "name": "Adilet",
    "age": 21,
    "courses": ["Intro to Web Programming", "German Language", "Algorithms"]
    }
'''

jsonData = json.loads(jsonData)
print(jsonData)


#Lab Exercise 3: Reading from and Writing to a JSON File
import json, time

data = {
    "name": "Adilet",
    "age": 21,
    "year of study": "Junior",
    "courses": ["Intro to Web Programming", "German Language", "Algorithms"]
}

with open("info.json", "w") as file:
    json.dump(data, file, indent=4)
print("Data has been saved to info.json")

with open("info.json", "r") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))