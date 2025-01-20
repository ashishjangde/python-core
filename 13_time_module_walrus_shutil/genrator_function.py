def genrator_function():
    for i in range(10):
        yield i

gen = genrator_function()
# print(next(gen))
# print(next(gen))
# for i in gen:
#     print(i)

"""
what is generator function?
- A generator function is a function that returns an object (iterator) which we can iterate over (one value at a time).
- A generator function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return.
- If the body of a def contains yield, the function automatically becomes a generator function.
- The yield keyword pauses the function and saves the local state of the function. The state is 
remembered across successive calls.
- Once the function yields, the function is paused and the control is transferred to the caller.
"""