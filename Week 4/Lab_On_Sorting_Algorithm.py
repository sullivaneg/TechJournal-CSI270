# Write the step by step algorithm that you chose for sorting a list of numbers.
# Show how it works on the following example:
# [10, 45, 20, 1, 55, 78, 9]

unsorted_list = [10, 45, 20, 1, 55, 78, 9]
list2 = [69, 96, 92, 68, 89, 41, 98, 74, 62, 77, 50, 72, 53, 91, 94, 76, 32, 87, 59, 18]

# I don't 100% understand the question, I'm assuming I'm supposed to make my own
# I made my own and am very aware that it just ended up being bubble sort, I learned
# That in 160 so it's in my brain

# Algorithm
# 1. Given a list of numbers my function will look at the first and second numbers to start
# 2. If the second number is larger than the first they will stay in the same position
# 3. If the second number is smaller they will switch positions
# 4. Then my second and third numbers will do the same and then back down to first and second
# 5. This will happen until the list is sorted

print("__________Alg 1___________")

def sort_list(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):
        for index in range(0, length-i-1):
            if unsorted_list[index] > unsorted_list[index+1]:
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index+1]
                unsorted_list[index+1] = temp
    return unsorted_list

print(sort_list(unsorted_list))
print(sort_list(list2))

# Here's another one I came up with that is super inefficient

# Algorithm: This algorithm only works if there are no duplicates
# 1. First I create a variable called length that will be the length of the unsorted list
# 2. Then I create an empty list and add a 0 for every number in the unsorted list
# 3. Then for each number in the unsorted list I create 3 counts, greater than, less than and equal to
# 4. I set all these counts to 0
# 5. Then I compare num to every other num and add to the greater than or less than tally accordingly
# 6. Then I change the empty list at the index number that is the number of numbers less than num
# 7. My algorithm returns the new list as sorted_list

print("__________Alg 2___________")

def sort2(unsorted_list):
    length = len(unsorted_list)
    sorted_list = []
    for i in range(length):
        sorted_list.append(0)
    for num in unsorted_list:
        lt = 0
        gt = 0
        eq = 0
        for i in range(length):
            if unsorted_list[i] > num:
                lt += 1
            elif unsorted_list[i] < num:
                gt += 1
            else:
                eq += 1
        sorted_list[gt] = num
    return (sorted_list)

print(sort2(unsorted_list))
print(sort2(list2))

