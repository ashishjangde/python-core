class base_class :
    def __init__(self):
        print("Base class constructor")
    
    def say_hello(self):
        print("Hello from base class")

class derived_class(base_class):
    def __init__(self):
        print("Derived class constructor")
    def say_hello(self):
        print("Hello from derived class")

class derived_derived_class(derived_class):
    def __init__(self):
        print("Derived derived class constructor")

    def say_hello(self):
        print("Hello from derived derived class")


# Create object of derived_derived_class

obj = derived_derived_class()

obj.say_hello() 