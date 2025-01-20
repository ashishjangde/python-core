import threading;
import time

'''
what is multithreading?
- Multithreading is a process of executing multiple threads simultaneously.
- It is a lightweight sub-process, the smallest unit of processing.
- Threads are independent, they share the same data space.
- Threads are used to perform multiple tasks at a time.
- Threads are used to perform long-running tasks without affecting the performance of the application.
- Threads are used to perform tasks in the background.
- Threads are used to perform tasks asynchronously.

'''
def print_numbers():
    for i in range(1, 11000):
        print(i)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)
t3 = threading.Thread(target=print_numbers)

time_start = time.perf_counter()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
# print_numbers()
# print_numbers()
# print_numbers()

time_end = time.perf_counter()
print(f"Time taken: {time_end - time_start} seconds")