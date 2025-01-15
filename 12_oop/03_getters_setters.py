class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, name):
        self._name = name
        
a1 = Animal("Dog")
print(a1.get_name)
a1.set_name = "Cat"
print(a1.get_name)