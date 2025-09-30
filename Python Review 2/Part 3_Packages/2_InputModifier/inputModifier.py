# All of these function names aren't in snake case so they are PEP 8 violations
# However the assignment specifies these names so I didn't change them


def inputString(message):
    """
     this function is used to read a string value from the user and return that value.
    :return: string
    """
    string = input(message)
    return string

def inputInt(message):
    """
    this function is used to read an int value from the user and return that value.
    :return:
    """
    integer = int(input(message))
    return integer

def inputFloat(message):
    """
    this function is used to read a float value from the user and return that value.
    :return:
    """
    float_num = float(input(message))
    return float_num