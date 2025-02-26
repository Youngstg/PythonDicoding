class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @staticmethod
    def greet():
        print("Hello! Welcome to the OOP example.")

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Calling methods
person1.display_info()
Person.greet()