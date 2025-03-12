#1. Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easier.")

#2. Reading from a File
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#3. Reading Files Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

#4. Appending Data to a File
with open("example.txt", "a") as file:
    file.write("\nThis is a later-added piece!")

#5. Checking if a File Exists Before Writing
try:
    with open("example.txt", "x") as file:
        file.write("This is a new file")
except FileExistsError:
    print("File already exists!")

#Processing Text Files
with open("dtat.txt", "w") as file:
    for line in file:
        print (f"Processed line: {line.strip()}")

# Processing CSV Files
# CSV (Comma-Separated Values) files store tabular data and are widely used for exchanging structured data.
# Python’s built-in csv module helps read and write CSV files efficiently.
# 1. Writing Data to a CSV File
import csv
data = [
    ["Name", "Age", "Country"],
    ["Lebron", "37", "United States of America"],
    ["Mikhail", "40", "Russia"],
    ["Farzon", "25", "Tajikistan"],
    ["Thomas", "55", "Germany"]
]

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


#2. Reading Data from a CSV File
import csv

with open("data.csv", "r",newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# 3. Reading CSV Files with Column Headers
import csv

with open("data.csv", "r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and from {row['Country']}.")

#4. Appending Data to a CSV File
import csv

newData = [
    ["David", "35", "Spain"],
    ["Ali", "28", "United Arab Emirates"],
]

with open("data.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(newData)