class Mamals:
    def __init__(self, legs=4):
        self.__legs = legs # Private variable with double underscore prefix # with single _ it is protected variable and without any underscore it is public variable
        self._eyes = 2  # Protected variable with single underscore prefix extended child class can access it no one else can access it
    @property
    def get_legs(self):
        return self.__legs
    
    @get_legs.setter
    def set_legs(self, legs):
        self.__legs = legs
        
    @property
    def get_eyes(self):
        return self._eyes
    
    @get_eyes.setter
    def set_eyes(self, eyes):
        self._eyes = eyes

class Dog(Mamals):
    def __init__(self , breed , leg):
        super().__init__(leg)
        self.__breed = breed
        
    @property
    def get_breed(self):
        return self.__breed
    
    @get_breed.setter
    def set_breed(self, breed):
        self.__breed = breed


d1 = Dog("Pug", 8  )
print(d1.get_legs)