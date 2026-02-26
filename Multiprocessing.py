
from multiprocessing import Process
import time

def counter():
    for i in range(1, 6):
        print("Counter:", i)
        time.sleep(1)

def timer():
    for i in range(5, 0, -1):
        print("Timer:", i)
        time.sleep(1)

if __name__ == "__main__":
    p1 = Process(target=counter)
    p2 = Process(target=timer)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finished multiprocessing example")

