x = 1

def change_x():
    global x  # This declares x as a global variable
    print(f"x before change: {x}")
    x = 2
    y = 3  # This is a local variable
    print(f"x after change: {x}")

change_x()

print(x)  # This will print 2 because x has been changed globally
# print(y)  # This will give an error because y is a local variable and is not accessible outside the function
