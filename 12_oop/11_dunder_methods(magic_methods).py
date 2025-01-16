class mamals :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) :
        print( f"Name: {self.name}\nAge: {self.age}")

m1 = mamals("Ashish", 25)

m1.__str__()