# 4. Define a function that takes two integers and return true if the first is a multiplication of the second number


def is_factor(num, factor):
    """
    This function check if the second number is factor of the first number.
    :param num: first number
    :param factor: the number to check
    :return: True or False
    """
    return num % factor == 0

print(
    '_______________________________________\n'
    'Exercise #4: Factor Function\n'
    '_______________________________________')

print(is_factor(6,3))
print(is_factor(6,4))