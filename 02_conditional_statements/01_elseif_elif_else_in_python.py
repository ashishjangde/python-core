number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")
    

# Nested if-else
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18 :
    print("You are teenager")   
    if age >= 60:
        print("You are a senior citizen")
    elif age < 60:
        print("You are an adult")
else:
    print("You are a senior citizen")
    