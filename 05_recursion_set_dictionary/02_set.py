#sets in python
#sets are unordered collection of unique elements 
#sets are mutable
#sets are defined by curly braces
#sets are unordered
#sets are unintialized by using set() function

#creating a set
set1 = {"apple", "banana", "cherry"}
print(set1)  # {'banana', 'apple', 'cherry'}

#accessing items
#you cannot access items in a set by referring to an index, since sets are unordered the items has no index
#but you can loop through the set items using a for loop or ask if a specified value is present in a set using the in keyword
for x in set1:
    print(x)
    
#check if an item is present in a set
print("banana" in set1)  # True

#change items
#once a set is created you cannot change its items but you can add new items

#add items
#to add one item to a set use the add() method
set1.add("orange")
print(set1)  # {'banana', 'apple', 'cherry', 'orange'}  # Note: Sets are unordered, so the items will appear in a random order.

#to add multiple items to a set use the update() method
set1.update(["orange", "mango", "grapes"])
print(set1)  # {'orange', 'banana', 'apple', 'mango', 'grapes', 'cherry'}

#length of a set
#to determine how many items a set has use the len() method
print(len(set1))  # 6

#remove items
#to remove an item in a set use the remove() or discard() method
set1.remove("banana")
print(set1)  # {'orange', 'apple', 'mango', 'grapes', 'cherry'}

#pop() method
#the pop() method will remove the last item
#set1.pop()
#print(set1)  # {'apple', 'mango', 'grapes', 'cherry'}
#note: sets are unordered so when using the pop() method you will not know which item that gets removed

#the clear() method empties the set
#set1.clear()

#the del keyword will delete the set completely
#del set1

#the remove() method will remove the specified item

#the discard() method will remove the specified item


#note: if the item to remove does not exist remove() will raise an error while discard() will not raise an error
# set1.discard("apple")
# print(set1)  # {'orange', 'mango', 'grapes', 'cherry'}


#union and intersection of sets
#union of sets
#the union() method returns a new set with all items from both sets
set2 = {"google", "microsoft", "apple"}
set3 = set1.union(set2)
print(set3)  # {'microsoft', 'google', 'orange', 'mango', 'grapes', 'cherry'}

#intersection of sets
#the intersection() method returns a new set with items that are present in both sets
set4 = set1.intersection(set2)
print(set4)  # {'apple'}
set4.add("orange")
print(set4)  # {'apple', 'orange'}


# The difference_update() method in Python is used with sets to remove elements that are present 
# in both the original set and the specified set(s). It modifies the original set in place, rather than creating a new set1
# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Use difference_update() to remove elements in set2 from set1
set1.difference_update(set2)

print(set1)  # Output: {1, 2}

# The difference() method in Python is also used with sets, but unlike difference_update(), 
# it creates and returns a new set containing the elements that are 
# in the original set but not in the specified set(s), without modifying the original set.

# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Use difference() to create a new set with elements in set1 but not in set2
new_set = set1.difference(set2)

print(new_set)  # Output: {1, 2}
print(set1)     # Output: {1, 2, 3, 4}  # Original set remains unchanged
