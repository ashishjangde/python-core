#raise keyword in py
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
#example
# raise ValueError("Invalid input")
#output
# ValueError: Invalid input
#example
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
#output
# Exception: Sorry, no numbers below zero