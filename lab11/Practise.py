#Python Data Structures
# 1. Lists

fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits.append("orange")
fruits.remove("cherry")

for fruit in fruits:
    print(fruit, end=" ")
print()

#2. Dictionaries
students = {
    "name": "John",
    "age": 22,
    "grade": "A"
}

print(students["age"])  # print the value based on a key

for key, value in students.items():
    print(f"{key} = {value}")

print()

students.update({"name": "Bob"})
students.update({"grade": "C-"})

for key, value in students.items():
    print(f"{key} = {value}")

#3. Sets
numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers.add(6)
print(numbers)

numbers.remove(3)
print(numbers)

evens = [2, 4, 6, 8]
print(numbers.intersection(evens))

#4. Tuples
points = (10, 20)
print(points[1])

for point in points:
    print(point, end=" ")

print()