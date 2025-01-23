integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")

print(f"The type of the integer is: {type(integer_input)}")
print(f"The type of the float is: {type(float_input)}")
print(f"The type of the string is: {type(string_input)}")

string_value = input("Enter a string representing a number: ")
integer_value = int(string_value)
float_value = float(integer_value)

print(f"String to integer: {integer_value}")
print(f"Integer to float: {float_value}")

personal_details = {
    "name": "John",
    "age": 25
}

print(f"Name: {personal_details['name']}")
print(f"Age: {personal_details['age']}")

my_set = {1, 2, 3}

my_set.add(4)
print(f"Set after adding 4: {my_set}")

my_set.remove(2)
print(f"Set after removing 2: {my_set}")

is_member = 3 in my_set
print(f"Is 3 in the set? {is_member}")
