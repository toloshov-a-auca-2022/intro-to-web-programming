# Custom and other errors
class NegativeNumber(Exception):
    def __init__(self, message="Index cannot be negative."):
        self.message = message
        super().__init__(self.message)

try:
    lst = [1, 2, 3]
    x = int(input("Enter a index to get the number: "))
    if x < 0:
        raise NegativeNumber()
    print(lst[x])
except NegativeNumber as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print(f"There is no such index as {x}.")

print()

# Type Error
try:
    print("25" + 15)
except TypeError:
    print("Type error has occurred.")

print()

# Key Error
try:
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict["a"])
except KeyError:
    print("KeyError has occurred.")