from collections import deque
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


    def front(self):
        return self.queue[-1]

if __name__=='__main__':
    queue = Queue()
    queue.enqueue("1")

    for i in range(15):
        front = queue.front()
        print("     ",front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        queue.dequeue()
