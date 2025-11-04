import random

def new_list():
    rand_int = [random.randint(1,100) for i in range(100)] #List comprehension
    unsort_list = rand_int
    print(unsort_list)

    sort_list = unsort_list
    sort_list.sort()
    print(sort_list)
new_list()