#implement queue using linklist
# wmt_stock_price_queue = []
# wmt_stock_price_queue.insert(0,132.22)
# wmt_stock_price_queue.insert(0,133.22)
# wmt_stock_price_queue.insert(0,134.22)
# print(wmt_stock_price_queue)

# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())

#implement queue using collection.deque
# from collections import deque
# queue = deque()
# queue.appendleft(132.22)
# queue.appendleft(133.22)
# queue.appendleft(134.22)
# print(queue)
# print(queue.pop())
# print(queue)
# print(queue.pop())
# print(queue)
# print(queue.pop())
# print(queue)
# print(queue.pop())

#using proper queue class
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        return self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)


if __name__=='__main__':
    pq = Queue()
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })
    print(pq.size())
    print(pq.dequeue())
    print(pq.queue)