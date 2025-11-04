#from ./stacks_queues_deques/stacks.py import Stack
from stacks import Stack
'''
Initial stack

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(12)
stack.push(2) Gets deleted from the stack
stack.push(34)
stack.push(True)
stack.push('A')
stack.push(3.2)
'''

'''
Revised stack

stack.push('A')
stack.push(True)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(12)
stack.push(34)
stack.push(3.2)
'''
stack = Stack() #Initializes the class

#Process below builds the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(12)
stack.push(2)
stack.push(34)
stack.push(True)
stack.push('A')
stack.push(3.2)

print("The complete original stack:",stack.data)

#This copies the stack to a list. The result is a nested list which
#must be cleaned up into a simple list
temp = []
temp.append(stack.data)
stored = []

#The loop below removes the data from a nested (two-dimensional) list to a simple list named 'stored'
for i in temp:
    for j in i:
        stored.append(j)

print("The temp list is:",temp)
print("The stored list is:",stored)

#temp.remove(2) #Removes this redundant element
'''
Remapping the elements in the list will be very useful here.
It will allow us to reorder the list so that the elements
will be added to the final stack in the order we want.
'''
order = [7, 6, 0, 1, 2, 3, 5, 8, 4] #For all elements in the list, these are new index positions

result = [stored[i] for i in order]

result.pop() #Knocks out the redundant '2'

print("This is the result:",result)

#Now it is time to clean out the original stack and restack the data
#Sometimes you want to preserve the original stack and just create a new,
#properly ordered new stack

while (not stack.data == []):
    stack.pop()

for item in result:
    stack.push(item)

print("The final stack is:",stack.data)