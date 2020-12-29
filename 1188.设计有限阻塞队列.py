import threading
import time
from collections import deque


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en_lock = threading.Lock()
        self.de_lock = threading.Lock()
        self.queue = deque()
        self.capacity = capacity
        self.block_event = threading.Event()
        self.block_event.set()
        self.empty_event = threading.Event()
        self.empty_event.clear()

    def enqueue(self, element: int) -> None:
        with self.en_lock:
            self.block_event.wait()
            print('=> {}'.format(element))
            self.queue.append(element)
            self.empty_event.set()
            if len(self.queue) == self.capacity:
                self.block_event.clear()

    def dequeue(self) -> int:
        with self.de_lock:
            self.empty_event.wait()
            value = self.queue.popleft()
            print('<= {}'.format(value))
            self.block_event.set()
            if len(self.queue) == 0:
                self.empty_event.clear()
            return value

    def size(self) -> int:
        return len(self.queue)


def produce(q):
    q.enqueue(1)
    time.sleep(2)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)


def consume(q):
    q.dequeue()
    q.dequeue()
    time.sleep(3)
    q.dequeue()


if __name__ == "__main__":
    q = BoundedBlockingQueue(2)
    t1 = threading.Thread(target=produce, args=(q,))
    t2 = threading.Thread(target=consume, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
