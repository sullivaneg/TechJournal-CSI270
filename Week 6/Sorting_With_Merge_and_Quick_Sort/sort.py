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

# Problem Statement
# 1. Implement the merge sort algorithm. Print the resulting array after each pass.
# 2. Implement the quick sort algorithm. Print the resulting array after each pass.
# 3. Using a random number generator, create lists of following sizes:
# 2^10, 2^11, 2^12, 2^13, 2^14, 2^15
# Perform a benchmark analysis using the above 2 implementations of sorting algorithms.
# What is the difference in execution speed? Use timit package. (Do not use the print
# statements while timing the code)
# Write a summary of your results. You can use graphics as needed.


import pandas as pd
import timeit
import random

# Generate a random list.
def gen_list(n):
    """
    Generates a list of random numbers
    :param n: # of elements in the list is 2^n, n is the exponent
    :return: a list with 2^n elements
    """
    li = random.sample(range(1, (2**(n+1))), 2**n)
    return li

def to_excel(df):
    """
    Exports the two dataframes into one Excel file with two sheets.
    :return: excel file with two sheets
    """
    """
    Author: Me (Emma Sullivan)
    Project: CSI-160 Final Project
    Date: November-December 2024
    Description: Exporting to an Excel file with two sheets.
    """
    # Exporting the two Excel files dataframes into one Excel file with 2 sheets
    df.to_excel("outcomes.xlsx")

# Work Cited: Felix Tech Tips - Youtube
# Source: https://www.youtube.com/watch?v=cVZMah9kEjI

def merge_sort(array):
    if len(array)<=1:
        return array
    else:
        # Left array from left to midpoint
        left_array = array[:len(array)//2]
        # Right array from midpoint to right
        right_array = array[len(array)//2:]

        # Recursion
        # Will recurse until len(array) = 1
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        # Merge
        # Want to compare left most indexes in both arrays
        # i for left-most in left array, j for right array, k for index in merged array
        i, j, k = 0, 0, 0
        while i < len(left_array) and j < len(right_array):
            # If left array is less than right array, save left array in the left position in the merged array
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1 # Don't increase j because it hasn't been moved yet
            else: # Left array is smaller than right array
                array[k] = right_array[j]
                j+=1 # Not i because we haven't moved it
            k+=1

        # In the case that we have used all of the right but not the left
        while i < len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1

        # In the case that we have used all of the left but not the right
        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1

        # PRINTING THE ARRAY AFTER EACH PASS - UNCOMMENT TO PRINT - COMMENT FOR BENCHMARK TEST
        #print("After merging:", array)

        return array

# Work Cited: Derrick Sherrill - Youtube
# Source: https://www.youtube.com/watch?v=kFeXwkgnQ9U
def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        # Set the pivot point to the last item
        pivot = array.pop()

    items_greater = [] # Greater than pivot point
    items_lower = [] # Less than pivot point

    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)


    # PRINTING THE ARRAY AFTER EACH PASS - UNCOMMENT TO PRINT - COMMENT FOR BENCHMARK TEST
    #print(items_lower + [pivot] + items_greater)

    # Recursion
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def gen_data():
    """
    Main program: Runs timeit.timeit on our structure and adds data to the dataframe.
    :parameters: None
    :return: nothing, it updates the dataframe accordingly
    """
    # Creating a dataframe for export to excel
    data = {
        "algorithm": [],
        "n in 2^n": [],
        "Time": []
    }

    df = pd.DataFrame(data)
    print("List dataframe:", df) #DEBUGGING

    df_index_merge = 0
    df_index_quick = 1
    for num in range(10,16):
            print("ROUND: 2^",num)
            li = gen_list(num)
            print("list:", li) #DEBUGGING

            # Merge Sort
            merge_time = timeit.timeit(lambda: merge_sort(li.copy()), globals=globals(), number=1)
            print(merge_time) # DEBUGGING

            # Quick Sort
            quick_time = timeit.timeit(lambda: quick_sort(li.copy()), globals=globals(), number=1)
            print(quick_time) # DEBUGGING

            # Adding data to dataframe
            # Merge Sort
            df.at[df_index_merge, "algorithm"] = "Merge Sort"
            df.at[df_index_merge, "n in 2^n"] = num
            df.at[df_index_merge, "Time"] = merge_time

            # Quick Sort
            df.at[df_index_quick, "algorithm"] = "Quick Sort"
            df.at[df_index_quick, "n in 2^n"] = num
            df.at[df_index_quick, "Time"] = quick_time

            # Update index positions
            df_index_merge += 2
            df_index_quick += 2

            # DEBUGGING
            print("dfl:", df)

    to_excel(df)

def benchmark_test():
    gen_data()

def print_fun():# WITH PRINT STATEMENTS UNCOMMENTED
    with open("log.txt", "a") as f:
        f.write("________________Printing_________________")
        for num in range(10,16):
            f.write(f'\nROUND: 2^{num}')
            li = gen_list(num)
            f.write(f'STARTING LIST:" {li}')
            f.write(f'\n_______MERGE SORT_________\n{merge_sort(li.copy())}\n_______END MERGE SORT_________\n')
            f.write(f'\n_______QUICK SORT_________\n{quick_sort(li.copy())}\n_______END QUICK SORT_________\n')
            f.write("END OF ROUND\n")
        f.write("THE END")

# CHANGE THIS TO MOVE BETWEEN TESTS
printing = False

# FOR BENCHMARK TEST
if not printing:
    benchmark_test()

# FOR PRINTING
if printing:
    print_fun()