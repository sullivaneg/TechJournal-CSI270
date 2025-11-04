from typing import Any


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

# Initialize
deque = Deque()

print("Is the dequeue empty?",deque.is_empty())  # True

# Add items
deque.add_front(1)
deque.add_front(2)
deque.add_rear(5)
deque.add_rear(6)

# Print items
print("The items in the dequeue are:",[item for item in deque.data])  # [6, 5, 1, 2]

# Remove items
deque.remove_front() #Removes the 2
print([item for item in deque.data])

deque.remove_rear() #Removes the 6
print([item for item in deque.data])  # [5, 1]