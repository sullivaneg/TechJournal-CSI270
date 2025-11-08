#Author: Emma Sullivan
# Class: CSI-270-01
# Certification of Authenticity:/3r45e30
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).

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

