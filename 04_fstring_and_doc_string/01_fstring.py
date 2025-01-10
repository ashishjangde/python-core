str="hello my name is {} adn i am {} years old"
name="sachin"
age=22
print(str.format(name,age))  # hello my name is sachin adn i am 22 years old

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example
# Use the format() method to insert numbers into strings:
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))  # I have a Ford, it is a Mustang.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example
# Use numbers to refer to the position of the arguments:
myorder = "I have a {0}, it is a {1}."
print(myorder.format("Ford", "Mustang"))  # I have a Ford, it is a Mustang.

# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values myorder.format(carname="Ford", model="Mustang"):


name="Ashish"
age=22
str = f"hello my name is {name} and i am {age} years old"
print(str)  # hello my name is Ashish and i am 22 years old