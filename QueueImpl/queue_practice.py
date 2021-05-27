"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue.
            This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order.
            All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.
"""
from collections import deque
import threading
import time
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        return self.queue.appendleft(val)

    def dequeue(self):
        if len(self.queue) == 0:
            print("QueueImpl is empty")
            return
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

food_order_queue = Queue()

def place_order(val):
    for order in val:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)
    return

def serve_order():
    time.sleep(1)
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        print("now serving :", order)
        time.sleep(2)

if __name__ == '__main__':
    queue = Queue()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()