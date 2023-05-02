# Private storage class for creating the Linked List nodes
class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# implementation of queue using a Linked list.
class Queue:
    # creates an empty queue
    def __init__(self):
        self._qHead = None
        self._qTail = None
        self._count = 0

    # returns True if the queue is empty
    def isEmpty(self):
        return self._qHead is None
    
    # returns the number of items in the queue
    def __len__(self):
        return self._count
    
    # prints all the items by traversing the L.L from the head to the tail
    def printQueue(self):
        current = self._qHead
        while current:
            print(current.item, end=" --> " if current.next else "\n")
            current = current.next
    
    # adds the given item to the queue
    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qHead = node
        else:
            self._qTail.next = node
        
        self._qTail = node
        self._count += 1

    # removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        node = self._qHead

        if self._qHead is self._qTail:
            self._qTail = None
        self._qHead = self._qHead.next
        self._count -= 1
        return node.item
    
pizzaQueue = Queue()

pizzaQueue.enqueue('James')
pizzaQueue.enqueue('Edward')
pizzaQueue.enqueue('Alex')
pizzaQueue.enqueue('Ann')
pizzaQueue.enqueue('Barak')
pizzaQueue.enqueue('Trump')

print(f"queue: {pizzaQueue.__len__()}")

pizzaQueue.printQueue()

pizzaQueue.dequeue()
pizzaQueue.dequeue()

pizzaQueue.printQueue()
print(f"queue: {pizzaQueue.__len__()}")

# results:
# queue: 6
# James --> Edward --> Alex --> Ann --> Barak --> Trump
# Alex --> Ann --> Barak --> Trump
# queue: 4
