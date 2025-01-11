tup = ("apple", "banana", "cherry")
print(tup)  # ('apple', 'banana', 'cherry')

# Accessing Items
# You access the list items by referring to the index number:
# Note: The first item has index 0.
print(tup[0])  # apple
print(tup[1])  # banana
print(tup[2])  # cherry

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(tup[-1])  # cherry
print(tup[-2])  # banana
print(tup[-3])  # apple

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
print(tup[1:3])  # ('banana', 'cherry')

# Note: The search will start at index 1 (included) and end at index 3 (not included).

# By leaving out the start value, the range will start at the first item:
print(tup[:2])  # ('apple', 'banana')

# By leaving out the end value, the range will go on to the end of the list:
print(tup[1:])  # ('banana', 'cherry')

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

print(tup[-3:-1])  # ('apple', 'banana')

# Change Item Value
# To change the value of a specific item, refer to the index number:
# tup[1] = "blackcurrant"  # TypeError: 'tuple' object does not support item assignment
# print(tup)  # ('apple', 'blackcurrant', 'cherry')

# Loop Through a List
# You can loop through the list items by using a for loop:
for fruit in tup:
    print(fruit)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in tup:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")
    
# List Length
# To determine how many items a list has, use the len() function:
print(len(tup))  # 3
# Note: Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Example
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"

x = tuple(y)

print(x)  # ('apple', 'kiwi', 'cherry')
# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# Example
# You cannot add items to a tuple:
# x = ("apple", "banana", "cherry")
# x[3] = "orange"  # TypeError: 'tuple' object does not support item assignment
# print(x)
# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# Example
# The del keyword can delete the tuple completely:
x = ("apple", "banana", "cherry")
del x
# print(x)  # NameError: name 'x' is not defined
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Example
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)  # ('apple', 'banana', 'cherry')

# Tuple Methods
# Python has two built-in methods that you can use on tuples.
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
# count()    Method 
# Returns the number of times a specified value occurs in a tuple
# Example
# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)


#adding a new item to the tuple
thistuple = thistuple + (9,)
print(thistuple)  # (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 9)

#deleting a tuple
del thistuple
# print(thistuple)  # NameError: name 'thistuple' is not defined

#count() method
#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  # 2