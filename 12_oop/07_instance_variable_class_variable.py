class hello :
    name = "Ashish"  # Class variable
    
    def __init__(self, age) :
        self.age = age # Instance variable
        
    def print_hello(self) :
        print("Hello my name is", self.name , "and I am", self.age, "years old")
        
    @classmethod  # Class method for changing the class variable
    def change_name(clx, name) :
        clx.name = name


h1 = hello(25)
h1.print_hello()
h1.change_name("Ashish Kumar")
h1.print_hello()
print(hello.name)