#Author: Emma Sullivan
# Class: CSI-270-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).

import pandas as pd
import timeit
import random
import inflect

# Generate a random list.
def gen_list(n):
    """
    Generates a list of random numbers.
    :param n: number of elements in the list
    :return: a list with n elements
    """
    li = random.sample(range(1,n*2), n)
    return li

# Generate a random dictionary
def gen_dict(n):
    """
    Generates a random list of number names for keys and integers for values and creates
    a dictionary with n elements.
    :param n:number of key-value pairs
    :return: a dictionary with n elements
    """
    # "Generate a text file of every number's name from 1 to 300" prompt. Perplexity AI
    # 7 Nov. version, Perplexity AI Inc., 7 November 2025, www.perplexity.ai
    # Annotation: I wanted to generate a txt file of number's names just to use in generating a random dict,
    # but the AI output actually pointed me inadvertently to the inflect library, which I then, without the help
    # of AI, used to create this program.
    p = inflect.engine()
    values = gen_list(n)
    keys = [p.number_to_words(value) for value in values]

    return dict(zip(keys, values))

# Generate which item of the list, is going to be deleted
def gen_rand_int(list):
    """
    Generates a random index position from the length of the list.
    :param list: list of integers
    :return: random integer representing an index position
    """
    length = len(list)
    num = random.choice(range(0, length))
    return num

def gen_rand_key(dict, int):
    """
    Generates a random key from the dictionary.
    :param dict: dictionary with n elements
    :return: random key
    """
    li = list(dict.keys())
    key = li[int]
    return key

def to_excel(dfl, dfd):
    """
    Exports the two dataframes into one Excel file with two sheets.
    :return: excel file with two sheets
    """
    """
    Author: Me (Emma Sullivan)
    Project: CSI-160 Final Project
    Date: November-December 2024
    Description: Exporting to an Excel file with two sheets.
    """
    # Exporting the two Excel files dataframes into one Excel file with 2 sheets
    with pd.ExcelWriter('outcomes.xlsx') as excel_writer:
        # List will be sheet 1
        dfl.to_excel(excel_writer, sheet_name='List', index=False)
        # Dictionary will be sheet 2
        dfd.to_excel(excel_writer, sheet_name='Dictionary', index=False)

def delete_time(lidi, idx):
    temp_structure = lidi.copy()
    del temp_structure[idx]

def copy_time(lidi):
    temp_structure = lidi.copy()


# TODO: gen_data(df1, structure, i)
def gen_data():
    """
    Main program: Runs timeit.timeit on our structure and adds data to the dataframe.
    :param df: which dataframe data is getting added to
    :param structure: the generated dictionary or list
    :param i: index: either the key or the integer
    :return: nothing, it updates the dataframe accordingly
    """
    # Creating separate dataframes for dictionary and list
    data_list = {
        "Num Cycles": [],
        "Num Elements": [],
        "Time": []
    }
    dfl = pd.DataFrame(data_list)
    print("List dataframe:", dfl) #DEBUGGING

    data_dict = {
        "Num Cycles": [],
        "Num Elements": [],
        "Time": []
    }
    dfd = pd.DataFrame(data_dict)
    print("Dictionary dataframe:", dfd)  # DEBUGGING

    test_round = 0
    for num_cycles in [100, 1000, 10000, 100000, 1000000]:
        for num_elements in [50, 100, 150, 200]:
            print("test_round:", test_round)
            li = gen_list(num_elements)
            print("list:", li) #DEBUGGING
            di = gen_dict(num_elements)
            print("dictionary:", di) #DEBUGGING
            rand_int = gen_rand_int(li)
            print("random integer:", rand_int) #DEBUGGING
            rand_key = gen_rand_key(di, rand_int)
            print("random key:", rand_key) #DEBUGGING

            # I used Perplexity to debug my globals() issue
            # _________START__________
            req_dict = {
                "li": li,
                "rand_int": rand_int,
                "di": di,
                "rand_key": rand_key,
                "delete_time": delete_time,
                "copy_time": copy_time
            }
            # _________END____________

            """
            I had an issue where because my list was getting smaller everytime it cycled through I was getting out 
            of index errors. HOWEVER, packaging copying a temp list into deleting will affect my timing results since
            copying a list is O(n). So I'm going to time copying a list and subtract that from my total time to get 
            just the deletion time.
            """
            total_time_li = timeit.timeit('delete_time(li, rand_int)', globals=req_dict, number=num_cycles)
            copy_time_li = timeit.timeit('copy_time(li)', globals=req_dict, number=num_cycles)
            del_time_li = total_time_li - copy_time_li
            print("total_time_li:", total_time_li) # DEBUGGING
            print("copy_time_li:", copy_time_li) # DEBUGGING
            print("del_time_li:", del_time_li) # DEBUGGING

            total_time_di = timeit.timeit('delete_time(di, rand_key)', globals=req_dict, number=num_cycles)
            copy_time_di = timeit.timeit('copy_time(di)', globals=req_dict, number=num_cycles)
            del_time_di = total_time_di - copy_time_di
            print("total_time_di:", total_time_di) # DEBUGGING
            print("copy_time_di:", copy_time_di) # DEBUGGING
            print("del_time_di:", del_time_di) # DEBUGGING

            # Adding data to dataframe
            #   List
            dfl.at[test_round, "Num Cycles"] = num_cycles
            dfl.at[test_round, "Num Elements"] = num_elements
            dfl.at[test_round, "Time"] = del_time_li
            #   Dictionary
            dfd.at[test_round, "Num Cycles"] = num_cycles
            dfd.at[test_round, "Num Elements"] = num_elements
            dfd.at[test_round, "Time"] = del_time_di

            #DEBUGGING
            print("dfl:", dfl)
            print("dfd:", dfd)

            # Increment round by 1
            test_round += 1

    to_excel(dfl, dfd)

gen_data()
