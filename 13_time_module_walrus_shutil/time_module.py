import time

def using_while():
    i = 0
    while i < 100000:
        print(i)
        i += 1

def using_for():
    for i in range(100000):
        print(i)
        
init1 = time.time()
using_while()
time_taken = time.time() - init1

init2 = time.time()
using_for()
print("Time taken by using_for:", time.time() - init2)
print("Time taken by using_while:", time_taken)