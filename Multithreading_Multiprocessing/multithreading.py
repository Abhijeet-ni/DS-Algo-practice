# from threading import Thread
# import threading
# def cube(x):
#     print("Cube: " , x*x*x)
#
# if __name__=='__main__':
#     for i in range(10):
#         th = Thread(target=cube, args=(i, ))
#
#         th.start()
#
#         print("Current Threads: %i." % threading.active_count())


import time
import threading
from threading import Thread

#python have global interpreter lock

def sleepMe(i):
    print(f"Thread {i} will sleep.")
    time.sleep(5)
    print("Thread %i is awake" % i)


for i in range(10):
    th = Thread(target=sleepMe, args=(i,))
    th.start()
    th.join()
    print("Current Threads: %i." % threading.active_count())