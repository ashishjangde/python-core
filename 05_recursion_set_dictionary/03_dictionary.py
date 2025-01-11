#dictionary in python
#dictionaries are unordered collection of items
#dictionaries are mutable
#dictionaries are defined by curly braces
#dictionaries are initialized by using dict() function
#dictionaries are indexed by keys

#creating a dictionary

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict1)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#accessing items
#you can access the items of a dictionary by referring to its key name
x = dict1["model"]
print(x)  # Mustang

#there is also a method called get() that will give you the same result
x = dict1.get("model")

#change values
#you can change the value of a specific item by referring to its key name
dict1["year"] = 2018
print(dict1)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
#loop through a dictionary
#you can loop through a dictionary by using a for loop
#when looping through a dictionary the return value are the keys of the dictionary but there are methods to return the values as well
for x in dict1:
    print(x)
    
#values() method
#to return the values of a dictionary use the values() method
for x in dict1.values():
    print(x)

#items() method
#the items() method will return each item in a dictionary as tuples
for x, y in dict1.items():
    print(x, y)
    
#check if key exists
#to determine if a specified key is present in a dictionary use the in keyword
if "model" in dict1:
    print("Yes, 'model' is one of the keys in the dict1 dictionary")
else:
    print("No, 'model' is not one of the keys in the dict1 dictionary")

#dictionary length
#to determine how many items a dictionary has use the len() method
print(len(dict1))  # 3

#adding items

#adding an item to the dictionary is done by using a new index key and assigning a value to it
dict1["color"] = "red"
print(dict1)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}

#removing items
#there are several methods to remove items from a dictionary
#the pop() method will remove the item with the specified key name
dict1.pop("model")

#the popitem() method will remove the last inserted item
dict1.popitem()

#the del keyword will delete the item with the specified key name
del dict1["brand"]

#the clear() method will empty the dictionary
dict1.clear()

#the del keyword will delete the dictionary completely
del dict1

#note: you cannot copy a dictionary by simply typing dict2 = dict1, because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2