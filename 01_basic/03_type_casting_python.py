a = "1"
b = "2"
print(a + b)  # Output: 12
print(int(a) + int(b))  # Output: 3  // type casting

# implicit type casting
a = 1
b = 2.5
c = a + b
print(c , type(c))  # Output: 3.5


# explicit type casting
a = 1
b = "2"
c = a + int(b)

print(c , type(c))  # Output: 3