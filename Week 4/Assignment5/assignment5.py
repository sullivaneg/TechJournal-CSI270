import random
import timeit

# Bubble Sort -> Source: https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/
def bubbleSort(arr):
    n = len(arr)
    # Go through the elements
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            # Move through the array from 0 to n-i-1
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # PRINTING
        print(f"Pass {i + 1}: {arr}")
        #with open("bubble.txt", "a") as f:
            #print(f"Pass {i+1}: {arr}", file=f)
        if swapped == False:
            break
    #with open("bubble.txt", "a") as f:
        #print(f"Finished List: {arr}", file=f)
    print(f"Finished List: {arr}")
    return arr

# Selection Sort -> Source: https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/
def selectionSort(arr):
    print(arr) # For Printing only
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # simultaneous assignment
        arr[i], arr[min_index] = arr[min_index], arr[i]

        #with open("selection.txt", "a") as f:
            #print(f"Pass {i + 1}: {arr}", file=f)
        print(f"Pass {i + 1}: {arr}")
    #with open("selection.txt", "a") as f:
        #print(f"Finished List: {arr}", file=f)
    print(f"Finished List: {arr}")
    return arr

# Testing - no print statements
def bubble_no_print():
    temp = test_list.copy()
    n = len(temp)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
                swapped = True
        if not swapped:
            break

def selection_no_print():
    temp = test_list.copy()
    n = len(temp)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if temp[j] < temp[min_index]:
                min_index = j
        temp[i], temp[min_index] = temp[min_index], temp[i]

# Test Random List
test_list = [random.randint(1, 10000) for _ in range(500)]
small_test_list = [random.randint(1, 100) for _ in range(10)]
bubble_time = timeit.timeit(bubble_no_print, number=1)
selection_time = timeit.timeit(selection_no_print, number=1)

#bubbleSort(small_test_list.copy())
#selectionSort(small_test_list.copy())
print("\n--- Test Results ---")
print(f"Bubble Sort Time: {bubble_time} seconds")
print(f"Selection Sort Time: {selection_time} seconds")

if bubble_time < selection_time:
    print(f"Bubble Sort Time was {selection_time/bubble_time:.2f} times faster than selection time")
elif selection_time < bubble_time:
    print(f"Selection Sort time was {bubble_time/selection_time:.2f} times faster than bubble time")
print("__________________________")