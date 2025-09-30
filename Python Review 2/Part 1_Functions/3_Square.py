# 3. Define a function and name it square, this function is needed to calculate the area and perimeter of squares.
# The function has two parameters as input. The first is an integer and the second is a letter. If the letter is “a”
# for area, return the area of the square, if the letter is “p: for perimeter, return the perimeter of the square.
# Print the result in the main function.

def square(num, letter):
    """
    This function returns the square area or perimeter.
    :param num: side length of square
    :param letter: whether the user wants the area or perimeter
    :return: prints result
    """
    if letter.lower() == "a":
        print("The area of the square is:", num * num)
    elif letter.lower() == "p":
        print("The perimeter of the square is:", num * 4)


print('_______________________________________\nExercise #3: Square Function\n_____________________________________')
square(7,"p")
square(6, "a")