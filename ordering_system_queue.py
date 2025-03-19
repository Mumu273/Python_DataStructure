from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            return print("Queue is empty")
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()
def place_orders(orders):
    for order in orders:
        print("Placing order for ", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving ", order)
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']


t1 = threading.Thread(target=place_orders, args=(orders, ))
t2 = threading.Thread(target=serve_orders)

t1.start()
t2.start()



# place_orders(orders)
# serve_orders()
