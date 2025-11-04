from queue_class import Queue
q = Queue()
myList = [1, 2, 3, 13, 11, 9, 4, 5, 6, 10, 8, 7]
save_tup = () #Tuple, it is immutable
save_tup = tuple(myList)

#print(save_tup)

'''
Create a program that will preserve the queue and then reverse the order of the data.
After this, order the queue by even numbers first, followed by odd numbers in proper
numeric order. The result is: [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11, 13]

Now insert the number 12 after the number 10 and before the number 1
'''

#myList.reverse()
#print(myList)

def build_q():
    for i in myList:
        q.enqueue(i)
        #print(q.data)

build_q()
print(q.data)
'''
for i in myList:
    q.enqueue(i)
    print(q.data)
'''

#y = q.dequeue()
#print(y)

'''
q.enqueue(456)
print(q.data)
'''
print(q.peek()) #Shows the first element in the queue

#Process to make the queue data accessible to list manipulation
new_list = []
new_list = q.data
print(new_list)

#Create two lists, one for odd and one for even numbers
odd_list = []
even_list = []

#Function to move numbers into their proper list
def arrange_list():
    for i in new_list:
        if(i%2 >0):
            odd_list.append(i)
        else:
            even_list.append(i)
arrange_list()

#Sort the lists into numerical order
odd_list.sort()
even_list.sort()

#Insert the '12' into even_list
even_list.append(12)
print(even_list)

print("The odd list:",odd_list)
print("The even list:",even_list)

#Joint the two lists into one list that is ready for
#conversion in to a queue
myList2 = even_list + odd_list
print(myList2)

q.data = myList2
'''
def new_q():
    for j in myList2:
        q.enqueue(j)
new_q()
'''
print("The new queue:",q.data)
print(q.peek())