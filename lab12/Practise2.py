#advanced OOP
#1 Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = int(balance)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.__owner}. New balance: {self.__balance}.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} from {self.__owner}. Remaining balance: {self.__balance}.")
        else:
            print("Insufficient balance")

    def getBalance(self):
        return self.__balance
    def getOwner(self):
        return self.__owner

account = BankAccount("Adilet", 250000)
account.deposit(5000)
account.withdraw(3000)

print(account.getBalance())


#Inheritance
class FootballPlayer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("")

class AcademyPlayer(FootballPlayer):
    def __init__(self, name, age, academy):
        super().__init__(name, age)
        self.academy = academy

    def displayInfo(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am playing in {self.academy}.")

class Coach(FootballPlayer):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def displayInfo(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I have {self.experience} years of experience.")

people = [
            AcademyPlayer("Lamine", 17, "Barca"),
            Coach("Xavi", 43, 2),
            AcademyPlayer("Cubarsi", 17, "Barca"),
            Coach("Flick", 60, 25)
        ]

for p in people:
    p.displayInfo()


#Polymorphism
class Bird(object):
    @staticmethod
    def fly():
        print("Bird fly")

class Airplane(Bird):
    @staticmethod
    def fly():
        print("Airplane fly")

class Fish(Bird):
     @staticmethod
     def fly():
        print("Fish fly")

for obj in (Airplane, Bird, Fish):
    obj.fly()


#Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass

class Car(Vehicle):
    def startEngine(self):
        print("Car is starting...")

class Motorcycle(Vehicle):
    def startEngine(self):
        print("Motorcycle is starting...")

car = Car()
motorcycle = Motorcycle()

car.startEngine()
motorcycle.startEngine()


#Method Overriding
class Father:
    @staticmethod
    def hello():
        print("Hello, Papa")

class Mother:
    @staticmethod
    def hello():
        print("Hello, Mama")

class Child(Father, Mother):
    @staticmethod
    def hello():
        print("Hello, Child")

print(Father.hello())
print(Mother.hello())
print(Child.hello())


#Multiple Inheritance
class A:
    @staticmethod
    def method_a():
        print("Method A")

class B:
    @staticmethod
    def method_b():
        print("Method B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()

#Real-World Example: OOP in a Library Management System
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def displayInfo(self):
        print(f"{self.__title} by {self.__author} ({self.__year}).")

class Library:
    def __init__(self):
        self.__books = []

    def addBook(self, book):
        self.__books.append(book)

    def listBooks(self):
        for book in self.__books:
            book.displayInfo()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To kill a Mockingbird", "Harper Lee", 1960)

library = Library()
library.addBook(book1)
library.addBook(book2)

library.listBooks()



