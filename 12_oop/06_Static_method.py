class Math:
    def __init__(self, a, b):
        self.__a = a  # Private variable
        self.__b = b  # Private variable

    def add(self):
        return self.__a + self.__b
    
    @staticmethod
    def addition(a, b):
        return a + b

m1 = Math(3, 4)
print(m1.add())        # Using instance method to add the private variables
print(Math.addition(5, 6))  # Using static method to add two numbers
