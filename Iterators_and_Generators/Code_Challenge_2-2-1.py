# Write two generators. First one create an infinite source of integers (call integers()), the other one
# integer squeares (call squares()). Write a function called take that takes two arguments, a number
# n and a generator sequance name (name of the one of the above functions) and prints a list of n
# integers from that sequence.
# print take(5, squares()) # prints [1, 4, 9, 16, 25]
# Note: Please note that seq.next() has been renamed seq.__next__() in Python 3 for consistency.

# Create a generator that is an infinite source of integers
def gen():
    num = 1
    while True:
        yield num
        num += 1

integers = gen()

# Create a generator that is an infinite source of integer squares
def gen2():
    num = 1
    while True:
        yield num ** 2
        num += 1

squares = gen2()

# Write a function called take that takes two arguments, a number n and a generator sequance name (name of the one of
# the above functions) and prints a list of n integers from that sequence.

def take(n, generator):
    num_list = []
    for num in range(n):
        num_list.append(next(generator))
    return num_list

# Test case: print take(5, squares()) # prints [1, 4, 9, 16, 25]

print(take(5, squares))