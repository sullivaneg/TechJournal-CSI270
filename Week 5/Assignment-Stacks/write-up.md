# Overview
The goal is to create a simulation of Hot Potato. From the assignment description "Assume that the child holding the 
potato will be at the front of the queue. Upon passing the potato, the simulation will simply dequeue and then
immediately enqueue that child, putting her at the end of the line. She will then wait until all the others have been 
at the front before it will be her turn again. After num dequeue/enqueue operations, the child at the front will be 
removed permanently and another cycle will begin. This process will continue until only one name remains (the size of
the queue is 1)." The program achieves this goal by using a double ended queue (deque) data structure.

# Algorithm
The program begins by outlining a Deque class. This class acts as a double-ended queue and has functions defined for 
removing a player at the front of the queue and a function for adding them to the rear. The class stores the contents 
of the queue in self.data. Since this program doesn't require adding a player to the front or taking one from the back,
the remove_rear, add_front and is_empty functions were not included.

> ### Methods
> * **add_rear(value)** -> Adds an item, in this case a name, to the back of the queue by inserting the value into index\[0].
> * **remove_front(value)** -> Removes the name from the front of the queue and returns that name by popping the value.

Then the main hot_potato function was created. This was not a class method, but the main function for the program. It
took a list of names of the players and an integer "num" as its parameters. To start the hot potato function: 
> 1. Initializes Deque
> 2. Adds players name to the queue by iterating through the list of names. 

Then a while loop is created that runs until one player remains. This while loop has a nested for loop that iterates
for i in num. Each round has two main functions that exist in each of those loops. 

### Passing the Potato - In for loop
The potato gets passed num times. This is done by removing the player at the front of the queue and immediately adding 
them to the back. This simulates the player getting the potato and passing it since our queue is basically the amount 
of players between any player and the ball. If a player is at the front of the queue they have the ball and how far they
are from the front is how many people are between them and the ball. 

### Eliminating a Player - In while loop
Once the potato has been passed n times, the player at the front of the deque is removed permanently.

The while loop stops when one player remains (the length of self.data is 1) and that player is crowned the victor.

## Testing
The program was run with print debug statements placed throughout the program (that are currently commented out) to act
as commentary for the game. A test case with 9 players and a num of 3 was run. The output of the debugging statements 
showed this: 

```
Starting Players
['dawn', 'steve', 'sandy', 'casper', 'julia', 'laura', 'rune', 'luc', 'emma']

Round  1
emma moves to the back
line now ['emma', 'dawn', 'steve', 'sandy', 'casper', 'julia', 'laura', 'rune', 'luc']
luc moves to the back
line now ['luc', 'emma', 'dawn', 'steve', 'sandy', 'casper', 'julia', 'laura', 'rune']
rune moves to the back
line now ['rune', 'luc', 'emma', 'dawn', 'steve', 'sandy', 'casper', 'julia', 'laura']
laura is out
Remaining players ['rune', 'luc', 'emma', 'dawn', 'steve', 'sandy', 'casper', 'julia']

Round  2
julia moves to the back
line now ['julia', 'rune', 'luc', 'emma', 'dawn', 'steve', 'sandy', 'casper']
casper moves to the back
line now ['casper', 'julia', 'rune', 'luc', 'emma', 'dawn', 'steve', 'sandy']
sandy moves to the back
line now ['sandy', 'casper', 'julia', 'rune', 'luc', 'emma', 'dawn', 'steve']
steve is out
Remaining players ['sandy', 'casper', 'julia', 'rune', 'luc', 'emma', 'dawn']

Round  3
dawn moves to the back
line now ['dawn', 'sandy', 'casper', 'julia', 'rune', 'luc', 'emma']
emma moves to the back
line now ['emma', 'dawn', 'sandy', 'casper', 'julia', 'rune', 'luc']
luc moves to the back
line now ['luc', 'emma', 'dawn', 'sandy', 'casper', 'julia', 'rune']
rune is out
Remaining players ['luc', 'emma', 'dawn', 'sandy', 'casper', 'julia']

Round  4
julia moves to the back
line now ['julia', 'luc', 'emma', 'dawn', 'sandy', 'casper']
casper moves to the back
line now ['casper', 'julia', 'luc', 'emma', 'dawn', 'sandy']
sandy moves to the back
line now ['sandy', 'casper', 'julia', 'luc', 'emma', 'dawn']
dawn is out
Remaining players ['sandy', 'casper', 'julia', 'luc', 'emma']

Round  5
emma moves to the back
line now ['emma', 'sandy', 'casper', 'julia', 'luc']
luc moves to the back
line now ['luc', 'emma', 'sandy', 'casper', 'julia']
julia moves to the back
line now ['julia', 'luc', 'emma', 'sandy', 'casper']
casper is out
Remaining players ['julia', 'luc', 'emma', 'sandy']

Round  6
sandy moves to the back
line now ['sandy', 'julia', 'luc', 'emma']
emma moves to the back
line now ['emma', 'sandy', 'julia', 'luc']
luc moves to the back
line now ['luc', 'emma', 'sandy', 'julia']
julia is out
Remaining players ['luc', 'emma', 'sandy']

Round  7
sandy moves to the back
line now ['sandy', 'luc', 'emma']
emma moves to the back
line now ['emma', 'sandy', 'luc']
luc moves to the back
line now ['luc', 'emma', 'sandy']
sandy is out
Remaining players ['luc', 'emma']

Round  8
emma moves to the back
line now ['emma', 'luc']
luc moves to the back
line now ['luc', 'emma']
emma moves to the back
line now ['emma', 'luc']
luc is out
Remaining players ['emma']
The winner is emma

```



