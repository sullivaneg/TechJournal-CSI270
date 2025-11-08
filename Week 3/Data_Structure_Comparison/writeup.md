### 7 November 2025
# Data Structure Comparison 
**CSI-270**
**Dr. Frank Canovatchel**
**Emma Sullivan**

## Introduction
The goal of this assignment is to create an experiment to test the
performance of the del operator on lists and dictionaries. This experiment 
analyzed the runtime performance by generating random data, timing deletion using the timeit module,
and saving data to two dataframes. The modules used for this experiment were PANDAS, random, inflect and timeit.

## Hypothesis
My hypothesis is that deleting the dictionary input will take less time, this is because
deleting an item from a list has a time complexity of O(n) since every item after the item
deleted needs to be reindexed one spot to the right. My hypothesis is that since a dictionary
is unordered, it will just delete the value associated with the key.

## Algorithm
To begin gen_list(n) and gen_dict(n) are defined. These functions generate n unique random elements to populate 
the list and dictionary. The list contains integers and the dictionary contains integers as values and their
corresponding number word as the key. 

Then a random integer is generated using gen_rand_int(list) to be used as the index position for the element being 
deleted. This integer is also used in gen_rand_key(dict, int) to find the key at the same index position in the 
dictionary. This was done to make the conditions the same between both variables list and dictionary.

Then the functions delete_time(list or dictionary, idx) and copy_time(list or dictionary). In earlier drafts of the 
experiment, it was realized that for each cycle of timeit the original list was being altered so an out of index error 
would return. To remedy this a delete_time function was created. This function created a temporary list copy of the
original list and deleted the element from that. This is what is later used in the timeit.timeit call. To minimize the
impact of copying the list on the final results, the function copy_time was created. Copy_time copies the original list
and gets called in another timeit.timeit call. Then the copy_time is subtracted from the delete_time for the time of 
just the del function. The function to_excel is also defined. This function exports the final dataframes to sheets 
in an Excel file. 

The main function call is the function gen_data(). In the function a round_counter is initialized at zero. This round 
counter increments each test and is used to point to the row in the dataframe to update. This function creates two 
empty dataframes for the list and dictionary test results, each with three columns, "num cycles", "num elements" and 
"time". Num elements and num cycles are two test parameters. This experiment calculates the runtime for 100, 1000, 
10000 and 1000000 cycles in timeit.timeit for 4 lengths of each data structure (50, 100, 150, 200 elements). To use 
both parameters the experiment program utilizes two loops. The outer loop loops through the num cycles and the inner 
loop loops through the num elements.

In each inner loop, test data is generated and a random index is selected. Then there are 4 timeit.timeit calls. The 
first times the delete_time of the list, the second is the copy_time of the list, 
the third is the delete_time of the dictionary and the fourth is the copy_time of the dictionary. Both actual times are 
calculated by subtracting copy_time from delete_time. Then data is added to the data frames.

## Calculations
The experiment was run five times, the average time from all five was recorded. Then that average time was divided by
the number of cycles in that test instance to determine the runtime per cycle. Then all the run times per cycle were 
averaged with the other tests that had the same number of elements. The result was the average runtime per cycle for 
the list and the dictionary depending on the number of elements. 

## Results
The hypothesis was found to be correct. The list runtime increased as the number of elements increased by the
same increment while the dictionary runtime remained constant.