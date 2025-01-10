fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    j = 0
    while j < len(fruits[i]):
        print(fruits[i][j], end=" ")
        j += 1
    print()
    i += 1