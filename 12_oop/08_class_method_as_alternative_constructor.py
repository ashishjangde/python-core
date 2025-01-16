class names :
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_list(cls, string):
        string = string.split("-")
        return cls(string[0] , int(string[1])) # This is an alternative constructor


n1 = names("Ashish", 10000)
print(n1.name)
print(n1.salary)

stri = "Ashish-10000"
n2 = names.from_list(stri)
print(n2.name)
print(n2.salary + 2000)