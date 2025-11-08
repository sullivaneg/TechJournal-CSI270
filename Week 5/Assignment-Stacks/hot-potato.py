#Author: Emma Sullivan
# Class: CSI-270-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).

from typing import Any

# From Class Code on Deques
class Deque:
    def __init__(self):
        self.data = []

    def add_rear(self, value: Any) -> None:
        self.data.insert(0, value)

    def remove_front(self) -> Any:
        return self.data.pop()


def hot_potato(names, num) -> Any:
    # Initialize dequeue
    deque = Deque()

    # Create the queue
    for name in names:
        deque.add_rear(name)

    #Debugging
    #print(deque.data)

    #count = 1 # for debugging -> round counter
    while len(deque.data) > 1 :
        #print("Round ", count)
        for i in range(num):
            player = deque.remove_front() # Removes and returns player at the front of the line
            #print(player, "moves to the back") # Debugging
            deque.add_rear(player) # Adds to the back of the line
            #print("line now", deque.data)
        deque.remove_front()
        #player1 = deque.remove_front() # debugging (player1)
        #print(player1, "is out") #debugging
        #print("Remaining players", deque.data) #debugging
        #count += 1

    print("The winner is", deque.data[0])

#TEST
names = ["emma", "luc", "rune", "laura", "julia", "casper", "sandy", "steve", "dawn"]
hot_potato(names, 3)
