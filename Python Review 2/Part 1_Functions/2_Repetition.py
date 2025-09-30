# 2. Define a function “repetition”, this function takes a string and a number as its input. The function will repeat
# printing the string according to the value of the number. Remember string multiplication in Python ;)


def repetition1(string, num):
    """
    This function takes a string and number and prints the string repeated num times.
    :param string: string of text user wants repeated
    :param num: number of times to repeat
    :return: prints the string repeated num times
    """
    string = string * num
    print(string)


def repetition2(string, num):
    """
    This function takes a string and number and prints the string repeated num times on different lines.
    :param string: string of text user wants repeated
    :param num: number of times to repeat
    :return: prints the string repeated num times on new lines
    """
    for i in range(num):
        print(string)

print(
    '_______________________________________\n'
    'Exercise #2: Repetition Function\n'
    '_______________________________________')

print(
    "________________________________________\n"
    "Repetition 1 \n"
    "________________________________________")

repetition1("repeat",3)

print(
    "________________________________________\n"
    "Repetition 2 \n"
    "________________________________________")

repetition2("repeat",3)
