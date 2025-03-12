#Creating a Class and Object in Python
#Example 1: Defining a Simple Class and Creating an Object
class FootballPlayers:
    def __init__(self, club, name, year):
        self.club = club
        self.name = name
        self.year = year

        def display(self):
            return f"{self.club} {self.name} ({self.year})"

footballPlayers = [  FootballPlayers("Inter Miami", "Messi", 37),
                FootballPlayers("Lamine", "Barcelona", 17) ]

for footballPlayers in footballPlayers:
    footballPlayers.display()

#Methods in Classes
class Dinosaur:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def scream(self):
        print(f"The {self.name} says rawr rawr!!!")

    def displayKind(self):
        print(f"The type of {self.name} is: {self.color}")

cat1 = Dinosaur("Brian", "black")
cat1.scream()
cat1.displayKind()

#Modifying Object Attributes
class Phone:
    def __init__(self, brand, price, currency):
        self.brand = brand
        self.price = int(price)
        self.currency = currency

    def display(self):
        print(f"The brand of the phone is {self.brand} and the price is {self.price} in {self.currency}.")

phones = [
        Phone("samsung", 1000, "dollar"),
        Phone("iphone", 87000, "som")
    ]

for phone in phones:
    phone.display()
    print()

#2
class Employee:
    companyName = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alex", 20000)
e2 = Employee("Bob", 30000)

print(e1.companyName)
print(e2.companyName)

Employee.companyName = "HighTechCorp"

print(e1.companyName)
print(e2.companyName)

#Using the self Keyword
class Calculator:
    def __init__(self, a):
        self.a = a

    def add(self, b):
        self.a += b

    def getValue(self):
        return self.a

calc = Calculator(5)
print(calc.getValue())
calc.add(7)
print(calc.getValue())


#Deleting Object Attributes or Objects
#Example 6: Deleting Attributes and Object
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("John", "<PASSWORD>")
print(user1.username)

del user1.username
# print(user1.username) cannot be done as attributes is deleted.
del user1
# user1 object is deleted.


#Real-World Example: User Authentication System
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        return password == self.__password

users = [
    User("Adi", "2004"),
    User("Fara", "gachi"),
    User("Mura", "boom")
]

username = input("Enter username: ")
password = input("Enter password: ")

for user in users:
    if user.username == username and user.login(password):
        print("Login successful!")
        break
else:
    print("Incorrect username or password!")

