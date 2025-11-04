from typing import Any


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

stack = Stack()

print(stack.is_empty())  # True

# Add items
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())  # False

# Remove item
last_item = stack.pop()
print("The last item in the stack is ",last_item,".")  # 3

# Check the remaining items
for item in stack.data:  # 1 2
    print("The remaining items in the stack are ",item)