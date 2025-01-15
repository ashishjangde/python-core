
def greet(fx):
    def wrapper():
        print("Hello,")
        fx()
        print("Goodbye!")
    return wrapper




@greet
def say_hello():
    print("Ashish")

# greet(say_hello)() # This is equivalent to above say_hello = greet(say_hello)
say_hello()