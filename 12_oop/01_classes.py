class Person:
    def __init__(self, name: str, age: int) :   # Constructor 
        self.__name = name  # Private variable with double underscore prefix # with single _ it is protected variable and without any underscore it is public variable
        self.__age = age
    
    def display(self) :
        print(f"Name: {self.__name}, Age: {self.__age}")

p1 = Person("Ashish", 25)
p1.display()

