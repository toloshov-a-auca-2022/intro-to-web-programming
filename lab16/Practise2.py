#Example 1: Converting Python Data to JSON (Serialization)
import json

data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_data = json.dumps(data, indent=4)
print("Serialization: ")
print(json_data)

#Example 2: Converting JSON Back to Python Data (Deserialization)
import json

json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
    }
'''

data = json.loads(json_string)
print("Deserialization: ")
print(json.dumps(data, indent=4))

#Example 3: Reading from and Writing to a JSON File
import json, time

data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been created.")
