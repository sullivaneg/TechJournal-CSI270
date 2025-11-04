from typing import Any


class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, value: Any) -> None:
        self.data.insert(0, value)

    def dequeue(self) -> Any:
        return self.data.pop()

    def peek(self) -> Any:
        if not self.is_empty():
            return self.data[-1]
        return

queue = Queue()

print("Is the queue empty?",queue.is_empty())  # True
print("What is in the queue?",queue.peek())  # None

# Add items, enqueue adds an element to the beginning of the queue
queue.enqueue(34)
queue.enqueue(25)
queue.enqueue(3)
queue.enqueue(23)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(5)
queue.enqueue(6)

print(queue.is_empty())  #Checks to see if the queue is empty: False
print("What is in there?",queue.peek())  # 34

# Remove item
first_item = queue.dequeue() #The dequeue removes an element from the front of the
print("The first item in the queue is",first_item)  # 34

# Check the remaining items
for item in queue.data:  # 3 25
    print("Items in the queue are:",item)

print("Here is the queue:",queue.data)