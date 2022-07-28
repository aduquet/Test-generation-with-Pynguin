# Queue (FIFO) data structure implementation
# lists can be used but not recommended . Use deque() built in collections class in python
from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0


def place_order(q, placed_orders):
    for order in placed_orders:
        print("Placing order for: ", order)
        q.enqueue(order)
        time.sleep(0.5)


def serve_order(q):
    if q.is_empty():
        return "Order queue is empty"
    else:
        while q.size() != 0:
            print("Order Served: ", q.dequeue())
            time.sleep(2)


if __name__ == '__main__':
    t = time.time()
    que = Queue()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    placeOrderQueue = threading.Thread(target=place_order, args=(que, orders))
    serveOrderQueue = threading.Thread(target=serve_order, args=(que,))

    placeOrderQueue.start()
    time.sleep(1)
    serveOrderQueue.start()

    placeOrderQueue.join()
    serveOrderQueue.join()

    timeTaken = time.time() - t
    print("Time taken: ", timeTaken)