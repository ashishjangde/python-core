fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']

# Accessing Items
# You access the list items by referring to the index number:
# Note: The first item has index 0.
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(fruits[-1])  # cherry
print(fruits[-2])  # banana
print(fruits[-3])  # apple


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
print(fruits[1:3])  # ['banana', 'cherry']

# Note: The search will start at index 1 (included) and end at index 3 (not included).

# By leaving out the start value, the range will start at the first item:
print(fruits[:2])  # ['apple', 'banana']

# By leaving out the end value, the range will go on to the end of the list:
print(fruits[1:])  # ['banana', 'cherry']

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

print(fruits[-3:-1])  # ['apple', 'banana']

# Change Item Value
# To change the value of a specific item, refer to the index number:
fruits[1] = "blackcurrant"
print(fruits)  # ['apple', 'blackcurrant', 'cherry']

# Loop Through a List
# You can loop through the list items by using a for loop:
for fruit in fruits:
    print(fruit)
    
# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

# List Length
# To determine how many items a list has, use the len() function:
print(len(fruits))  # 3
