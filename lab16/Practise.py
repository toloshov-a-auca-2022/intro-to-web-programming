#1. Converting Python Objects to JSON (Serialization)
import json

data = {
    "name": "Adilet",
    "age": 22,
    "city of birth": "New York"
}

json_data = json.dumps(data)
print(json_data)

#2. Writing JSON to a File
import json

data = {
    "name": "Adilet",
    "age": 22,
    "city of birth": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


#3. Reading JSON from a File
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))


# 4. Converting JSON to a Python Object (Deserialization)
import json

text = '{"name": "Adilet","age": 22,"city of birth": "New York"}'
data = json.loads(text)

print(data['name'])
print(type(data['age']))

#5. Working with Lists in JSON
import json

data = [
    {"name": "Alice", "age": 35},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 22}
]

jsonData = json.dumps(data, indent=4)
print(jsonData)


#6. Writing a List of Dictionaries to a File
import json

data = [
    {"name": "Alice", "age": 35},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 22}
]

with open('users.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


#7. Handling JSON Errors
import json

text = '{"name": "Adilet","age": 22,"city of birth": "New York"'

try:
    datas = json.loads(text)
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")



