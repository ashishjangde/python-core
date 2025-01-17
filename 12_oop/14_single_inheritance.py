class animal :
    def speak(self):
        print("Animal Speaking")
        
class dog(animal):
    
    def speak(self):
        print("Dog Speaking")
    
    def bark(self):
        print("Dog Barking")

d = dog()
d.bark()
d.speak()