#3. Exception Handling Using try and except
while True:
    try:
        x = int(input("Enter a number: "))
        print(x)
    except ValueError:
        print("Please enter a valid INT.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

#4. Handling Multiple Exceptions
while True:
    try:
        x = int(input("Enter a number: "))
        print(10 / x)
    except (ValueError, ZeroDivisionError):
        print("Error: Invalid input")

#5. Using else in Exception Handling
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please, enter a valid INT")
else:
    print(result)

#6. Using finally
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file.")
    file.close()

#7. Raising Exceptions
def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(100, 100)
except Exception as e:
    print("Error:", e)
else:
    print("Withdraw successful!")

import math


#8. Custom Exceptions
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return math.sqrt(number)

try:
    result = square_root(25)
except NegativeNumberError as e:
    print("Error:", e)
else:
    print("Result:", result)