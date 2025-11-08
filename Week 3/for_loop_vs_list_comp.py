import timeit

def for_loop(n):
    nums = []
    for i in range(n+1):
        nums.append(i)
    return nums

def list_comp(n):
    nums = [i for i in range(n+1)]
    return nums


print(timeit.timeit('for_loop(1000)', globals=globals()))
print(timeit.timeit('list_comp(1000)', globals=globals()))

