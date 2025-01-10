def addition(a, b):
    return a + b

result = addition(2, 3)
print(result)  # Output: 5

#function with default arguments
def addition(a, b=5):
    return a + b

result = addition(2)
print(result)  # Output: 7

#function with variable number of arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

result = addition(2, 3, 4, 5)
print(result)  # Output: 14

#function with variable number of keyword arguments
def addition(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result

result = addition(a=2, b=3, c=4, d=5)
print(result)  # Output: 14

#function with variable number of arguments and keyword arguments
def addition(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        result += kwargs[key]
    return result

result = addition(2, 3, 4, 5, a=2, b=3, c=4, d=5)
print(result)  # Output: 28

