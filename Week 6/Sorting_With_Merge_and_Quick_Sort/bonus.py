from sort import *
num = 15
# while True:
#     print("NUM =", num)
#     li = gen_list(num)
#     merge_sort(li.copy())
#     print(f'MERGE SORT WITH LIST SIZE 2^{num} SUCCESSFUL')
#     num += 1

while True:
    print("NUM =", num)
    li = gen_list(num)
    quick_sort(li.copy())
    print(f'QUICK SORT SUCCESSFUL WITH LIST SIZE 2^{num} SUCCESSFUL')
    num += 1