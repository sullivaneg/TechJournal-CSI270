# Asks the user to input four integers. Reads the integers from the user and puts them in a list. Sort the numbers in
# descending order (using the techniques you learned so far) and reprint them after being sorted.


# Getting the User's integers and error handling
nums = []
for i in range(1, 5):
    while True:
        num = input(f'{i}. Enter your integer: ')
        try:
            num = int(num)
            nums.append(num)
            break

        except ValueError:
            print("Please enter a number")
            continue


# Sorting the list
nums_sorted = sorted(nums)
nums_sorted.reverse()
print(f'Your numbers in descending order are: {nums_sorted}')