from inputModifier import *


def output(name, sum):
    """
    This function is just to store the print output
    :return: prints the output
    """
    print("______________________________\nInput Modifier Test\n______________________________")
    print("Process Name: ", name)
    print("Sum of all consumed memory: ", sum)


def main():
    """
    This is the main function.
    :return: Takes user input and calls output() to print out the output.
    """
    process = inputString("Please input the process name: ")
    thread_num = inputInt("Please input the number of threads: ")
    memory_count = 0
    for i in range(thread_num):
        memory = inputFloat(f'Please input the memory size for thread {i+1}: ')
        memory_count += memory
    output(process, memory_count)

main()