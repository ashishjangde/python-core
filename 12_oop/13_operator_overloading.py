class vector:
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z"
    
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
v1 = vector(1, 2, 3)
print(v1) # 1x + 2y + 3z
v2 = vector(4, 5, 6)
print(v2) # 4x + 5y + 6z
v3 = v1 + v2
print(v3) # 5x + 7y + 9z
print(type(v3)) # <class '__main__.vector'>

        