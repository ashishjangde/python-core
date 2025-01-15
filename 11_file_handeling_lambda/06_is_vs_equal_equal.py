a = 2
b = "2"

print("a == b:", a == b)
print("a is b:", a is b)

a = 2
b = 2
print("a == b:", a == b)
print("a is b:", a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print("a == b:", a == b)
print("a is b:", a is b)  # False because a and b are two different objects

a = [1, 2, 3]
b = a
print("a == b:", a == b)
print("a is b:", a is b)

a = [1, 2, 3]
b = a[:]
print("a == b:", a == b)
print("a is b:", a is b)  # False because a and b are two different objects

a = "Ashish"
b = "Ashish"
print("a == b:", a == b)
print("a is b:", a is b)
