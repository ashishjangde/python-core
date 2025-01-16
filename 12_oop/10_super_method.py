class human :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def show(self) :
        print(f"Name: {self.name}\nAge: {self.age}")
        
class person(human) :
    def __init__(self, name, age, salary) :
        super().__init__(name, age)
        self.salary = salary

    def show(self) :
        super().show()
        print(f"Salary: {self.salary}")

p1 = person("Ashish", 25, 10000)
p1.show()