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
# Given a sorted array of n integers that has been rotated an unknown number of times,
# write code to find and element in the array. You may assume that the array was originally sorted

# Rotating still keeps one half sorted, so we could try using a binary search
# Work Cited -> Derrick Sherrill -> Youtube
# Source: https://www.youtube.com/watch?v=DnvWAd-RGhk
# I changed it to fit a rotated array
def binary_search(array, target):
    begin_index = 0
    end_index = len(array) - 1

    while begin_index <= end_index:
        middle_index = begin_index + (end_index - begin_index) // 2
        mid_value = array[middle_index]
        if mid_value == target:
            return f'Found at index position {middle_index}'

        # Left half is sorted if the mid-value is greater than or equal to the beginning value
        elif array[begin_index] <= mid_value:
            if array[begin_index] <= target < mid_value: # target is on the left side
                end_index = middle_index - 1
            else:
                begin_index = middle_index + 1 # move to the right


        # Right Half is sorted
        else:
            # If the mid-value is less than the end value the right side is sorted
            if mid_value < target <= array[end_index]:
                begin_index = middle_index + 1
            else:
                end_index = middle_index - 1
    return None


# Test
rotated_array = [5,6,7,1,2,3,4]
print(binary_search(rotated_array, 6))

rotated_array2 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(binary_search(rotated_array2, 44))
