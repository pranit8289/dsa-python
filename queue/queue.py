from collections import deque

# wallmart_price_queue = []

# # wallmart_price_queue.insert(0, 131.1)

# # wallmart_price_queue.insert(0, 131.2)

# # print(wallmart_price_queue)
# q = deque()

# q.appendleft(131.1)
# q.extendleft([132.1, 133.1])
# a = q.pop()
# print(a)

# print(q)


class Queue():

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        if self.buffer.__len__() >= 1:
            self.buffer.pop()
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        print(len(self.buffer))
        return 
    

queue = Queue()

queue.enqueue(10)

queue.size()