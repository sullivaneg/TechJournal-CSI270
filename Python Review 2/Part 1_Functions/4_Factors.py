# 4. Define a function that takes two integers and return true if the first is a multiplication of the second number

def is_factor(num, factor):
    """
    This function check if the second number is factor of the first number.
    :param num: first number
    :param factor: the number to check
    :return: True or False
    """
    if num % factor == 0:
        return True
    else:
        return False

print('_______________________________________\nExercise #4: Factor Function\n_____________________________________')
print(is_factor(6,3))
print(is_factor(6,4))