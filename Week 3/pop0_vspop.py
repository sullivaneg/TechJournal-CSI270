import random
import timeit

def pop(list):
    list_copy = list.copy()
    return list_copy.pop()

def pop_time(list):
    list_copy = list.copy()
    return list_copy

def pop0(list):
    list_copy = list.copy()
    return list_copy.pop(1)

def pop0_time(list):
    list_copy = list.copy()
    return list_copy

list1 = random.sample(range(1,1000), 30)
var_dict = {
    "list1": list1.copy(),
    "pop": pop,
    "pop_time": pop_time,
    "pop0": pop0,
    "pop0_time": pop0_time,
}

total_time = timeit.timeit('pop(list1)', globals=var_dict)
copy_time = timeit.timeit('pop_time(list1)', globals=var_dict)
pop0_time = total_time - copy_time
print(pop0_time)

total_time = timeit.timeit('pop0(list1)', globals=var_dict)
copy_time = timeit.timeit('pop0_time(list1)', globals=var_dict)
pop1_time = total_time - copy_time
print(pop1_time)
