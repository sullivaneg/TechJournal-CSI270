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

q = Queue()
