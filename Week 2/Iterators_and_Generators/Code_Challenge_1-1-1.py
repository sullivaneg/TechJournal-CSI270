#You are provided with a list of strings flash. You will practice iterating over the list by using
# a for loop. You will also create an iterator for the list and access the values from the iterator. 1.
# Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
# 2. Create an iterator for the list flash and assign the result to superspeed. 3. Print each of the items
# from superspeed using next() 4 times.

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for item in flash:
    print(item)

# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))