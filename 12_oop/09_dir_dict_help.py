x = ["ashish", "sachin", "rahul", "sourav"]
# print(dir(x))
# print(x.__add__)

# print(help(x))  # This will print the help for the list class

class person :

    def __init__(self, name, age):
        self.name = name
        self.age = age

pers = person("Ashish", 25)
print(pers.__dict__)  # This will print the docstring of the dict class