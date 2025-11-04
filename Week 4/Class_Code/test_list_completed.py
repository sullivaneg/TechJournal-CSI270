import random
import timeit

'''
The lines below generate a random list of integers and saves the result to a list,
'rand_int', which is used for a sequential list. The next step is to sort the list
for a binary search.
'''
rand_int = [random.randint(1, 100) for i in range(50)]  # List comprehension
unsort_list = rand_int

rand_int.sort()
seq_list = rand_int

print(rand_int) #Pick a repeating integer
x = int(input("Enter a number to search for in the list: "))

idx_list1 = [] #Holds index positions of the found value
#Sequential search
def seq_srch(unsort_list,x):
    count1 = 0
    for idx, val in enumerate(unsort_list):
        if(val == x):
            #print(f"Index: {idx}, Value: {val}")
            count1 += 1
            idx_list1.append(idx)
        else:
            pass

    if(count1 >0 and count1 <2):
        print("The integer was found",count1, "time.")
        print("The item was found in the following")
        for j in idx_list1:
            print("index position: ",j)
    elif (count1 >= 2):
        print("The integer was found", count1, "times.")
        print("The item was found in the following index positions:")
        for j in idx_list1:
            print(j)
    else:
        print("The integer was not found")

def bin_srch(a,b):
    low = 0
    high = len(seq_list) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if seq_list[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif seq_list[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array

#Function call for the sequential search
result1 = seq_srch(unsort_list,x)

# Function call for the binary search
result2 = bin_srch(seq_list, x)
if result2 != -1:
    print("After a binary search, the element is present at index", result2)
else:
    print("After a binary search, the element is not present in the list.")


t1 = timeit.timeit('seq_srch', globals=globals())
t2 = timeit.timeit('bin_srch', globals=globals())

print("The time of execution of the sequential search equals",t1)
print("The time of execution of the binary search equals",t2)