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

    #This was added to the original code to support the printer class code
    def size(self):
        return len(self.data)

class Deque:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def add_front(self, value: Any) -> None:
        self.data.append(value)

    def add_rear(self, value: Any) -> None:
        self.data.insert(0, value)

    def remove_front(self) -> Any:
        return self.data.pop()

    def remove_rear(self) -> Any:
        return self.data.pop(0)

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def push(self, value: Any) -> None:
        self.data.append(value)

    def pop(self) -> Any:
        return self.data.pop()

