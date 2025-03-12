#1.Defining a Function
def greeting():
    print("Welcome to Python!")
greeting()

#2. Function Parameters
def greeting(name):
    print("Hello " + name + "!")
greeting("Jimmy")
greeting("Michael")


#3. Default Parameters
def greeting(name = "Guest"):
    print(f"Hello, {name}!")

greeting()
greeting("Adilet")

#4. Returning Values
def add(num1 = 0, num2 = 0):
    return num1 + num2

print(add())

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(add(a, b))

#5. Multiple Return Values
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter

area, perimeter = rectangle_properties(10, 20)
print(f"Area: {area} and Perimeter: {perimeter}")

#6. Variable-Length Arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5, 6))

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Adilet", age="20", location="Bishkek")

#7. Lambda Functions
square = lambda x: x * x
print(square(5))

square_of_square = lambda x: square(x) * square(x)
print(square_of_square(5))

#8. Scope of Variables
def local_scope():
    x = 5
    print(x)
local_scope()
# print(x), we cannot do that because x is local scope of function, and not accessible outside

x = 5
def modify_global():
    global x
    x += 15

modify_global()
print(x)

#9. Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))

#10. Docstrings
def multiply(a, b):
    """This function returns the product of two numbers!"""
    return a * b

print(multiply.__doc__)
print(multiply(2,3))



