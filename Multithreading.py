
import threading
import time

def counter():
    for i in range(1, 6):
        print("Counter:", i)
        time.sleep(1)

def timer():
    for i in range(5, 0, -1):
        print("Timer:", i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=counter)
t2 = threading.Thread(target=timer)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Finished multithreading example")

