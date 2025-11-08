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

    def peek(self) -> Any:
        return self.data[-1]

    def size(self) -> int:
        return len(self.data)

# stack = Stack()
#
# print(stack.is_empty())  # True
#
# # Add items
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print(stack.is_empty())  # False
#
# # Remove item
# last_item = stack.pop()
# print("The last item in the stack is ",last_item,".")  # 3
#
# # Check the remaining items
# for item in stack.data:  # 1 2
#     print("The remaining items in the stack are ",item)
#
#
# print("\n__________________Emma's Stack Test__________________\n")
# print("Log: Creating stack")
# stack2 = Stack()
# print("Log: Stack is empty:", stack2.is_empty(), "\n")
# print("Log: Adding elements")
# print("Log: Adding Red")
# stack2.push("red")
# print("Log: Adding Orange")
# stack2.push("orange")
# print("Log: Adding Yellow")
# stack2.push("yellow")
# print("Log: Adding Green")
# stack2.push("green")
# print("Log: Adding Blue")
# stack2.push("blue")
# print("Log: Adding Purple\n")
# stack2.push("purple")
# print("Log: Size of stack is:", stack2.size(), "\n")
#
# print("Log: Peeking and Popping elements")
# print("Log: Removing... ", stack2.peek())
# stack2.pop()
# print("Log: Purple popped from the stack")
# print("Log: Removing...", stack2.peek())
# stack2.pop()
# print("Log: Blue popped from the stack")
# print("Log: Removing...", stack2.peek())
# stack2.pop()
# print("Log: Green popped from the stack")
# print("Log: Removing...", stack2.peek())
# stack2.pop()
# print("Log: Yellow popped from the stack")
# print("Log: Removing...", stack2.peek())
# stack2.pop()
# print("Log: Orange popped from the stack")
# print("Log: Removing...", stack2.peek())
# stack2.pop()
# print("Log: Red popped from the stack")
#
#
#
# print("----")
# s=Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())