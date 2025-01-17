class mamals :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) :
        return f"Name: {self.name}\nAge: {self.age}"
    
    def __len__(self) :
        return len(self.name)

m1 = mamals("Ashish", 25)

print(str(m1)) # Name: Ashish
print(len(m1)) # 6