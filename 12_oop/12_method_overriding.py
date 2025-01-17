import math

class shape:
    def __init__(self , x , y):
        self.x = x 
        self.y = y
        
    def area(self):
        return self.x * self.y
    

class circle(shape):
    def __init__(self , radius):
        super().__init__(radius, radius)
        
    def area(self):
        return math.pi * super().area()

c = circle(5)

print(c.area()) # 78.53981633974483 