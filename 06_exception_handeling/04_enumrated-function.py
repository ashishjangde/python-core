
fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']

# enumerate() creates an iterator that returns pairs of (index, element)
# i: represents the index starting from 0
# fruit: represents each element in the fruits list
for i, fruit in enumerate(fruits):
    print(i, fruit)  # prints index followed by the fruit name