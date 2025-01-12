#short hand if else
age = int(input("Enter your age: "))

print("You are eligible to vote and you are an adult" if age > 18 else "You are eligible to vote" if age == 18 else "You are not eligible to vote")
