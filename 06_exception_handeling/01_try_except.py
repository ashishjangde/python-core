try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("This block of code will always execute")