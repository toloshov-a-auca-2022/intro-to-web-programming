#1
import time

fileName = "data.txt"
content = ("Good morning, programmers! "
         "Welcome to learning new Programming Language.")

with open(fileName, "w") as file:
    file.write(content)
print(f"Content is successfully written to: {fileName}\n")

with open(fileName, "r") as file:
    content = file.readlines()
    print(content)

print(f"Content is successfully read from: {fileName}")

#2
import csv, time

fileName = "info.csv"
data = [
    ["Name", "Age", "City"],
    ["Fara", "20", "Tashkent"],
    ["Adilet", "20", "Jalal-Abad"],
    ["Aziret", "19", "Talas"],
]


with open(fileName, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Content is successfully written to: {fileName}\n")

print(f"Content is reading from the file: {fileName}")
with open(fileName, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


#3
import time

fileName = "data.txt"
appendText = "\nPythong programming language."

with open(fileName, "a") as file:
    file.write(appendText)
print(f"Additional content is successfully written to: {fileName}\n")

with open(fileName, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

print(f"Content is successfully read from: {fileName}")
