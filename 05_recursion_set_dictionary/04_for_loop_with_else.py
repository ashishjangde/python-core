#for loop with else 
# A for loop can have an optional else block as well.
# The else part is executed if the items in the sequence used in for loop exhausts.
# The break keyword can be used to stop the execution of the loop.
# In such cases, the else part is ignored.
# Hence, a for loop's else part runs if no break occurs.
# Here is an example to illustrate this.
# Example 1: for loop with else
# In this example, the else part is executed if no break occurs.

for i in range(10):
    print(i)
else:
    print("No break")  # no break is executed so the else part is executed because the loop is exhausted

# Output
# 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9 , No break

# Example 2: for loop with break
# In this example, the else part is not executed because the loop is broken.

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("No break")

# Output
# 0, 1, 2, 3, 4, 5

