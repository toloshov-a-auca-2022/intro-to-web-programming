#Example 1: Basic Text File Operations
import time

fileName = "example.txt"
content = "Hello, World!\nWelcome to Python!"

print(f"Content is writing to a file...")
time.sleep(3)
with open(fileName, "w") as file:
    file.write(content)
print(f"Content is successfully written to: {fileName}\n")

print(f"Content is reading from the file...")
time.sleep(3)

with open(fileName, "r") as file:
    content = file.read()
print(content)
print(f"Content is successfully read from: {fileName}")
print("\nGoodbye!")

#Example 2: Processing CSV Files
import csv, time

fileName = "data.csv"
data = [
    ["Name","Age","City"],
    ["Adilet", "20", "New York"],
    ["Fara", "20", "Los Angeles"],
    ["Nuris", "21", "Chicago"],
]

print("Writing to a csv file...")
time.sleep(3)
with open(fileName, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Content is successfully written to: {fileName}\n")

print("Reading from a csv file...")
time.sleep(3)
with open(fileName, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print (row["Name"])

print("\nDone!")

# Example 3: Appending Data to a File
import time

fileName = "example.txt"
addContent = "\nHave a good learning process!"

print("Content is appending to an existing file...")
time.sleep(3)
with open(fileName, "a") as file:
    file.write(addContent)
print(f"Content is successfully appended to: {fileName}\n")

print("Reading an updated file...")
time.sleep(3)
with open(fileName, "r") as file:
    content = file.read()
    print(content)
print(f"Content is successfully read from updated file: {fileName}\n")

print("Done!")