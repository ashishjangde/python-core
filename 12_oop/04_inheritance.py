class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed


d1 = Dog("Tommy", "Pug")

print(d1.name)
print(d1.breed)