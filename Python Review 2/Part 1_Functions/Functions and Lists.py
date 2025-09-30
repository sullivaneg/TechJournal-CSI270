# Functions and lists:
# Assume the operating system stores process IDs of type integer for all running processes in a list named x. Since the
# OS tracks the processes by their IDs, then each process ID must have a unique value.
# x = [12, 3, 6, 4, 31, 11, 8, 21, 6, 16, 22, 1, 0, 123, 34, 2, 9]
# Read another list from the user that contains four process IDs (pid)
# The new list elements should be integer too.
# Sort the two lists
# Write a function and name it IsSubset(), this function is used to search for a subset of processes from the system process list (x).
# The IsSubset() function takes a list variable as a parameter.
# The IsSubset() function prints if the entered list is subset of the x or not.


def IsSubset(set, subset): # IsSubset is not PEP 8 approved name but the assignment told me to name it that
    """
    This function checks if one set is a subset of the other.
    :param set: large set
    :param subset: subset to check
    :return: print out if it's a subset or not
    """
    set.sort()
    subset.sort()

    count = 0
    for element in subset:
        if element in set:
            count += 1
        else:
            continue
    if count == len(subset):
        print(f'{subset} is a subset of {set}')
    else:
        print(f'{subset} is not a subset of {set}')


print(
    '_______________________________________\n'
    'Functions and Lists\n'
    '_______________________________________')

IsSubset(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c'])
IsSubset([1, 2, 3, 4, 5], [2, 3, 4])
IsSubset([1, 2, 3, 4, 5], [6, 7, 8])