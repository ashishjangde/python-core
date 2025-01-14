l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cube = lambda x: x ** 3

# Using map() function
cubes = list(map(cube, l))
print(cubes)



# Using filter() function
is_grater_than_5 = lambda x: x > 5
filtered = list(filter(is_grater_than_5, l))
print(filtered)

# Using reduce() function
from functools import reduce

add = lambda x, y: x + y

sum = list(reduce(add, l))

print(sum)