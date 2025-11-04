# 5. Define a function that named find_element, this function takes a list and a number as parameters, and return the
# index of the number in the list , otherwise return -1


def find_element(nums, num):
    """
    This function finds the element in a list.
    :param nums: the list of numbers.
    :param num: the number we are looking for.
    :return: index of element in nums or -1 if not found.
    """
    if num in nums:
        return f'The index position of {num} is {nums.index(num)} .'
    else:
        return -1

print(
    '_______________________________________\n'
    'Exercise #5: Find_Element\n'
    '_______________________________________')

print(find_element([1,2,3,4], 4))
print(find_element([1,2,3,4,5], 6))